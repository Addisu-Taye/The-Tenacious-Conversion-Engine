import json
import sys
from pathlib import Path
from itertools import combinations


def get_text(task: dict) -> str:
    input_obj = task.get("input", {})
    return " ".join([
        input_obj.get("prospect_context", ""),
        input_obj.get("signal_brief", ""),
        input_obj.get("bench_context", ""),
        input_obj.get("prior_thread", ""),
        task.get("candidate_output", "")
    ]).lower()


def ngrams(text: str, n: int = 8) -> set[str]:
    tokens = text.split()
    return {" ".join(tokens[i:i+n]) for i in range(max(len(tokens) - n + 1, 0))}


def load_jsonl(path: Path) -> list[dict]:
    rows = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def main(paths: list[str]) -> None:
    tasks = []
    for p in paths:
        for task in load_jsonl(Path(p)):
            task["_source_file"] = p
            tasks.append(task)

    duplicate_pairs = []

    for a, b in combinations(tasks, 2):
        overlap = ngrams(get_text(a)).intersection(ngrams(get_text(b)))
        if overlap:
            duplicate_pairs.append({
                "task_a": a.get("task_id"),
                "task_b": b.get("task_id"),
                "shared_8grams": list(overlap)[:5]
            })

    print(json.dumps({
        "tasks_checked": len(tasks),
        "duplicate_pairs": duplicate_pairs,
        "num_duplicate_pairs": len(duplicate_pairs)
    }, indent=2))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generation_scripts/dedupe_check.py <file1.jsonl> <file2.jsonl> ...")
        sys.exit(1)

    main(sys.argv[1:])