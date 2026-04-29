# Synthesis Memo: Best Practices and Lessons Learned on Synthetic Data for Language Models

## Summary

The synthetic data paper argues that synthetic data is most useful when it is grounded in real task structure, filtered aggressively, and evaluated against held-out examples that are not generated from the same distribution. The paper is directly relevant to Tenacious-Bench because the project begins from a small seed corpus rather than a large historical labeled dataset.

The most important lesson for this project is that synthetic data should not be treated as a cheap way to create volume. It should be treated as a way to create coverage over known failure modes. For Tenacious-Bench, those failure modes include generic sales language, missing signal grounding, unsafe pricing claims, weak objection handling, and missing next steps.

## Design Choice Applied

For Tenacious-Bench v0.1, synthetic tasks are anchored to seed materials:

- discovery-call transcripts
- Week 10 agent traces
- enrichment outputs
- competitor gap briefs
- failure taxonomy

The dataset records `source_mode` for each task so that later analysis can compare trace-derived, programmatic, multi-LLM, and adversarial tasks.

## Disagreement / Limitation

The paper emphasizes scalable generation, but for this project I intentionally prioritize smaller, higher-control generation. The Tenacious domain has strong tone and commercial-safety constraints; therefore, authoring 50 diagnostic tasks is more valuable than generating 500 weakly grounded variants.

## Impact on Methodology

This memo supports the decision to make the dataset schema explicit and mechanically scorable before scaling task count. It also supports the decision to use judge filtering and contamination checks before publishing the dataset.