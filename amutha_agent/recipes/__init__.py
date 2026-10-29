"""A recipe (ingredients with quantities + step-by-step method) for every dish.

Quantities serve 4: 2 adults and 2 teenagers.
"""

from __future__ import annotations

from ..dishes import Dish
from . import breakfast, dinner, evening, lunch, sides, simple
from .base import Recipe

RECIPES: dict[str, Recipe] = {}
for _module in (breakfast, lunch, sides, dinner, evening, simple):
    _overlap = RECIPES.keys() & _module.RECIPES.keys()
    if _overlap:
        raise ValueError(f"recipe defined twice: {sorted(_overlap)}")
    RECIPES.update(_module.RECIPES)


def recipe_for(dish: Dish) -> Recipe | None:
    return RECIPES.get(dish.name)


def recipe_text(recipe: Recipe) -> str:
    """All the words in a recipe, for the rule checks."""
    return " ".join((recipe.time, *recipe.ingredients, *recipe.steps, recipe.tip))


__all__ = ["RECIPES", "Recipe", "recipe_for", "recipe_text"]
