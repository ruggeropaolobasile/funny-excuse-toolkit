import json
import random
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def load_json(path: Path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def generate_excuse(problem: str, tone: str) -> str:
    reasons = load_json(BASE_DIR / "data" / "reasons.json")
    tones = load_json(BASE_DIR / "data" / "tones.json")

    if problem not in reasons:
        available = ", ".join(sorted(reasons.keys()))
        raise ValueError(f"Problema non supportato: {problem}. Disponibili: {available}")

    if tone not in tones:
        available = ", ".join(sorted(tones.keys()))
        raise ValueError(f"Tono non supportato: {tone}. Disponibili: {available}")

    reason = random.choice(reasons[problem])
    template = tones[tone]
    return template.format(reason=reason)


def main():
    if len(sys.argv) != 3:
        print("Uso: python scripts/generate_excuse.py <problema> <tono>")
        print("Esempio: python scripts/generate_excuse.py ritardo corporate")
        sys.exit(1)

    problem = sys.argv[1]
    tone = sys.argv[2]

    try:
        excuse = generate_excuse(problem, tone)
        print(excuse)
    except ValueError as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
