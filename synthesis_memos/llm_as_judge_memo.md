# Synthesis Memo: LLM-as-a-Judge Survey

## Summary

The LLM-as-a-Judge literature shows that model-based evaluators can scale qualitative assessment, but they introduce risks such as bias, inconsistency, and preference leakage. For Tenacious-Bench, this is especially important because tone and objection handling cannot always be captured by deterministic rules alone.

The survey supports using a hybrid scoring strategy: deterministic rules for simple constraints and LLM-as-a-judge for nuanced tone evaluation.

## Design Choice Applied

The interim evaluator is rule-based for reproducibility. Future versions will add an LLM judge for tone adherence, but only after calibration on hand-labeled examples. The generation and judge models will be separated to reduce preference leakage.

## Disagreement / Limitation

For the interim version, I do not rely on an LLM judge as the primary evaluator. The reason is that deterministic scoring is easier to reproduce and inspect. Since this is the first version of the benchmark, transparent failure modes are more valuable than sophisticated but opaque scoring.

## Impact on Methodology

This memo justifies the current scoring evaluator while also defining the next step: calibrated LLM-based scoring for tone and sales-quality dimensions.