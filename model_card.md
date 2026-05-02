# Model Card: Tenacious Judge LoRA

## Model

**Adapter name:** `tenacious_judge_lora`  
**Base model:** `Qwen/Qwen2.5-0.5B-Instruct`  
**Training method:** LoRA supervised judge-selection training  
**Path:** Path B — judge / critic  

---

## Purpose

This adapter is trained to act as a lightweight critic for Tenacious-style B2B sales-agent outputs. It learns to prefer responses that are:

*   **Grounded** in the provided business signal
*   **Specific** and low-hype
*   **Safe** from exaggerated commercial claims
*   **Oriented** toward a concrete next step

---

## Training Data

Training data comes from:  
`training_data/judge_preferences.jsonl`

Each row contains:
*   **Prompt**
*   **Chosen:** Follows Tenacious tone and grounding constraints.
*   **Rejected:** Intentionally contains common failure modes such as generic sales language, overpromising, or missing signal grounding.

---

## Training Configuration

| Parameter | Value |
| :--- | :--- |
| **Train size** | 108 |
| **Eval size** | 12 |
| **Epochs** | 2 |
| **Trainable parameters** | 8,798,208 |
| **Total parameters** | 502,830,976 |
| **Trainable percentage** | 1.7497% |

### Training Results

| Epoch | Training Loss | Validation Loss |
| :--- | :--- | :--- |
| 1 | 1.890827 | 0.719504 |
| 2 | 0.356951 | 0.292725 |

---

## Intended Use

The adapter is intended as a **judge/critic layer** for the Tenacious Conversion Engine. It can be used to score or filter candidate outputs before outreach is sent.

---

## Limitations

*   The dataset is synthetic and programmatically generated.
*   Human inter-rater agreement is not fully completed.
*   The model has not yet been evaluated on a large sealed held-out set.
*   **It should not be used for real customer outreach without human review.**

---

## Ethical / Safety Notes

The model should be used to reduce generic or unsafe sales language. It should not be used to automate unreviewed outreach to real prospects.