"""Builds the day's menu.

The plan is a pure function of the date, so the agent needs no database:
running it twice for the same day gives the same menu, and the multi-day
rules (maida once a fortnight, mutton at most once a week, less rice) hold
because they are built into a fixed 14-day rhythm:

    Day  Mon   Tue  Wed      Thu  Fri   Sat       Sun
    Wk1  fish  dal  chicken  egg  fish  biryani   mutton
    Wk2  fish  dal  chicken  egg  fish  chicken*  fish     (* Treat Night: maida)

Rice is limited by the same rhythm: rice lunches (half a cup) only on
Mon, Fri, Sun and the biryani Saturday, and on those days breakfast and
dinner come from the no-rice tiffin lists.

Within that rhythm every list rotates through shuffled passes, so a dish
does not come back until the rest of its list has been used.
"""

from __future__ import annotations

import datetime as dt
import random
from typing import Sequence

from . import dishes as D
from .dishes import Dish
from .rules import DayMenu, check_plan

EPOCH = dt.date(2024, 1, 1)  # a Monday; fortnights are counted from here

# One entry per day of the fortnight: (lunch protein, rice lunch?, breakfast list, dinner list)
# "bf0"/"dn0" = no-rice tiffins, "bf1"/"dn1" = tiffins with a little rice.
FORTNIGHT = [
    ("fish", True, "bf0", "dn0"),
    ("dal", False, "bf1", "dn0"),
    ("chicken", False, "bf0", "dn1"),
    ("egg", False, "bf1", "dn0"),
    ("fish", True, "bf0", "dn0"),
    ("biryani", True, "bf0", "dn0"),
    ("mutton", True, "bf0", "dn0"),
    ("fish", True, "bf0", "dn0"),
    ("dal", False, "bf0", "dn1"),
    ("chicken", False, "bf1", "dn0"),
    ("egg", False, "bf0", "dn1"),
    ("fish", True, "bf0", "dn0"),
    ("chicken", False, "bf1", "treat"),
    ("fish", True, "bf0", "dn0"),
]
TREAT_OFFSET = next(i for i, day in enumerate(FORTNIGHT) if day[3] == "treat")

KID_TIPS = [
    "Let the children pick tomorrow's fruit from two options - choice reduces fights.",
    "Plate like a restaurant: small bowls, a sauce-dip on the side, food arranged in colours.",
    "Give the dish its 'hotel name' (e.g. 'Desi Pizza', 'Tamil Noodles') - teens judge by the name first.",
    "Serve the crunchy item (fry / roast) first - it opens the appetite for the rest of the plate.",
    "No phones at the table for 20 minutes; talk about their day - meals finish faster.",
    "Ask one child to be 'chef of the day' and help with tempering or rolling - they eat what they cook.",
    "Keep a 'healthy junk' box: ragi murukku, chikki, roasted makhana - so hunger never meets a packet of chips.",
    "Do not argue about the plate. Serve, smile, and remove it after 30 minutes without comment.",
    "Offer new vegetables next to a favourite one - small portions, repeated over the week.",
    "Take a family photo of Treat Night dinner - it gives them something to look forward to every fortnight.",
    "Make extra chilli tadka in a separate bowl for adults so the main dish stays kid-mild.",
    "Pack the lunchbox in a fun way: mini idlis, rolled chapatis, cut fruit with toothpicks.",
    "Praise what they finish, never compare with other children.",
    "Freeze grapes or mango cubes as 'ice candy' for the evening craving.",
]


def _pass_order(pool: Sequence[Dish], key: str, n_pass: int) -> list[Dish]:
    order = list(pool)
    random.Random(f"{key}:{n_pass}").shuffle(order)
    if n_pass > 0 and len(order) > 2:
        prev = list(pool)
        random.Random(f"{key}:{n_pass - 1}").shuffle(prev)
        if order[0] == prev[-1]:  # never repeat across the joint of two passes
            order[0], order[1] = order[1], order[0]
    return order


def _pick(pool: Sequence[Dish], key: str, k: int) -> Dish:
    """The k-th dish of an endless run of shuffled passes over pool."""
    n_pass, idx = divmod(k, len(pool))
    return _pass_order(pool, key, n_pass)[idx]


def _uses_before(day_index: int, column: int, value: object) -> int:
    """How many earlier days of the rhythm used this value in this column."""
    fortnight, offset = divmod(day_index, len(FORTNIGHT))
    col = [day[column] for day in FORTNIGHT]
    return fortnight * col.count(value) + col[:offset].count(value)


BREAKFAST_LISTS = {
    "bf0": [d for d in D.BREAKFAST if d.rice == 0],
    "bf1": [d for d in D.BREAKFAST if d.rice > 0],
}
DINNER_LISTS = {
    "dn0": [d for d in D.DINNER if d.rice == 0],
    "dn1": [d for d in D.DINNER if d.rice > 0],
}
BIRYANI = [d for d in D.LUNCH_MAIN if d.one_pot]


def plan_day(date: dt.date) -> DayMenu:
    day_index = (date - EPOCH).days
    fortnight, offset = divmod(day_index, len(FORTNIGHT))
    protein, rice_lunch, bf_list, dn_list = FORTNIGHT[offset]

    # Lunch: protein main + small carb base + vegetable side
    if protein == "biryani":
        lunch_main = _pick(BIRYANI, "biryani", fortnight)
        lunch_base = None
    else:
        mains = [d for d in D.LUNCH_MAIN if d.protein == protein and not d.one_pot]
        lunch_main = _pick(mains, f"main-{protein}", _uses_before(day_index, 0, protein))
        bases = [d for d in D.LUNCH_BASE if bool(d.rice) == rice_lunch]
        lunch_base = _pick(bases, f"base-{rice_lunch}", _uses_before(day_index, 1, rice_lunch))
    lunch_side = _pick(D.LUNCH_SIDE, "side", day_index)

    breakfast = _pick(BREAKFAST_LISTS[bf_list], bf_list, _uses_before(day_index, 2, bf_list))
    if dn_list == "treat":
        dinner = D.MAIDA_TREAT[fortnight % len(D.MAIDA_TREAT)]
    else:
        dinner = _pick(DINNER_LISTS[dn_list], dn_list, _uses_before(day_index, 3, dn_list))

    in_season = [d for d in D.FRUIT if date.month in d.months]
    return DayMenu(
        date=date,
        breakfast=breakfast,
        fruit=_pick(in_season, f"fruit-{date.month}", day_index),
        lunch_main=lunch_main,
        lunch_base=lunch_base,
        lunch_side=lunch_side,
        soup=_pick(D.SOUP, "soup", day_index),
        snack=_pick(D.SNACK, "snack", day_index),
        dinner=dinner,
        bedtime=_pick(D.BEDTIME, "bedtime", day_index),
    )


def plan_range(start: dt.date, days: int) -> list[DayMenu]:
    return [plan_day(start + dt.timedelta(days=i)) for i in range(days)]


def plan_with_checks(date: dt.date) -> DayMenu:
    """Plan the day and verify every rule over the surrounding fortnight."""
    window = plan_range(date - dt.timedelta(days=13), 27)
    problems = check_plan(window)
    if problems:
        raise ValueError("Menu breaks Amutha's rules:\n" + "\n".join(problems))
    return window[13]


def kid_tip(date: dt.date) -> str:
    return KID_TIPS[(date - EPOCH).days % len(KID_TIPS)]


def is_treat_night(date: dt.date) -> bool:
    return (date - EPOCH).days % len(FORTNIGHT) == TREAT_OFFSET


def days_to_next_treat(date: dt.date) -> int:
    return (TREAT_OFFSET - (date - EPOCH).days % len(FORTNIGHT)) % len(FORTNIGHT)


def prep_for_tomorrow(date: dt.date) -> list[str]:
    tomorrow = plan_day(date + dt.timedelta(days=1))
    return [f"{d.prep_ahead} ({d.name})" for d in tomorrow.dishes() if d.prep_ahead]


def shopping_list(day: DayMenu) -> list[str]:
    items: list[str] = []
    for dish in day.dishes():
        for ing in dish.ingredients:
            if ing not in items:
                items.append(ing)
    return sorted(items)
