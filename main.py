import os

# One funny single-line one-star review from a house cat about its human.
# Written exactly, with no trailing newline: byte count is a tie-break,
# so fewer bytes wins.
LINE = "One star. I knocked his glass off the table to test gravity. It worked. Would not recommend this human."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
