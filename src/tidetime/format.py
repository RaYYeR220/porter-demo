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


_LONG = {"d": "day", "h": "hour", "m": "minute", "s": "second"}


def format_duration(delta: timedelta, style: str = "short") -> str:
    """Format a timedelta as "1h 30m" (style="short") or "1 hour 30 minutes"
    (style="long"). Zero becomes "0s" / "0 seconds"."""
    if style not in ("short", "long"):
        raise ValueError(f"unknown style: {style!r}")
    parts = _parts(delta)
    if style == "short":
        return " ".join(f"{n}{u}" for n, u in parts) or "0s"
    if not parts:
        return "0 seconds"
    return " ".join(f"{n} {_LONG[u]}{'' if n == 1 else 's'}" for n, u in parts)
