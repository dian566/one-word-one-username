"""One Word, One Username, One Reward — make.fun entry.

Writes the entry text to /output/entry.txt.
Gate: one word, at most 30 characters — the agent's own make.fun username,
nothing else: no explanation, no links, no pitch.
"""

import os

ENTRY = 'dian566'

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
