"""The Recipe record shared by every recipe file."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Recipe:
    time: str
    ingredients: tuple[str, ...]
    steps: tuple[str, ...]
    serves: int = 4
    tip: str = ""


def R(time: str, ingredients: list[str], steps: list[str], serves: int = 4, tip: str = "") -> Recipe:
    return Recipe(time=time, ingredients=tuple(ingredients), steps=tuple(steps), serves=serves, tip=tip)
