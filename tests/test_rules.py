import datetime as dt

import pytest

from amutha_agent import dishes as D
from amutha_agent.dishes import Dish
from amutha_agent.planner import EPOCH, is_treat_night, plan_day, plan_range, plan_with_checks
from amutha_agent.rules import (
    MAX_DAILY_RICE_SCORE,
    check_catalogue,
    check_dish,
    check_plan,
    screen_free_text,
)

TWO_YEARS = plan_range(dt.date(2026, 1, 1), 730)


def test_catalogue_follows_every_rule():
    assert check_catalogue(D.ALL_DISHES) == []


def test_two_years_of_menus_follow_every_rule():
    assert check_plan(TWO_YEARS) == []


def test_maida_only_once_in_any_fortnight():
    maida_days = [d.date for d in TWO_YEARS if d.has_maida]
    assert maida_days, "the fortnightly treat should still happen"
    gaps = {(b - a).days for a, b in zip(maida_days, maida_days[1:])}
    assert gaps == {14}
    assert all(is_treat_night(d) for d in maida_days)


def test_rice_is_limited():
    assert max(d.rice_score for d in TWO_YEARS) <= MAX_DAILY_RICE_SCORE
    for i in range(len(TWO_YEARS) - 6):
        assert sum(d.has_rice_lunch for d in TWO_YEARS[i:i + 7]) <= 4


def test_more_fish_and_chicken_than_mutton():
    lunches = [d.lunch_main.protein for d in TWO_YEARS]
    assert lunches.count("fish") + lunches.count("chicken") > 5 * lunches.count("mutton")
    for i in range(len(TWO_YEARS) - 6):
        week = [d.lunch_main.protein for d in TWO_YEARS[i:i + 7]]
        assert week.count("mutton") <= 1


def test_soup_and_fruit_every_day():
    for day in TWO_YEARS:
        assert day.soup.slot == "soup"
        assert day.fruit.slot == "fruit"
        assert day.date.month in day.fruit.months


def test_no_dish_twice_in_a_row():
    for prev, cur in zip(TWO_YEARS, TWO_YEARS[1:]):
        for slot in ("breakfast", "lunch_main", "lunch_side", "dinner", "soup", "snack"):
            assert getattr(prev, slot) != getattr(cur, slot), (cur.date, slot)


def test_plan_is_stable_for_a_date():
    assert plan_day(dt.date(2026, 10, 22)) == plan_day(dt.date(2026, 10, 22))
    assert plan_with_checks(dt.date(2026, 10, 22)) == plan_day(dt.date(2026, 10, 22))


def test_epoch_is_a_monday():
    assert EPOCH.weekday() == 0


@pytest.mark.parametrize("bad", ["cheese", "pork", "beef", "mayonnaise", "bread", "paneer", "maggi"])
def test_banned_ingredients_are_caught(bad):
    dish = Dish("Test dish", "t", "dinner", ingredients=("onion", bad), nutrition="-")
    assert check_dish(dish)


def test_hidden_maida_is_caught():
    dish = Dish("Sneaky parotta", "t", "dinner", ingredients=("maida", "egg"), nutrition="-")
    assert any("maida" in p for p in check_dish(dish))


def test_too_spicy_is_caught():
    dish = Dish("Fire curry", "t", "lunch_main", ingredients=("chilli",), nutrition="-", spice=3)
    assert check_dish(dish)


def test_words_inside_other_words_are_not_flagged():
    assert screen_free_text("shallots, gingham, hamper") == []
    assert screen_free_text("Add cheese on top") == ["cheese"]


def test_every_dish_has_a_recipe_that_follows_the_rules():
    from amutha_agent.recipes import RECIPES, recipe_text
    from amutha_agent.rules import MAIDA_WORDS, banned_words_in

    names = {d.name for d in D.ALL_DISHES}
    assert names == set(RECIPES), "recipes and dishes must match one to one"
    for dish in D.ALL_DISHES:
        r = RECIPES[dish.name]
        assert r.ingredients and r.steps and r.time, dish.name
        hits = [w for w in banned_words_in(recipe_text(r)) if not (dish.maida and w in MAIDA_WORDS)]
        assert hits == [], (dish.name, hits)


def test_recipes_stand_alone():
    """Each recipe card is cooked from the email alone, so no 'see the X recipe'."""
    import re

    from amutha_agent.recipes import RECIPES, recipe_text

    pattern = re.compile(r"\b(as in|see|from) the [^.;]*recipe", re.IGNORECASE)
    for name, r in RECIPES.items():
        assert not pattern.search(recipe_text(r)), name
