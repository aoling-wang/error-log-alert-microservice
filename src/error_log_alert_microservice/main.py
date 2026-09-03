from error_log_alert_microservice.alerts.webhook import WebhookClient
from error_log_alert_microservice.config import load_settings
from error_log_alert_microservice.service.aggregator import LogAggregator


def main() -> None:
    settings = load_settings()

    webhook_client = WebhookClient(
        webhook_url=settings.webhook_url,
    )

    aggregator = LogAggregator(
        log_file=settings.log_file,
        webhook_client=webhook_client,
    )

    aggregator.process()


if __name__ == "__main__":
    main()