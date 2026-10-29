"""Turns a day's menu into the morning email (plain text and HTML)."""

from __future__ import annotations

import html
from dataclasses import dataclass

from . import dishes as D
from .dishes import Dish
from .recipes import Recipe, recipe_for
from .planner import days_to_next_treat, is_treat_night, kid_tip, prep_for_tomorrow, shopping_list
from .rules import DayMenu


@dataclass
class Meal:
    time: str
    title: str
    dishes: list[Dish]
    note: str = ""


def meals_for(day: DayMenu) -> list[Meal]:
    lunch = [day.lunch_main] + ([day.lunch_base] if day.lunch_base else []) + [day.lunch_side]
    return [
        Meal("7:00 AM", "Breakfast (Tiffin)", [day.breakfast]),
        Meal("10:30 AM", "Fruit / Fresh Juice", [day.fruit], "Pack in the lunchbox or serve mid-morning."),
        Meal("1:00 PM", "Lunch", lunch, "Curd or " + D.DAILY_HYDRATION.split(" with ")[0] + " on the side."),
        Meal("5:00 PM", "Children's Soup + Evening Snack", [day.soup, day.snack],
             "Soup first, snack after - hungry children drink the soup happily."),
        Meal("8:00 PM", "Dinner", [day.dinner]),
        Meal("9:30 PM", "Bedtime Drink", [day.bedtime]),
    ]


RULES_SUMMARY = [
    "Maida only on Treat Night - once in two weeks",
    "Rice kept small (half cup on rice days, millets and phulka on other days)",
    "Fish and chicken more often than mutton; no beef, no pork",
    "Soup for the children every day",
    "Fruit or fresh juice every day",
    "No processed or packaged food, no cheese, no shop mayonnaise",
    "Fresh vegetables at every lunch; Indian / Tamil home food only",
    "Spice kept child-safe - extra chilli only for adults",
]


def subject(day: DayMenu) -> str:
    tag = " - Treat Night!" if is_treat_night(day.date) else ""
    return f"Amutha's Kitchen | {day.date:%a %d %b}: {day.breakfast.name.split(' with ')[0]}, " \
           f"{day.lunch_main.name.split(' with ')[0]}{tag}"


def _treat_line(day: DayMenu) -> str:
    n = days_to_next_treat(day.date)
    if n == 0:
        return "Tonight is TREAT NIGHT - the fortnightly Madurai parotta special. Celebrate it!"
    return f"Next Treat Night (Madurai parotta) in {n} day{'s' if n != 1 else ''} - remind the children!"


def recipes_for(day: DayMenu) -> list[tuple[str, Dish, Recipe]]:
    """(meal title, dish, recipe) in meal order, for every dish that has a recipe."""
    out = []
    for meal in meals_for(day):
        for dish in meal.dishes:
            recipe = recipe_for(dish)
            if recipe is not None:
                out.append((meal.title, dish, recipe))
    return out


def _recipes_text(day: DayMenu) -> list[str]:
    out = ["=" * 70, "TODAY'S RECIPES (each serves 4: 2 adults + 2 children)", "=" * 70, ""]
    for n, (meal_title, dish, r) in enumerate(recipes_for(day), 1):
        out.append(f"{n}. {dish.name} ({dish.tamil}) - {meal_title}")
        out.append(f"   Time: {r.time}")
        out.append("   Ingredients:")
        out += [f"     - {i}" for i in r.ingredients]
        out.append("   Method:")
        out += [f"     {k}. {step}" for k, step in enumerate(r.steps, 1)]
        if r.tip:
            out.append(f"   Tip: {r.tip}")
        out.append("")
    return out


def to_text(day: DayMenu, family: str, ai_note: str | None = None) -> str:
    out = [f"Vanakkam {family}! Today's healthy menu for {day.date:%A, %d %B %Y}", ""]
    for meal in meals_for(day):
        out.append(f"{meal.time}  {meal.title.upper()}")
        for dish in meal.dishes:
            out.append(f"  - {dish.name} ({dish.tamil})")
            out.append(f"      Nutrition: {dish.nutrition}")
            if dish.kid_hook:
                out.append(f"      For the kids: {dish.kid_hook}")
            if recipe_for(dish):
                out.append("      Recipe: see TODAY'S RECIPES below")
        if meal.note:
            out.append(f"  Note: {meal.note}")
        out.append("")
    out += _recipes_text(day)
    out += [f"Hydration: {D.DAILY_HYDRATION}", "", _treat_line(day), "",
            f"Tip to win the children over: {kid_tip(day.date)}", ""]
    if ai_note:
        out += ["A note from the AI chef:", ai_note, ""]
    prep = prep_for_tomorrow(day.date)
    if prep:
        out.append("Get ready for tomorrow:")
        out += [f"  - {p}" for p in prep]
        out.append("")
    out.append("Ingredients for today: " + ", ".join(shopping_list(day)))
    out += ["", "Rules followed today:"] + [f"  [x] {r}" for r in RULES_SUMMARY]
    return "\n".join(out)


def _dish_html(dish: Dish) -> str:
    e = html.escape
    hook = f'<div style="color:#b45309;font-size:13px;margin-top:2px">For the kids: {e(dish.kid_hook)}</div>' \
        if dish.kid_hook else ""
    see = '<div style="color:#047857;font-size:12px;margin-top:2px">Recipe below &darr;</div>' \
        if recipe_for(dish) else ""
    return (
        f'<div style="margin:6px 0 10px">'
        f'<div style="font-weight:600;font-size:15px">{e(dish.name)} '
        f'<span style="color:#6b7280;font-weight:400">({e(dish.tamil)})</span></div>'
        f'<div style="color:#374151;font-size:13px">{e(dish.nutrition)}</div>{hook}{see}</div>'
    )


def _recipes_html(day: DayMenu) -> str:
    e = html.escape
    cards = []
    for n, (meal_title, dish, r) in enumerate(recipes_for(day), 1):
        ingredients = "".join(f"<li style='margin:2px 0'>{e(i)}</li>" for i in r.ingredients)
        steps = "".join(f"<li style='margin:4px 0'>{e(step)}</li>" for step in r.steps)
        tip = (f"<div style='background:#fef3c7;border-radius:6px;padding:6px 10px;margin-top:6px;font-size:13px'>"
               f"<b>Tip:</b> {e(r.tip)}</div>") if r.tip else ""
        cards.append(
            f"<div style='border:1px solid #d1fae5;border-radius:8px;padding:12px 14px;margin:12px 0'>"
            f"<div style='font-size:12px;color:#047857;text-transform:uppercase;letter-spacing:.05em;font-weight:700'>"
            f"{n}. {e(meal_title)}</div>"
            f"<div style='font-weight:700;font-size:16px;margin:2px 0'>{e(dish.name)} "
            f"<span style='color:#6b7280;font-weight:400'>({e(dish.tamil)})</span></div>"
            f"<div style='font-size:13px;color:#6b7280'>Time: {e(r.time)} &middot; Serves {r.serves}</div>"
            f"<div style='font-weight:600;margin-top:8px'>Ingredients</div>"
            f"<ul style='margin:4px 0 0 18px;padding:0;font-size:14px'>{ingredients}</ul>"
            f"<div style='font-weight:600;margin-top:8px'>Method</div>"
            f"<ol style='margin:4px 0 0 18px;padding:0;font-size:14px'>{steps}</ol>{tip}</div>"
        )
    return ("<h3 style='color:#065f46;margin:22px 0 4px'>Today's Recipes</h3>"
            "<div style='font-size:13px;color:#6b7280'>Each recipe serves 4 (2 adults + 2 children).</div>"
            + "".join(cards))


def to_html(day: DayMenu, family: str, ai_note: str | None = None) -> str:
    e = html.escape
    rows = []
    for meal in meals_for(day):
        note = f'<div style="color:#6b7280;font-size:12px;font-style:italic">{e(meal.note)}</div>' if meal.note else ""
        rows.append(
            f'<tr><td style="vertical-align:top;padding:12px 10px;width:90px;color:#065f46;font-weight:700;'
            f'border-bottom:1px solid #e5e7eb">{e(meal.time)}</td>'
            f'<td style="padding:12px 10px;border-bottom:1px solid #e5e7eb">'
            f'<div style="text-transform:uppercase;letter-spacing:.05em;font-size:12px;color:#047857;'
            f'font-weight:700">{e(meal.title)}</div>'
            + "".join(_dish_html(d) for d in meal.dishes) + note + "</td></tr>"
        )
    prep = prep_for_tomorrow(day.date)
    prep_html = ("<h3 style='color:#065f46;margin:18px 0 6px'>Get ready for tomorrow</h3><ul>"
                 + "".join(f"<li>{e(p)}</li>" for p in prep) + "</ul>") if prep else ""
    ai_html = (f"<div style='background:#eef2ff;border-radius:8px;padding:12px 14px;margin:14px 0'>"
               f"<b>A note from the AI chef</b><br>{e(ai_note).replace(chr(10), '<br>')}</div>") if ai_note else ""
    rules = "".join(f"<li>{e(r)}</li>" for r in RULES_SUMMARY)
    return f"""<!doctype html><html><body style="margin:0;background:#f0fdf4;font-family:Arial,Helvetica,sans-serif;color:#111827">
<div style="max-width:640px;margin:0 auto;background:#ffffff;padding:20px 18px">
<h2 style="margin:0;color:#065f46">Amutha's Healthy Kitchen</h2>
<div style="color:#374151;margin:4px 0 14px">Vanakkam {e(family)}! Menu for <b>{day.date:%A, %d %B %Y}</b></div>
<div style="background:#fef3c7;border-radius:8px;padding:10px 14px;margin-bottom:12px">{e(_treat_line(day))}</div>
<table style="width:100%;border-collapse:collapse">{''.join(rows)}</table>
{_recipes_html(day)}
<p style="margin:14px 0 0"><b>Hydration:</b> {e(D.DAILY_HYDRATION)}</p>
<div style="background:#ecfeff;border-radius:8px;padding:12px 14px;margin:14px 0">
<b>Tip to win the children over:</b><br>{e(kid_tip(day.date))}</div>
{ai_html}{prep_html}
<h3 style="color:#065f46;margin:18px 0 6px">Ingredients for today</h3>
<div style="font-size:13px;color:#374151">{e(', '.join(shopping_list(day)))}</div>
<h3 style="color:#065f46;margin:18px 0 6px">Amutha's rules - all followed today</h3>
<ul style="font-size:13px;color:#374151">{rules}</ul>
<div style="font-size:11px;color:#9ca3af;margin-top:18px">Sent by the Amutha Healthy Food agent.</div>
</div></body></html>"""
