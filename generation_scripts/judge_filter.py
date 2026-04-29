import json
import sys
from pathlib import Path

MIN_FIELDS = [
    "task_id",
    "source_mode",
    "segment",
    "difficulty",
    "input",
    "candidate_output",
    "ground_truth",
]


def validate_task(task: dict) -> tuple[bool, list[str]]:
    errors = []

    for field in MIN_FIELDS:
        if field not in task:
            errors.append(f"missing field: {field}")

    output = task.get("candidate_output", "")
    ground_truth = task.get("ground_truth", {})

    if len(output.strip()) < 40:
        errors.append("candidate_output too short")

    if not ground_truth.get("required_signal_reference"):
        errors.append("missing required_signal_reference")

    if not ground_truth.get("required_next_step"):
        errors.append("missing required_next_step")

    if "forbidden_claims" not in ground_truth:
        errors.append("missing forbidden_claims")

    return len(errors) == 0, errors


def main(path: str) -> None:
    input_path = Path(path)
    passed = []
    failed = []

    with input_path.open("r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue

            task = json.loads(line)
            ok, errors = validate_task(task)

            if ok:
                passed.append(task)
            else:
                failed.append({"task_id": task.get("task_id"), "errors": errors})

    print(json.dumps({
        "input_file": str(input_path),
        "passed": len(passed),
        "failed": len(failed),
        "failures": failed
    }, indent=2))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generation_scripts/judge_filter.py <tasks.jsonl>")
        sys.exit(1)

    main(sys.argv[1])