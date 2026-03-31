from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parent.parent

REQUIRED_PATHS = [
    BASE_DIR / "README.md",
    BASE_DIR / "CHANGELOG.md",
    BASE_DIR / "docs" / "hitl-flow.md",
    BASE_DIR / "data" / "reasons.json",
    BASE_DIR / "data" / "tones.json",
    BASE_DIR / "scripts" / "generate_excuse.py",
    BASE_DIR / "scripts" / "hitl_excuse_flow.py",
    BASE_DIR / "scripts" / "validate_structure.py",
    BASE_DIR / "prompts" / "excuse-generator.md",
    BASE_DIR / "prompts" / "apology-generator.md",
    BASE_DIR / "templates" / "short.txt",
    BASE_DIR / "templates" / "corporate.txt",
    BASE_DIR / "templates" / "epic.txt",
    BASE_DIR / ".github" / "workflows" / "validate-toolkit.yml",
    BASE_DIR / ".githooks" / "pre-commit",
]


def main() -> int:
    missing = [str(path.relative_to(BASE_DIR)) for path in REQUIRED_PATHS if not path.exists()]
    if missing:
        print("Missing required files:")
        for item in missing:
            print(f"- {item}")
        return 1

    print("Toolkit structure validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
