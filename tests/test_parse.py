from datetime import timedelta

import pytest

from tidetime import parse_duration


def test_compound():
    assert parse_duration("1h30m") == timedelta(hours=1, minutes=30)


def test_minutes_only():
    assert parse_duration("90m") == timedelta(minutes=90)


def test_days_and_seconds():
    assert parse_duration("2d45s") == timedelta(days=2, seconds=45)


def test_fractional():
    assert parse_duration("1.5h") == timedelta(minutes=90)


def test_iso():
    assert parse_duration("PT1H30M") == timedelta(hours=1, minutes=30)
    assert parse_duration("P1DT2H") == timedelta(days=1, hours=2)


@pytest.mark.parametrize("bad", ["", "abc", "10", "5x", "P", "PT"])
def test_invalid(bad):
    with pytest.raises(ValueError):
        parse_duration(bad)


def test_uppercase_units():
    assert parse_duration("90M") == timedelta(minutes=90)
    assert parse_duration("1H30M") == timedelta(hours=1, minutes=30)
