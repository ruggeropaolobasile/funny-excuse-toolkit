import json
import random
import sys
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
REVIEW_DIR = BASE_DIR / "output" / "review"
FINAL_DIR = BASE_DIR / "output" / "final"


def load_json(path: Path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def generate_candidates(problem: str, tone: str, count: int = 3):
    reasons = load_json(DATA_DIR / "reasons.json")
    tones = load_json(DATA_DIR / "tones.json")

    if problem not in reasons:
        available = ", ".join(sorted(reasons.keys()))
        raise ValueError(f"Problema non supportato: {problem}. Disponibili: {available}")

    if tone not in tones:
        available = ", ".join(sorted(tones.keys()))
        raise ValueError(f"Tono non supportato: {tone}. Disponibili: {available}")

    template = tones[tone]
    pool = reasons[problem][:]
    if len(pool) < count:
        pool = pool * count
    random.shuffle(pool)
    selected = pool[:count]
    return [template.format(reason=reason) for reason in selected]


def write_review_artifact(problem: str, tone: str, candidates: list[str]) -> Path:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = REVIEW_DIR / f"review_{timestamp}.json"
    payload = {
        "created_at": timestamp,
        "problem": problem,
        "tone": tone,
        "status": "pending_human_review",
        "candidates": [
            {"id": index + 1, "text": text} for index, text in enumerate(candidates)
        ]
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
    return path


def publish_final(text: str) -> Path:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = FINAL_DIR / f"final_{timestamp}.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(text.strip() + "\n")
    return path


def main():
    if len(sys.argv) != 3:
        print("Uso: python scripts/hitl_excuse_flow.py <problema> <tono>")
        print("Esempio: python scripts/hitl_excuse_flow.py ritardo corporate")
        sys.exit(1)

    problem = sys.argv[1]
    tone = sys.argv[2]

    try:
        candidates = generate_candidates(problem, tone)
    except ValueError as e:
        print(e)
        sys.exit(1)

    review_path = write_review_artifact(problem, tone, candidates)
    print(f"Review artifact creato: {review_path}")
    print()
    print("Candidati generati:")
    for idx, text in enumerate(candidates, start=1):
        print(f"{idx}. {text}")

    print()
    choice = input("Seleziona il numero del candidato da approvare: ").strip()
    if not choice.isdigit():
        print("Scelta non valida.")
        sys.exit(1)

    choice_index = int(choice) - 1
    if choice_index < 0 or choice_index >= len(candidates):
        print("Indice fuori range.")
        sys.exit(1)

    selected = candidates[choice_index]
    print()
    print(f"Selezionato: {selected}")
    edited = input("Modifica opzionale (invio per lasciare invariato): ").strip()
    final_text = edited if edited else selected

    print()
    approval = input("Approvi la pubblicazione finale? (yes/no): ").strip().lower()
    if approval != "yes":
        print("Pubblicazione annullata dall'umano.")
        sys.exit(0)

    final_path = publish_final(final_text)
    print(f"Output finale pubblicato in: {final_path}")


if __name__ == "__main__":
    main()
