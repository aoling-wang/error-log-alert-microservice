from error_log_alert_microservice.parser.log_parser import parse_log_line

def test_parse_error_log() -> None:
    log_line = "2024-06-01 12:34:56 ERROR Database connection failed"
    parse_event = parse_log_line(log_line)

    assert parse_event is not None
    assert parse_event.timestamp == "2024-06-01 12:34:56"
    assert parse_event.level == "ERROR"
    assert parse_event.message == "Database connection failed"

def test_parse_critical_log() -> None:
    log_line = "2024-06-01 12:35:00 CRITICAL System outage detected"
    parse_event = parse_log_line(log_line)

    assert parse_event is not None
    assert parse_event.timestamp == "2024-06-01 12:35:00"
    assert parse_event.level == "CRITICAL"
    assert parse_event.message == "System outage detected"

def test_parse_other_log() -> None:
    log_line = "2024-06-01 12:35:00 INFO Application started"
    parse_event = parse_log_line(log_line)

    assert parse_event is None