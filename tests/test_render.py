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


class _FakeResponse:
    def __init__(self, body):
        self._body = body

    def read(self):
        return self._body

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False


def test_resend_request(monkeypatch):
    import json

    from amutha_agent import emailer

    sent = {}

    def fake_urlopen(request, timeout):
        sent["url"] = request.full_url
        sent["headers"] = dict(request.header_items())
        sent["body"] = json.loads(request.data)
        return _FakeResponse(b'{"id": "abc123"}')

    monkeypatch.setattr(emailer.urllib.request, "urlopen", fake_urlopen)
    s = Settings(email_provider="resend", resend_api_key="re_test",
                 amutha_email="amutha@example.com", family_emails=["kid@example.com"],
                 email_from="Kitchen <kitchen@example.com>")
    receipt = emailer.send(s, "Menu", "plain", "<p>html</p>")

    assert receipt == "resend:abc123"
    assert sent["url"] == "https://api.resend.com/emails"
    assert sent["headers"]["Authorization"] == "Bearer re_test"
    assert sent["body"] == {"from": "Kitchen <kitchen@example.com>",
                            "to": ["amutha@example.com", "kid@example.com"],
                            "subject": "Menu", "html": "<p>html</p>", "text": "plain"}


def test_resend_needs_api_key():
    import pytest

    from amutha_agent import emailer

    s = Settings(email_provider="resend", amutha_email="a@example.com", email_from="k@example.com")
    with pytest.raises(RuntimeError, match="RESEND_API_KEY"):
        emailer.send(s, "Menu", "plain", "<p>html</p>")


def test_provider_from_env(monkeypatch):
    for key in ("EMAIL_PROVIDER", "RESEND_API_KEY", "SMTP_USER"):
        monkeypatch.delenv(key, raising=False)
    monkeypatch.setenv("RESEND_API_KEY", "re_x")
    assert Settings.from_env().email_provider == "resend"
    monkeypatch.delenv("RESEND_API_KEY")
    monkeypatch.setenv("SMTP_USER", "me@gmail.com")
    assert Settings.from_env().email_provider == "smtp"


def test_email_contains_every_recipe():
    from amutha_agent.recipes import recipe_for

    day = plan_day(dt.date(2026, 10, 31))  # Treat Night
    text = render.to_text(day, "Fam")
    page = render.to_html(day, "Fam")
    assert "TODAY'S RECIPES" in text and "Today's Recipes" in page
    for dish in day.dishes():
        r = recipe_for(dish)
        assert r is not None
        assert r.steps[0] in text
