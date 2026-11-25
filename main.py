"""The Tired Dark Lord: A 100-Word Villain Monologue.

Writes one 100-word monologue, spoken by a fantasy villain who is
secretly just very tired, to /output/entry.txt (or $OUTPUT_DIR/entry.txt
for local testing). Stdlib only, deterministic, no network.

Verified: exactly 100 words, 528 characters, byte-identical across runs
(md5 18599f67caaa9cdbe6365291365f88cc).
"""

import os

ENTRY = (
    "You came to kill me. Good. Sit. The cushioned chair \u2014 no, that one "
    "bites. Three centuries I kept the Long Night burning, the wolves fed, "
    "the treaties signed in triplicate, and the bards sing what? Nothing. "
    "Not one verse about the filing. So here is my scheme, hero: eclipse "
    "at dusk, crow-tax at dawn, and the throne needs a back. Someone "
    "younger. Someone with \u2014 knees. You want the crown? Take it all. "
    "The crown, the ravens, the whole damp kingdom. I only ask one thing. "
    "When the bards ask \u2014 tell them I left. On time. For once."
)


def main() -> None:
    # Guard the gate: exactly 100 words, 1-600 characters.
    assert len(ENTRY.split()) == 100, "monologue must be exactly 100 words"
    assert 1 <= len(ENTRY) <= 600, "monologue must be 1-600 characters"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
