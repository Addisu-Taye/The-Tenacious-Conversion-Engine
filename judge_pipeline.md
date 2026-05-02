# Judge Filter Pipeline Implementation

## Overview

The judge/critic model acts as a quality control layer between generation and delivery.

## Pipeline Flow

1. Agent generates candidate output
2. Output is passed to judge model
3. Judge evaluates based on:
   - signal grounding
   - tone adherence
   - actionability
   - safety constraints
4. Decision:
   - accept output
   - reject or revise output

## Training

- Model: Qwen2.5-0.5B-Instruct
- Method: LoRA fine-tuning
- Data: preference pairs (chosen vs rejected)

## Implementation

Files:

- training_data/judge_preferences.jsonl
- training/tenacious_judge_lora/
- scripts/compute_results.py

## Example Behavior

Chosen:
"I noticed your Python roles have been open for 60 days..."

Rejected:
"We help companies scale quickly..."

## Impact

- reduces generic outputs
- enforces signal grounding
- improves conversion quality

## Deployment Plan

- integrate as pre-send filter
- monitor via Langfuse
- refine with A/B testing