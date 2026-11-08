# tidetime

Human-friendly duration parsing and formatting. Pure standard library, Python 3.10+.

This repository is the demo repository for Porter, a front desk that answers issues from strangers: https://porter-frontdesk.vercel.app

## Install

```sh
pip install -e .
```

## Examples

```python
from datetime import timedelta
from tidetime import parse_duration, format_duration

parse_duration("1h30m")    # timedelta(seconds=5400)
parse_duration("90m")      # timedelta(seconds=5400)
parse_duration("PT1H30M")  # ISO-8601, same result

format_duration(timedelta(hours=1, minutes=30))  # "1h 30m"
format_duration(timedelta(hours=1, minutes=30), style="long")  # "1 hour 30 minutes"
```

Supported units: `w`, `d`, `h`, `m`, `s`. Fractions such as `1.5h` are allowed.

## Development

```sh
pip install -e ".[test]"
python -m pytest -q
```

See [CONTRIBUTING.md](CONTRIBUTING.md) and [CHANGELOG.md](CHANGELOG.md). MIT licensed.
