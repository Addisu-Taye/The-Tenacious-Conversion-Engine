# Datasheet for Tenacious-Bench v0.1

## 1. Motivation

Tenacious-Bench v0.1 is a domain-specific evaluation dataset for B2B sales-agent behavior in the Tenacious Conversion Engine workflow. Existing public agent benchmarks evaluate generic tool use, transaction completion, and sequential reasoning, but they do not sufficiently measure Tenacious-specific behavior: signal-grounded outreach, low-hype sales tone, qualification before pitching, objection handling, pricing safety, and conversion-oriented next steps.

The dataset is intended to evaluate whether an agent can produce outputs that are not only fluent, but commercially usable in a real sales workflow.

## 2. Composition

The interim dataset contains tasks across five sales segments:

1. Series B startup
2. Mid-market restructure
3. New CTO transition
4. Specialized capability gap
5. Objection-heavy cross-segment scenario

Each task contains:

- `task_id`
- `source_mode`
- `segment`
- `difficulty`
- input context
- candidate output
- ground-truth scoring fields

The scoring dimensions are:

- signal grounding
- tone adherence
- actionability
- constraint safety

The interim partitions are:

| Partition | File | Purpose |
|---|---|---|
| Train | `tenacious_bench_v0.1/train/train.jsonl` | Development/training seed |
| Dev | `tenacious_bench_v0.1/dev/dev.jsonl` | Public validation |
| Held-out | `tenacious_bench_v0.1/held_out/held_out.jsonl` | Sealed evaluation slice |

## 3. Collection Process

Tasks were authored from a small seed corpus, including:

- Week 10 Conversion Engine outputs
- Week 10 failure patterns
- synthetic Tenacious discovery-call transcripts
- enrichment and competitor-gap output formats

The task authoring modes are:

1. Trace-derived tasks
2. Programmatic parameter sweeps
3. Multi-LLM synthesis design patterns
4. Hand-authored adversarial tasks

For the interim version, most tasks are manually authored or programmatically structured from the seed transcripts and Week 10 artifacts. The full version will expand to 200–300 tasks using the same schema and generation protocol.

## 4. Preprocessing / Cleaning / Labeling

Tasks are stored as JSONL records. Each task includes explicit ground-truth fields so the scoring evaluator can score outputs without human intervention.

The initial cleaning process checks:

- required field presence
- partition assignment
- banned phrase coverage
- required signal phrase presence
- required next-step phrase presence

For interim submission, the evaluator is rule-based with deterministic scoring. Later versions may include LLM-as-a-judge scoring for nuanced tone dimensions, with model-family separation between generator and judge to reduce preference leakage.

## 5. Uses

Intended uses:

- evaluating Tenacious-style sales-agent outputs
- testing signal-grounding behavior
- detecting generic or overhyped sales language
- measuring conversion-oriented next-step behavior
- preparing preference data for judge/critic training

Out-of-scope uses:

- evaluating general-purpose customer-service agents
- measuring factual knowledge outside provided input context
- ranking human sales representatives
- using the benchmark for real customer targeting

## 6. Distribution

The dataset is currently pre-publication and stored in the project repository for interim review. If published, the intended license is CC-BY-4.0, assuming all included content remains synthetic or publicly derived.

The held-out partition should remain sealed for final evaluation and should not be used for training.

## 7. Maintenance

The benchmark will be expanded in later phases by:

- increasing task count to 200–300
- improving source-mode balance
- adding automated contamination checks
- adding inter-rater agreement results
- adding LLM-as-a-judge calibration logs
- publishing a full HuggingFace dataset card

## 8. Data Card Layering

### Telescopic View

Tenacious-Bench v0.1 evaluates whether a sales agent can produce grounded, low-hype, conversion-oriented B2B sales responses aligned with Tenacious-style engagement.

### Periscopic View

The dataset covers multiple prospect segments and failure modes, including hiring pressure, restructuring, new executive transitions, specialized capability gaps, and skepticism about offshore delivery.

### Microscopic View

Each task includes concrete scoring anchors, such as a required signal reference, required next step, forbidden claims, and tone markers. This makes the benchmark more mechanically gradable than a generic “on-brand” rubric.