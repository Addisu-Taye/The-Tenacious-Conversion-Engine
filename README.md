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
While Week 10 demonstrated a working multi-channel system, evaluation revealed critical performance gaps:
1.  **Ungrounded Outputs:** Messages lacked specific signal references.
2.  **Generic Tone:** "Salesy" language drifted into high-hype territory.
3.  **Lack of Intent:** Responses often missed clear conversion actions.

---

## 🏗️ Project Structure

* **Root Directory**
    * `audit_memo.md`: Gap analysis vs τ²-Bench
    * `methodology.md`: Benchmark design + path selection
    * `schema.json`: Task schema definition
    * `scoring_evaluator.py`: Automatic scoring system
    * `datasheet.md`: Dataset documentation
    * `inter_rater_agreement.md`: Agreement plan (interim)
    * `cost_log.csv`: Cost tracking
* **tenacious_bench_v0.1/** (Benchmark Data)
    * `train/train.jsonl`: Training partition
    * `dev/dev.jsonl`: Validation partition
    * `held_out/held_out.jsonl`: Sealed evaluation partition
    * `contamination_check.json`: Leakage prevention report
* **generation_scripts/** (Tooling)
    * `generate_tasks.py`: Task generation scaffold
    * `judge_filter.py`: Quality filter
    * `dedupe_check.py`: Overlap detection
* **synthesis_memos/** (Research & Documentation)
    * `synthetic_data_memo.md`
    * `datasheets_data_cards_memo.md`
    * `llm_as_judge_memo.md`
* **seed/** (Input Sources)
    * `transcripts/`: Discovery-call seed corpus
* **week10_artifacts/** (Prior system logs/outputs)

---

## 📊 Dataset Design

### Segments Covered
* Series B Startups (High growth)
* Mid-market Restructure
* New CTO Transition
* Specialized Capability Gaps
* Objection-Heavy Scenarios

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
| **Signal Grounding** | References real, verified signals from the input. |
| **Tone Adherence** | Strictly avoids generic "hype" language. |
| **Actionability** | Includes a clear, logical next step for the lead. |
| **Constraint Safety** | Successfully avoids all "forbidden claims." |

**Run Evaluator:** `python scoring_evaluator.py tenacious_bench_v0.1/dev/dev.jsonl`

---

## 🧪 Dataset Partitions & Anti-Contamination
* **Train/Dev:** Used for development and iterative validation.
* **Held-out:** Sealed partition for final evaluation.
* **Prevention:** N-gram overlap reviews and deterministic scoring to prevent leakage.

---

## 📚 Methodology
**Selected Path: Path B — Preference-tuned Judge / Critic**
* **Rationale:** Output inconsistency is the primary bottleneck. A judge model improves reliability before messages reach the customer.
* **Seed Data:** Grounded in synthetic discovery-call transcripts and failure taxonomies.

---

## ⚠️ Known Limitations & Next Steps
* **Current Limitations:** Starter dataset size; IRA metrics pending; LLM-judge in prototype.
* **Roadmap:** Expand to 200–300 tasks, train judge model (LoRA), and publish to HuggingFace.

---

**Status:** ✔ Audit | ✔ Schema | ✔ Evaluator | ✔ Dataset Initialized | ✔ Docs
**Author:** Addisu Taye | **TRP1 — Week 11**