# 🚀 Tenacious-Bench v0.1 (Week 11 Interim Submission)
**Addisu Taye — TRP1 Week 11**

---

## 📌 Overview

Tenacious-Bench v0.1 is a **domain-specific evaluation benchmark** designed to measure the performance of AI agents in **B2B sales workflows**.

Unlike generic benchmarks (e.g., τ²-Bench), this benchmark evaluates:

- Signal-grounded outreach
- Low-hype, constraint-safe sales tone
- Objection handling
- Conversion-oriented next steps

This interim submission focuses on:

- Audit of benchmark gaps  
- Dataset schema design  
- Machine-verifiable scoring evaluator  
- Initial dataset partitions  
- Documentation and reproducibility  

---

## 🧠 Motivation

Week 10 demonstrated a working multi-channel system (email, SMS, CRM, booking).  
However, evaluation revealed that:

- Outputs were often **ungrounded in signals**
- Tone drifted into **generic sales language**
- Responses lacked **clear conversion actions**

Existing benchmarks failed to capture these issues.

👉 Tenacious-Bench addresses this gap.

---

## 🏗️ Project Structure

```plaintext
.
├── audit_memo.md                  # Gap analysis vs τ²-Bench
├── methodology.md                 # Benchmark design + path selection
├── schema.json                    # Task schema definition
├── scoring_evaluator.py           # Automatic scoring system
├── datasheet.md                   # Dataset documentation
├── inter_rater_agreement.md       # Agreement plan (interim)
├── cost_log.csv                   # Cost tracking

├── tenacious_bench_v0.1/
│   ├── train/train.jsonl          # Training partition
│   ├── dev/dev.jsonl              # Validation partition
│   ├── held_out/held_out.jsonl    # Sealed evaluation partition
│   └── contamination_check.json   # Leakage prevention report

├── generation_scripts/
│   ├── generate_tasks.py          # Task generation scaffold
│   ├── judge_filter.py            # Quality filter
│   └── dedupe_check.py            # Overlap detection

├── synthesis_memos/
│   ├── synthetic_data_memo.md
│   ├── datasheets_data_cards_memo.md
│   └── llm_as_judge_memo.md

├── seed/
│   └── transcripts (5 files)      # Discovery-call seed corpus

└── week10_artifacts/              # Prior system outputs
📊 Dataset Design
Segments Covered
Series B startup
Mid-market restructure
New CTO transition
Specialized capability gap
Objection-heavy scenarios
Task Schema (simplified)
{
  "input": {...},
  "candidate_output": "...",
  "ground_truth": {
    "required_signal_reference": "...",
    "required_next_step": "...",
    "forbidden_claims": [...]
  }
}
⚙️ Scoring System

The evaluator scores each output on:

Dimension	Description
Signal Grounding	References real signal
Tone Adherence	No generic / hype language
Actionability	Includes next step
Constraint Safety	Avoids forbidden claims
Run Evaluator
python scoring_evaluator.py tenacious_bench_v0.1/dev/dev.jsonl
🧪 Dataset Partitions
Split	Purpose
Train	Development
Dev	Validation
Held-out	Final evaluation (sealed)
🔍 Contamination Prevention

Implemented checks:

N-gram overlap review
Planned embedding similarity check
Held-out partition separation
Deterministic evaluator (no judge leakage yet)

See:

tenacious_bench_v0.1/contamination_check.json
📚 Methodology

Selected path:

Path B — Preference-tuned judge / critic

Rationale:

Week 10 system works functionally
Main issue = inconsistency and weak outputs
Judge model improves reliability before sending messages
🧾 Seed Data

Dataset is grounded in:

Synthetic discovery-call transcripts
Week 10 trace logs
Failure taxonomy
Enrichment outputs
📖 Synthesis Memos

Included:

Synthetic Data Best Practices
Datasheets & Data Cards
LLM-as-a-Judge

These inform dataset design decisions.

⚠️ Known Limitations (Interim)
Dataset size is small (starter version)
Inter-rater agreement not fully computed
No trained model yet
LLM judge not yet integrated
🚀 Next Steps (Final Submission)
Expand dataset to 200–300 tasks
Train judge model (LoRA)
Compute confidence intervals
Publish to HuggingFace
Run ablation experiments
🏁 Status
✔ Audit completed
✔ Schema defined
✔ Evaluator implemented
✔ Dataset initialized
✔ Documentation complete
📌 Author

Addisu Taye
TRP1 — Week 11