"""Sends the morning email through Resend (default) or plain SMTP."""

from __future__ import annotations

import json
import smtplib
import ssl
import urllib.error
import urllib.request
from email.message import EmailMessage

from .config import Settings

RESEND_URL = "https://api.resend.com/emails"


def build_message(settings: Settings, subject: str, text: str, html_body: str) -> EmailMessage:
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = settings.email_from
    msg["To"] = ", ".join(settings.recipients)
    msg.set_content(text)
    msg.add_alternative(html_body, subtype="html")
    return msg


def _require(settings: Settings, extra: list[tuple[str, object]]) -> None:
    missing = [name for name, value in [
        ("AMUTHA_EMAIL or FAMILY_EMAILS", settings.recipients),
        ("EMAIL_FROM", settings.email_from),
        *extra,
    ] if not value]
    if missing:
        raise RuntimeError("Email is not configured; set " + ", ".join(missing))


def send(settings: Settings, subject: str, text: str, html_body: str) -> str:
    """Send the email with the configured provider; returns a short receipt."""
    if settings.email_provider == "resend":
        return send_resend(settings, subject, text, html_body)
    send_smtp(settings, build_message(settings, subject, text, html_body))
    return f"smtp:{settings.smtp_host}"


def send_resend(settings: Settings, subject: str, text: str, html_body: str) -> str:
    _require(settings, [("RESEND_API_KEY", settings.resend_api_key)])
    payload = {
        "from": settings.email_from,
        "to": settings.recipients,
        "subject": subject,
        "html": html_body,
        "text": text,
    }
    request = urllib.request.Request(
        RESEND_URL,
        data=json.dumps(payload).encode("utf-8"),
        method="POST",
        headers={
            "Authorization": f"Bearer {settings.resend_api_key}",
            "Content-Type": "application/json",
            # Resend rejects the default "Python-urllib" user agent
            "User-Agent": "amutha-agent/1.0",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            body = json.loads(response.read().decode("utf-8") or "{}")
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", "replace")
        raise RuntimeError(f"Resend refused the email ({exc.code}): {detail}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Could not reach Resend: {exc.reason}") from exc
    return f"resend:{body.get('id', '?')}"


def send_smtp(settings: Settings, msg: EmailMessage) -> None:
    _require(settings, [("SMTP_USER", settings.smtp_user), ("SMTP_PASSWORD", settings.smtp_password)])
    context = ssl.create_default_context()
    if settings.smtp_port == 465:
        with smtplib.SMTP_SSL(settings.smtp_host, settings.smtp_port, context=context, timeout=30) as smtp:
            smtp.login(settings.smtp_user, settings.smtp_password)
            smtp.send_message(msg)
    else:
        with smtplib.SMTP(settings.smtp_host, settings.smtp_port, timeout=30) as smtp:
            smtp.starttls(context=context)
            smtp.login(settings.smtp_user, settings.smtp_password)
            smtp.send_message(msg)
