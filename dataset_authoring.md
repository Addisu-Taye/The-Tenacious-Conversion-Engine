# Dataset Authoring: Four-Mode Implementation

Tenacious-Bench v1.0 uses a four-mode dataset construction strategy to ensure coverage, realism, and robustness.

## 1. Trace-Derived Tasks

Source:
- Week 10 Langfuse traces
- Agent outputs and failure cases

Purpose:
- Capture real system behavior
- Identify failure patterns such as generic messaging and missing signal grounding

## 2. Programmatic Generation

Source:
- generation_scripts/generate_full_dataset.py

Method:
- Controlled variation across:
  - signals (hiring, layoffs, leadership)
  - segments (startup, mid-market, CTO transition)
  - difficulty levels

Purpose:
- Scale dataset to 200+ tasks
- Ensure structured coverage

## 3. Multi-LLM Synthesis (Design Stage)

Method:
- Prompt-based generation of variations across:
  - tone
  - objection handling
  - capability positioning

Purpose:
- Introduce linguistic diversity
- Simulate realistic variations

## 4. Adversarial Task Design

Method:
- Manual + programmatic injection of failure cases:
  - generic sales language
  - unsafe claims
  - missing next steps

Purpose:
- Stress-test agent robustness
- Improve evaluation sensitivity

## Summary

This four-mode approach ensures:
- realism (trace-derived)
- scalability (programmatic)
- diversity (multi-LLM)
- robustness (adversarial)