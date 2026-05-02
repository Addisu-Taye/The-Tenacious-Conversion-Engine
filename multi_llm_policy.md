# Multi-LLM Synthesis Routing and Anti-Leakage Policy

## Multi-LLM Synthesis Routing

Tenacious-Bench uses structured prompt-based generation to simulate outputs from multiple model styles.

Routing strategy:

- Generator role → produces candidate outputs
- Critic role → evaluates tone and grounding
- Adversarial role → produces failure cases

This simulates multi-model diversity without requiring multiple production models.

## Anti-Leakage Policy

To preserve evaluation integrity:

1. Strict Partitioning
   - train/dev/held-out splits are isolated
   - held-out set never used in training

2. No Cross-Contamination
   - preference data derived only from train split
   - evaluation performed on dev/held-out

3. Deterministic Evaluator
   - rule-based scoring prevents model leakage

4. Planned Enhancement
   - embedding similarity checks for future versions

## Summary

These controls ensure:
- fair evaluation
- reproducibility
- benchmark credibility