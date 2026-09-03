import os
from dataclasses import dataclass
from dotenv import load_dotenv

# Load test environment variables from a .env file if it exists

load_dotenv()

# Define a dataclass object to hold the configuration settings

@dataclass(frozen=True)
class Settings:
    log_file: str
    webhook_url: str


def load_settings() -> Settings:

    # Insert any additional logic here if needed to import logs from other sources (e.g., databases, cloud storage, etc.)

    log_file = os.getenv("LOG_FILE")
    webhook_url = os.getenv("WEBHOOK_URL")

    # Validate that the required environment variables are set

    if not log_file:
        raise ValueError("LOG_FILE environment variable is required.")

    if not webhook_url:
        raise ValueError("WEBHOOK_URL environment variable is required.")

    # Return the settings as a dataclass instance to be processed by main.py

    return Settings(
        log_file=log_file,
        webhook_url=webhook_url,
    )