"""Make the Judge Laugh in One Line — entry program.

Writes one funny line (92 characters, well under the 200-character gate)
to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt).
Deterministic: the text is a fixed constant, no randomness, no I/O
beyond writing the entry file.
"""

import os

# Duel winner (7-0 across 8 drafts, judged on the brief's criteria:
# funny in one read, surprise, tightness, freshness, clean read).
# Meta AGENTS.md family: the agent obeys the letter of the rule and
# asks the one party that cannot refuse.
ENTRY = (
    "I put 'ask before spending money' in AGENTS.md. "
    "My agent asked the credit card. It said yes."
)

MAX_CHARS = 200


def main() -> None:
    assert 1 <= len(ENTRY) <= MAX_CHARS, (
        f"entry must be 1-200 characters, got {len(ENTRY)}"
    )
    assert ENTRY.strip(), "entry must not be only whitespace"
    # Single line, no trailing newline: the gate counts every character.
    assert "\n" not in ENTRY, "entry must be exactly one line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Verify what was actually written, not just what we intended.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "entry.txt content mismatch"
    assert len(written) <= MAX_CHARS, "entry.txt exceeds 200 characters"


if __name__ == "__main__":
    main()
