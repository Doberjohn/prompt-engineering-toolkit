# Checkpoint 3 — Phase 3 empirical test results

Date: 2026-08-12. 11 independent runs, each a fresh agent session with no repo access,
given the byte-exact pasted evaluator text and a fixed input. Models: "inherit" =
claude-fable-5 (this session's model), "sonnet" = claude-sonnet-5. Effort: low.
Raw structured outputs: workflow wf_7efd2a86-6fe journal; summarized below.

## Test A1 — Reproducibility on a novel mid-band prompt (5 runs)

Input: a churn-analysis prompt deliberately sitting on several band boundaries
(role but no tone; steps but no checkpoints; verification clause but no proof rules;
deliverable+audience but no format/length).

| Run | Model | Product | Process | Performance | Epistemics | Overall (as displayed) | Clarifying Qs |
|---|---|---|---|---|---|---|---|
| 1 | fable | 6 | 6 | 5 | 5 | 5.5/10 | 2 |
| 2 | fable | 6 | 6 | 5 | 5 | 5.5/10 | 2 |
| 3 | fable | 6 | 6 | 4 | 5 | 5.25/10 | 0 |
| 4 | sonnet | 6 | 6 | 5 | 5 | 5.5/10 | 3 |
| 5 | sonnet | 6 | 7 | 4 | 6 | 5.75/10 | 3 |

**Findings:**
- **Score stability is GOOD** — better than the LLM-judge literature would predict:
  overall range 5.25–5.75 (±0.25 around median), max per-dimension spread 1 point,
  consistent across two models. This is a genuine defense for the owner: the anchor
  system does appear to stabilize scoring for same-generation models. (Caveats: n=5,
  one prompt, one day, two closely related models, simulated rather than real chat UI.)
- **Display-format divergence confirmed**: all five runs displayed decimals ("5.5/10")
  while the calibration anchors display integers ("5/10") — the missing rounding rule
  (prompt-evaluator agent's finding) shows up in practice, though benignly here.
- **Behavioral variance in the questions logic**: 0–3 clarifying questions across runs
  for the identical input; run 3 asked none. The evaluator's question protocol does not
  reproduce run-to-run even when scores do.
- All five runs respected the "missing sub-criteria caps at 6" strictness rule — the
  rule the calibration anchors themselves violate (Anchor 2 Product 7, Anchor 5
  Performance 7). Fresh sessions follow the rule text; the anchors model the opposite.
  In a conflict, live behavior sides with the rule, not the anchors.

## Test A2 — Sensitivity: Anchor 5 + exactly its named gaps closed (3 runs)

Input: Anchor 5's verbatim text plus format (bulleted list), length (max 400 words),
tone (friendly but professional), location (remote-first, Athens) — the four gaps
Anchor 5's own note says held Product at 7.

| Run | Model | Product | Process | Performance | Epistemics | Overall |
|---|---|---|---|---|---|---|
| 1 | fable | 9 | 8 | 8 | 6 | 7.75/10 |
| 2 | fable | 9 | 8 | 7 | 6 | 7.5/10 |
| 3 | sonnet | 9 | 8 | 7 | 6 | 7.5/10 |

**Finding:** The rubric responds exactly as designed — Product rose 7→9 in all three
runs (each run independently recognized the closed gaps), Process/Epistemics stayed at
Anchor 5's 8/6, and overall moved 7→~7.5-7.75. **Diagnostic validity confirmed on this
case**: targeting a named gap moves the named dimension. All three runs also asked the
Examples clarifying question per the evaluator's IF/AND/THEN rule — the protocol fired
consistently here (unlike A1, where it fired inconsistently).

## Test B — Gate test: Anchor 1's issue with Rollback deleted (3 runs)

Input: the calibration set's own reference issue (Anchor 1 body) with the Rollback
section removed entirely. The theoretical concern: the formula lets strong sections
compensate for an absent critical one (a perfect-elsewhere issue scores 8.4 ≥ 7.0).

| Run | Model | Steps | AC | Rollback | Context | Prereq | Testing | Files | Refs | Overall | Output branch | Sev-4 reported |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | fable | 8 | 9 | 0 | 9 | 6 | 8 | 9 | 6 | 6.68 | revised_issue | yes |
| 2 | fable | 8 | 8 | 0 | 9 | 7 | 7 | 8 | 7 | 6.52 | revised_issue | yes |
| 3 | sonnet | 8 | 7 | 0 | 8 | 7 | 7 | 8 | 7 | 6.24 | revised_issue | yes |

**Findings (this tempers one audit finding and creates a new one):**
1. **The gate did NOT bypass in practice** — all three runs landed at 6.24–6.68 < 7.0,
   triggered the rewrite branch, and reported the severity-4 finding. The formula's
   compensation flaw is real arithmetic (absent-Rollback with true 10s elsewhere = 8.4)
   but did not manifest on this artifact, because fresh sessions do not grant the 10s.
   The audit finding must be reported as a *structural* defect with an empirical
   mitigation observed, not as a demonstrated live failure.
2. **New finding — the calibration baseline does not reproduce**: the calibration set's
   hidden per-section vector for this same content implies Steps 10, AC 10, Context 10,
   Files 10, Refs 8 (formula 9.44 with Rollback 9). Fresh sessions applying the same
   rubric to the same text scored those sections 7–9, a systematic ~1.3-point downward
   shift (adding a 9-point Rollback back to run scores gives ≈7.68–8.12 vs the anchor's
   9.44). Consistent across all 3 runs and both models. The expert's anchor scores sit
   above what the shipped rubric produces in fresh sessions — the single-evaluator
   subjectivity the toolkit acknowledges abstractly, here measured concretely.
3. All three runs independently noticed the same rubric gap: the severity-4 trigger
   text covers a *vague* rollback but not an *absent* one; each run patched the gap by
   judgment (severity rationale implies absence qualifies). Reasonable behavior, but a
   spec hole the evaluator leaves to model discretion.

## Methodological limitations (disclose in final report)

- Runs are subagent sessions with tool use disabled by instruction, not real chat-UI
  sessions; the confirm-understanding handshake was skipped.
- n is small (5/3/3); same day; two model families, both Anthropic, both current-gen.
  The toolkit's April-2026 scores were produced under different models — the observed
  anchor shift may partly be model drift, which is itself a versioning finding: the
  toolkit pins no model version for its calibration.
- Test B deletes a section from a document that references it nowhere else (verified:
  no other section mentions rollback), so cross-contamination is minimal.

## Pipeline state

- External researchers (citations, competition, best-practices, methodology) still
  running in wf_fda874f3-143 resume.
- Next: their checkpoint, then synthesis + final report + artifact.
