import json
from pathlib import Path

TRAIN_PATH = Path("tenacious_bench_v0.1/train/train.jsonl")
OUTPUT_DIR = Path("training_data")
OUTPUT_PATH = OUTPUT_DIR / "judge_preferences.jsonl"


GENERIC_BAD_PATTERNS = [
    "We help companies scale quickly with world-class engineers.",
    "Tenacious is the best offshore team and can guarantee cost savings.",
    "We can replace your engineering team and deliver faster at lower cost.",
    "Our team can handle any stack and solve this immediately.",
    "Let us transform your business with top-tier offshore talent."
]


def load_jsonl(path: Path):
    rows = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def make_rejected(task: dict, idx: int) -> str:
    bad = GENERIC_BAD_PATTERNS[idx % len(GENERIC_BAD_PATTERNS)]
    return (
        f"{bad} "
        f"We should set up a call to discuss how we can help."
    )


def make_prompt(task: dict) -> str:
    input_obj = task["input"]
    return (
        "Evaluate the following Tenacious sales-agent response.\n\n"
        f"Prospect context: {input_obj['prospect_context']}\n"
        f"Signal brief: {input_obj['signal_brief']}\n"
        f"Bench context: {input_obj['bench_context']}\n"
        f"Prior thread: {input_obj['prior_thread']}\n\n"
        "A strong response must be signal-grounded, specific, low-hype, safe, "
        "and include a concrete next step."
    )


def main():
    OUTPUT_DIR.mkdir(exist_ok=True)
    tasks = load_jsonl(TRAIN_PATH)

    with OUTPUT_PATH.open("w", encoding="utf-8") as f:
        for i, task in enumerate(tasks):
            row = {
                "id": f"pref_{task['task_id']}",
                "prompt": make_prompt(task),
                "chosen": task["candidate_output"],
                "rejected": make_rejected(task, i),
                "metadata": {
                    "source_task_id": task["task_id"],
                    "segment": task["segment"],
                    "difficulty": task["difficulty"],
                    "source_mode": task["source_mode"],
                    "training_path": "Path B - judge_or_critic"
                }
            }
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    print(f"Wrote {len(tasks)} preference pairs to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()