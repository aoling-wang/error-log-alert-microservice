import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class Settings:
    log_file: str
    webhook_url: str


def load_settings() -> Settings:
    log_file = os.getenv("LOG_FILE", default="sample_logs/application.log")
    webhook_url = os.getenv("WEBHOOK_URL", default="https://discord.com/api/webhooks/1545199188638179418/4sH_fD_RpBC0BZPOB_Z6zovxTKCMu2Ul9N4-XFIN7v1UHgFwAGpH7NcSbiNz0CqgDr0h")

    if not log_file:
        raise ValueError("LOG_FILE environment variable is required.")

    if not webhook_url:
        raise ValueError("WEBHOOK_URL environment variable is required.")

    return Settings(
        log_file=log_file,
        webhook_url=webhook_url,
    )