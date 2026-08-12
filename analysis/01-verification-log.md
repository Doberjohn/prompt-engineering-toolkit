# Checkpoint 2 — Coordinator verification log + pipeline state

Date: 2026-08-12 ~16:50 UTC.

## Session-limit incident (for the record)

The first 10-agent wave (launched ~11:50 UTC) completed 6/10 agents before the account's
5-hour session limit killed the 4 external researchers (citations, competition,
best-practices, methodology) at ~12:31 UTC. No completed work was lost — the 6 finished
reports sat in the workflow journal on disk and were extracted and pushed as checkpoint 1
(commit a94ac16) when the limit reset at 16:30 UTC. The 4 failed agents were relaunched
at ~16:40 UTC via workflow resume (cached replay for the 6, live re-run for the 4).
Lesson applied: all remaining phases are sequenced with commit+push checkpoints between
them, and heavy waves are not launched late in a budget window.

## Direct spot-verifications by the coordinator (own eyes, this session)

1. **"Expert judgment override" confirmed** — examples/issue-calibration-set.md:144:
   "Expert judgment override: formula score 9.44 rounded to 10/10 given that the gap is
   context-specific and does not reduce actionability." Resolves checkpoint-0 item 3
   (anchor 1 breaking the rounding pattern) and confirms the issue-evaluator agent's
   self-override finding.

2. **Single-change-per-anchor violation confirmed** — Anchor 2's stated degradation is
   "References section removed entirely" (issue-calibration-set.md:325), but its SQL
   block (lines 353-365) has 10 columns vs Anchor 1's 20 (lines 172-193) — dropping
   full_text, full_text_sections, version, strength, willpower, lore, move_cost,
   subtypes, rarity, number — and omits Anchor 1's "Service role write" RLS policy
   (line 198). Confirms the issue-evaluator agent's methodology-violation finding.

3. **Scoring-scale table vs formula contradiction confirmed** — the band table at
   issue-calibration-set.md:129-135 puts "one or more critical sections absent" in the
   3-4 band, while the weighted formula gives an otherwise-perfect issue with an absent
   critical section (250−40)/25 = 8.4, which passes the ≥7.0 gate. Pure arithmetic;
   verified.

4. **Strictness-rule contradiction verified from my own full read** — the rule at
   prompts/prompt-evaluator.md:55 ("A prompt missing sub-criteria should not score above
   6 on that dimension") vs Anchor 2 Product 7 with "Missing format, length, tone,
   location" (its own note) — contradiction stands as the prompt-evaluator agent claims.

5. **implement-issue gaps verified from my own full read** — no issue-type/out-of-scope
   guard anywhere in skills/implement-issue/SKILL.md; decision logic at lines 165-207
   has only two branches (>=7.0 / <7.0), no <2.0 template branch; write-back via
   `gh issue edit` at lines 202-204.

6. **Floor-clause counterexample verified (arithmetic)** — max(x, 0.5) with References=5
   alone: 10/25 = 0.4 → floored to 0.5, contradicting "applies only when all sections
   are entirely absent" (prompts/issue-evaluator.md:113).

## Cross-agent corroborations noted (independent agents, same finding)

- LLM-Rubric author misattribution ("Eisenstein" vs real authors
  Hashemi/Eisner/Rosset/Van Durme/Kedzie): found independently by prompt-evaluator and
  issue-evaluator agents via different sources; also flagged by hygiene. Treat as
  confirmed pending the citations agent's third pass.
- Inkweave issue #278 / repo 404: found independently by issue-evaluator and hygiene.
- Broken README path prompts/uiux-evaluation-prompts.md: coordinator (checkpoint 0),
  uiux, and hygiene all confirmed independently.

## Pipeline state

- **Running:** wf_fda874f3-143 resume — 4 external researchers (citations, competition,
  best-practices, methodology).
- **Running:** wf_7efd2a86-6fe — Phase 3 empirical tests, 11 runs at low effort:
  - A1: novel mid-band "churn analysis" prompt × 5 fresh evaluator sessions
    (3 inherit-model + 2 sonnet) — measures run-to-run and cross-model score variance.
  - A2: Anchor 5 text + format/length/tone/location fixes × 3 runs — tests whether
    Product moves as the rubric predicts (the anchor's own note names those exact gaps).
  - B: Anchor 1 issue with the Rollback section deleted × 3 runs — tests whether the
    7.0 gate passes an issue missing a "critical" section (formula predicts 8.00) and
    which of formula/band-table/judgment the model follows.
- **Next after both land:** checkpoint reports → cross-check citations agent vs
  issue-evaluator agent's citation findings → targeted skeptic verification only for
  major claims lacking independent corroboration → final report (analysis/REPORT.md)
  → web artifact.
