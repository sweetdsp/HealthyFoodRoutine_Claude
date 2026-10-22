"""Command line entry point.

    python -m amutha_agent                 # print today's menu
    python -m amutha_agent --send          # print and email it
    python -m amutha_agent --week          # preview the next 7 days
    python -m amutha_agent --daemon        # stay running, email every morning
"""

from __future__ import annotations

import argparse
import datetime as dt
import logging
import sys
import time
from zoneinfo import ZoneInfo

from . import emailer, render
from .ai_chef import chef_note
from .config import Settings
from .planner import plan_range, plan_with_checks

log = logging.getLogger("amutha_agent")


def today_in(tz: str) -> dt.date:
    return dt.datetime.now(ZoneInfo(tz)).date()


def run_once(settings: Settings, date: dt.date, send: bool, html_out: str | None, use_ai: bool) -> None:
    day = plan_with_checks(date)  # raises if any of Amutha's rules would be broken
    note = chef_note(day, settings.ai_model) if use_ai else None
    text = render.to_text(day, settings.family_name, note)
    html_body = render.to_html(day, settings.family_name, note)
    print(render.subject(day))
    print("=" * 70)
    print(text)
    if html_out:
        with open(html_out, "w", encoding="utf-8") as f:
            f.write(html_body)
        log.info("HTML email written to %s", html_out)
    if send:
        receipt = emailer.send(settings, render.subject(day), text, html_body)
        log.info("Menu emailed to %s (%s)", ", ".join(settings.recipients), receipt)


def run_daemon(settings: Settings, use_ai: bool) -> None:
    hour, minute = map(int, settings.send_time.split(":"))
    tz = ZoneInfo(settings.timezone)
    log.info("Daemon started; emailing every day at %s %s", settings.send_time, settings.timezone)
    while True:
        now = dt.datetime.now(tz)
        target = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
        if target <= now:
            target += dt.timedelta(days=1)
        time.sleep((target - now).total_seconds())
        try:
            run_once(settings, target.date(), send=True, html_out=None, use_ai=use_ai)
        except Exception:  # keep the daemon alive; try again tomorrow
            log.exception("Failed to send today's menu")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="amutha_agent", description="Amutha's healthy daily cooking routine")
    parser.add_argument("--date", help="plan for this date (YYYY-MM-DD); default is today")
    parser.add_argument("--send", action="store_true", help="email the menu to Amutha and the family")
    parser.add_argument("--html", metavar="FILE", help="also save the HTML email to FILE")
    parser.add_argument("--week", action="store_true", help="print a 7-day overview and exit")
    parser.add_argument("--no-ai", action="store_true", help="skip the optional Claude chef note")
    parser.add_argument("--daemon", action="store_true", help="keep running and send every morning")
    args = parser.parse_args(argv)

    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    settings = Settings.from_env()
    use_ai = settings.ai_chef and not args.no_ai
    date = dt.date.fromisoformat(args.date) if args.date else today_in(settings.timezone)

    if args.week:
        for day in plan_range(date, 7):
            plan_with_checks(day.date)
            base = f" + {day.lunch_base.name}" if day.lunch_base else ""
            print(f"{day.date:%a %d %b}")
            print(f"  Breakfast: {day.breakfast.name}")
            print(f"  Fruit:     {day.fruit.name}")
            print(f"  Lunch:     {day.lunch_main.name}{base} + {day.lunch_side.name}")
            print(f"  Evening:   {day.soup.name} + {day.snack.name}")
            print(f"  Dinner:    {day.dinner.name}")
            print(f"  Bedtime:   {day.bedtime.name}")
        return 0

    if args.daemon:
        run_daemon(settings, use_ai)
        return 0

    try:
        run_once(settings, date, args.send, args.html, use_ai)
    except (RuntimeError, ValueError) as exc:
        log.error("%s", exc)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
