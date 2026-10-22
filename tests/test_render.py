import datetime as dt

from amutha_agent import render
from amutha_agent.config import Settings
from amutha_agent.emailer import build_message
from amutha_agent.planner import plan_day


def test_email_has_every_meal():
    day = plan_day(dt.date(2026, 10, 22))
    text = render.to_text(day, "Test family")
    for title in ("BREAKFAST", "FRUIT", "LUNCH", "SOUP", "DINNER", "BEDTIME"):
        assert title in text
    assert day.soup.name in text and day.fruit.name in text


def test_ai_note_is_escaped_in_html():
    day = plan_day(dt.date(2026, 10, 22))
    page = render.to_html(day, "Fam", ai_note="<script>x</script>")
    assert "<script>" not in page


def test_message_goes_to_amutha_and_family():
    s = Settings(amutha_email="amutha@example.com",
                 family_emails=["kid@example.com", "amutha@example.com"],
                 email_from="kitchen@example.com")
    assert s.recipients == ["amutha@example.com", "kid@example.com"]
    msg = build_message(s, "subj", "text", "<p>html</p>")
    assert msg["To"] == "amutha@example.com, kid@example.com"
