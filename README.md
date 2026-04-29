# 🚀 Tenacious-Bench v0.1 (Week 11 Interim Submission)
**Addisu Taye — TRP1 Week 11**

---

## 📌 Overview
Tenacious-Bench v0.1 is a **domain-specific evaluation benchmark** designed to measure the performance of AI agents in **B2B sales workflows**. Unlike generic benchmarks (e.g., τ²-Bench), this evaluates performance against the nuanced realities of high-stakes outreach.

### Key Focus Areas
* **Signal-grounded outreach:** Ensuring references to lead data are accurate and relevant.
* **Low-hype tone:** Maintaining a constraint-safe, professional sales voice.
* **Objection handling:** Managing complex pushback effectively.
* **Conversion-oriented next steps:** Driving measurable outcomes.

---

## 🧠 Motivation
While Week 10 demonstrated a working multi-channel system (Email, SMS, CRM, Booking), evaluation revealed critical performance gaps:
1.  **Ungrounded Outputs:** Messages lacked specific signal references.
2.  **Generic Tone:** "Salesy" language drifted into high-hype territory.
3.  **Lack of Intent:** Responses often missed clear conversion actions.

**Tenacious-Bench** was built to codify these requirements into a measurable framework.

---

## 🏗️ Project Structure
.
├── audit_memo.md                 # Gap analysis vs τ²-Bench
├── methodology.md                # Benchmark design + path selection
├── schema.json                   # Task schema definition
├── scoring_evaluator.py          # Automatic scoring system
├── datasheet.md                  # Dataset documentation
├── inter_rater_agreement.md      # Agreement plan (interim)
├── cost_log.csv                  # Cost tracking
├── tenacious_bench_v0.1/
│   ├── train/train.jsonl         # Training partition
│   ├── dev/dev.jsonl             # Validation partition
│   ├── held_out/held_out.jsonl   # Sealed evaluation partition
│   └── contamination_check.json  # Leakage prevention report
├── generation_scripts/
│   ├── generate_tasks.py         # Task generation scaffold
│   ├── judge_filter.py           # Quality filter
│   └── dedupe_check.py           # Overlap detection
├── synthesis_memos/
│   ├── synthetic_data_memo.md
│   ├── datasheets_data_cards_memo.md
│   └── llm_as_judge_memo.md
├── seed/
│   └── transcripts/              # Discovery-call seed corpus (5 files)
└── week10_artifacts/             # Prior system outputs

---

## 📊 Dataset Design

### Segments Covered
* **Series B Startups:** High-growth agility.
* **Mid-market Restructure:** Complex organizational change.
* **New CTO Transition:** Specific persona-based outreach.
* **Specialized Capability Gaps:** Technical solution matching.
* **Objection-Heavy Scenarios:** Resistance-focused stress testing.

### Task Schema (Simplified)
{
  "input": {...},
  "candidate_output": "...",
  "ground_truth": {
    "required_signal_reference": "...",
    "required_next_step": "...",
    "forbidden_claims": ["..."]
  }
}

---

## ⚙️ Scoring System
The evaluator analyzes each candidate output across four primary dimensions:

| Dimension | Description |
| :--- | :--- |
| Signal Grounding | References real, verified signals from the input. |
| Tone Adherence | Strictly avoids generic "hype" language. |
| Actionability | Includes a clear, logical next step for the lead. |
| Constraint Safety | Successfully avoids all "forbidden claims." |

**Run Evaluator:**
python scoring_evaluator.py tenacious_bench_v0.1/dev/dev.jsonl

---

## 🧪 Dataset Partitions & Anti-Contamination
* **Train:** Used for model development and fine-tuning.
* **Dev:** Used for validation and iterative testing.
* **Held-out:** Sealed partition for final, unbiased evaluation.

### Contamination Prevention
To ensure integrity, the following checks are implemented:
* N-gram overlap reviews.
* Planned embedding similarity checks.
* Physical separation of the held-out partition.
* Deterministic scoring to prevent judge leakage.

---

## 📚 Methodology
**Selected Path: Path B — Preference-tuned Judge / Critic**

* **Rationale:** The Week 10 system is functionally sound; the primary bottleneck is output inconsistency. Implementing a judge model improves reliability and "sanity checks" messages before they reach the customer.
* **Seed Data:** Grounded in synthetic discovery-call transcripts, Week 10 trace logs, failure taxonomies, and enrichment outputs.

---

## ⚠️ Known Limitations & Next Steps

### Current Limitations
* Dataset size is currently a "starter" version.
* Inter-rater agreement (IRA) metrics are still being computed.
* LLM-as-a-Judge integration is in the prototyping phase.

### Roadmap to Final Submission
1.  **Scale:** Expand dataset to 200–300 high-quality tasks.
2.  **Train:** Implement judge model training via LoRA.
3.  **Validate:** Compute confidence intervals and publish to HuggingFace.
4.  **Ablate:** Run experiments to determine the impact of different prompts.

---

**Status:** ✔ Audit | ✔ Schema | ✔ Evaluator | ✔ Dataset Initialized | ✔ Docs

**Author:** Addisu Taye | **TRP1 — Week 11**