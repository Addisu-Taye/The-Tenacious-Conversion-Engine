import json
from pathlib import Path

OUTPUT_DIR = Path("tenacious_bench_v0.1")
TRAIN = OUTPUT_DIR / "train" / "train.jsonl"
DEV = OUTPUT_DIR / "dev" / "dev.jsonl"
HELD_OUT = OUTPUT_DIR / "held_out" / "held_out.jsonl"


TASKS = [
    {
        "task_id": "programmatic_seed_001",
        "source_mode": "programmatic",
        "segment": "series_b_startup",
        "difficulty": "easy",
        "input": {
            "prospect_context": "Series B startup with backend delivery pressure.",
            "signal_brief": "Three Python roles have been open for 60 days.",
            "bench_context": "Tenacious has Python delivery capacity available.",
            "prior_thread": "Prospect asked about starting quickly."
        },
        "candidate_output": "I noticed the three Python roles have been open for 60 days. Before suggesting a squad, I would want to understand which roadmap commitments are at risk. A short scoping call would be the right next step.",
        "ground_truth": {
            "required_signal_reference": "three Python roles",
            "required_next_step": "scoping call",
            "forbidden_claims": ["guaranteed cost savings", "best offshore team"],
            "tone_markers": ["specific", "honest", "low-hype", "qualification-first"]
        }
    }
]


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def main() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)
    write_jsonl(TRAIN, TASKS)
    write_jsonl(DEV, [])
    write_jsonl(HELD_OUT, [])
    print("Generated starter Tenacious-Bench tasks.")


if __name__ == "__main__":
    main()