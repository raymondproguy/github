"""slugify: convert arbitrary text to a URL-safe slug."""
from __future__ import annotations

import re
import unicodedata


def slugify(text: str, separator: str = "-") -> str:
    """Convert *text* to a URL-safe slug.

    Args:
        text: Input string to slugify.
        separator: Character used to separate words (default "-").

    Returns:
        Lowercase slug with accents removed and non-alphanumeric characters
        replaced by *separator*.

    Raises:
        TypeError: If *text* is not a string.
        ValueError: If *separator* is empty or whitespace.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if not separator or separator.strip() == "":
        raise ValueError("separator must be a non-empty string")

    normalized = unicodedata.normalize("NFKD", text)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    lowered = ascii_text.lower()

    # Replace any run of non-alphanumeric characters with a single separator.
    slug = re.sub(r"[^a-z0-9]+", separator, lowered)
    slug = slug.strip(separator)
    return slug


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python slugify.py <text>", file=sys.stderr)
        raise SystemExit(1)
    print(slugify(sys.argv[1]))
