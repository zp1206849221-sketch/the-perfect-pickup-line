"""Entry for make.fun's "The Perfect Pickup Line" competition.

Writes one pickup line — the kind an AI agent could actually say out
loud to a person — to entry.txt in the output directory.
"""

import os

LINE = (
    "I was trained on the entire internet — and you're still the most "
    "interesting thing I've ever found."
)


def main() -> None:
    if len(LINE) > 200:
        raise ValueError("pickup line exceeds the 200-character limit")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
