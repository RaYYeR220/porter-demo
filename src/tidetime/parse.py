"""Parse duration strings into ``datetime.timedelta``."""

from __future__ import annotations

import re
from datetime import timedelta

_UNITS = {
    "w": "weeks",
    "d": "days",
    "h": "hours",
    "m": "minutes",
    "s": "seconds",
}

_COMPACT = re.compile(r"^(?:\d+(?:\.\d+)?[wdhms])+$", re.IGNORECASE)
_PART = re.compile(r"(\d+(?:\.\d+)?)([wdhms])", re.IGNORECASE)
_ISO = re.compile(
    r"^P(?:(?P<days>\d+)D)?(?:T(?:(?P<hours>\d+)H)?(?:(?P<minutes>\d+)M)?"
    r"(?:(?P<seconds>\d+(?:\.\d+)?)S)?)?$"
)


def _parse_iso(text: str) -> timedelta:
    match = _ISO.match(text)
    if not match or not any(match.groupdict().values()):
        raise ValueError(f"invalid ISO-8601 duration: {text!r}")
    return timedelta(**{k: float(v) for k, v in match.groupdict().items() if v})


def parse_duration(text: str) -> timedelta:
    """Parse "1h30m", "90m" or "PT1H30M" into a timedelta."""
    if not isinstance(text, str):
        raise TypeError("parse_duration() expects a string")
    text = text.strip()
    if not text:
        raise ValueError("empty duration string")
    if text.startswith("P"):
        return _parse_iso(text)
    if not _COMPACT.match(text):
        raise ValueError(f"invalid duration: {text!r}")
    total = timedelta()
    for value, unit in _PART.findall(text):
        total += timedelta(**{_UNITS[unit.lower()]: float(value)})
    return total
