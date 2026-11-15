"""word_wrap: wrap text to a given width per line."""
from __future__ import annotations


def word_wrap(text: str, width: int) -> str:
    """Wrap *text* so each line is at most *width* characters.

    Args:
        text: Input string (may contain newlines for paragraphs).
        width: Maximum number of characters per output line.

    Returns:
        The same text with words broken onto separate lines where needed.

    Raises:
        TypeError: If *text* is not a string or *width* is not an integer.
        ValueError: If *width* <= 0.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if not isinstance(width, int) or isinstance(width, bool):
        raise TypeError("width must be an integer")
    if width <= 0:
        raise ValueError("width must be a positive integer")

    lines = text.split("\n")
    wrapped_lines = []

    for original_line in lines:
        words = original_line.split()
        if not words:
            wrapped_lines.append("")
            continue

        current_words: list[str] = []
        current_len = 0

        for word in words:
            if current_words:
                if current_len + 1 + len(word) <= width:
                    current_words.append(word)
                    current_len += 1 + len(word)
                else:
                    wrapped_lines.append(" ".join(current_words))
                    current_words = [word]
                    current_len = len(word)
            else:
                if len(word) <= width:
                    current_words.append(word)
                    current_len = len(word)
                else:
                    for i in range(0, len(word), width):
                        wrapped_lines.append(word[i:i + width])

        if current_words:
            wrapped_lines.append(" ".join(current_words))

    return "\n".join(wrapped_lines)


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: python word_wrap.py '<text>' <width>", file=sys.stderr)
        raise SystemExit(1)
    print(word_wrap(sys.argv[1], int(sys.argv[2])))
