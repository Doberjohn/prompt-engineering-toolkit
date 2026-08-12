# Checkpoint 0 — First-hand verification notes (main session)

Date: 2026-08-12. These are observations verified directly by the coordinating session
before agent findings arrived. Each carries its own evidence. Agent findings will be
cross-checked against these.

Scope decisions (from owner):
- Purpose: presentation/interview defense in a few days.
- Companion app repo + live Vercel demo: OUT OF SCOPE entirely.
- Deliverable: full report committed to this branch + web artifact.

## Verified observations

1. **Broken internal reference for Epistemics N/A** — `framework/ppep-framework.md:175`
   says "When Epistemics is N/A (see Epistemics scoring guidance above for when this
   applies)" but the framework's Epistemics scoring guidance (lines 132-140) never
   defines an N/A condition. The definition only exists in `prompts/prompt-evaluator.md`
   (Anchor 7 note, lines 159-163) and `examples/prompt-calibration-set.md:176-180`.
   The framework doc — presented as the theoretical source — points to a definition
   it does not contain.

2. **Stale README instruction** — `README.md:136` tells users to open
   `prompts/uiux-evaluation-prompts.md`. That file does not exist in the tree
   (deleted in commit f6c1216); the actual files are `prompts/uiux-evaluator/{url,screenshot,codebase}-mode.md`.
   The primary "Getting started" path for the UI/UX evaluator is therefore broken.

3. **Anchor label vs formula rounding inconsistency** — `prompts/issue-evaluator.md:179-191`
   calibration table: every anchor's x/10 label equals its formula score rounded
   (8.80→9, 7.28→7, 3.88→4, 2.76→3, 1.80→2, 0.50→1 (rounded up)) EXCEPT Anchor 1, where
   formula 9.44 is labeled 10/10 (9.44 rounds to 9). Either the labeling rule is
   undocumented or Anchor 1 is special-cased without explanation.

4. **Prompt-evaluator anchor arithmetic verifies** — all nine anchors in
   `prompts/prompt-evaluator.md` / `examples/prompt-calibration-set.md`: overall =
   mean of dimension scores (Anchor 2: (7+2+3+1)/4=3.25→3; Anchor 3: 2.75→3; Anchor 4:
   5.25→5; Anchor 5: 7.0; Anchor 6: 8.0; Anchor 7: (9+10+8)/3=9.0 with Epistemics N/A;
   Anchors 8/9: all 10s). The two files are mutually consistent on scores and text.

5. **Issue-evaluator weight math is coherent** — weights 4+4+4+3+3+3+2+2 = 25; formula
   divides by 25 so max is 10.0. Score drops between consecutive anchors in the
   calibration table are all consistent with integer per-section scores (e.g. 9.44→8.80
   implies References was 8/10 × weight 2 = 16/25 = 0.64). Full recomputation against
   the per-section tables in `examples/issue-calibration-set.md` delegated to audit agent.

6. **LICENSE year anomaly** — LICENSE says "Copyright (c) 2025 John Giannelos" but the
   repo's initial commit is 2026-04-15.

7. **CI workflow dependency** — `.github/workflows/notify-companion.yml` fires only on
   pushes to main touching `prompts/**` and depends on secret `COMPANION_DEPLOY_HOOK`.
   Changes to `framework/**`, `examples/**`, `skills/**` do not trigger it. (Companion
   itself out of scope.)

8. **Skill frontmatter uses** `name`, `description`, `argument-hint`, `allowed-tools`
   (both skills; also mandated by CONTRIBUTING.md). Whether this matches the current
   official Claude Code skills spec, and whether the README's install path
   `.claude/commands/<name>/SKILL.md` (README.md:148,156) works at all — delegated to
   skills audit agent for doc-cited verdict.

## Open items pending agent evidence
- Citation verification (all 13 README references + inline citations).
- MIT vs CC BY-NC-SA 4.0 derivative-work analysis.
- Competitive landscape and Aug-2026 best-practice currency.
- Methodology rigor (93% confidence claim, single-source degradation, anchor circularity).
- Full recomputation of issue calibration per-section scores.
- UI/UX modes: Nielsen/WCAG fidelity + capability realism per mode.

## Pipeline state
- Phase 1+2 workflow launched: run ID wf_fda874f3-143 (10 agents: framework,
  prompt-evaluator, issue-evaluator, uiux, skills, hygiene, citations, competition,
  best-practices, methodology).
- Next: checkpoint agent reports here under analysis/, then Phase 3 (empirical
  reproducibility test), Phase 4 (adversarial verification of major negatives),
  then final report + artifact.
