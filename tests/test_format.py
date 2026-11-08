from datetime import timedelta

import pytest

from tidetime import format_duration


def test_basic():
    assert format_duration(timedelta(hours=1, minutes=30)) == "1h 30m"


def test_zero():
    assert format_duration(timedelta(0)) == "0s"


def test_days():
    assert format_duration(timedelta(days=2, seconds=5)) == "2d 5s"


def test_negative_rejected():
    with pytest.raises(ValueError):
        format_duration(timedelta(seconds=-1))
