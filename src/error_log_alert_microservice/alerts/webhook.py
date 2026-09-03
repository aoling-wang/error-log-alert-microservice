import httpx

from error_log_alert_microservice.models.log_event import LogEvent


class WebhookClient:
    def __init__(self, webhook_url: str) -> None:
        self.webhook_url = webhook_url

    def send_alert(self, event: LogEvent) -> None:
        payload = {
            "content": (
                f"🚨 {event.level}\n"
                f"Timestamp: {event.timestamp}\n"
                f"Message: {event.message}"
            )
        }

        response = httpx.post(
            self.webhook_url,
            json=payload,
            timeout=10.0,
        )

        response.raise_for_status()