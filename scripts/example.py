"""Display the location of the portable guided-collaboration rules."""

from pathlib import Path


def main() -> None:
    rules_path = Path(__file__).resolve().parent.parent / "references" / "universal-rules.md"
    print(rules_path)


if __name__ == "__main__":
    main()
