# Prompt Engineering Toolkit — Complete Analysis

**Prepared:** 2026-08-12, for the owner's upcoming presentation/interview defense.
**Scope:** this repository only (companion app and live demo excluded by owner instruction).
**Method:** 10-agent audit fleet (6 internal auditors, 4 external researchers) + 11-run
empirical experiment + coordinator verification pass. Every claim below carries evidence
(file:line, arithmetic, or web source) and survived cross-checking; confidence is flagged
where it is less than high. Full per-agent evidence: `analysis/agents/*.md`. Empirical
raw results: `analysis/02-empirical-tests.md`.

---

## 1. Verdict

This is a **well-crafted teaching artifact wearing the costume of a measurement
instrument** — and the costume is where nearly all the trouble lives.

The genuinely good parts are real: the Epistemics dimension is a sharp, practice-derived
contribution that anticipated where Anthropic's own guidance later went; the calibration-
anchor mechanism demonstrably stabilizes scoring (we measured it); the two Claude Code
skills are disciplined, working prompt engineering; the internal arithmetic reproduces
exactly; and the intellectual lineage (Anthropic's AI Fluency framework) is real,
current, and honestly attributed at the competency level.

The serious problems cluster into three groups: **originality overclaims** (three of the
four "PPEP" dimensions are Anthropic's own named components of the Description
competency, undisclosed), **a scholarly apparatus that fails spot-checks** (six
fabricated author attributions, an unverifiable quotation, a methodology claim none of
its cited sources support, and a "93% confidence" figure with no derivation), and
**measurement design that contradicts itself** (a weighted formula that defeats the
rubric's own criticality story, calibration anchors that violate the evaluator's own
scoring rules, and zero external validation of anything).

None of this is fatal for a presentation — *if* the claims are corrected first. The
underlying work is defensible as "I operationalized Anthropic's Description competency
into scoreable rubrics, added a novel Epistemics dimension, and built calibration sets —
here is what I learned, including what I got wrong." It is indefensible as "a
research-backed framework with 93% confidence." Section 7 gives the fix list and the
hard-question playbook.

---

## 2. How this analysis was produced

- **Fleet:** 6 internal auditors (framework, prompt-evaluator+calibration,
  issue-evaluator+calibration, UI/UX modes, skills, repo hygiene) and 4 external
  researchers (citation verification, competitive landscape, Aug-2026 best practices,
  evaluation methodology), all required to prove every claim with file:line quotes,
  shown arithmetic, or fetched/searched web sources, and to report confidence per finding.
- **Empirical phase:** 11 fresh-session runs (two Claude models) measuring score
  reproducibility, rubric sensitivity, and quality-gate behavior on controlled inputs.
- **Verification:** every critical/major finding in this report is corroborated by at
  least two independent agents using different methods, verified directly by the
  coordinator against the files, or is pure arithmetic. One finding (the gate bypass)
  was *downgraded* after empirical testing contradicted its worst-case reading — the
  adversarial process ran in both directions.
- **Known limitations:** several primary sources (nngroup.com, w3.org, arxiv.org,
  aclanthology.org, anthropic.com, Hertzum 2006 full text) were unreachable through this
  environment's egress proxy; facts from them were verified via multiple concordant
  secondary sources and are flagged medium confidence where that matters. Empirical
  tests are small-n (5/3/3), one day, Anthropic-family models only, simulated sessions.

---

## 3. What is genuinely good

Each item survived deliberate attack. These are the load-bearing walls of the
presentation story.

1. **The Epistemics dimension is a real contribution.** "Inventory before judging,"
   "negative claims require proof (show the search)," and "no summarizing as facts" do
   not appear as *named scoring criteria* in Anthropic's or OpenAI's guides (verified
   against both), nor in any named prompt framework (CO-STAR, CRISPE, RISEN, RACE, TCREI
   — surveyed). Anthropic's current best-practices doc now ships an
   `<investigate_before_answering>` pattern ("Never speculate about code you have not
   opened") that is nearly this dimension written by Anthropic itself — the toolkit
   *anticipated* official guidance. The paired weak/strong example
   (`framework/ppep-framework.md:119-127`) is the best pedagogy in the repo.
2. **The calibration-anchor mechanism works — we measured it.** Five fresh sessions
   across two models scored a novel mid-band prompt within 5.25–5.75 overall (max
   per-dimension spread: 1 point). That is *better* stability than the LLM-judge
   literature would predict for unanchored 1-10 scoring. Closing exactly the four gaps
   Anchor 5's note names moved Product 7→9 in 3/3 runs — the rubric is diagnostic in
   the designed direction. (Caveats in §5.)
3. **The internal arithmetic is honest.** All nine prompt-anchor overalls equal the mean
   of their dimension scores; all ten issue-anchor formula scores (including the
   headline 9.44) reproduce exactly from a single consistent per-section vector; weights
   sum to 25; evaluator and calibration files agree verbatim on anchor texts and scores.
   The numbers were computed, not invented.
4. **The skills are the best-engineered artifacts in the repo.** Valid frontmatter per
   the current spec, explicit WAIT gates before every irreversible action, bounded
   clarifying-question protocols, deterministic templates, a cross-skill quality-gate
   handoff — and the README's contested install path **actually works on current Claude
   Code v2.1.228** (empirically tested with planted-token probes), though it is an
   undocumented legacy layout (see §4.7).
5. **The three-tier VERIFIED/INFERRED/SUSPECTED confidence labeling** in the UI/UX
   prompts, with mandatory per-finding format and "to verify" instructions, is genuinely
   rare epistemic design, and each mode ships a mandatory "what this mode cannot assess"
   disclosure.
6. **The AI Fluency lineage is real and honestly attributed at the competency level.**
   The 4D definitions match Anthropic's official ones; the CC BY-NC-SA license note and
   the HEA Ireland support note are accurate; the framework is still live and taught
   (Coursera/Skilljar, Aug 2026).
7. **Most citations exist.** 30 of 31 unique external sources resolve to real, topically
   relevant documents. Several suspicious-looking ones are fully real: "CorsoUX" is the
   actual brand of courseux.com (quote verified near-verbatim on the page); the Sayagh
   arXiv paper (2512.21426) is real, on-point, correctly dated; the GitHub Copilot
   "ideal task" quotation is verbatim-accurate; "25+ citations" is numerically exact (25).
8. **The closed loop is a real, unowned niche.** Same 8-section rubric driving an
   evaluator prompt + a drafting skill + an implement-time quality gate does not exist
   as a packaged unit anywhere we searched, despite issue-creation skills being commodity
   (15,360 SKILL.md files on GitHub contain `gh issue create`).
9. **Candid limitation prose (in places).** The calibration sets disclose
   single-evaluator scoring and explicitly refuse to generalize from nine examples —
   better epistemic hygiene than the README that markets them.

---

## 4. What is broken

Ordered by interview lethality, not by count. **CRITICAL** = will end an interview badly
if discovered live. **MAJOR** = a sharp interviewer finds it in minutes. **MINOR** =
credibility erosion.

### 4.1 Originality overclaims (CRITICAL)

- **Product/Process/Performance are Anthropic's own named components of the Description
  competency** — "Product Description (defining what you want... outputs, format,
  audience), Process Description (how the AI approaches your request), Performance
  Description (the AI's behavior during collaboration)" per Anthropic's official AI
  Fluency page (triple-verified, including a coordinator search). The framework presents
  the four-dimension model as its own ("developed through iterative testing,"
  `framework/ppep-framework.md:8`) and attributes only the *competency*, never the
  component triad. The true novel contribution is Epistemics + the rubrics/anchors —
  which is still a good story, but not the one currently told.
- **"Independently surfaced... not found in most prompting guides"** (README.md:62)
  overreaches: the toolkit's own entry-level Epistemics technique ("Ask It to Think
  First") is imported from the same Anthropic handout, and the *content* (verification,
  grounding, hallucination reduction) is prominent in Anthropic's and OpenAI's official
  guidance. What is genuinely novel is the packaging as a scored dimension — say that
  instead.
- **"Most prompt engineering guides are opinion-based"** (README.md:26) is an unproven
  negative claim — precisely the class of claim the framework's own Epistemics rules
  forbid without a shown inventory. No survey of guides exists in the repo. This
  self-contradiction is the single sharpest attack vector in the whole repo: the
  framework fails its own flagship standard on its flagship claims.

### 4.2 The scholarly apparatus (CRITICAL)

- **Six of fourteen author-named academic citations carry fabricated author names**
  (43%): "Eisenstein" → real: Hashemi/Eisner/Rosset/Van Durme/Kedzie (LLM-Rubric, ACL
  2024, cited three times); "Li" → Sülün/Saçakçı/Tüzün (TOSEM); "Wang" →
  Zhang/Peng/Zhang (IEEE); "Arya" → Huang/da Costa/Zhang/Zou (Springer); "Zhang" →
  Acharya/Ginde (arXiv/EASE); "Holterman" → Hong et al. (RULERS). In every case the
  title, venue, and URL are correct — only the humans are invented: the classic
  signature of unverified AI-generated bibliography, in a repo whose banner is "proof of
  every decision." Independently confirmed by three agents.
- **The "93% confidence" figure is pseudo-quantification.** No metric, procedure, or
  data anywhere in the repo (grep-verified); 93% = 100% − 7% where 7% is asserted, not
  derived; and the cited literature documents single-evaluator unreliability *far larger*
  than 7% (Nielsen: single-evaluator severity ratings "too unreliable to be trusted";
  Hertzum & Jacobsen: any-two-evaluator agreement 5–65%). The citations undercut the
  number they are offered to support.
- **"Confidence intervals... documented throughout" is flatly false** (README.md:35):
  the word "interval" appears exactly once in the repository — inside that sentence.
- **The controlled-degradation methodology claim is unsupported.** "Recommended by NLP
  evaluation research to avoid central tendency bias" + "synthetic examples are
  theatrically bad": none of the three cited sources (LLM-Rubric, RULERS, Label Studio)
  discusses controlled degradation at all, and "theatrically bad" is untraceable in the
  literature. (Central-tendency bias in LLM judges is real — but the cited support is
  for anchors generally, not this specific method.)
- **A quotation presented three times as Nielsen-via-Hertzum is unlocatable verbatim**
  in either source (medium confidence — Hertzum 2006 is paywalled; the substance is
  accurate Nielsen doctrine, but quotation marks imply verbatim text no one could find).
- **The LLM-Rubric paper is also mischaracterized:** it calibrates against *multiple
  disagreeing human judges* — it is evidence against the single-evaluator ground truth
  it is cited to justify.
- **The Anthropic CDN PDF cited as "AI Fluency: Framework and Foundations"** appears to
  actually be a course handout (Google-indexed title: "6 Techniques for Effective
  Prompt Engineering"; a second source calls it a prompt-engineering guide). Medium
  confidence — unfetchable from this environment. **Owner action: download it and see
  what it actually is before citing it aloud.**

### 4.3 Measurement design (MAJOR)

- **The weighted formula defeats the rubric's own criticality story.** An issue with a
  "Critical" section entirely absent but 10s elsewhere scores 210/25 = **8.4** and passes
  the 7.0 gate with only "targeted suggestions" — while the calibration set's own band
  table (`issue-calibration-set.md:129-135`) says one absent critical section = the 3-4
  band, and the evaluator's own rule says "a strong Steps section does not compensate
  for an absent Rollback" (which is exactly what the formula does). *Empirical nuance:
  in 3/3 live runs the gate did catch a Rollback-deleted issue (6.24–6.68), because
  fresh sessions don't grant the 10s — the flaw is structural, not yet observed live
  (§5).* 2026 judge practice would hard-fail on absent critical sections.
- **The calibration anchors violate the evaluator's own strictness rule.** "A prompt
  missing sub-criteria should not score above 6 on that dimension"
  (prompt-evaluator.md:55) is contradicted by at least five of the nine anchors (Anchor
  2 Product 7 while "missing format, length, tone, location"; Anchor 5 Performance 7
  with "no role defined, no tone specified"; etc.). Our fresh-session runs followed the
  *rule*, not the anchors — meaning live behavior systematically diverges from the
  published calibration.
- **Several anchor scores contradict the framework's own band definitions**: Anchor 7
  Process 10 with no checkpoints or completion conditions (band 9-10 requires both);
  Anchor 6 Epistemics 8 while its own note admits negative claims aren't covered (band
  8-9 requires them); Anchor 9 Epistemics 10 without inventory-before-judging — and its
  supposed proof-for-negative-claims sentence is garbled and literally says the opposite
  ("that you don't give negative claims").
- **No external ground truth exists anywhere.** Anchors scored by the framework's
  author, using his own framework, on artifacts from his own project (the 10/10 "gold
  standard" Anchor 8 is the owner's own Inkweave prompt; the issue calibration source is
  an Inkweave issue) — validation is self-rescoring until stabilization, and the
  framework's predictive claim ("predicts how useful the AI's response will be") has
  zero outcome data. 2026 table stakes: 100-300 human-labeled samples, Cohen's kappa.
- **Two-decimal precision is unsupported**: propagated uncertainty on the issue formula
  is ±0.36 under optimistic assumptions, and we measured a ~1.3-point systematic
  expert-vs-fresh-session offset. Only the integer digit is signal; "9.44" implies
  precision the instrument does not have.
- **No model version is pinned anywhere** ("Developed and validated using Claude" — no
  model, no date) even though scores are declared model-relative. The measured offset
  may partly be model drift since April; without a pin, drift is undetectable and the
  calibration unfalsifiable.
- **1-10-with-decimals scale design runs against the 2026 evals consensus** (binary or
  1-5 with defined endpoints; Hamel Husain's widely-cited guidance; Anthropic's own eval
  docs) — defensible for a teaching tool, indefensible as production instrument.
- **Anchor coverage is thinnest exactly where real prompts land**: no overall exemplars
  at 2, 4, or 6; Epistemics has zero exemplars in the 4-5 band — the very band whose
  distinctness is the stated justification for its five-band scale. Our A1 test prompt
  landed at 5.25–5.75 — in the gap.

### 4.4 Calibration-set integrity (MAJOR)

- **Anchor 1 carries an undisclosed-in-README "Expert judgment override"**: formula 9.44
  labeled 10/10 (all other anchors follow plain rounding), an override the shipped
  evaluator is never authorized to perform — the set's first data point demonstrates the
  formula yielding to unstructured judgment.
- **Anchor 1's own narrative is arithmetically impossible**: "only gap is Prerequisites"
  cannot produce 9.44 (Prereq-only deficits yield 9.40 or 9.52, never 9.44); the actual
  hidden vector requires four sections below 10.
- **The "single-change-per-anchor" principle is violated at the first step**
  (coordinator-verified directly): Anchor 2's declared change is "References removed,"
  but its SQL silently drops 10 of 20 columns and a security policy; Anchor 3 restores
  a policy Anchor 2 removed — impossible under cumulative degradation.
- **Per-section vectors are published nowhere**, so "formula-verified" is not verifiable
  by any reader without solving the inter-anchor deltas (we did; the vector is uniquely
  recoverable — publishing it would cost one table).
- **The source issue is publicly unverifiable**: Doberjohn/inkweave is **private** (not
  deleted — confirmed via GitHub API), so the cited issue #278 URL 404s for every
  reader, against the set's own "so any developer can verify... independently."
- "Ten controlled degradations" is off by one (1 reference + 9 degradations), and
  Anchor 4 carries a Severity-3 finding while sitting in the band the table reserves for
  "Severity 2 findings only."

### 4.5 Capability realism (MAJOR)

- **URL mode asks for observations a chat AI has zero signal for**: page load within
  2.5s (LCP), visible layout shift, animation smoothness, blur tests, color appearance —
  chat-AI URL access fetches pages as markdown text without rendering, CSS, JS, or
  timing. The "Inferred" hedge misrepresents zero-signal as weak-signal. Yet the README
  compatibility table rates URL mode "Full" on all four surfaces — while its own
  codebase-mode row gets a footnote for a lesser problem, and the Claude column marks
  codebase mode "Full" in direct contradiction of its own footnote text.
- Screenshot mode asks whether images "appear to have alt text" (invisible in pixels)
  and whether tap targets "appear ≥44px" (no CSS-pixel scale exists in a screenshot).
- Codebase mode's header claims "All verifiable from code" and then its own Step 5
  admits rendering-dependent dimensions are not; it demands shown contrast-ratio
  calculations without ever instructing the agent to compute them with a script
  (nonlinear sRGB math LLMs are unreliable at mentally); its 11 grep commands all work
  (executed in sandbox) but traverse node_modules and include very low-precision
  patterns.

### 4.6 Standards fidelity (MAJOR)

- **WCAG 2.2 branding is decorative**: none of the nine success criteria new in 2.2
  appears in any mode (grep-verified); the 44×44px tap-target figure is the AAA/Apple
  number while the actual 2.2 AA criterion (2.5.8, 24×24px) never appears; SC 1.4.12 is
  misquoted as mandating 1.5 line-height (it only requires surviving *user-applied*
  spacing overrides); a 16px minimum font size is presented as WCAG-compliant (no such
  requirement exists at any level). Double-confirmed by two agents.
- **The debunked 3-click rule is a scoring sub-criterion** in a framework marketed as
  NN/g-grounded — NN/g's own article is titled "The 3-Click Rule for Navigation Is
  False."
- **Only 7 of Nielsen's 10 heuristics are mapped** (H8 aesthetic/minimalist and H10
  help/documentation absent entirely, H4 covered but unattributed) under a persona
  claiming "deep knowledge of Nielsen's 10."
- The UI/UX evaluator is also **the only evaluator with no calibration set, no weights,
  no aggregation, and no example outputs** — in a toolkit whose central differentiator
  is calibration.
- Smaller: Nielsen's 0-4 severity scale is claimed "preserved exactly" while the
  toolkit's working scales drop level 0; severity-4 trigger text covers a *vague*
  rollback but not an *absent* one (every empirical run had to patch this by judgment).

### 4.7 Repo hygiene and truth-in-packaging (MAJOR → MINOR)

- **The README's primary UI/UX "Getting started" step points to a file deleted on
  2026-04-20** (`prompts/uiux-evaluation-prompts.md`); the three real mode files are
  never path-referenced anywhere in the README. Broken for ~4 months, surviving two
  subsequent README edits.
- **License posture is unaddressed**: MIT toolkit self-described as "built on top of" a
  CC BY-NC-SA 4.0 work, importing its technique taxonomy plus a verbatim quote. Our
  non-lawyer read: likely defensible under idea/expression (frameworks and methods are
  not copyrightable; the borrowed *expression* is small), but ShareAlike/NC would bind
  any actual adaptation, and no NOTICE reconciles the two. A guaranteed interview
  question; prepare the answer or add the notice.
- **LICENSE names "John Giannelos" (2025)** while every commit is authored by John
  Fanidis and the repo began 2026-04-15 — likely a copy-paste from another project;
  an easy interviewer gotcha either way.
- **The skills install path is legacy**: `.claude/commands/<name>/SKILL.md` works today
  (empirically verified) but is undocumented loader behavior; canonical is
  `.claude/skills/`. The docs' own naming table predicts the documented path should
  fail — it survives by special-casing that could regress.
- **"Claude Code only" was arguably already wrong when written**: SKILL.md became an
  open standard in Dec 2025 (adopted by OpenAI Codex, Cursor, Gemini CLI, etc. —
  medium-high confidence, secondary sources), four months before the README was
  committed.
- implement-issue applies the rubric to *any* issue type (the evaluator's out-of-scope
  guard is absent), collapses the three-tier policy into two (mandating a full rewrite
  even below 2.0, where the evaluator itself says rewrites are meaningless — then
  pushing it to GitHub via `gh issue edit`), and neither skill sets
  `disable-model-invocation` despite side effects — with over-broad `Bash(git:*)`/
  `Bash(gh:*)` grants.
- Zero versioning (no tags/releases/changelog) for a toolkit whose promise is *stable
  calibrated scoring*; no issue templates in a repo about issue quality; no CI check
  that would have caught the broken README path; "end to end" overstates a loop whose
  implement leg stops at branch setup; three hand-synced rubric copies already drifting
  (frequency dimension, tier policy, score bands).
- The "nine real prompts" are seven scenarios (two base texts reused); the framework
  doc's Epistemics-N/A pointer references a definition it doesn't contain; "grounded in
  research from usability, communication, and epistemology" — the repo contains zero
  communication or epistemology references.

### 4.8 Currency: April → August 2026 (MAJOR for positioning)

- **Zero engagement with the current platform layer** (grep-verified zeros): extended/
  adaptive thinking, context windows, prompt caching, structured outputs, XML tags,
  subagents, MCP, few-shot, chain-of-thought. XML structuring — Anthropic's signature
  technique — is absent from a toolkit that says "works best with Claude."
- **The Process dimension's universal "full ordered steps = 9-10" contradicts current
  reasoning-model guidance** from both Anthropic ("Prefer general instructions over
  prescriptive steps... Claude's reasoning frequently exceeds what a human would
  prescribe") and OpenAI ("think step by step is unnecessary"). Epistemics gets an N/A
  rule; Process never does.
- **The "fully specified = 10/10" ideal is the inverse of context engineering** ("the
  smallest possible set of high-signal tokens") — the now-dominant framing the toolkit
  never mentions.
- **The paste-in session-intro delivery was already legacy at creation**: Agent Skills
  shipped Oct 2025 across claude.ai/API/Claude Code precisely to avoid re-pasting
  reusable expertise; the toolkit's core evaluators ship only as paste-prompts. (The
  honest defense: paste is the only fully cross-vendor pattern, and the README's
  ChatGPT/Gemini columns suggest that was intentional. Say so.)
- "Ask It to Think First" is increasingly a no-op (thinking always-on for current
  models; Anthropic lists manual CoT as a fallback), and Anthropic now warns that
  verification instructions tuned for older models cause *over*-verification on Opus 5.
  The aggressive emphasis style ("mandatory" ×9, "NON-NEGOTIABLE", "strict professor")
  is the pattern Anthropic now advises dialing back.

---

## 5. Empirical results (what we measured)

Full detail: `analysis/02-empirical-tests.md`. Three experiments, 11 fresh-session runs:

- **Reproducibility (A1):** novel mid-band prompt, 5 runs, 2 models → overall 5.25–5.75;
  per-dimension spread ≤1. **Good stability — the owner's strongest empirical defense**,
  with honest caveats: small n, one day, Anthropic-family only, produced by this audit
  (the toolkit itself shipped zero reliability data). Also observed: display-format
  divergence (decimals vs the anchors' integers — no rounding rule exists) and
  inconsistent clarifying-question behavior (0–3 questions for identical input).
- **Sensitivity (A2):** Anchor 5 + exactly its four named gaps closed → Product 7→9 in
  3/3 runs, other dimensions stable. The rubric is diagnostic in the designed direction.
- **Gate test (B):** Anchor 1's issue with Rollback deleted → all 3 runs scored 6.24–6.68
  (< 7.0), triggered the rewrite branch, and reported severity 4. **The theoretical 8.4
  bypass did not manifest** — because fresh sessions score the other sections 6–9, not
  the 10s the calibration implies. Which surfaces the deeper finding: **the calibration
  baseline itself does not reproduce** — fresh sessions sit ~1.3 points below the
  expert's published anchor scores on near-identical content, consistently across runs
  and models. The anchors encode one person's April-2026 judgment, not what the shipped
  rubric produces.

---

## 6. Where it stands against the competition

| Category | Who owns it (Aug 2026) | This toolkit's position |
|---|---|---|
| Prompt guides/frameworks | dair-ai guide (77.4k★), official Anthropic/OpenAI/Google docs, mnemonic frameworks (CO-STAR etc.) | Zero adoption (1★, 0 forks); PPEP unknown to any third party; but **no named framework has a scored verification dimension** — Epistemics-as-rubric is genuinely unoccupied ground |
| Prompt eval tooling | promptfoo (24.2k★, `llm-rubric` is a built-in one-liner), Anthropic Console Evals (Humanloop team), Braintrust ($80M B), OpenAI evals | Paste-in evaluator lacks every table-stakes feature (versioning, datasets, CI, model comparison, structured output); competes as pedagogy, not tooling |
| Issue quality / AI-readiness | GitHub's official 3-element Copilot guidance, spec-kit (126k★), native AI triage | The scored gate + rewrite loop as a packaged unit is genuinely absent elsewhere; but the runbook ideology (mandatory Rollback, weight 4) exceeds what GitHub's own guidance asks and penalizes ordinary feature issues |
| UI/UX auditing | axe-core/Lighthouse/WAVE (free, deterministic), Baymard UX-Ray (346 heuristics, productized), UX Pilot | LLM heuristic evaluation is a credible emerging instrument (published kappa ≈0.5), but this evaluator has no calibration set and never articulates why an LLM should eyeball what axe-core measures |
| Claude Code skills | anthropics/skills (168k★), marketplaces, six-figure-star community collections; issue-creation skills are commodity | Well-engineered but unpackaged (no plugin manifest, manual copy install), unversioned, no evals — invisible to the distribution channels that matter |

**The honest positioning statement:** *"A calibration-first evaluation-methodology
demonstration built on Anthropic's AI Fluency Description competency — original in its
Epistemics scoring dimension and its scored issue-quality gate, portable into real eval
tooling, and honest about being a solo teaching artifact rather than a product."*

**The comparison an interviewer will most likely throw:** "Why a paste-in prompt instead
of promptfoo / Console evals?" — answer with the cross-vendor accessibility rationale
and the teaching-artifact framing, then show you know the tooling landscape.

---

## 7. The interview playbook

### The story to tell (3 sentences)

"I took Anthropic's AI Fluency Description competency and operationalized it: scoreable
rubrics, calibration anchors, and a novel fourth dimension — Epistemics — that scores
whether a prompt makes the AI prove what it claims, which Anthropic's own guidance later
converged on. I then applied the same calibration discipline to a real delegation
problem: an eight-section quality gate that decides whether a GitHub issue is safe to
hand to a coding agent. The measurement claims outran the validation in places — here's
what I'd fix and how I'd validate it properly."

That last clause is load-bearing: **preempting the flaws converts them from gotchas into
maturity.**

### Fix before presenting — Tier 1 (≈2-3 hours, do all of these)

1. Fix the six fabricated author names (and "Sayagh, M., et al." → sole author).
2. Delete or re-derive the 93%/7% figure everywhere (3 files); delete "confidence
   intervals documented throughout."
3. Add one attribution sentence: "The Product/Process/Performance dimensions come
   directly from the AI Fluency course's Description components; Epistemics and the
   scoring rubrics are this toolkit's additions." (Also resolves most of the license
   tension when paired with a NOTICE line.)
4. Fix README.md:136 → point to `prompts/uiux-evaluator/` (three modes).
5. Fix the LICENSE name/year line.
6. Make inkweave#278 public, or export the issue as a gist/screenshot linked from the
   calibration set.
7. Soften "Most prompt engineering guides are opinion-based" and "not found in most
   prompting guides" to claims you can prove (or show the survey).
8. Reword the controlled-degradation "recommended by NLP evaluation research" sentence
   to "inspired by anchor-based calibration practice" and drop "theatrically bad."
9. Download the Anthropic CDN PDF and confirm what it actually is; retitle the citation.

### Fix if time allows — Tier 2 (≈a day)

10. Publish the per-section score vector table for the ten issue anchors (you have it —
    it reproduces).
11. Add a min-gate to the formula: `if any critical section == 0 → cap at 3.9` (aligns
    formula with the band table; one line in three files).
12. Reconcile the strictness rule with the anchors (change "should not score above 6"
    to describe what the anchors actually model, or re-score the anchors).
13. Add a WCAG 2.2 pass: swap 44px→24px (SC 2.5.8 AA), fix SC 1.4.12 wording, drop the
    16px "compliance" claim, remove the 3-click rule.
14. Update install docs to `.claude/skills/`, add the out-of-scope guard and <2.0
    template branch to implement-issue.
15. Pin the model + date the calibration was scored against; add a CHANGELOG.

### Prepare answers for these questions (the ones we'd ask)

1. "Your rule caps a dimension at 6 when sub-criteria are missing; Anchor 2 scores
   Product 7 while missing four of them — which is wrong, the rule or the anchor?"
2. "Who wrote the LLM-Rubric paper you cite three times?" *(and the follow-up: "that
   paper models multiple disagreeing judges — why is your ground truth one person?")*
3. "Where does 93% come from? Show me the computation."
4. "Name one success criterion that's new in WCAG 2.2." *(none appears in the prompts)*
5. "What does the model actually receive when you give it a URL?"
6. "An issue missing Rollback entirely — walk me through what your formula gives it."
   *(8.4 with 10s elsewhere; know the band-table contradiction and the empirical result)*
7. "Have you ever measured the variance reduction the calibration set claims?" *(Answer:
   post-hoc audit runs show ±0.25 same-model stability but a ~1.3-point offset from the
   published anchors — know both numbers.)*
8. "Why 1-10 with two decimals when the evals community uses binary or 1-5?"
9. "Product, Process, Performance — where do those names come from?"
10. "Why .claude/commands/ six months after .claude/skills/ became canonical?"
11. "MIT on top of CC BY-NC-SA — how does that work?"
12. "Anchor 8, your 10/10 gold standard — who wrote that prompt, and who scored it?"

### The one strategic choice

Several verdicts flip depending on framing: as **(a) a teaching artifact** for the human
skill of describing intent, it is defensible and even ahead of its time in one
dimension; as **(b) production evaluation tooling**, it is indefensible without model
pinning, held-out validation, structured outputs, and packaging. **Pick (a) explicitly
and preempt (b).** The README currently claims (b)'s virtues ("production-ready,"
"93%," "formula-verified") — that is the mismatch to fix.

---

## 8. Confidence statement

Headline findings (§4.1-4.4, §4.7 hygiene items, all arithmetic, all empirical results)
are high-confidence: independently corroborated by 2-3 agents with different methods
and/or coordinator-verified directly in the files. Medium-confidence items, flagged
inline: the CDN PDF's exact identity; verbatim absence of the Nielsen/Hertzum quote
(paywalled full text); the Dec-2025 skills open-standard adoption list (secondary
sources); ChatGPT/Gemini default-surface rendering capabilities (vendor docs
unreachable). Nothing in this report rests solely on a single agent's unverified claim.

Claims we investigated and **cleared**: the "CorsoUX" citation (real brand of
courseux.com); the Sayagh arXiv paper (real, on-point); the "25+ citations" count
(exactly 25); the anchor arithmetic (all reproduce); the README skills install path
(works today, though undocumented); the GitHub Copilot quotation (verbatim-accurate);
inkweave's existence (real, private).

---

## Appendix

- `analysis/agents/framework.md` — PPEP framework audit
- `analysis/agents/prompt-evaluator.md` — prompt evaluator + calibration set
- `analysis/agents/issue-evaluator.md` — issue evaluator + calibration set (formula recomputation)
- `analysis/agents/uiux.md` — three UI/UX modes (WCAG/Nielsen fidelity, capability realism)
- `analysis/agents/skills.md` — Claude Code skills (incl. empirical install test)
- `analysis/agents/hygiene.md` — README accuracy, license, CI, git history
- `analysis/agents/citations.md` — all 31 citations verified
- `analysis/agents/competition.md` — Aug-2026 landscape with live adoption numbers
- `analysis/agents/best-practices.md` — currency grading vs Aug-2026 guidance
- `analysis/agents/methodology.md` — evaluation-science rigor
- `analysis/00-first-hand-notes.md`, `01-verification-log.md`, `02-empirical-tests.md` — coordinator checkpoints

*Note: this `analysis/` directory lives on the audit branch only. Decide deliberately
whether any of it should ever merge to main — an audit this candid is for you, not
necessarily for your repo's public face.*
