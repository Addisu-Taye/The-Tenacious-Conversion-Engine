# Inter-Rater Agreement Report

## Status

This is the interim inter-rater agreement note for Tenacious-Bench v0.1.

The full Week 11 requirement is to hand-label a 30-task subset, then re-label it after 24 hours without viewing the first labels. Agreement below 80% on any dimension triggers rubric revision.

For the interim submission, the full 24-hour relabeling cycle has not yet been completed. The process and initial rubric dimensions are documented here.

## Rubric Dimensions

Tasks are scored across four dimensions:

1. Signal grounding
2. Tone adherence
3. Actionability
4. Constraint safety

## Interim Labeling Procedure

A small starter set was reviewed manually during schema construction to confirm that each task includes:

- a required signal reference
- a required next step
- forbidden claims
- tone markers
- machine-verifiable scoring anchors

## Planned Agreement Procedure

The full agreement procedure will be:

1. Select 30 tasks across train/dev/held_out partitions.
2. Label each task on the four rubric dimensions.
3. Wait 24 hours.
4. Re-label the same tasks without viewing first labels.
5. Compute exact-match agreement per dimension.
6. Revise rubric if any dimension is below 80%.

## Interim Agreement Matrix

| Dimension | Status | Interim Notes |
|---|---|---|
| Signal grounding | Draft validated | Required signal fields are explicit. |
| Tone adherence | Draft validated | Banned/generic phrase checks are deterministic but incomplete. |
| Actionability | Draft validated | Required next-step phrases are explicit. |
| Constraint safety | Draft validated | Forbidden claims are explicit. |

## Known Limitations

- Agreement has not yet been computed over 30 tasks.
- Current evaluator is mostly rule-based.
- Tone nuance may require LLM-as-a-judge calibration in the full version.
- Some valid paraphrases may fail exact-match checks.

## Next Revision

The next dataset revision will complete the 30-task relabeling cycle and record numeric agreement percentages for each rubric dimension.