"""Amutha's 12 kitchen rules, written as code.

The planner only builds menus that pass :func:`check_plan`, and the dish
catalogue itself is screened by :func:`check_dish`. If a rule is ever broken
the agent refuses to send the email instead of sending a bad menu.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from typing import Iterable

from .dishes import Dish

# Rule 1: maida at most once in 14 days
MAIDA_WINDOW_DAYS = 14
MAIDA_MAX_PER_WINDOW = 1

# Rule 2: less rice. Score per day (lunch rice base = 2, rice tiffin = 1).
MAX_DAILY_RICE_SCORE = 3
MAX_RICE_LUNCHES_PER_WEEK = 4

# Rule 3: more fish and chicken than mutton; no beef or pork
MAX_MUTTON_PER_WEEK = 1

# Rule 12: spice welcome, but never tongue-burning for the children
MAX_SPICE_FOR_CHILDREN = 2

ALLOWED_CUISINES = {"tamil", "indian"}  # Rule 10 / 11

# Rules 3, 6, 7, 8 - things that must never reach the plate.
BANNED_INGREDIENTS = {
    # Rule 3
    "beef", "pork", "bacon", "ham", "salami", "pepperoni", "lard",
    # Rule 6 - processed foods
    "sausage", "nugget", "instant noodles", "maggi", "packet", "packaged", "frozen fries",
    "ready-to-eat", "bread", "ketchup", "sauce bottle", "soup powder", "cornflakes",
    "ajinomoto", "msg", "food colour", "margarine", "processed",
    # Rule 7 - no cheese (paneer is fresh cheese, so it is left out too)
    "cheese", "paneer",
    # Rule 8 - no shop mayonnaise
    "mayonnaise", "mayo",
}

# Rule 1 - maida and its aliases; only treat dishes may contain these
MAIDA_WORDS = {"maida", "all-purpose flour", "refined flour"}


@dataclass
class DayMenu:
    """What the planner produces for one date (filled in by planner.py)."""

    date: "object"
    breakfast: Dish
    fruit: Dish
    lunch_main: Dish
    lunch_base: Dish | None
    lunch_side: Dish
    soup: Dish
    snack: Dish
    dinner: Dish
    bedtime: Dish

    def dishes(self) -> list[Dish]:
        items = [self.breakfast, self.fruit, self.lunch_main, self.lunch_base,
                 self.lunch_side, self.soup, self.snack, self.dinner, self.bedtime]
        return [d for d in items if d is not None]

    @property
    def rice_score(self) -> int:
        return sum(d.rice for d in self.dishes())

    @property
    def has_rice_lunch(self) -> bool:
        base_rice = self.lunch_base.rice if self.lunch_base else 0
        return max(base_rice, self.lunch_main.rice) >= 2

    @property
    def has_maida(self) -> bool:
        return any(d.maida for d in self.dishes())


def _text(dish: Dish) -> str:
    return " ".join((dish.name, *dish.ingredients)).lower()


def check_dish(dish: Dish) -> list[str]:
    """Problems with a single dish (empty list = dish is allowed)."""
    problems = []
    text = _text(dish)
    for word in banned_words_in(text):
        if word not in MAIDA_WORDS:
            problems.append(f"{dish.name}: banned item '{word}'")
    has_maida_word = any(w in text for w in MAIDA_WORDS)
    if has_maida_word and not dish.maida:
        problems.append(f"{dish.name}: contains maida but is not marked as the fortnightly treat")
    if dish.maida and not has_maida_word:
        problems.append(f"{dish.name}: marked maida but maida is not listed in ingredients")
    if dish.spice > MAX_SPICE_FOR_CHILDREN:
        problems.append(f"{dish.name}: spice {dish.spice} is too hot for the children")
    if dish.cuisine not in ALLOWED_CUISINES:
        problems.append(f"{dish.name}: cuisine '{dish.cuisine}' is not Indian")
    return problems


def check_catalogue(dishes: Iterable[Dish]) -> list[str]:
    problems = []
    for d in dishes:
        problems.extend(check_dish(d))
    return problems


def check_day(day: DayMenu) -> list[str]:
    problems = []
    for d in day.dishes():
        problems.extend(check_dish(d))
    if day.soup is None or day.soup.slot != "soup":
        problems.append(f"{day.date}: no soup for the children (rule 4)")
    if day.fruit is None or day.fruit.slot != "fruit":
        problems.append(f"{day.date}: no fruit / juice (rule 5)")
    if day.rice_score > MAX_DAILY_RICE_SCORE:
        problems.append(f"{day.date}: too much rice (score {day.rice_score} > {MAX_DAILY_RICE_SCORE}) (rule 2)")
    if not any(d.slot in {"lunch_side"} for d in day.dishes()):
        problems.append(f"{day.date}: no vegetable side (rule 9)")
    return problems


def check_plan(days: list[DayMenu]) -> list[str]:
    """Check a run of consecutive days, including the multi-day rules."""
    problems = []
    for day in days:
        problems.extend(check_day(day))

    # Rule 1: any 14-day window holds at most one maida meal
    for i in range(len(days)):
        window = days[i:i + MAIDA_WINDOW_DAYS]
        count = sum(1 for d in window if d.has_maida)
        if count > MAIDA_MAX_PER_WINDOW:
            problems.append(f"{window[0].date}..{window[-1].date}: maida {count} times in 14 days (rule 1)")
            break

    # Variety: the same dish never comes back the very next day
    for prev, cur in zip(days, days[1:]):
        repeated = {d.name for d in prev.dishes()} & {d.name for d in cur.dishes()}
        repeated -= {d.name for d in cur.dishes() if d.slot in {"lunch_base", "fruit"}}
        if repeated:
            problems.append(f"{cur.date}: repeated from yesterday: {', '.join(sorted(repeated))} (variety)")

    # Weekly rules over every 7-day window
    for i in range(0, max(len(days) - 6, 0)):
        week = days[i:i + 7]
        proteins = Counter(d.protein for day in week for d in day.dishes())
        if proteins["mutton"] > MAX_MUTTON_PER_WEEK:
            problems.append(f"{week[0].date}: mutton {proteins['mutton']} times in a week (rule 3)")
        if proteins["fish"] + proteins["chicken"] <= proteins["mutton"] * 2:
            problems.append(f"{week[0].date}: not enough fish/chicken vs mutton (rule 3)")
        rice_lunches = sum(1 for day in week if day.has_rice_lunch)
        if rice_lunches > MAX_RICE_LUNCHES_PER_WEEK:
            problems.append(f"{week[0].date}: rice lunch {rice_lunches} times in a week (rule 2)")
    return problems


def banned_words_in(text: str) -> list[str]:
    """Banned words (incl. maida) found in text, matched on whole words."""
    lowered = text.lower()
    tokens = set("".join(c if c.isalnum() else " " for c in lowered).split())
    hits = []
    for word in BANNED_INGREDIENTS | MAIDA_WORDS:
        if " " in word or "-" in word:
            found = word in lowered
        else:
            found = word in tokens or word + "s" in tokens
        if found:
            hits.append(word)
    return sorted(hits)


def screen_free_text(text: str) -> list[str]:
    """Banned words appearing in free text (used to screen the AI chef note)."""
    return banned_words_in(text)
