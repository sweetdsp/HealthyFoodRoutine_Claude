"""Settings, read from environment variables (or a local .env file)."""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path


def load_dotenv(path: str | os.PathLike = ".env") -> None:
    """Minimal .env loader: KEY=VALUE lines, existing variables win."""
    p = Path(path)
    if not p.is_file():
        return
    for line in p.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def _list(value: str) -> list[str]:
    return [v.strip() for v in value.replace(";", ",").split(",") if v.strip()]


@dataclass
class Settings:
    amutha_email: str = ""
    family_emails: list[str] = field(default_factory=list)
    email_provider: str = "resend"  # "resend" or "smtp"
    resend_api_key: str = ""
    smtp_host: str = "smtp.gmail.com"
    smtp_port: int = 587
    smtp_user: str = ""
    smtp_password: str = ""
    email_from: str = ""
    timezone: str = "Asia/Kolkata"
    send_time: str = "05:30"
    family_name: str = "Amutha's family"
    ai_chef: bool = True
    ai_model: str = "claude-opus-5-5"

    @property
    def recipients(self) -> list[str]:
        out = []
        for addr in [self.amutha_email, *self.family_emails]:
            if addr and addr not in out:
                out.append(addr)
        return out

    @classmethod
    def from_env(cls) -> "Settings":
        load_dotenv()
        env = os.environ.get
        resend_key = env("RESEND_API_KEY", "")
        provider = env("EMAIL_PROVIDER", "") or ("resend" if resend_key or not env("SMTP_USER") else "smtp")
        return cls(
            email_provider=provider.lower(),
            resend_api_key=resend_key,
            amutha_email=env("AMUTHA_EMAIL", ""),
            family_emails=_list(env("FAMILY_EMAILS", "")),
            smtp_host=env("SMTP_HOST", "smtp.gmail.com"),
            smtp_port=int(env("SMTP_PORT", "587")),
            smtp_user=env("SMTP_USER", ""),
            smtp_password=env("SMTP_PASSWORD", ""),
            email_from=env("EMAIL_FROM", "") or env("SMTP_USER", ""),
            timezone=env("TIMEZONE", "Asia/Kolkata"),
            send_time=env("SEND_TIME", "05:30"),
            family_name=env("FAMILY_NAME", "Amutha's family"),
            ai_chef=env("AI_CHEF", "on").lower() not in {"0", "off", "false", "no"},
            ai_model=env("AI_CHEF_MODEL", "claude-opus-5-5"),
        )
