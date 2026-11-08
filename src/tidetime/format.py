"""Format ``datetime.timedelta`` values for humans."""

from __future__ import annotations

from datetime import timedelta


def _parts(delta: timedelta) -> list[tuple[int, str]]:
    total = int(delta.total_seconds())
    if total < 0:
        raise ValueError("negative durations are not supported")
    days, rem = divmod(total, 86400)
    hours, rem = divmod(rem, 3600)
    minutes, seconds = divmod(rem, 60)
    return [
        (n, u)
        for n, u in ((days, "d"), (hours, "h"), (minutes, "m"), (seconds, "s"))
        if n
    ]


def format_duration(delta: timedelta) -> str:
    """Format a timedelta as "1h 30m". Zero becomes "0s"."""
    parts = _parts(delta)
    if not parts:
        return "0s"
    return " ".join(f"{n}{u}" for n, u in parts)
