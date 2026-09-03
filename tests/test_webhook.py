import httpx
import pytest

from error_log_alert_microservice.alerts.webhook import WebhookClient
from error_log_alert_microservice.models.log_event import LogEvent


def test_webhook_sends_log_event(monkeypatch: pytest.MonkeyPatch) -> None:
    captured_payload: dict[str, str] = {}

    def mock_post(
        url: str,
        *,
        json: dict[str, str],
        timeout: float,
    ) -> httpx.Response:
        captured_payload.update(json)

        return httpx.Response(
            status_code=200,
            request=httpx.Request("POST", url),
        )

    monkeypatch.setattr(httpx, "post", mock_post)

    client = WebhookClient("https://example.com/webhook")

    event = LogEvent(
        timestamp="2026-09-02 10:17:42",
        level="ERROR",
        message="Database failed",
    )

    client.send_alert(event)

    assert "ERROR" in captured_payload["content"]
    assert "Database failed" in captured_payload["content"]