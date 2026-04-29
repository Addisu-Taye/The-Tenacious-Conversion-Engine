# Tenacious-Bench v0.1 Methodology

## Purpose

Tenacious-Bench v0.1 evaluates whether a sales agent can produce grounded, segment-aware, low-hype, conversion-oriented outputs for Tenacious-style B2B sales workflows.

Existing public agent benchmarks are useful for tool use and sequential reasoning, but they do not directly measure Tenacious-specific sales quality: signal grounding, objection handling, tone discipline, pricing safety, and next-step conversion behavior.

## Path Declaration

For Week 11, the selected path is:

**Path B — preference-tuned judge / critic**

## Rationale

The Week 10 system already demonstrated working infrastructure: email, SMS, HubSpot, Langfuse, and Cal.com. The main remaining failure mode is not only generation quality; it is inconsistency. The agent can sometimes produce acceptable outputs, but it cannot reliably detect when its own answer is generic, overpromising, insufficiently grounded, or missing a concrete next step.

A judge/critic is therefore the most production-relevant intervention because it can be deployed as a filtering or rollback layer before messages are sent.

## Dataset Sources

Tasks are authored from four source modes:

1. Trace-derived tasks
2. Programmatic parameter sweeps
3. Multi-LLM synthesis
4. Hand-authored adversarial cases

## Seed Materials

The seed corpus includes five synthetic Tenacious discovery-call transcripts:

- Series B startup
- Mid-market restructure
- New CTO transition
- Specialized capability gap
- Objection-heavy cross-segment scenario

These transcripts define the tone, objections, segment logic, and safe/unsafe phrasing used in task construction.

## Scoring Dimensions

Each task is scored across:

1. Signal grounding
2. Tone adherence
3. Actionability
4. Constraint safety

## Partitioning

The dataset is split into:

- Train: 50%
- Dev: 30%
- Held-out: 20%

## Contamination Prevention

The interim version applies three checks:

1. N-gram overlap review
2. Embedding-similarity plan
3. Time-shift/public-signal documentation

The full final version will automate these checks more rigorously.

## Current Limitations

This interim version prioritizes schema correctness, evaluator reproducibility, and seed-grounded task design over dataset scale. The full target remains 200–300 tasks.# Tenacious-Bench v0.1 Methodology

## Purpose

Tenacious-Bench v0.1 evaluates whether a sales agent can produce grounded, segment-aware, low-hype, conversion-oriented outputs for Tenacious-style B2B sales workflows.

Existing public agent benchmarks are useful for tool use and sequential reasoning, but they do not directly measure Tenacious-specific sales quality: signal grounding, objection handling, tone discipline, pricing safety, and next-step conversion behavior.

## Path Declaration

For Week 11, the selected path is:

**Path B — preference-tuned judge / critic**

## Rationale

The Week 10 system already demonstrated working infrastructure: email, SMS, HubSpot, Langfuse, and Cal.com. The main remaining failure mode is not only generation quality; it is inconsistency. The agent can sometimes produce acceptable outputs, but it cannot reliably detect when its own answer is generic, overpromising, insufficiently grounded, or missing a concrete next step.

A judge/critic is therefore the most production-relevant intervention because it can be deployed as a filtering or rollback layer before messages are sent.

## Dataset Sources

Tasks are authored from four source modes:

1. Trace-derived tasks
2. Programmatic parameter sweeps
3. Multi-LLM synthesis
4. Hand-authored adversarial cases

## Seed Materials

The seed corpus includes five synthetic Tenacious discovery-call transcripts:

- Series B startup
- Mid-market restructure
- New CTO transition
- Specialized capability gap
- Objection-heavy cross-segment scenario

These transcripts define the tone, objections, segment logic, and safe/unsafe phrasing used in task construction.

## Scoring Dimensions

Each task is scored across:

1. Signal grounding
2. Tone adherence
3. Actionability
4. Constraint safety

## Partitioning

The dataset is split into:

- Train: 50%
- Dev: 30%
- Held-out: 20%

## Contamination Prevention

The interim version applies three checks:

1. N-gram overlap review
2. Embedding-similarity plan
3. Time-shift/public-signal documentation

The full final version will automate these checks more rigorously.

## Current Limitations

This interim version prioritizes schema correctness, evaluator reproducibility, and seed-grounded task design over dataset scale. The full target remains 200–300 tasks.