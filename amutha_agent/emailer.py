"""Sends the morning email over SMTP (works with a Gmail app password)."""

from __future__ import annotations

import smtplib
import ssl
from email.message import EmailMessage

from .config import Settings


def build_message(settings: Settings, subject: str, text: str, html_body: str) -> EmailMessage:
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = settings.email_from
    msg["To"] = ", ".join(settings.recipients)
    msg.set_content(text)
    msg.add_alternative(html_body, subtype="html")
    return msg


def send(settings: Settings, msg: EmailMessage) -> None:
    missing = [name for name, value in [
        ("AMUTHA_EMAIL or FAMILY_EMAILS", settings.recipients),
        ("SMTP_USER", settings.smtp_user),
        ("SMTP_PASSWORD", settings.smtp_password),
        ("EMAIL_FROM", settings.email_from),
    ] if not value]
    if missing:
        raise RuntimeError("Email is not configured; set " + ", ".join(missing))

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
