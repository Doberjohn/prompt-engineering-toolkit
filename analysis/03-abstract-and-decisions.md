# Checkpoint 5 — The exact abstract, and decisions taken 2026-08-14

This file records the submitted abstract **verbatim** (previously only paraphrased from
memory — see `HANDOFF.md` §6.1) and the decisions John made on 2026-08-14. It supersedes
the handoff's §6.1 paraphrase and updates §6.2/§7.

---

## 1. The submitted abstract (verbatim, pasted by John, 2026-08-14)

> Coding agents fail predictably: they execute confidently on underspecified inputs and
> produce confident nonsense. This talk introduces a quality gate pattern that scores
> GitHub issues against a calibrated rubric and refuses to let agents proceed below the
> threshold. I will cover the calibration methodology (controlled degradation, eight
> weighted sections drawn from agile and SRE research), demonstrate the gate live in
> Claude Code, and share four months of production data. Plus, there was an unexpected
> finding: a prompt that my rubric scored 10/10, which Opus 4.7 partially refused to
> execute. Rubric scoring is necessary but not sufficient for agent reliability.

**Still unknown:** whether the abstract is editable with the organizers, plus event
logistics (talk length, date, audience profile, stage network/projector constraints).
These remain the top open questions for John.

---

## 2. Decisions taken 2026-08-14 (John, via structured questions)

| Topic | Decision |
|---|---|
| Production data (claim 5) | "Likely yes" that toolkit-era usage data exists in Inkweave, but **do not mine now** — P2 deferred. P1 (controlled experiments) is the working fallback for talk section 4. |
| Opus 4.7 refusal receipts (claim 6) | **No receipts exist.** Per the audit standard: cut the claim or reduce it to an explicitly-unverified one-line aside. |
| LICENSE | Holder is **John Fanidis, year 2026** — fixed in commit `fabad28` (toolkit-only, cherry-pickable). |
| Abstract text | Provided verbatim (above). Editability not yet stated. |

---

## 3. Claim-by-claim status against the exact wording

1. **"Coding agents fail predictably… confident nonsense."** ✅ Solid; literature
   supports (Sayagh 2025, GitHub Copilot guidance). No change from handoff.
2. **"Quality gate pattern… refuses to let agents proceed below the threshold."** ✅
   Real, demo-able; formula hole patched (`ed9742b`). Note the precise mechanism for
   the talk: the skill refuses below 7.0 and routes to a rewrite, it does not merely warn.
3. **"Calibration methodology (controlled degradation, eight weighted sections drawn
   from agile and SRE research)."** ✅→⚠️ The exact wording is *more defensible than the
   handoff's paraphrase feared*: it claims the **sections** are drawn from agile/SRE
   research (true — GitHub issue-completeness + Agile + SRE sources, citations now
   corrected in `88fd244`; the abstract actually undersells by omitting the GitHub
   research stream). It does **not** claim controlled degradation comes from research.
   On stage, keep that line: degradation is the toolkit's own design, inspired by
   anchor-based calibration practice.
4. **"Demonstrate the gate live in Claude Code."** ✅ Feasible (install path empirically
   verified). Needs P4 rehearsal, including characterizing the issue-evaluator path's
   own run-to-run variance (the measured 0–3 clarifying-questions range came from the
   prompt evaluator).
5. **"Share four months of production data."** 🔴 Still the biggest risk. Decision:
   mining deferred, so as of today this claim is **unbacked**. Working plan: P1's
   controlled experiments (now running, 34 fresh evaluator sessions) become talk
   section 4, honestly labeled. **Before the talk, one of two things must happen:**
   (a) Inkweave gets mined after all and the claim is backed by whatever honestly
   exists, or (b) the abstract/talk wording is changed to match the controlled-
   experiment evidence. The claim must not reach the stage as-is.
6. **"A prompt that my rubric scored 10/10, which Opus 4.7 partially refused to
   execute."** 🔴 **No receipts** (decided today). The specific claim about Opus 4.7 is
   unverifiable and should be cut from the talk or delivered as an explicitly-unverified
   aside. Two honest salvage options:
   - **P7 (candidate):** try to *reproduce the phenomenon* on current models — e.g.,
     whether an intense mandatory-verification 10/10 prompt (Anchor 8 style) draws
     partial refusal or pushback today. If it reproduces, the talk can show a verified
     current-model instance instead of the unverifiable memory. Cheap to test; needs
     John's go-ahead.
   - **The meta move:** if the abstract is locked and promises this finding, own it on
     stage: "I made this claim without saving the transcript — my own rubric's
     Epistemics dimension would fail me for it. Here's what I can actually show." That
     line *is* the talk's thesis, practiced.
7. **"Rubric scoring is necessary but not sufficient."** ✅ Excellent thesis; the audit's
   ~1.3-point expert-vs-fresh-session offset is quantified supporting evidence, and P1
   is re-measuring it across four current models.

---

## 4. State of work packages (2026-08-14)

- **P1 — running** (workflow `wf_9d6676b6-a42`, 34 evaluator runs: test-retest on a
  novel prompt + novel issue; cross-model re-scoring of the reference issue and Anchor
  5 on fable/sonnet/opus/haiku; all three single-critical-section deletions × 4 runs
  verifying the `ed9742b` 3.9 cap). Results land in `analysis/02-empirical-tests.md`
  as an extension when complete. Note: the original A1 churn-prompt text was not
  preserved, so the retest uses a **reconstruction to the same design recipe** (role/no
  tone, steps/no checkpoints, verification/no proof rules, deliverable+audience/no
  format-length) — comparisons to A1 are distributional, not exact.
- **P2 — deferred** by John (2026-08-14). Revisit before the talk; see claim 5.
- **P3 — partially unblocked**: exact text now recorded (above); still blocked on
  editability.
- **P4, P5 — pending** logistics (length, audience, demo constraints) and P1 results.
- **P6 — open** (Tier-2 repo fixes).
- **P7 — proposed** (see claim 6): current-model refusal reproduction probe.

Open items only John can do, updated: Inkweave #278 visibility (unchanged), the
Anthropic CDN PDF check (unchanged), cherry-pick of `88fd244`, `ed9742b`, and now
`fabad28` to `main` (unchanged), abstract editability + event logistics (new top ask).
