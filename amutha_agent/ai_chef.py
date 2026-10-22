"""Optional: a short, warm note from Claude to win the children over.

The menu itself always comes from the rule-checked planner. Claude only
writes encouragement and serving ideas for dishes already on the menu, and
the note is screened for banned words before it goes into the email. If
there is no API key, or anything goes wrong, the email is sent without it.
"""

from __future__ import annotations

import logging

from .rules import DayMenu, screen_free_text

log = logging.getLogger(__name__)

SYSTEM_PROMPT = """You help Amutha, a gold-medalist nutritionist (MSc Nutrition) from Madurai, \
get her teenage children (born after 2005, fond of junk food) to enjoy her healthy Tamil home food.

Write a short note (under 120 words) for today's email:
- 2 or 3 playful, teen-friendly serving or presentation ideas for dishes that are ALREADY on the menu.
- One line the parents can say at the table to hype the food.
- A warm sign-off with a little Tamil (in English letters).

Hard rules: do not add, replace or suggest any dish or ingredient that is not on the menu. \
Never mention cheese, paneer, mayonnaise, maida, bread, beef, pork, packaged or processed food, even as a \
comparison. Keep spice advice child-safe. Plain text only, no markdown headings."""


def _menu_text(day: DayMenu) -> str:
    lines = [f"Date: {day.date:%A %d %B %Y}"]
    for label, dish in [
        ("Breakfast", day.breakfast), ("Fruit", day.fruit), ("Lunch", day.lunch_main),
        ("Lunch base", day.lunch_base), ("Vegetable", day.lunch_side), ("Soup", day.soup),
        ("Evening snack", day.snack), ("Dinner", day.dinner), ("Bedtime", day.bedtime),
    ]:
        if dish is not None:
            lines.append(f"{label}: {dish.name}")
    return "\n".join(lines)


def chef_note(day: DayMenu, model: str = "claude-opus-5-5") -> str | None:
    try:
        import anthropic
    except ImportError:
        log.info("anthropic package not installed; skipping AI chef note")
        return None

    try:
        client = anthropic.Anthropic()
        response = client.beta.messages.create(
            model=model,
            max_tokens=2000,
            system=SYSTEM_PROMPT,
            output_config={"effort": "low"},
            betas=["server-side-fallback-2026-07-01"],
            fallbacks="default",
            messages=[{"role": "user", "content": _menu_text(day)}],
        )
    except (TypeError, anthropic.AuthenticationError):
        # TypeError: the SDK found no credentials at all
        log.info("No valid Anthropic credentials; skipping AI chef note")
        return None
    except anthropic.APIError as exc:
        log.warning("AI chef note failed: %s", exc)
        return None

    if response.stop_reason == "refusal":
        log.warning("AI chef note was declined; sending the email without it")
        return None
    text = "".join(b.text for b in response.content if b.type == "text").strip()
    if not text:
        return None
    hits = screen_free_text(text)
    if hits:
        log.warning("AI chef note mentioned %s; dropping it", ", ".join(hits))
        return None
    return text
