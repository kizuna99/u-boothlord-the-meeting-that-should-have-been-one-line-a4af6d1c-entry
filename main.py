# SPDX-License-Identifier: MIT
"""Write the Meeting That Should Have Been One Line entry to /output/entry.txt."""
import os
from pathlib import Path

ENTRY_TEXT = (
    "Decision: we ship Friday, cut the scope, "
    "and never meet about this again."
)


def render() -> bytes:
    """Return the entry exactly as it must land on disk (no trailing newline)."""
    return ENTRY_TEXT.encode("utf-8")


def main() -> None:
    data = render()
    text = data.decode("utf-8")
    assert 1 <= len(text) <= 200 and text.strip(), "entry must be 1-200 chars"
    assert text.count(".") <= 2, "one line, one sentence plus its closer"
    out = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(data)


if __name__ == "__main__":
    main()
