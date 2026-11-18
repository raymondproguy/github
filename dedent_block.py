"""dedent_block: remove common leading whitespace from a multiline string."""
from __future__ import annotations


def dedent_block(text: str) -> str:
    """Remove the common leading whitespace from every line of *text*.

    This is a stricter, predictable version of `textwrap.dedent`:
    - It finds the minimum leading whitespace among all **non‑empty** lines.
    - It strips exactly that many spaces (no tab handling).
    - Empty lines are preserved.

    Args:
        text: Multiline string to dedent.

    Returns:
        The dedented string.

    Raises:
        TypeError: If *text* is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    lines = text.splitlines(True)  # keep line endings
    if not lines:
        return ""

    # Determine the minimum leading space count among non‑empty lines.
    # Blank / whitespace‑only lines are ignored when computing min_indent.
    min_indent = None
    for line in lines:
        if line.strip() == "":
            continue
        stripped = line.lstrip(' ')
        indent = len(line) - len(stripped)
        if min_indent is None or indent < min_indent:
            min_indent = indent

    # If there were no non‑empty lines, nothing to dedent.
    if min_indent is None:
        return text

    # Strip min_indent spaces from each line.
    result_lines = []
    for line in lines:
        if line.strip() == "":
            # Preserve blank / whitespace‑only lines as‑is.
            result_lines.append(line)
        else:
            if min_indent <= len(line):
                result_lines.append(line[min_indent:])
            else:
                result_lines.append(line)

    return "".join(result_lines)


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python dedent_block.py '<multiline text>'", file=sys.stderr)
        raise SystemExit(1)
    print(dedent_block(sys.argv[1]))
