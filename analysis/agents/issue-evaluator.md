# Agent report: issue-evaluator

## Executive summary

The issue-evaluator lane is a mix of genuinely careful arithmetic and resume-killing citation rot. The weighted formula is sound (weights sum to 25, normalization correct) and — remarkably — all ten "formula-verified" anchor scores, including the headline 9.44, reproduce exactly under a single consistent per-section score vector, so the numbers are not fabricated. But that vector is published nowhere, it contradicts Anchor 1's own stated "only gap is Prerequisites" narrative, and the anchor texts drift in ways the "single-change-per-anchor" methodology explicitly forbids (Anchor 2 silently halves the SQL schema and drops a security policy; Anchor 3 restores a policy Anchor 2 removed). Worse, five of the academic citations in the methodology section carry fabricated author names (real papers, real URLs, wrong authors — a classic LLM-hallucination signature), and the core methodological claim ("controlled degradation recommended by NLP evaluation research to avoid central tendency bias") is not supported by any of the three sources cited for it. Finally, the additive formula quietly defeats the framework's own criticality story: an issue with Rollback (or Implementation Steps) entirely absent still scores 8.4 and sails through the 7.0 quality gate, directly contradicting the calibration set's scoring-scale table. The source issue (Doberjohn/inkweave#278) 404s publicly, so the calibration baseline is unverifiable.

## Strengths (with evidence)

- **The scoring formula is arithmetically sound: the eight weights (4,4,4,3,3,3,2,2) sum to 25, the formula divides by exactly 25, and a perfect issue scores exactly 10.0.**
  - Evidence: prompts/issue-evaluator.md:98-110 — weights 4+4+4+3+3+3+2+2 = 25; formula is `(Σ section×weight)/25`; 250/25 = 10.
- **All ten anchor formula scores — including the headline 9.44 — reproduce exactly to two decimals from one consistent hidden per-section vector, with every inter-anchor drop attributable to exactly one section change; the numbers were computed carefully, not invented.**
  - Evidence: Recomputed: baseline (Steps 10, AC 10, Rollback 9, Context 10, Prereq 9, Testing 9, Files 10, Refs 8) → 236/25=9.44; then Refs→0: 8.80; Files→0: 8.00; Testing→3: 7.28; Prereq→0: 6.20; Context→0: 5.00; Rollback→2: 3.88; AC→3: 2.76; Steps→4: 1.80; all→0 floored: 0.50. Matches prompts/issue-evaluator.md:179-191 exactly.
- **Action thresholds are exhaustive and non-overlapping with boundary behavior fully defined (exactly 7.0 → suggestions; exactly 2.0 → rewrite), and README and evaluator agree.**
  - Evidence: prompts/issue-evaluator.md:155-159 ('>= 7.0', '< 7.0 AND >= 2.0', '< 2.0') matches README.md:71 ('score >= 7.0', '2.0 <= score < 7.0', 'score < 2.0').
- **Nielsen's severity scale is represented accurately: the 0-4 levels and the frequency/impact/persistence factors quoted in the calibration set match the real NN/g source, and the frequency-separate-from-severity point matches MeasuringU.**
  - Evidence: examples/issue-calibration-set.md:81 ('0 = not a problem, 1 = cosmetic, 2 = minor, 3 = major, 4 = catastrophic') and :86 ('frequency, impact, and persistence') verified via web search against https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/ and https://measuringu.com/rating-severity/.
- **Every one of the 13 citation URLs I checked resolves to a real, on-topic source — no dead-link or invented-paper hallucinations — and spot-checked substantive claims hold (e.g., the '1,084,300 projects' figure from IEEE 10633301 is real; the IssuePilot gist's Why/What/How structure matches).**
  - Evidence: Verified via WebSearch/WebFetch: NN/g, MeasuringU, ACL 2024.acl-long.745 (LLM-Rubric), arXiv 2601.08654 (RULERS), labelstud.io blog, oneuptime.com 2026-02-02 post, dev.to Thesius post, courseux.com (branded 'CorsoUX'), gist c9efc3e0e4fb81b4aefa3bf43d22391b, dl.acm.org/10.1145/3643673, ieeexplore 10633301 (1,084,300 projects confirmed), springer s10664-018-9636-3, arXiv 2504.18804.
- **The self-scoring limitation is honestly disclosed rather than hidden, and the observations section is properly hedged as heuristics, not findings.**
  - Evidence: examples/issue-calibration-set.md:14 ('Scores were assigned by the subject matter expert (the developer who owns the repository...)') and :927-928 ('They are not formal research findings — they are heuristics surfaced by a single subject matter expert').
- **The per-section rubric bands are operational, not vibes: each band names concrete observable features (checkboxes, code blocks, per-step verification, Created/Modified split), and the vague-rollback-as-false-confidence insight is genuinely good SRE-informed design.**
  - Evidence: prompts/issue-evaluator.md:46-91 (band definitions) and :60 ('Single vague sentence such as "revert all changes." Provides false confidence... flag it explicitly as a severity 4 finding').

## Findings

- **[CRITICAL] [fabricated-citations]** Five academic citations in the calibration set's methodology section carry wrong (apparently fabricated) author names — the papers, titles, and URLs are real but the authors are not — a classic LLM-hallucination signature in a document that claims 'Every claim... is traceable to a specific source.'
  - Evidence: examples/issue-calibration-set.md:17 cites 'Eisenstein, J., et al.' for LLM-Rubric (real authors: Hashemi, Eisner, Rosset, Van Durme, Kedzie — aclanthology.org/2024.acl-long.745); :18 cites 'Holterman, B., et al.' for RULERS arXiv 2601.08654 (real authors: Hong, Yao, Shen, Xu, Wei, Dong — huggingface.co/papers/2601.08654, github.com/LabRAI/Rulers); :47 cites 'Zhang, Y., et al.' for arXiv 2504.18804 (real authors: Jagrit Acharya, Gouri Ginde); :41 cites 'Li, X., et al.' for ACM 10.1145/3643673 (real authors: Sülün, Saçakçı, Tüzün — confirmed via ACM/TOSEM); :45 cites 'Arya, D., et al.' for s10664-018-9636-3 (real authors: Huang, da Costa, Zhang, Zou — link.springer.com). Contradicts :8 'traceable to a specific source.'
  - Confidence: high — each author list confirmed via web search against the publisher/aggregator pages; only caveat is I could not open aclanthology/arxiv directly (egress-blocked) and relied on Microsoft Research, Semantic Scholar, HuggingFace, ACM, Springer search results.
- **[CRITICAL] [formula-design]** The additive weighted mean defeats the framework's own criticality claims: an issue with a critical section (e.g., Rollback or Implementation Steps) entirely absent but everything else perfect scores 8.4 and passes the >=7.0 gate with only 'targeted suggestions', while the calibration set's own scoring-scale table says one absent critical section means the 3-4 band.
  - Evidence: Arithmetic: 250 − (4×10) = 210; 210/25 = 8.4 ≥ 7.0. Contradicts examples/issue-calibration-set.md:134 ('3-4 | One or more critical sections absent... | One or more severity 4 findings') and prompts/issue-evaluator.md:169 ('A strong Steps section does not compensate for an absent Rollback' — the overall formula does exactly that compensation). All three critical sections absent still scores (250−120)/25 = 5.2 ('revised issue'), not the 1-2 band the table claims.
  - Confidence: high — pure arithmetic from the stated formula; the only mitigation is that a Severity 4 finding would still be reported alongside the passing score.
- **[MAJOR] [unsupported-methodology-claim]** The claim that controlled degradation is 'grounded in NLP evaluation research which shows that synthetic low-quality examples tend to be theatrically bad... producing central tendency bias' is not supported by any of the three sources cited for it; none recommends controlled degradation of a real artifact, and the 'theatrically bad' claim has no source at all.
  - Evidence: examples/issue-calibration-set.md:12 (claim) and :17-19 (sources). LLM-Rubric is about calibrating LLM judges to human judgments via a personalized network; RULERS is about locked rubrics, evidence anchoring, and Wasserstein post-hoc calibration; the Label Studio post covers rubrics, ground-truth anchor sets, calibrated scoring, and disagreement review — none mentions degradation-based anchor construction (verified via search summaries of all three). Central tendency bias in LLM judges is real and anchor examples are a documented mitigation (e.g., arxiv.org/pdf/2605.16386), but that supports 'use anchors', not 'degrade one real issue'.
  - Confidence: medium-high — I could not read the three sources' full texts (egress-blocked), only search-engine summaries; but the summaries describe each paper's actual mechanism and none is about degradation.
- **[MAJOR] [unverifiable-verification]** 'Formula-verified score' is not verifiable by any reader: the calibration set never publishes the per-section scores for any anchor, so reproducing 9.44 (or any anchor score) requires solving a system of linear equations from the inter-anchor deltas — and even then the weight-4 assignment is underdetermined.
  - Evidence: examples/issue-calibration-set.md contains no per-section score table for any of the ten anchors (checked the full 943 lines; anchors state only severity-finding counts, e.g., :579 '2x Severity 2, 1x Severity 3'). My reconstruction shows the hidden baseline must be Prereq 9, Testing 9, Refs 8, and exactly one of Steps/AC/Rollback at 9 (7 = 4+3 is the unique decomposition), which no reader could know from the document.
  - Confidence: high — exhaustive read of the file plus arithmetic shown in report.
- **[MAJOR] [internal-contradiction]** Anchor 1's stated failure narrative ('Failure mode: None. Minor gap in Prerequisites...') is arithmetically impossible: if Prerequisites were the only imperfect section, the formula score would be of the form (250−3k)/25 — 9.40 or 9.52 near the target — never 9.44; the actual 9.44 requires four sections below 10 (Prereq 9, Testing 9, References 8, and one weight-4 section at 9).
  - Evidence: examples/issue-calibration-set.md:144 ('Failure mode: None. Minor gap in Prerequisites (missing local environment setup)...'). Arithmetic: Prereq-only deficits give 8.80, 8.92, 9.04, 9.16, 9.28, 9.40, 9.52, 9.64, 9.76, 9.88 — 9.44 is not in the set. 9.44 ⇒ weighted deficit 14 = 4(Refs 8) + 3(Prereq 9) + 4+3 (one weight-4 section and Testing at 9), forced by the A2/A4/A5 deltas.
  - Confidence: high — arithmetic; assumes integer per-section scores, which the 0-10 rubric implies.
- **[MAJOR] [methodology-violation]** The anchor texts violate the stated 'single-change-per-anchor' principle: Anchor 2 (claimed change: 'References section removed' only) also cuts the SQL schema from 20 columns to 10, drops the 'Service role write' security policy, removes 2 Files-Affected rows and 2 Testing checkboxes; Anchor 3 then restores the security policy Anchor 2 removed — impossible under cumulative degradation.
  - Evidence: Computed from the file: Anchor 1 SQL = 20 columns, policies ['Public read','Service role write'] (lines 172-199); Anchor 2 SQL = 10 columns, policies ['Public read'] only (352-367) despite :325 'Degradation applied: References section removed entirely' and :327-328 'All critical sections: Present and complete'; Anchor 3 SQL again has both policies (491-505). Files-table rows 9→7 (271-279 vs 423-429: `database.types.ts` and `download-card-images.mjs` rows gone); Testing checkboxes 8→6. Contradicts :94 'single-change-per-anchor, ensuring each score difference is traceable to exactly one variable.'
  - Confidence: high — direct text extraction with counts.
- **[MAJOR] [anchor-text-score-mismatch]** From Anchor 4 onward the Implementation Steps text loses its SQL code block and all per-step verification, yet the hidden score chain requires Steps = 10 through Anchor 8 — the anchors' own texts would not earn their labels under the evaluator's rubric ('Code block for every command... Verification instruction per step' for 8-10).
  - Evidence: Anchor 4 Step 1 (examples/issue-calibration-set.md:601) is prose ('Create `preview_cards` table... with name, full_name... fields') with no SQL block and no Verify lines for steps 4-11 (611-625), while headers still claim 'All critical sections: Present and complete' (:581); rubric at prompts/issue-evaluator.md:46-47 puts such steps in Acceptable (5-7). The score chain (deltas 28, 28, 24 at A7-A9) only balances if Steps stays 10 until Anchor 9.
  - Confidence: high for the text facts; the Steps=10 requirement follows from the delta arithmetic.
- **[MAJOR] [decorative-derivation]** 'Weights derived from Nielsen's severity scale' is decorative: the 'derivation' consists of reusing an ordinal severity label (4/3/2) as a ratio-scale multiplicative weight, which Nielsen's framework does not support — Nielsen severity is a post-hoc judgment of observed problems (frequency+impact+persistence), not an a-priori importance weight, and nothing in Nielsen implies a Critical section matters exactly 2× a Supporting one.
  - Evidence: prompts/issue-evaluator.md:26 ('Section weights (derived from Nielsen severity scale)') and README.md:71; the mapping at examples/issue-calibration-set.md:114-123 assigns weight = severity number. Nielsen's actual scale (verified at nngroup.com via search) rates individual observed usability problems 0-4 for fix-priority; it contains no section-weighting construct. Also no section is assigned severity 1 and severity 0 is dropped, so only 3 of 5 levels are used.
  - Confidence: high on what Nielsen's scale is; the 'decorative' characterization is analytic judgment.
- **[MAJOR] [unverifiable-source]** The calibration baseline (Inkweave issue #278) is publicly unverifiable: both the issue URL and the repository return 404 anonymously, so no reader can confirm the 9.44 reference issue is real or unmodified — the README even omits the repo name entirely.
  - Evidence: examples/issue-calibration-set.md:146 links https://github.com/Doberjohn/inkweave/issues/278 — WebFetch returned HTTP 404; https://github.com/Doberjohn/inkweave also 404 (repo private or deleted; it existed publicly at some point per dependabot.ecosyste.ms index). README.md:77 says only 'GitHub issue #278' with no repo. Mitigation: Anchor 1 embeds the full issue text inline.
  - Confidence: high for the 404s today; medium on 'was public once' (ecosyste.ms indexing).
- **[MINOR] [internal-contradiction]** Anchor 4 contradicts the scoring-scale table: it carries a Severity 3 finding yet scores 7/10 (formula 7.28), while the table defines the 7-8 band as 'Severity 2 findings only' and puts 'one or more severity 3 findings' in the 5-6 band.
  - Evidence: examples/issue-calibration-set.md:579 ('Severity findings introduced: 2x Severity 2, 1x Severity 3') vs :132-133 ('7-8 ... Severity 2 findings only' / '5-6 ... One or more severity 3 findings').
  - Confidence: high — direct quotes.
- **[MINOR] [self-override]** The flagship anchor overrides the framework's own formula by fiat: 9.44 is relabeled 10/10 via 'Expert judgment override' (9.44 rounds to 9, not 10), so the calibration set's very first data point demonstrates that the formula yields to unstructured judgment.
  - Evidence: examples/issue-calibration-set.md:139 ('Score: 10/10 (formula: 9.44)') and :144 ('Expert judgment override: formula score 9.44 rounded to 10/10 given that the gap is context-specific'). All other anchors follow normal rounding (8.80→9, 3.88→4, 1.80→2).
  - Confidence: high.
- **[MINOR] [dual-scale-ambiguity]** Every anchor carries two scores (integer label and formula score) and the evaluator never says which one its thresholds consume; at Anchor 9 the two scales straddle the 2.0 action boundary — label 2/10 would trigger a full rewrite, formula 1.80 triggers the template path.
  - Evidence: prompts/issue-evaluator.md:179-191 (table with both 'Score' and 'Formula' columns; row 9: '2/10 | 1.80') vs :157-159 (thresholds keyed to overall_score, which :149 says comes from the formula — but anchor comparison guidance at :192 says 'An issue with similar gaps to a reference anchor should score similarly' without specifying which scale).
  - Confidence: high on the ambiguity existing; the practical impact depends on the model's reading.
- **[MINOR] [incoherent-rule]** The 'vague rollback is worse than absent' rule is numerically inverted: a vague rollback scores 1-4 while an absent one scores 0, so the failure mode the evaluator calls worse yields a higher score.
  - Evidence: prompts/issue-evaluator.md:60 ('This is worse than absent — flag it explicitly as a severity 4 finding') vs :60-61 (Poor 1-4, Absent 0). The severity channel treats both as Severity 4, but the score channel rewards the 'worse' case.
  - Confidence: high.
- **[MINOR] [data-leakage]** A real Supabase project reference and region are published in the calibration document's reference issue.
  - Evidence: examples/issue-calibration-set.md:314 ('Supabase project: `ttyidjyaxnycbpwngqr` (eu-central-1)'). Project refs appear in public client URLs so this is not a credential, but it is live-infrastructure detail in a public toolkit repo.
  - Confidence: high on presence; low on exploitability.
- **[NITPICK] [spec-imprecision]** The floor clause misdescribes the formula: prose says the 0.5 floor 'applies only when all sections are entirely absent', but max(x, 0.5) applies to any score below 0.5 (e.g., References=5 alone → 0.40 → floored to 0.5).
  - Evidence: prompts/issue-evaluator.md:98-113 ('max(..., 0.5)' and 'The floor of 0.5 applies only when all sections are entirely absent'). Counterexample arithmetic: 5×2/25 = 0.4 < 0.5.
  - Confidence: high.
- **[NITPICK] [terminology-drift]** The calibration set titles itself for the 'Implementation Plan Issue Validator' and says 'the validator should detect...', while the tool everywhere else is the 'Issue Evaluator'.
  - Evidence: examples/issue-calibration-set.md:2 ('Ten Scored Anchor Issues for the Implementation Plan Issue Validator') and :937 ('The validator should detect...') vs prompts/issue-evaluator.md:1 ('Issue Evaluator') and README.md:70 ('The Issue Evaluator').
  - Confidence: high.
- **[NITPICK] [consistency]** The source issue's title is quoted inconsistently: 'Add set 12 cards in the card pool' vs 'Add set 12 cards to the card pool'.
  - Evidence: examples/issue-calibration-set.md:313 ('Issue #278: Add set 12 cards in the card pool') vs :921 and prompts/issue-evaluator.md:190 ('Add set 12 cards to the card pool').
  - Confidence: high.
- **[NITPICK] [severity-accounting]** Anchor 10's severity accounting is incomplete: with all eight sections absent the framework's own mapping implies 3 Severity-4 + 3 Severity-3 + 2 Severity-2 findings, but the anchor reports only the three Severity 4s.
  - Evidence: examples/issue-calibration-set.md:916 ('All eight sections absent. Three critical sections absent = three Severity 4 findings.') vs the mapping at :114-123.
  - Confidence: high.

## Open questions

- Cross-cutting: the same five miscited papers (Eisenstein/Li/Zhang etc.) also appear in README.md:176-179 — the README auditor should re-check its whole reference list plus the Sayagh 'arXiv 2512.21426' citation (README.md:177), which I did not verify (out of my lane).
- Cross-cutting: skills/implement-issue inherits the 7.0 gate; the skills auditor should check whether an absent-Rollback issue scoring 8.4 would be handed to an AI agent without a rewrite (my formula finding implies yes).
- Author attribution for IEEE 10633301 ('Wang, Y., et al.') could not be confirmed or refuted — search results did not surface that paper's author list; given 5/6 other academic citations have wrong authors, treat as suspect until checked.
- Whether the Zhang/EASE-cited five quality dimensions (Atomicity, Conciseness, Completeness, Understandability, Reproducibility) actually appear in arXiv 2504.18804 (they resemble the CTQRS rubric the paper uses) — unverified due to egress blocks.
- Can the owner restore public access to Doberjohn/inkweave (or export issue #278) before the interview? The 404 makes the calibration baseline a trust-me claim.
- Commit 42cd405 (2026-08-12, author 'Claude', adds analysis/00-first-hand-notes.md) is audit-fleet contamination in the working tree, not owner work — synthesis should not attribute it to the project.
- Note on network constraints: nngroup.com, aclanthology.org, arxiv.org, labelstud.io, and gist.githubusercontent.com were egress-blocked for direct fetch; all verifications for those went through WebSearch result summaries (flagged per-finding where it lowers confidence).

---

## Full report

# Audit: `prompts/issue-evaluator.md` + `examples/issue-calibration-set.md`

Auditor lane: Issue Evaluator prompt (197 lines) and Issue Calibration Set (943 lines — largest file in repo). Both read in full. All arithmetic below recomputed; all load-bearing citations checked on the web where the egress proxy allowed (nngroup.com, aclanthology.org, arxiv.org, labelstud.io, gist.githubusercontent.com were blocked for direct fetch — those were verified via WebSearch result summaries, and confidence is flagged wherever that matters).

Files (absolute paths):
- `/home/user/prompt-engineering-toolkit/prompts/issue-evaluator.md`
- `/home/user/prompt-engineering-toolkit/examples/issue-calibration-set.md`
- Claims cross-checked against `/home/user/prompt-engineering-toolkit/README.md:70-77, 165-181`

Git provenance: the calibration set was committed 2026-04-15 (`c101720 Added issue calibration set`, revised `7ac9289` same day and `dbfe137` 2026-04-16); the evaluator 2026-04-16 (`d42baeb`), last touched 2026-04-20 (`ad73d84`). Note: commit `42cd405` (2026-08-12, author "Claude", adds `analysis/00-first-hand-notes.md`) is the audit fleet's own artifact, not owner work.

---

## 1. The scoring formula and the "derived from Nielsen" claim

**Formula (issue-evaluator.md:98-110):** `overall_score = max((Steps×4 + AC×4 + Rollback×4 + Context×3 + Prereqs×3 + Testing×3 + Files×2 + Refs×2)/25, 0.5)`.

**Weights sum check: PASS.** 4+4+4+3+3+3+2+2 = **25**, the divisor is 25, so a perfect issue scores exactly 250/25 = 10.0. Normalization is correct.

**Nielsen verification.** Nielsen's severity scale (verified via web search against https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/, direct fetch egress-blocked) is: 0 = not a usability problem, 1 = cosmetic, 2 = minor, 3 = major, 4 = usability catastrophe; severity combines **frequency, impact, persistence**. The calibration set quotes this accurately (issue-calibration-set.md:81, :86), and its "treat frequency separately from severity" attribution to MeasuringU/Sauro matches https://measuringu.com/rating-severity/.

**Is the derivation real or decorative? Mostly decorative.** The entire "derivation" is: assign each section a severity-if-absent rating (4/3/2), then use that ordinal label *as the multiplicative weight* (issue-calibration-set.md:114-123). Problems:

1. **Ordinal-as-ratio leap.** Nielsen's scale is an ordinal fix-priority rating of *observed problems*; nothing in it implies severity-4 content matters exactly 2× severity-2 content in a weighted mean. That 2:1 ratio is an unstated design choice.
2. **Category error.** Nielsen severity is judged per observed problem, post-hoc, combining frequency/impact/persistence. Here it is an a-priori importance weight on document sections. The doc's own bridging logic ("how badly does the absence of this section hurt... execution", :88) is reasonable *as an analogy* — but "derived from" (README.md:71, issue-evaluator.md:26) overstates it.
3. **Only 3 of 5 levels used.** No section gets severity 1, severity 0 is dropped. The framework is really just "three importance tiers, weighted 4/3/2."

The honest defense is "Nielsen-*inspired* tiering." The indefensible version is the README's "weighted formula derived from Nielsen's severity scale."

**The formula's real design flaw — compensation.** The framework's prose insists critical sections are non-negotiable ("A strong Steps section does not compensate for an absent Rollback", issue-evaluator.md:169; "Rollback... non-negotiable", :32). The arithmetic disagrees:

- Rollback **entirely absent**, everything else perfect: 250 − 40 = 210 → 210/25 = **8.4** → passes the ≥7.0 gate; output is "targeted improvement suggestions" only.
- Implementation Steps entirely absent: same **8.4**.
- **All three critical sections absent** (no steps, no acceptance criteria, no rollback): 130/25 = **5.2** → "revised issue," not even the template path.

Compare the calibration set's own scoring-scale table (issue-calibration-set.md:131-135): "3-4 | One or more critical sections absent... | One or more severity 4 findings"; "1-2 | Multiple critical sections absent." The formula and the band table only agree along the *specific cumulative degradation path* the anchors happen to take (supporting sections removed first). Off that path, they contradict each other badly. Since `implement-issue` uses the 7.0 score as a delegation gate (README.md:84), a rollback-less production runbook can clear the gate. This is the sharpest technical attack available on this component.

(Mitigating fairness note: the evaluator has a second, parallel channel — Severity 4 findings would still be reported at :117-131. But the *action* is keyed to the score, not the findings.)

Minor spec bug: the prose says the 0.5 floor "applies only when all sections are entirely absent" (:113), but `max(x, 0.5)` fires for any score < 0.5 (e.g., References=5 alone → 0.40 → 0.5).

---

## 2. Recomputation of every "formula-verified" score

The calibration set **never publishes per-section scores for any anchor** — only degradation narratives and severity-finding counts. So "formula-verified" cannot be directly checked by a reader; it has to be reverse-engineered. I did. Implied weighted sums (score × 25) and successive drops:

| Anchor | Stated | Sum (=score×25) | Drop | Stated change | Implied by drop |
|---|---|---|---|---|---|
| 1 | 9.44 | 236 | — | reference | baseline deficit 14 |
| 2 | 8.80 | 220 | 16 | Refs removed | Refs was **8** (16/2) |
| 3 | 8.00 | 200 | 20 | Files removed | Files was **10** (20/2) |
| 4 | 7.28 | 182 | 18 | Testing → vague | Testing dropped **6** (18/3) |
| 5 | 6.20 | 155 | 27 | Prereqs removed | Prereqs was **9** (27/3) |
| 6 | 5.00 | 125 | 30 | Context removed | Context was **10** (30/3) |
| 7 | 3.88 | 97 | 28 | Rollback → vague | Rollback dropped **7** (28/4) |
| 8 | 2.76 | 69 | 28 | AC → vague prose | AC dropped **7** (28/4) |
| 9 | 1.80 | 45 | 24 | Steps → 3 bullets | Steps dropped **6** (24/4) |
| 10 | 0.50 | (0, floored) | — | everything removed | max(0, 0.5) = 0.5 ✓ |

**Result: the chain reproduces EXACTLY** under the hidden baseline vector **(Steps 10, AC 10, Rollback 9, Context 10, Prereqs 9, Testing 9, Files 10, Refs 8)**:

- A1: 40+40+36+30+27+27+20+16 = 236 → **9.44** ✓
- A2 (Refs→0): 220 → **8.80** ✓ ... A4 (Testing 9→3): 182 → **7.28** ✓ ... A7 (Rollback 9→2): 97 → **3.88** ✓ ... A9 (Steps 10→4): 45 → **1.80** ✓ (all ten verified by script; every drop maps to exactly one section change)

Three consequences, one good and two bad:

1. **GOOD (and worth saying in the interview's defense): the numbers are real arithmetic, not decoration.** Ten scores mutually consistent to two decimals across nine transitions is essentially impossible by accident.
2. **BAD: it is unverifiable as published.** No reader can check "formula-verified" without solving the linear system I solved. And the solution is underdetermined — deficit 14 at A1 decomposes uniquely as 4(Refs=8)+3(Prereq=9)+**4+3**, but which weight-4 section holds the 9 (Steps, AC, or Rollback) cannot be determined from the document.
3. **BAD: the hidden baseline contradicts Anchor 1's own narrative.** :144 says "Failure mode: None. Minor gap in Prerequisites (missing local environment setup)." If Prerequisites were the *only* gap, possible scores are (250−3k)/25 ∈ {9.88, 9.76, 9.64, 9.52, **9.40**, 9.28, ...} — **9.44 is not achievable**. The arithmetic forces *four* imperfect sections in the reference issue (Prereqs 9, Testing 9, Refs 8, one weight-4 section at 9), three of which are never mentioned.

**The headline "10/10 (formula: 9.44)":** the flagship anchor is scored 10/10 by "Expert judgment override" (:144) even though 9.44 rounds to 9. Every other anchor label is the normally-rounded formula score (8.80→9, 3.88→4, 1.80→2). So the calibration set's very first data point demonstrates the formula being overridden by unstructured judgment — an easy interviewer jab ("your formula's first output was overruled by the person it was supposed to discipline").

**Dual-scale ambiguity:** each anchor has an integer label and a formula score, and the evaluator never says which scale "score similarly to the anchor" (:192) means. At Anchor 9 it matters: label 2/10 → full-rewrite path; formula 1.80 → template path (threshold at 2.0).

### Anchor text drift (violates the stated methodology)

":94 — 'The specific degradation plan follows a principle of single-change-per-anchor, ensuring each score difference is traceable to exactly one variable.'" The texts say otherwise (all counts computed by script):

| Anchor | SQL cols | Policies | Checkboxes | File-table rows |
|---|---|---|---|---|
| 1 | 20 | Public read + **Service role write** | 16 | 9 |
| 2 | **10** | Public read only | **14** | **7** |
| 3 | 10 | Public read + **Service role write (restored!)** | 14 | 0 |
| 4 | **0 (SQL block gone)** | — | 8 | 0 |

- **A1→A2** (claimed change: "References section removed entirely," :325; "All critical sections: Present and complete," :327): the SQL schema silently loses 10 of 20 columns and the `Service role write` RLS policy; the Modified-files table loses `database.types.ts` and `download-card-images.mjs`; Testing loses 2 checkboxes; Context loses its final paragraph (:158).
- **A2→A3** (claimed: Files Affected removed only): the Service-role policy A2 removed **reappears** (:504-505) — impossible under strict cumulative degradation. The anchors were evidently regenerated (likely LLM-drafted) per anchor, not cut down from a single master.
- **A4 onward**: Step 1 becomes prose with **no SQL code block** and steps 4-11 have no Verify lines — yet the score chain requires Steps = 10 through Anchor 8, and the evaluator's own rubric (:46-47) caps code-block-less, verification-less steps at Acceptable (5-7). **An evaluator faithfully applying the rubric to Anchor 4's actual text would score it below its 7.28 label.** The scores model an idealized degradation; the texts show a different one.

---

## 3. Citations: the methodology claim and the "25+" count

**Count: exactly 25 distinct citations** (methodology 3 + GitHub research 10 + Agile 4 + SRE 5 + severity 3, including the URL-less Nielsen 1993 book at :85). "25+" is technically satisfied at the minimum possible margin.

**Existence: surprisingly good.** All 13 URLs I checked resolve to real, on-topic sources: NN/g, MeasuringU, ACL LLM-Rubric, arXiv RULERS, Label Studio, OneUptime (2026-02-02 post exists at the exact URL), Thesius dev.to (exists — though it's a **$29 template sales post**, thin as "SRE framework research"), CorsoUX (site branded CorsoUX at domain courseux.com — the name mismatch is real branding, not an error), the IssuePilot gist (resolves; content matches the Why/What/How claim per search summary), ACM TOSEM 3643673, IEEE 10633301 (the **1,084,300 projects** figure is confirmed real), Springer s10664-018-9636-3, arXiv 2504.18804.

**Authors: catastrophically bad.** Five academic citations carry wrong author names — real paper, real URL, fabricated attribution:

| Cited as | Actual authors | Source |
|---|---|---|
| "Eisenstein, J., et al." — LLM-Rubric, ACL 2024 (:17; also README:179) | **Hashemi, Eisner, Rosset, Van Durme, Kedzie** | aclanthology.org/2024.acl-long.745, Microsoft Research, Semantic Scholar |
| "Holterman, B., et al." — RULERS, arXiv 2601.08654 (:18) | **Hong, Yao, Shen, Xu, Wei, Dong** (LabRAI) | huggingface.co/papers/2601.08654, github.com/LabRAI/Rulers |
| "Li, X., et al." — TOSEM 10.1145/3643673 (:41; also README:176) | **Sülün, Saçakçı, Tüzün** | dl.acm.org, ACM TOSEM announcement |
| "Zhang, Y., et al." — arXiv 2504.18804, EASE 2025 (:47) | **Acharya, Ginde** | ResearchGate/arXiv listing |
| "Arya, D., et al." — EMSE s10664-018-9636-3 (:45) | **Huang, da Costa, Zhang, Zou** | link.springer.com |

This is the signature of LLM-generated citations (plausible-sounding surnames attached to real works — "Eisenstein" is almost certainly a corruption of co-author *Eisner*). In a document that opens with "Every claim in the section weight mapping and scoring scale is traceable to a specific source. This section exists so any developer can verify, challenge, or extend the framework independently" (:8), this is the single most damaging discoverable fact. It is also trivially fixable before the interview. ("Wang, Y." for IEEE 10633301 I could neither confirm nor refute — treat as suspect.)

**The central methodological claim is unsupported.** :12 claims the approach "is grounded in NLP evaluation research which shows that synthetic low-quality examples tend to be theatrically bad rather than realistically bad, producing central tendency bias in evaluators," citing (:17-19) LLM-Rubric, RULERS, and a Label Studio blog post. Verified content of all three (via search summaries; direct fetch blocked):

- **LLM-Rubric**: calibrating LLM judges to human judgments via a personalized calibration network. Nothing about degradation-built anchor sets.
- **RULERS**: locked/versioned rubrics, evidence-anchored structured decoding, Wasserstein post-hoc calibration. Nothing about controlled degradation.
- **Label Studio post** ("Scale AI Evaluation with Rubrics and Calibration"): rubrics + ground-truth anchor sets + calibrated automated scoring + disagreement review. Anchors, yes; degradation, no.

Central tendency bias in LLM judges is a real, documented phenomenon (e.g., arxiv.org/pdf/2605.16386 studies it directly), and anchor examples are a real documented mitigation — so the *spirit* is defensible. But no cited source "recommends" controlled degradation, and the "theatrically bad" claim has no source at all. README.md:77's "the same controlled degradation methodology recommended by NLP evaluation research" is attribution of the author's own (reasonable!) idea to literature that doesn't say it.

---

## 4. Action thresholds

**Boundary behavior: fully defined and consistent.** issue-evaluator.md:155-159: `>= 7.0` → suggestions; `< 7.0 AND >= 2.0` → rewrite; `< 2.0` → template. Exhaustive, non-overlapping; exactly 7.0 → suggestions, exactly 2.0 → rewrite. README.md:71 matches exactly. The `< 2.0` clarifying-questions override (:136) uses the same boundary. This part is clean.

**Rationale: implicit at best.** No document argues *why* 7.0 and 2.0. The implicit anchor is the band table (7-8 = "supporting sections missing," 1-2 = "not usable as a runbook") plus the anchors bracketing the gate (A4 = 7.28 gets suggestions, A5 = 6.20 gets rewrite — so the suggestion/rewrite boundary operationally means "did you have Prerequisites"). But: (a) the band table itself is contradicted by Anchor 4 (Severity 3 finding at 7/10, vs :132 "7-8 ... Severity 2 findings only"); (b) as shown in §1, the 7.0 gate does not actually guarantee "all critical sections present" — 8.4 with zero Rollback passes. The cutoffs are calibrated to one degradation path, not defended in general.

---

## 5. Consistency between evaluator and calibration set

**Consistent:** the eight section names, the 4/4/4/3/3/3/2/2 weights, severity-if-absent labels (evaluator :28-37 vs calibration :114-123), the anchor summary table (evaluator :179-191 matches all ten anchors' scores, formulas, and degradation one-liners, including A7's exact vague-rollback sentence and A10's title), the file path reference (:177), Nielsen severity levels (evaluator drops Nielsen's level 0, reasonably).

**Drift found (all minor):**
- Calibration set title calls the tool the "Implementation Plan Issue **Validator**" (:2) and ":937 'The validator should detect...'" — everywhere else it is the "Issue **Evaluator**."
- Issue title quoted two ways: "Add set 12 cards **in** the card pool" (:313) vs "**to** the card pool" (:921; evaluator :190).
- Evaluator's severity list omits Nielsen's 0 level while the calibration set quotes the full 0-4 scale and claims "Our mapping preserves this scale exactly" (:82).
- "Worse than absent" incoherence: a vague Rollback is declared worse than an absent one (evaluator :60) but scores 1-4 vs absent's 0 — the score channel rewards the failure mode the prose calls worse.
- Anchor 10's severity accounting counts only the three Severity-4s and ignores the 3×Sev-3 + 2×Sev-2 that its own mapping implies for eight absent sections (:916).

---

## 6. Issue #278 verifiability

- README.md:77 says only "GitHub issue #278" — no repo named at all.
- issue-calibration-set.md:146 gives the full URL: `https://github.com/Doberjohn/inkweave/issues/278`. **Fetched: HTTP 404.** The repo root `github.com/Doberjohn/inkweave` also 404s anonymously. The repo did exist publicly at some point (dependabot.ecosyste.ms has it indexed with Dependabot PRs, e.g., inkweave#244), so it is now private or deleted.
- Net: **the calibration baseline is currently unverifiable by any reader.** Partial mitigation: Anchor 1 embeds the complete claimed issue text inline (:150-317), so the artifact is inspectable — but its provenance ("produced by Claude Code," real issue, unmodified) is a trust-me claim.
- Side observations: the reference issue self-cites #278 in its own References (:313), consistent with the plan being posted on/for a pre-existing one-line issue whose bare title is exactly Anchor 10; and :314 publishes a real Supabase project ref + region (`ttyidjyaxnycbpwngqr`, eu-central-1) — not a credential, but live-infrastructure detail in a public doc.

---

## 7. Overall assessment and the interviewer attack list

**Is this defensible applied-evaluation design?** Partially — and more defensible than it first looks, but only after fixes. The genuinely good core: a concrete, operational rubric (checkboxes/code blocks/per-step verification are observable features, not vibes); a real artifact degraded into a full-range anchor ladder; internally *exact* score arithmetic; defined boundary behavior; honest disclosure of single-SME scoring; hedged observations. That is more evaluation discipline than most prompt collections have.

What breaks it: the scholarly apparatus is partly cosplay. Five fabricated author attributions, a methodology "recommendation" no cited source makes, a "derivation" from Nielsen that is number-reuse, a band table its own anchors violate, a gate its own formula undermines, and a baseline artifact nobody can check.

**What a sharp interviewer attacks first, in order:**
1. *"Your methodology section cites 'Eisenstein et al.' for LLM-Rubric. Who actually wrote it?"* — Hashemi, Eisner, et al. Then Holterman/Li/Zhang/Arya. If they've checked one citation, the "every claim is traceable" framing collapses. **Fix before interview: re-verify all 25 author lists.**
2. *"An issue with no rollback section at all — what does your formula give it?"* — 8.4, passes the gate that exists to catch exactly that. The band table says 3-4. Pick one.
3. *"Show me the per-section scores behind 9.44."* — Not published anywhere; and the A1 narrative ("only gap: Prerequisites") is arithmetically impossible.
4. *"You claim single-change-per-anchor. Why does Anchor 2's SQL lose ten columns and a security policy, and why does Anchor 3 get the policy back?"*
5. *"Which NLP paper recommends controlled degradation to avoid central tendency bias?"* — None cited does.
6. *"Why is the reference issue 404?"*
7. *"Your formula said 9.44; you called it 10/10 by expert override. Why should I trust the formula's other outputs?"*
8. *"Claude Code wrote the issue, Claude runs the evaluator, and you — the issue's author — scored the anchors. Where's the independent signal?"* (self-scoring is at least disclosed at :14, :106).

**Defense lines that actually hold:** the arithmetic consistency (show the hidden vector and the ten exact reproductions); boundary definitions; the accurate Nielsen quotation; every checked URL being real; the vague-rollback insight; the honest hedging of the observations section. The strongest honest posture is: "the evaluation *design* is mine and sound; the citation layer was AI-assisted and inadequately verified — here is the corrected version," ideally with corrections committed before the interview.