import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    log_file: str
    webhook_url: str


def load_settings() -> Settings:
    log_file = os.getenv("LOG_FILE")
    webhook_url = os.getenv("WEBHOOK_URL")

    if not log_file:
        raise ValueError("LOG_FILE environment variable is required.")

    if not webhook_url:
        raise ValueError("WEBHOOK_URL environment variable is required.")

    return Settings(
        log_file=log_file,
        webhook_url=webhook_url,
    )