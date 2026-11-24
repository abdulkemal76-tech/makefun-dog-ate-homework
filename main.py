"""Dog Ate My Homework: the excuse the dog gives after being caught.

Writes one line, under 200 characters, to /output/entry.txt.
Python 3.13, standard library only.
"""

import os

LINE = (
    "Bruno here. I ate page 47 of your algebra homework at 3 a.m. because "
    "it told me to solve for x, and x was clearly hiding inside the paper."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
