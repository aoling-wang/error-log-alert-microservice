import re

from error_log_alert_microservice.models.log_event import LogEvent

LOG_PATTERN = re.compile(
    r'^(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})'
    r' (?P<level>ERROR|CRITICAL)'
    r' (?P<message>.+)$'
)

def parse_log_line(line: str) -> LogEvent | None:
    match = LOG_PATTERN.match(line)
    if match:
        return LogEvent(
            timestamp=match.group('timestamp'),
            level=match.group('level'),
            message=match.group('message')
        )
    else:
        return None