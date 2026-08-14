# HANDOFF — Prompt Engineering Toolkit: audit, fixes, and presentation prep

**Written:** 2026-08-14, by the Claude session that ran the full toolkit audit.
**For:** the next Claude session (cloud) continuing this work with John, and for John himself.
**Read order for a fresh session:** this file → `analysis/REPORT.md` →
`analysis/03-abstract-and-decisions.md` (2026-08-14 update: exact abstract text +
John's decisions — supersedes §6.1 and parts of §5/§7 below) → whatever the task needs.

---

## 0. Situation

John (GitHub `Doberjohn`, the repo owner) is preparing a **conference presentation** built on
this repository. He is going on holiday and will continue the work **only through Claude cloud
sessions** (his PC will be off). Everything the next session needs is in this branch; nothing
lives only on his machine or in the old conversation.

Two work streams are active:

1. **Repo credibility fixes** — an adversarial audit of this toolkit found real problems
   (fabricated citation authors, an underived "93% confidence" figure, originality
   overclaims, a scoring-formula hole). Tier-1 fixes are **already applied and pushed**
   (see §4). A few items remain that only John can do (see §5).
2. **Presentation prep** — John submitted a talk abstract whose claims partly outrun the
   evidence. The claim-by-claim assessment and proposed talk structure are in §6. Several
   decisions are blocked on John (§7), and there are ready-to-execute work packages (§8).

The project ethos, established during the audit and accepted by John: **truth-first**. The
talk's thesis is about verification; every claim on stage must survive the same adversarial
scrutiny the audit applied to the repo. Do not let convenient claims back in.

---

## 1. Repos, branches, artifacts

| Thing | Value |
|---|---|
| Main repo | `Doberjohn/prompt-engineering-toolkit` (public) |
| Working branch | `claude/prompt-toolkit-analysis-jybfdm` (pushed, tracks origin); continued 2026-08-14 on `claude/handoff-analysis-review-czbm3s`, which contains it plus later commits |
| Default branch | `main` — do **not** push to it without John's explicit OK |
| Related private repo | `Doberjohn/inkweave` — NOT in session scope; use `add_repo` if John approves mining it |
| Published audit artifact | "The PPEP Audit" — https://claude.ai/code/artifact/b96ceb32-d793-4d15-9b8b-d0285e5bfbbe (John can read it from his phone; a future session can update it in place by passing this URL to the Artifact tool) |

**Branch discipline:** a fresh cloud session will likely be assigned its own designated
branch. If continuing this work, either check out / branch from
`claude/prompt-toolkit-analysis-jybfdm` or cherry-pick from it — but push only to the branch
the new session is told to use. The two fix commits (§4) were deliberately kept free of
`analysis/` files so John can `git cherry-pick 88fd244 ed9742b` onto `main` when ready.

**Commit map of this branch** (oldest → newest, on top of `main`):

| Commit | Content |
|---|---|
| `42cd405` | Checkpoint 0 — first-hand verification notes (`analysis/00-first-hand-notes.md`) |
| `a94ac16` | Checkpoint 1 — six internal audit agent reports (`analysis/agents/`) |
| `ce02da2` | Checkpoint 2 — coordinator verification log (`analysis/01-verification-log.md`) |
| `405b3b4` | Checkpoint 3 — empirical reproducibility + gate tests (`analysis/02-empirical-tests.md`) |
| `e091dfc` | Checkpoint 4 — four external research agent reports (`analysis/agents/`) |
| `1724d8a` | Final synthesized report (`analysis/REPORT.md`, 515 lines) |
| `88fd244` | **FIX COMMIT 1** — citations, attribution, unsupported claims (toolkit files only) |
| `ed9742b` | **FIX COMMIT 2** — critical-section cap in the scoring formula (toolkit files only) |
| `3a1a7c8`+ | This handoff document and any later commits |

(Verify hashes with `git log --oneline` — trust the log over this table.)

---

## 2. What the toolkit is (60-second map)

- **`framework/ppep-framework.md`** — PPEP: four scored dimensions for prompts.
  Product/Process/Performance come **directly from the AI Fluency framework's Description
  components** (Dakan, Feller & Anthropic 2025); **Epistemics** + the rubrics + calibration
  sets are John's additions. This attribution is now explicit in the docs (it wasn't).
- **`prompts/prompt-evaluator.md`** — scores a prompt 1–10 per PPEP dimension, averaged;
  Epistemics can be N/A. Strictness rule: missing sub-criteria caps a dimension at 6.
- **`prompts/issue-evaluator.md`** — scores a GitHub issue over **eight weighted sections**
  (weights sum 25): critical = Implementation Steps, Acceptance Criteria, Rollback;
  important = Context/Why, Prerequisites, Testing; supporting = Files Affected, References.
  Formula: `max(weighted_sum/25, 0.5)`, now with the **critical-section cap** (§4).
- **`prompts/uiux-evaluator/`** — three modes (`url-mode.md`, `screenshot-mode.md`,
  `codebase-mode.md`), Nielsen heuristics + WCAG 2.2.
- **`skills/draft-issue/`**, **`skills/implement-issue/`** — Claude Code skills. The
  **quality gate**: `implement-issue` scores the issue first and **refuses to proceed below
  7.0/10**, telling the user what to fix. This gate is the heart of the talk.
- **`examples/prompt-calibration-set.md`** — 9 anchor prompts, 1/10→10/10.
- **`examples/issue-calibration-set.md`** — real Inkweave issue #278 (formula score 9.44,
  published anchor label 10/10 via a documented expert-judgment override) + 9 controlled
  degradations, each with a declared change and formula-verified score.

---

## 3. The audit: where everything lives

Produced 2026-08-11/12 by a multi-agent pipeline (10 auditor/researcher agents + empirical
test runs), coordinator-verified — **every claim in `REPORT.md` was independently
re-verified before inclusion; maintain that standard.**

| File | Contents |
|---|---|
| `analysis/REPORT.md` | **The synthesis. Read this.** Verdict, what's good, what's broken (§4.1–4.8), empirical results, competition, interview playbook, tiered fixes. |
| `analysis/00-first-hand-notes.md` | Coordinator's own file-by-file verification notes |
| `analysis/01-verification-log.md` | Which agent claims were confirmed/refuted and how |
| `analysis/02-empirical-tests.md` | The 11-run empirical study, full protocol + results |
| `analysis/agents/*.md` | 10 raw agent reports (citations, framework, methodology, skills, prompt-evaluator, issue-evaluator, uiux, hygiene, best-practices, competition) |

**Findings digest** (details + line numbers in `REPORT.md` §4):

1. **Six citations had fabricated author names** (real papers, wrong authors — e.g.
   LLM-Rubric attributed to "Eisenstein" instead of Hashemi et al.). One "et al." was a
   sole author (Sayagh). → **FIXED** in `88fd244`.
2. **"93% confidence / 7% irreducible subjectivity"** — no derivation exists anywhere.
   → **REMOVED**, replaced with honest limitations sections, in `88fd244`.
3. **Originality overclaims** — P/P/P presented as if original; "not found in most
   prompting guides" claims unprovable. → **REFRAMED** in `88fd244`.
4. **"Controlled degradation recommended by NLP evaluation research"** — the cited papers
   don't prescribe it; it's John's own (defensible) design. → **REWORDED** in `88fd244`.
5. **Formula hole** — weighted averaging let an issue with a critical section entirely
   absent score up to ~8.4 and pass the 7.0 gate. → **FIXED** in `ed9742b` (cap at 3.9 when
   Steps/AC/Rollback = 0). Verified: changes no published anchor score.
6. **Single-change-per-anchor violated** in some calibration anchors — substantively, not
   cosmetically (e.g. Anchor 2's declared change is "References removed" but its SQL also
   drops 10 of 20 columns and a security policy; Anchor 3 restores a policy Anchor 2
   removed, impossible under cumulative degradation — see `REPORT.md` §4.4). → Disclosed
   in `88fd244` wording; regenerating anchors is an open Tier-2 item (P6).
7. **Expert-anchor offset** — fresh evaluator runs score the reference issue ~1.3 points
   below John's 9.44 (see §9). Open item; feeds the talk's "not sufficient" thesis.
8. **README pointed to a deleted file** for the UI/UX evaluator. → **FIXED** in `88fd244`.
9. **LICENSE says "John Giannelos" and an inconsistent year** — repo owner is John
   Fanidis. Only John can say which name is legally right. → **OPEN (John)**.
10. **Inkweave is private** but the calibration set's ground-truth issue #278 lives there
    — external readers can't verify the set's foundation. → **OPEN (John)**.
11. **An Anthropic CDN PDF citation** couldn't be fetched from the sandbox, and per
    `REPORT.md` §4.2 it appears to actually be a course handout titled "6 Techniques for
    Effective Prompt Engineering" — i.e. the citation's title is likely wrong, not merely
    unverified. → **OPEN (John: download, confirm, retitle the citation)**.

---

## 4. Fixes already applied (pushed to the working branch)

**`88fd244` — "Correct citations, attribution, and unsupported claims"**
(touches `README.md`, `framework/ppep-framework.md`, both `examples/*.md`)
- Citation authors corrected to first-author-correct form: Hashemi et al. (LLM-Rubric,
  ACL 2024), Hong et al. (RULERS, arXiv 2601.08654), Sülün et al. (TOSEM templates),
  Zhang J. et al. (IEEE 10633301), Huang et al. (ESE s10664-018-9636-3), Acharya & Ginde
  (EASE 2025), Sayagh sole author.
- 93%/7% removed everywhere; "Confidence and limitations" sections rewritten to state the
  real limitation: single-evaluator judgment, no reliability study run yet.
- AI Fluency attribution made explicit in framework + README; Epistemics scoped as "the
  toolkit's addition"; unprovable negatives ("most guides are opinion-based") softened.
- Degradation methodology reworded as a design choice, not research-prescribed.
- README UI/UX path fixed to `prompts/uiux-evaluator/` modes.
- Nielsen severity scale noted as adapted (levels 1–4; level 0 unused).

**`ed9742b` — "Add critical-section cap to the issue scoring formula"**
(touches `prompts/issue-evaluator.md`, both `skills/*/SKILL.md`)
- If Implementation Steps, Acceptance Criteria, or Rollback scores 0 → overall capped at
  3.9. Rationale + anchor-preservation argument in the commit message.
- Floor-clause description corrected (applies below 0.5, not "only when all absent").

---

## 5. Open items only John can do

1. **LICENSE** — ~~fix holder name and year~~ **DONE 2026-08-14**: John confirmed
   "John Fanidis, 2026"; fixed in commit `fabad28` (toolkit-only, cherry-pickable).
2. **Inkweave #278 visibility** — either make `inkweave` public, or copy issue #278's full
   text into `examples/` as the canonical reference artifact (recommended: the copy).
3. **Anthropic CDN PDF** — download it, confirm it is the AI Fluency course material the
   citation claims, adjust the citation title if not.
4. **Cherry-pick fixes to `main`** — `git cherry-pick 88fd244 ed9742b fabad28` (or ask a
   session to do it with explicit permission to push `main`).

---

## 6. The presentation

### 6.1 The submitted abstract — claims (PARAPHRASED from the old conversation)

⚠️ The exact submitted text is not preserved here. **First thing to ask John: paste the
exact abstract text**, plus the event name, date, talk length, and audience profile —
none of which are recorded in the repo. His paraphrased claims:

1. Coding agents fail predictably: they execute confidently on underspecified inputs.
2. A **quality-gate pattern**: score GitHub issues against a calibrated rubric; agents may
   not proceed below threshold.
3. A **calibration methodology**: controlled degradation; eight weighted sections "drawn
   from agile and SRE research".
4. **Live demo** of the gate in Claude Code.
5. **"Four months of production data."**
6. A prompt his rubric scored 10/10 that **Opus 4.7 partially refused** to execute.
7. Thesis: **rubric scoring is necessary but not sufficient** for agent reliability.

### 6.2 Claim-by-claim status

| # | Claim | Status |
|---|---|---|
| 1 | Confident failure on underspecified input | ✅ Solid; literature supports (Sayagh 2025, GitHub Copilot guidance) |
| 2 | Quality-gate pattern | ✅ Real, works, demo-able; formula hole now patched |
| 3 | Calibration methodology | ⚠️ Present as **his design** + audit disclosure. Sections ARE synthesized from GitHub/Agile/SRE sources (true, citations now correct). Do NOT claim the degradation method comes from research. |
| 4 | Live demo | ✅ Feasible — skill install empirically verified. Needs rehearsal (§8, P4). Note: run-to-run variance is real but the measured 0–3 clarifying-questions range comes from the PROMPT evaluator (Test A1), not the issue evaluator the demo uses — P4 rehearsal must characterize the demo path's own variance. |
| 5 | **Four months of production data** | 🔴 **BIGGEST RISK.** No recorded data exists in this repo, and those months are the repo's dormancy window. Either mine `inkweave` (lead: July 2026 session artifacts show active Inkweave issue work, e.g. #472 — toolkit-era usage likely exists there) or replace with the controlled experiments, honestly labeled. **Never let this claim reach the stage unbacked.** |
| 6 | Opus 4.7 refusal of a 10/10 prompt | ⚠️ Great story IF receipts (prompt + transcript) exist. Ask John. If reproducible → slide; if not → cut or one-line aside. |
| 7 | Necessary but not sufficient | ✅ Excellent thesis. The audit **strengthens** it: the ~1.3-point offset between the author's anchor scores and fresh evaluator runs (consistent across runs AND models — cross-model spread was only ~0.3–0.4) is quantified evidence that a rubric calibrated by its author does not transfer unchanged to independent evaluators. |

### 6.3 Proposed talk structure (agreed direction; works with or without production data)

1. **The failure** — confident nonsense on an underspecified issue; one vivid example.
2. **The gate** — live demo: bad issue blocked → rewritten → passes → agent proceeds.
3. **How it's calibrated — and how I know where it's wrong.** Degradation methodology,
   then the audit findings John chooses to disclose (expert-anchor offset, the formula cap
   he added, cross-model drift). This is the credibility engine: the speaker who
   red-teamed his own tool.
4. **The data** — Inkweave mining results OR the controlled experiments, honestly labeled.
5. **The refusal** (if receipts) → **thesis**: the rubric gates what you specify; the
   model gates what it will do; reliability needs both.
6. **What's next** — human-agreement validation, model pinning, shipping as skills.

---

## 7. Decisions blocked on John — status 2026-08-14 (details in `03-abstract-and-decisions.md`)

a. Production data: **answered** — "likely yes" it exists in Inkweave, but mining
   **deferred by John**; P1 controlled experiments are the working fallback. Revisit
   before the talk — claim 5 must not reach the stage unbacked.
b. Opus 4.7 refusal receipts: **answered — none exist.** Cut or one-line unverified
   aside; see the P7 reproduction-probe proposal.
c. Abstract: **text obtained verbatim** (recorded in `03-abstract-and-decisions.md`);
   **editability still unknown** — now the top open question.
d. **Event logistics** — still open: talk length, date, audience, live-demo feasibility
   (projector, network, Claude Code access on stage vs. recorded fallback).
e. LICENSE: **answered and fixed** (`fabad28`).
f. Preferred slide tooling (pptx? reveal.js artifact? — the `pptx` skill is available in
   cloud sessions) — still open.

---

## 8. Ready-to-execute work packages

**P1 — Scaled reproducibility study** (valuable under EVERY scenario; can start without
John). Extend `analysis/02-empirical-tests.md` from 11 → 30–50 runs: (i) same-model
test-retest on 2–3 novel prompts/issues, (ii) cross-model anchor re-scoring (current
Claude generations), (iii) gate behavior under each single critical-section deletion —
now also verifying the `ed9742b` cap fires. Keep the existing protocol: fresh agent
sessions, no repo access, evaluator prompt pasted verbatim, record per-dimension/
per-section scores. Deliverable: updated `02-empirical-tests.md` + a talk-ready summary
table. This becomes talk section 4 if Inkweave data doesn't materialize.

**P2 — Inkweave data mining** (needs John's approval + `add_repo`). Inventory issues
since the toolkit's creation: which were drafted with `draft-issue` / scored by the gate
(look for scorecards in issue bodies/comments), rewrite frequency, before/after scores,
outcomes of implemented issues. Deliverable: honest quantification of whatever exists —
even "n=9 issues, here's what happened" beats a vague claim.

**P3 — Abstract redraft** (needs exact text + editability). Keep claims 1, 2, 4, 7;
reframe 3 per §6.2; replace/downgrade 5 and 6 per what P2 and the receipts yield.

**P4 — Demo script + rehearsal.** Write `analysis/demo-script.md`: a prepared bad issue
(suggest: degrade a real one, in the toolkit's own style), exact commands, expected gate
output, the rewrite, expected pass, fallback screenshots for every step (assume stage
network fails). Rehearse in a cloud session end-to-end at least twice; note variance
(clarifying-questions behavior) and how to handle it live.

**P5 — Slide deck** from the §6.3 structure once P1–P3 resolve. Include the audit-
disclosure slide (talk section 3) — it is the differentiator, don't let it get cut.

**P6 — Remaining Tier-2 repo fixes** (see `REPORT.md` §"Tier 2"): regenerate anchors that
violate single-change-per-anchor; reconcile the strictness rule vs. anchor scores in the
prompt calibration set; consider model-version pinning notes in the evaluators.

---

## 9. Key numbers (verified; sources: `analysis/02-empirical-tests.md`, `REPORT.md` §5)

- Empirical study: **11 independent runs**, 2026-08-12, fresh agent sessions, no repo access.
- **Test A1** (novel mid-band prompt, 5 runs): overall range 5.25–5.75 (**±0.25** around
  median); max per-dimension spread 1 point; 0–3 clarifying questions across runs; all
  runs respected the "missing sub-criteria caps at 6" strictness rule.
- **Test A2** (Anchor 5 with exactly its named gaps closed, 3 runs): the named dimension
  moved as predicted in all runs; Process and Epistemics held at the anchor's values in
  all runs, while Performance varied by 1 point in one of the three runs.
- **Test B** (gate test: reference issue with Rollback deleted, 3 runs): scores
  **6.24–6.68 < 7.0** — the gate held in practice in all runs (though pre-`ed9742b` the
  formula alone did not guarantee it).
- **Expert-anchor offset**: fresh runs score the reference issue **~1.3 points below** its
  formula score of 9.44 (published anchor label: 10/10 via expert override) — consistent
  across runs and models; cross-model spread in Test B was only ~0.3–0.4 points. The
  sources hedge the cause: it **may** be partly model drift since April, which — if
  confirmed — is itself a versioning finding for the talk.
- Formula: `max(weighted_sum/25, 0.5)`; gate threshold **7.0**; critical-section cap
  **3.9** (added in `ed9742b`).
- Issue #278: formula score **9.44/10**, published anchor label **10/10** (expert
  override). Calibration sets: 9 prompt anchors; 1+9 issue anchors.

---

## 10. Conduct notes for the next session

- **Verify before trusting** — including this document. The repo and git log are ground
  truth; `REPORT.md` was coordinator-verified; this handoff was written from context and
  double-checked, but if it disagrees with the repo, the repo wins.
- The paraphrased abstract (§6.1) is memory, not record — get the real text from John.
- Don't soften the two red flags (§6.2 #5, #6) to be agreeable. John explicitly asked to
  "be more honest about what is even presentable." Holding that line is the job.
- John's style in this collaboration: direct, technical, appreciates candor about his own
  work's weaknesses, wants recommendations rather than option lists.
- The published artifact (§1) can be updated in place — pass its URL to the Artifact tool
  — e.g., to add P1/P2 results so John can follow along from his phone.
