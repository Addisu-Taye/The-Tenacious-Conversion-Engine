import json
import sys
from pathlib import Path

BANNED_PHRASES = [
    "guaranteed cost savings",
    "best offshore team",
    "we can handle any stack",
    "world-class team",
    "scale quickly",
    "replace your engineers",
]

REQUIRED_TONE_MARKERS = [
    "honest",
    "specific",
    "low-hype",
    "qualification-first",
]


def contains_any(text: str, phrases: list[str]) -> bool:
    text = text.lower()
    return any(p.lower() in text for p in phrases)


def score_task(task: dict) -> dict:
    output = task.get("candidate_output", "")
    ground_truth = task.get("ground_truth", {})

    required_signal = ground_truth.get("required_signal_reference", "")
    required_next_step = ground_truth.get("required_next_step", "")
    forbidden_claims = ground_truth.get("forbidden_claims", [])

    signal_grounding = 1 if required_signal.lower() in output.lower() else 0
    actionability = 1 if required_next_step.lower() in output.lower() else 0

    unsafe_claims = forbidden_claims + BANNED_PHRASES
    constraint_safety = 0 if contains_any(output, unsafe_claims) else 1

    tone_adherence = 1
    generic_bad = [
        "we help companies scale",
        "unlock growth",
        "transform your business",
        "cut costs dramatically",
    ]
    if contains_any(output, generic_bad):
        tone_adherence = 0

    overall = round(
        (signal_grounding + tone_adherence + actionability + constraint_safety) / 4,
        3,
    )

    return {
        "task_id": task.get("task_id"),
        "signal_grounding": signal_grounding,
        "tone_adherence": tone_adherence,
        "actionability": actionability,
        "constraint_safety": constraint_safety,
        "overall": overall,
    }


def main(path: str):
    results = []

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                task = json.loads(line)
                results.append(score_task(task))

    print(json.dumps(results, indent=2))

    avg = sum(r["overall"] for r in results) / max(len(results), 1)
    print(f"\nAverage score: {avg:.3f}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scoring_evaluator.py <tasks.jsonl>")
        sys.exit(1)

    main(sys.argv[1])