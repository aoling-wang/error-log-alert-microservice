from dataclasses import dataclass

@dataclass (frozen=True)
class LogEvent:
    timestamp: str
    level: str
    message: str