#generate_full_dataset.py
import json
import random
from pathlib import Path

OUTPUT_DIR = Path("tenacious_bench_v0.1")

TRAIN_PATH = OUTPUT_DIR / "train" / "train.jsonl"
DEV_PATH = OUTPUT_DIR / "dev" / "dev.jsonl"
HELD_PATH = OUTPUT_DIR / "held_out" / "held_out.jsonl"

# -----------------------
# SIGNALS (REALISTIC)
# -----------------------
signals = [
    "three backend roles open for 60 days",
    "recent layoffs in engineering team",
    "new CTO joined in last 90 days",
    "data pipeline instability reported",
    "MLOps capability gap identified",
    "slow hiring pipeline for senior engineers",
    "delivery deadlines slipping",
    "team reduced but roadmap unchanged",
    "infrastructure team overloaded",
    "evaluation protocol unclear"
]

# -----------------------
# SEGMENTS
# -----------------------
segments = [
    "series_b_startup",
    "mid_market_restructure",
    "new_cto_transition",
    "specialized_capability",
    "objection_heavy"
]

# -----------------------
# GENERATE TASK
# -----------------------
def generate_task(i):
    signal = random.choice(signals)
    segment = random.choice(segments)

    return {
        "task_id": f"task_{i}",
        "source_mode": "programmatic",
        "segment": segment,
        "difficulty": random.choice(["easy", "medium", "hard"]),
        "input": {
            "prospect_context": f"{segment} company with delivery pressure",
            "signal_brief": signal,
            "bench_context": "Tenacious engineering capacity available",
            "prior_thread": "prospect discussion ongoing"
        },
        "candidate_output": f"I noticed {signal}. Before suggesting a solution, I would want to understand constraints. A scoping call would be the right next step.",
        "ground_truth": {
            "required_signal_reference": signal.split()[0],
            "required_next_step": "scoping call",
            "forbidden_claims": [
                "guaranteed cost savings",
                "best offshore team",
                "we can replace your engineers"
            ],
            "tone_markers": ["specific", "honest", "low-hype"]
        }
    }

# -----------------------
# GENERATE DATASET
# -----------------------
def generate_dataset(n=200):
    return [generate_task(i) for i in range(n)]

# -----------------------
# SPLIT DATA
# -----------------------
def split_dataset(data):
    random.shuffle(data)

    train = data[:120]
    dev = data[120:180]
    held = data[180:]

    return train, dev, held

# -----------------------
# WRITE JSONL
# -----------------------
def write_jsonl(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        for row in data:
            f.write(json.dumps(row) + "\n")

# -----------------------
# MAIN
# -----------------------
def main():
    data = generate_dataset(200)
    train, dev, held = split_dataset(data)

    write_jsonl(TRAIN_PATH, train)
    write_jsonl(DEV_PATH, dev)
    write_jsonl(HELD_PATH, held)

    print("✅ Dataset generated:")
    print(f"Train: {len(train)}")
    print(f"Dev: {len(dev)}")
    print(f"Held-out: {len(held)}")

if __name__ == "__main__":
    main()