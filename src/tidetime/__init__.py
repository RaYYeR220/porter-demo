"""tidetime: human-friendly duration parsing and formatting."""

from .format import format_duration
from .parse import parse_duration

__all__ = ["parse_duration", "format_duration"]
__version__ = "0.1.0"
