from pathlib import Path

from error_log_alert_microservice.alerts.webhook import WebhookClient
from error_log_alert_microservice.parser.log_parser import parse_log_line


class LogAggregator:
    def __init__(self, log_file: str, webhook_client: WebhookClient) -> None:
        self.log_file = Path(log_file)
        self.webhook_client = webhook_client

    def process(self) -> None:
        with self.log_file.open("r", encoding="utf-8") as file:
            for line in file:
                event = parse_log_line(line)

                if event is not None:
                    self.webhook_client.send_alert(event)