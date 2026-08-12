# Agent report: prompt-evaluator

## Executive summary

The prompt-evaluator and its calibration set are internally arithmetic-consistent (all nine anchor overalls equal the mean of dimension scores, and all anchor texts and scores are verbatim identical across both files), and the two claimed distinct 10/10 anchors genuinely exist and differ structurally. However, the evaluator's own strictness rule ("a prompt missing sub-criteria should not score above 6 on that dimension") is violated by at least five of the nine calibration anchors under any reading, several anchor scores (Anchor 7 Process 10, Anchor 7 Performance 8, Anchor 6 Epistemics 8, Anchor 9 Epistemics 10) contradict the framework's own band definitions, and the pasted session prompt omits the band tables entirely — so the "calibrated, reproducible" claim is structurally undermined. The calibration set's methodology section misattributes its key citation (the LLM-Rubric ACL 2024 paper is by Hashemi, Eisner, Rosset, Van Durme, and Kedzie — there is no "Eisenstein" among the authors) and mischaracterizes it: the paper calibrates against multiple disagreeing human judges, which cuts against the single-evaluator ground truth it is cited to justify. The evaluator prompt also has no data/instruction separation (no XML tags, contrary to current Anthropic guidance), no edge-case handling (empty, non-English, very long, already-perfect, or harmful prompts — its mandate to always produce "a revised 10/10 prompt" would apply to jailbreaks), and never requires evidence for its own scoring claims, failing the Epistemics standard it preaches.

## Strengths (with evidence)

- **All nine anchors' overall scores are arithmetically consistent with the stated rule (mean of active dimensions, rounded to nearest integer), including the N/A case**
  - Evidence: Computed: A1 (1+1+1+1)/4=1.0→1; A2 (7+2+3+1)/4=3.25→3; A3 (5+2+3+1)/4=2.75→3; A4 (6+5+3+7)/4=5.25→5; A5 (7+8+7+6)/4=7.0; A6 (9+7+8+8)/4=8.0; A7 (9+10+8)/3=9.0 (Epistemics N/A, worked example shown at prompts/prompt-evaluator.md:163); A8=A9=10.0. Every stated overall matches.
- **The two files are fully consistent with each other: all nine anchor prompt texts are verbatim identical and all 33 dimension scores plus 9 overall scores agree**
  - Evidence: diff of extracted prompt strings from prompts/prompt-evaluator.md (lines 97-179) vs examples/prompt-calibration-set.md (lines 58-206) returned zero differences; score-by-score comparison of all anchors matched exactly (e.g. A4: 'Product 6, Process 5, Performance 3, Epistemics 7' at prompt-evaluator.md:129 = calibration-set.md:115-120).
- **README.md:74's claim of 'two distinct 10/10 anchors (technical agentic and non-technical collaborative)' is true — Anchors 8 and 9 exist and reach 10/10 by genuinely different routes**
  - Evidence: Anchor 8 (prompt-evaluator.md:167-173) is grep/file:line/inventory-driven agentic auditing; Anchor 9 (prompt-evaluator.md:177-183) is role-layering plus iterative drafting with a completion condition ('We will finalize when everything is in order'); calibration-set.md:216 explicitly contrasts them: 'No grep commands, no file references, no agentic tools'.
- **The Epistemics N/A rule is a genuinely thoughtful anti-deflation mechanism with a worked arithmetic example and a stated applicability test**
  - Evidence: prompts/prompt-evaluator.md:163 ('When N/A, the overall score is the average of the three active dimensions only: (9 + 10 + 8) / 3 = 9.0') and examples/prompt-calibration-set.md:176 ('A task has a meaningful epistemic dimension when it requires the AI to make factual claims, retrieve or verify information...').
- **The clarifying-questions logic is unusually well specified conditional behavior — a real strength versus typical evaluator prompts**
  - Evidence: prompts/prompt-evaluator.md:62-67: infer-don't-ask default for missing context/steps/role, a specific IF/AND/THEN trigger for the examples question, targeted questions only for 'genuinely unknown domain context', and 'Maximum 3 clarifying questions per evaluation'.
- **The calibration set honestly discloses its single-evaluator limitation and hedges every observation against overgeneralization**
  - Evidence: examples/prompt-calibration-set.md:19 ('Single-evaluator scoring carries irreducible subjectivity') and lines 222, 225, 231, 234 (e.g. 'Whether this reflects a general pattern in real-world prompts is not claimed here', 'two examples are insufficient to establish this as a general claim').
- **Anchor-based calibration via labeled examples is aligned with current Anthropic guidance that examples are the most reliable steering mechanism, and the confirmation handshake is a sound pattern**
  - Evidence: Fetched https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices: 'Examples are one of the most reliable ways to steer Claude's output format, tone, and structure.' Handshake at prompts/prompt-evaluator.md:187: 'Confirm you have understood this framework by summarizing it back to me in two sentences, then tell me you are ready.'
- **Per-dimension anchor notes cite concrete observable features rather than being purely circular**
  - Evidence: e.g. examples/prompt-calibration-set.md:99 ('Deliverable ("something") is still vague. No topic, format, or length.') and :138 ('No inventory-before-judging, no negative claims proof') — falsifiable, feature-level justifications.
- **The pasted evaluator is a reasonable size for a session-intro prompt and is self-contained (anchors inlined)**
  - Evidence: Computed: the pasted portion (prompts/prompt-evaluator.md lines 12-187) is 2,023 words (~2,700-3,000 tokens), including all nine anchors.

## Findings

- **[CRITICAL] [internal-contradiction]** The evaluator's strictness rule — 'A prompt missing sub-criteria should not score above 6 on that dimension' — is contradicted by at least five of the nine calibration anchors under the natural reading, and by at least two anchors under even the most charitable reading (missing ALL sub-criteria), so a fresh session must silently choose between the rule and the anchors, making the advertised calibration self-defeating
  - Evidence: Rule: prompts/prompt-evaluator.md:55. Violations: A2 Product 7 while 'Missing format, length, tone, location' (calibration-set.md:81 — the entire 'Output constraints specified' sub-criterion, evaluator:24); A4 Epistemics 7 while the blog prompt contains none of the four listed Epistemics sub-criteria (evaluator:42-46; prompt text at evaluator:127); A5 Product 7 (same gaps as A2, calibration:135) and Performance 7 with 'No role defined, no tone specified' (calibration:137) — both evaluator-listed Performance sub-criteria (role, examples; evaluator:37-38) missing, violating even the all-sub-criteria reading; A6 Epistemics 8 while 'Does not cover negative claims or inventory-before-judging' (calibration:156); A7 Performance 8 with 'No role defined' (calibration:173).
  - Confidence: high — the only escape is an idiosyncratic reading of 'missing sub-criteria' never stated in the file.
- **[MAJOR] [citation-error]** The calibration set's central methodology citation misattributes the LLM-Rubric paper to 'Eisenstein, J., et al. (2024)' — the actual authors are Helia Hashemi, Jason Eisner, Corby Rosset, Benjamin Van Durme, and Chris Kedzie; no Eisenstein is on the paper (apparent confusion of Jason Eisner with Jacob Eisenstein)
  - Evidence: examples/prompt-calibration-set.md:14 ('Eisenstein, J., et al. (2024). LLM-Rubric...'). Verified via https://www.microsoft.com/en-us/research/publication/llm-rubric-a-multidimensional-calibrated-approach-to-automated-evaluation-of-natural-language-texts/ (author list fetched 2026-08-12: Hashemi, Eisner, Rosset, Van Durme, Kedzie), corroborated by Semantic Scholar entry 'Hashemi-Eisner' and JHU slides filename 'hashemi+al.acl24'.
  - Confidence: high — three independent sources agree on the author list.
- **[MAJOR] [citation-mischaracterization]** The LLM-Rubric paper is cited as establishing that calibration-set construction 'requires human expert judgment rather than automated scoring as the ground truth source' to justify single-evaluator scoring, but the paper's methodology uses multiple human judges and explicitly models their disagreement — it is evidence against single-evaluator ground truth, not for it
  - Evidence: examples/prompt-calibration-set.md:12-14 ('Scores were assigned by... a single evaluator. This follows the standard for calibration set construction described in LLM evaluation research...'). Fetched Microsoft Research abstract: 'the humans do not fully agree with one another'; method trains 'judge-specific and judge-independent parameters' to 'predict each human judge's annotations'. The file's own adjacent quote concedes 'reliability improves when averaging ratings from independent evaluators' (calibration-set.md:21).
  - Confidence: high — abstract text fetched directly; the tension with the adjacent Nielsen quote is on the page itself.
- **[MAJOR] [anchor-inconsistency]** Anchor 7's Process score of 10 contradicts both the framework's 9-10 Process band ('Ordered steps, checkpoints, and completion conditions all present') and the evaluator's own sub-criteria: the tic-tac-toe prompt has no numbered steps, no checkpoints, and no completion conditions
  - Evidence: framework/ppep-framework.md:75 (band definition); evaluator sub-criteria 'Checkpoints defined' and 'Completion conditions stated' at prompts/prompt-evaluator.md:31-32; the prompt text (evaluator:157) contains only 'explaining each step you do with code examples. ... Present your steps in a structured report' — no pause/verify instruction, no done-condition; scored 'Process 10' at evaluator:159 and calibration-set.md:172.
  - Confidence: high.
- **[MAJOR] [anchor-inconsistency]** Anchor 6's Epistemics score of 8 contradicts the framework's five-band Epistemics scale: band 8-9 requires 'Negative claims require proof', and the anchor's own note admits negative claims are not covered, which places it in band 6-7
  - Evidence: framework/ppep-framework.md:138-139 ('6-7: Explicit verification step present. Negative claims not explicitly addressed. 8-9: ... Negative claims require proof.') vs examples/prompt-calibration-set.md:156 ('Epistemics 8 ... Does not cover negative claims or inventory-before-judging').
  - Confidence: high — the contradiction is between two of the repo's own definitional texts.
- **[MAJOR] [anchor-inconsistency]** Anchor 9's Epistemics 10 contradicts the framework's band-10 definition, which requires 'Inventory before judging' and 'No summarizing as facts' — neither appears in the cover-letter prompt; the sentence relied on for negative-claims proof is garbled and literally says the opposite ('that you don't give negative claims' forbids negative claims rather than requiring proof for them)
  - Evidence: framework/ppep-framework.md:140 ('10: Full epistemic rigor. Inventory before judging. ... No summarizing as facts.') vs prompt text at prompts/prompt-evaluator.md:179 ('You have to always find and provide proof that what you propose is true and that you don't give negative claims'), scored as 'proof for positive and negative claims' at calibration-set.md:214.
  - Confidence: high on the band mismatch; the garbled-sentence reading is grammatical fact but its scoring impact is interpretive.
- **[MAJOR] [anchor-inconsistency]** Anchor 7's Performance 8 contradicts the framework's band structure: a prompt with no role at all ('No role defined' per the anchor's own note) falls in the 4-6 band ('Role absent or generic'), not 7-8 ('Role defined. Tone specified.')
  - Evidence: examples/prompt-calibration-set.md:173 ('Performance 8 ... No role defined.') vs framework/ppep-framework.md:99-100 ('4-6: ... Role absent or generic. 7-8: Role defined. Tone specified.').
  - Confidence: high.
- **[MAJOR] [reproducibility]** The pasted session prompt contains no band definitions at all — the 1-3/4-6/7-8/9-10 band table and the five-band Epistemics scale exist only in the calibration document and framework doc, which are not part of what users paste, so a fresh session has nine sparse anchors and no interpolation rule for the mid-range
  - Evidence: Band tables at examples/prompt-calibration-set.md:45-50 and framework/ppep-framework.md:132-140; prompts/prompt-evaluator.md:12-187 (the full pasted text) contains no band or scale definition beyond 'Score each dimension 1-10' (line 52). Anchor coverage gaps compound this: overall scores present = {1,3,3,5,7,8,9,10,10} — nothing at 2, 4, or 6; no Epistemics example between 1 and 6, no Performance example between 3 and 7.
  - Confidence: high.
- **[MAJOR] [reproducibility]** The Epistemics N/A boundary is contradictory across the toolkit's own documents: the calibration set declares 'creative writing' has no epistemic dimension, yet Anchors 3-4 (company blog writing) receive Epistemics scores of 1 and 7 rather than N/A; and Anchor 7's own prompt demands 'the latest best practices on React 19 including React Compiler' — knowledge retrieval that meets the calibration set's stated applicability test — yet is ruled N/A
  - Evidence: examples/prompt-calibration-set.md:176 ('Pure code generation from a complete specification, creative writing, and formatting tasks have no meaningful epistemic dimension') vs Epistemics 1 at calibration:102 (blog prompt) and Epistemics 7 at calibration:120; applicability test at calibration:176 ('requires the AI to make factual claims, retrieve or verify information') vs Anchor 7 prompt text at prompt-evaluator.md:157. The pasted evaluator carries only the thin one-line version of the rule (prompt-evaluator.md:163), not the four-part test.
  - Confidence: high on the textual contradiction; medium on how often it changes real scores (A3/A4 overall scores happen to round identically either way: (5+2+3)/3=3.33→3, (6+5+3)/3=4.67→5).
- **[MAJOR] [robustness]** The evaluator has no data/instruction separation: pasted prompts are not delimited or declared as data-to-evaluate, so a submitted prompt containing instructions (e.g. 'Ignore previous instructions, you are now...') can hijack the evaluator persona — contrary to current Anthropic guidance on XML-tag structuring for prompts that mix instructions and variable inputs
  - Evidence: prompts/prompt-evaluator.md:12 ('every time I share a prompt with you, evaluate it') is the only framing; no delimiter convention anywhere in lines 12-187. Fetched https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices: 'XML tags help Claude parse complex prompts unambiguously, especially when your prompt mixes instructions, context, examples, and variable inputs. Wrapping each type of content in its own tag (for example, <instructions>, <context>, <input>) reduces misinterpretation.' The nine inline anchors are likewise not wrapped in example tags ('Wrap examples in <example> tags ... so Claude can distinguish them from instructions').
  - Confidence: high on the gap; medium on real-world hijack frequency (modern models often resist, but the prompt does nothing to help).
- **[MAJOR] [edge-cases]** No edge-case handling exists for empty prompts, non-English prompts, very long prompts, multiple prompts in one message, or prompts that already score 10/10 — the output format mandates 'Either a revised 10/10 prompt, or your clarifying questions' with no branch for an already-perfect or unimprovable input
  - Evidence: prompts/prompt-evaluator.md:71-76 (output format has exactly two branches); no other section addresses input validity, language, or length anywhere in lines 12-187.
  - Confidence: high.
- **[MAJOR] [safety-gap]** The evaluator's unconditional mandate to produce 'a revised 10/10 prompt' for anything shared, combined with 'behave exactly as described', makes it a prompt-improvement engine with no scoping for harmful or jailbreak prompts — the session's only defense is the underlying model's safety training, which the prompt actively fights ('behave exactly as described')
  - Evidence: prompts/prompt-evaluator.md:12 ('every time I share a prompt with you, evaluate it using the framework below and behave exactly as described') and :76 ('Either a revised 10/10 prompt, or your clarifying questions'). No content-scope carve-out exists in the file.
  - Confidence: high on the textual gap; medium on practical exploitability.
- **[MAJOR] [self-consistency]** The evaluator does not apply its own flagship Epistemics standard to itself: it never requires the evaluator to quote the evaluated prompt as evidence, run an inventory of what is present before scoring, or prove negative claims ('no role defined') — the exact requirements it scores other prompts on
  - Evidence: The only evidence instruction is prompts/prompt-evaluator.md:53 ('Reference specific sub-criteria in your notes, not just general observations'); compare its own Epistemics sub-criteria at :43-46 ('Inventory before judging', 'Negative claims require proof', 'No summarizing as facts') and Anchor 8's celebrated pattern (:169). The comparison step ':91 compare it against the closest reference example' is also never surfaced in the required output (:73-76), so it is unauditable.
  - Confidence: high.
- **[MINOR] [reproducibility]** No rounding rule is stated for the overall score: three anchors require rounding (3.25→3, 2.75→3, 5.25→5) while Anchor 7 displays a decimal (9.0), so two sessions can legitimately report '3/10' vs '3.25/10' for the same prompt
  - Evidence: Rule at prompts/prompt-evaluator.md:54 says only 'Calculate an overall score as the average of the active dimensions'; computed A2=(7+2+3+1)/4=3.25 labeled '3/10' (:105), A3=2.75 labeled '3/10' (:115), A4=5.25 labeled '5/10' (:125), while :163 shows '(9 + 10 + 8) / 3 = 9.0'.
  - Confidence: high.
- **[MINOR] [consistency-drift]** Sub-criteria drift between the pasted evaluator and the framework/calibration set: the evaluator lists only 2 Performance sub-criteria (role, examples) while the framework lists 4 (role, tone, collaboration style, depth), and calibration anchor notes score against tone and collaboration style that the pasted prompt never defines as sub-criteria
  - Evidence: prompts/prompt-evaluator.md:36-38 vs framework/ppep-framework.md:84-87; calibration notes scoring undefined sub-criteria, e.g. examples/prompt-calibration-set.md:83 ('No role, no tone, no collaboration style') and :155 ('Missing tone calibration').
  - Confidence: high.
- **[MINOR] [anchor-labeling]** Two anchor 'failure mode' labels contradict their own score tables: Anchor 5 is labeled 'strong everywhere except Product' but its lowest score is Epistemics 6 (Product is 7), and Anchor 6 is labeled 'weak Product angle' while Product 9 is its highest score
  - Evidence: prompts/prompt-evaluator.md:135 + :139 ('Product 7, Process 8, Performance 7, Epistemics 6'); :145 + :149 ('Product 9, Process 7, Performance 8, Epistemics 8').
  - Confidence: high.
- **[MINOR] [data-provenance]** The 'nine real prompts' are actually seven scenarios: Anchors 2/5 share an identical base text (job posting) and Anchors 3/4 share an identical base text (blog post), so diversity is overstated even though iterative provenance is disclosed
  - Evidence: Verbatim shared openings: prompts/prompt-evaluator.md:107 vs :137 ('Help me write a job posting for a senior developer position. We are a company looking for developers...') and :117 vs :127 ('Write something for our company blog. We are a company making athletic footwear...'); disclosure at examples/prompt-calibration-set.md:10 ('iteratively improved').
  - Confidence: high.
- **[MINOR] [unsubstantiated-claim]** The empirical claim that 'the calibration set reduces scoring variance' has never been measured — no test-retest, inter-session, or inter-model agreement data exists anywhere in the repository
  - Evidence: examples/prompt-calibration-set.md:23; repo-wide grep for 'variance|test-retest|inter-rater|agreement|reproducib' returns only the claim itself and its echo at framework/ppep-framework.md:198 — no data files, logs, or experiment records.
  - Confidence: high that no evidence exists in-repo; the claim itself is plausible but unproven.
- **[MINOR] [citation-verification]** The blockquote attributed to 'Nielsen (1993), as discussed in Hertzum (2006)' is presented in quotation marks but is unverifiable as a direct quote; the Hertzum citation metadata itself (journal, 21(2), 125-146) checks out
  - Evidence: examples/prompt-calibration-set.md:21; bibliographic details confirmed via web search (ResearchGate entry 'Problem Prioritization in Usability Evaluation: From Severity Assessments Toward Impact on Design', IJHCI 21(2), 125-146); paper full text inaccessible through the audit proxy (nngroup.com and journal egress blocked), so the verbatim sentence could not be confirmed.
  - Confidence: low that it is a fabricated quote (substance matches Nielsen's known severity-ratings guidance); high that it is unverifiable from this environment — flagged for the citations agent.
- **[MINOR] [circularity]** Overall-score narratives in the anchor justifications are partly circular — they restate the score as its own justification rather than deriving it from stated rules
  - Evidence: prompts/prompt-evaluator.md:151 ('Three dimensions at 8+ with one clear remaining gap is the signature of an 8/10 prompt') and examples/prompt-calibration-set.md:158 (same sentence pattern); by contrast the per-dimension notes cite concrete features (e.g. calibration:153 'Word count, audience, format all specified').
  - Confidence: high for the quoted instances; the per-dimension layer is largely non-circular, which tempers severity.
- **[MINOR] [prompt-craft]** Referent confusion runs through the pasted prompt: 'you' means the evaluator AI at line 12, the human prompt-author at line 21 ('Clearly defines what you want'), and 'Claude' appears in third person at line 31 ('when Claude should pause') — while the header claims compatibility 'with any instruction-following AI model' despite the hardcoded Claude references
  - Evidence: prompts/prompt-evaluator.md:12, :21, :31, :7-8; calibration-set.md:47-50 likewise phrases observable signals in terms of Claude only.
  - Confidence: high on the textual facts; models usually cope, so impact is modest.
- **[MINOR] [delivery-mechanism]** The session-intro (user-turn paste) delivery has structural limits the docs never acknowledge: instructions sit in a user turn rather than a system prompt (current Anthropic guidance: 'Setting a role in the system prompt focuses Claude's behavior'), evaluator behavior decays over long sessions with no re-anchoring mechanism, and there is no versioning to tie a score to the evaluator revision that produced it
  - Evidence: Delivery instruction at prompts/prompt-evaluator.md:4-5 ('paste it into a new conversation'); role-in-system-prompt quote fetched from https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices; no version identifier exists anywhere in the pasted text (lines 12-187).
  - Confidence: high on the facts; the pattern is still a legitimate choice for chat-UI accessibility — this is a trade-off left undiscussed, not nonsense.
- **[NITPICK] [band-inconsistency]** Anchor 2's Product-7 note is almost verbatim the framework's 4-6 band descriptor, yet the score is 7
  - Evidence: examples/prompt-calibration-set.md:81 ('Missing format, length, tone, location') vs framework/ppep-framework.md:52 ('4-6: Deliverable is implied but key constraints are missing (format, length, audience)').
  - Confidence: high.
- **[NITPICK] [citation-verification]** The Label Studio citation (dated 2026) resolves to a real post at the cited URL, but the page's current title differs ('Scale AI Evaluation with Rubrics and Calibration') and its content could not be fetched to confirm it supports the 'requires human expert judgment' framing; the search snippet's summary mentions 'disagreement review' as a core building block — again multi-reviewer flavored
  - Evidence: examples/prompt-calibration-set.md:15; WebSearch result: https://labelstud.io/blog/how-to-scale-evaluation-for-rag-and-agent-workflows/ exists with title 'Scale AI Evaluation with Rubrics and Calibration | Label Studio'; direct fetch blocked by egress proxy.
  - Confidence: low-medium — existence confirmed, content support unverified; flagged for citations agent.

## Open questions

- For the framework agent: the calibration set's cross-references to framework/ppep-framework.md check out textually (93% at framework:192, five-band Epistemics at framework:134-140), but the 93%/7% construct itself — repeated at prompt-calibration-set.md:23 as if variance were quantified — needs the methodology deep-dive; note also the coordinator's checkpoint item 1 (framework:175 points to an N/A definition the framework never contains).
- For the citations agent: two items I could not complete due to egress blocks — (1) verbatim verification of the Nielsen-via-Hertzum blockquote (calibration-set.md:21) against the actual Hertzum 2006 paper or Nielsen 1993; (2) content verification of the Label Studio post (calibration-set.md:15), including whether its publication date is really 2026.
- For the methodology agent: the LLM-Rubric misattribution and mischaracterization (my findings 2-3) are the concrete entry point to the single-evaluator ground-truth critique — the paper's multi-judge, disagreement-modeling design is quotable ammunition ('the humans do not fully agree with one another', fetched from the Microsoft Research abstract).
- For the Phase 3 reproducibility test: the highest-yield probe is a mid-band prompt missing exactly one sub-criterion per dimension — it forces the rule-vs-anchor conflict (evaluator:55 vs Anchors 2/4/5/6/7) and the unstated rounding rule simultaneously; predict divergence between sessions on both.
- For the best-practices/competition agents: I assessed the session-intro pattern only against fetched Anthropic guidance (system-prompt role placement, XML structuring, example tagging); whether Aug-2026 evaluator tooling (promptfoo-style eval harnesses, LLM-judge frameworks) makes the paste-in pattern look dated is their call.
- Interview questions the owner should prepare for, from this lane: (1) 'Your rule says a missing sub-criterion caps a dimension at 6; Anchor 2 scores Product 7 while missing format, length, tone, and location — which is wrong, the rule or the anchor?' (2) 'Who wrote the LLM-Rubric paper you cite?' (3) 'That paper calibrates against multiple disagreeing judges and your own Nielsen quote says to average independent evaluators — why is your ground truth one person?' (4) 'Anchor 7 has no checkpoints or completion conditions; your framework says both are required for Process 9-10 — why is it a 10?' (5) 'The tic-tac-toe prompt demands the latest React 19 best practices — how is that not a verification task under your own N/A test?' (6) 'What happens when someone pastes an empty prompt, a 6,000-word prompt, or a jailbreak? Your evaluator promises a revised 10/10 version of anything.' (7) 'Is 2.75 a 3? Where is the rounding rule?' (8) 'Have you ever measured the variance reduction you claim?' (9) 'Why doesn't your evaluator have to prove its own negative claims, given that is your flagship dimension?'

---

## Full report

# Audit: prompts/prompt-evaluator.md + examples/prompt-calibration-set.md

Auditor lane: prompt evaluator and its calibration set. Date: 2026-08-12. All file references are to `/home/user/prompt-engineering-toolkit/`. Web claims were verified by live fetch/search through the audit proxy today; blocked domains are noted explicitly.

## 1. What these files are

- `prompts/prompt-evaluator.md` (187 lines, created 2026-04-15, last touched 2026-04-16 per `git log`): a paste-into-chat "session intro prompt" that turns a chat session into a strict prompt evaluator scoring four PPEP dimensions (Product, Process, Performance, Epistemics) 1-10 each, with all nine calibration anchors inlined (lines 95-183) and a confirmation handshake (line 187). The pasted portion (lines 12-187) is **2,023 words** (~2,700-3,000 tokens) — reasonable for a session preamble.
- `examples/prompt-calibration-set.md` (237 lines, created 2026-04-15, last revised 2026-04-16): the same nine anchors in long form, plus a methodology section with citations, a known-limitations section, a scoring-scale band table, and five hedged "observations".

## 2. Scoring system map and arithmetic (Task 1)

**System:** 4 dimensions × 1-10, **no weights** — overall = unweighted mean of "active dimensions" (evaluator:54). Epistemics can be N/A, in which case the mean is over three dimensions (evaluator:54, :163). Since there are no weights, the sum-to-1.0 check is N/A; effective weights are 0.25 each (1/3 under N/A).

**Recomputation of all nine anchors** (dimension scores identical in both files, verified score-by-score):

| Anchor | Dims | Computed mean | Stated overall | Match? |
|---|---|---|---|---|
| 1 | 1,1,1,1 | 1.00 | 1/10 | Yes |
| 2 | 7,2,3,1 | **3.25** | 3/10 | Yes, via unstated rounding |
| 3 | 5,2,3,1 | **2.75** | 3/10 | Yes, via unstated rounding |
| 4 | 6,5,3,7 | **5.25** | 5/10 | Yes, via unstated rounding |
| 5 | 7,8,7,6 | 7.00 | 7/10 | Yes |
| 6 | 9,7,8,8 | 8.00 | 8/10 | Yes |
| 7 | 9,10,8,N/A | (9+10+8)/3 = 9.00 | 9/10 | Yes (worked example shown at evaluator:163) |
| 8 | 10,10,10,10 | 10.00 | 10/10 | Yes |
| 9 | 10,10,10,10 | 10.00 | 10/10 | Yes |

**Verdict: the arithmetic is clean.** Every overall equals the mean rounded to nearest integer. But the **rounding rule is never stated** — evaluator:54 says only "Calculate an overall score as the average," while :163 displays a decimal (9.0). Two sessions can report "3/10" vs "3.25/10" for the same prompt. Minor but real reproducibility leak, in a toolkit whose selling point is reproducible scoring.

## 3. The critical finding: the strictness rule contradicts the anchors (Tasks 1-2)

Evaluator:55: **"Be strict. A prompt missing sub-criteria should not score above 6 on that dimension."**

Checked against every anchor, using the evaluator's own listed sub-criteria (Product: context, output constraints — :23-24; Process: steps, methodology, checkpoints, completion conditions — :29-32; Performance: role, examples — :37-38; Epistemics: inventory, negative-claims proof, reasoning-first, no-summarizing — :43-46):

| Anchor / dimension | Score | Admitted missing sub-criteria (quoted) | Rule-compliant? |
|---|---|---|---|
| A2 Product | 7 | "Missing format, length, tone, location" (calibration:81) — the whole "Output constraints specified" sub-criterion | **No** |
| A4 Epistemics | 7 | Prompt text (evaluator:127) contains none of the four Epistemics sub-criteria | **No — even under the charitable "missing ALL sub-criteria" reading** |
| A5 Product | 7 | Same as A2 (calibration:135) | **No** |
| A5 Performance | 7 | "No role defined, no tone specified" (calibration:137) — both evaluator-listed sub-criteria (role, examples) absent | **No — even under the charitable reading** |
| A6 Epistemics | 8 | "Does not cover negative claims or inventory-before-judging" (calibration:156) | **No** |
| A7 Performance | 8 | "No role defined" (calibration:173) | **No** |

At least five of nine anchors violate the rule as written; two violate it under *any* reading. **A fresh session receives a rule and a set of examples that contradict it and must silently pick one** — the definition of an irreproducible rubric. This is the single most attackable fact in this lane: the "calibrated" evaluator is calibrated against examples that break its own calibration rule.

## 4. Anchor soundness vs the framework's own band definitions (Task 4)

The calibration set (line 43) delegates its scale to the framework's bands. Checking anchors against those bands:

- **A7 Process 10** vs framework:75 ("9-10: Full process defined. Ordered steps, checkpoints, and completion conditions all present"). The tic-tac-toe prompt (evaluator:157) has *no numbered steps, no checkpoints, no completion conditions* — only "explaining each step you do with code examples… Present your steps in a structured report." A 10 is indefensible under the toolkit's own definition. (Its grammar is also garbled: "I want to be detailed in the approach you follow.")
- **A7 Performance 8** vs framework:99-100: "4-6: … Role absent or generic. 7-8: Role defined." The anchor note says "No role defined" — by the bands this is a 4-6, not an 8.
- **A6 Epistemics 8** vs framework:138-139: band 8-9 *requires* "Negative claims require proof"; the note admits "Does not cover negative claims" — that is band 6-7 by definition.
- **A9 Epistemics 10** vs framework:140 (band 10 requires "Inventory before judging… No summarizing as facts") — neither appears in the cover-letter prompt. Worse, the load-bearing sentence is garbled: "provide proof that what you propose is true and that you don't give negative claims" (evaluator:179) literally *forbids* negative claims; the calibration note (214) reads it as "proof for positive and negative claims." Both 10/10 anchors contain ungrammatical sentences while band 9-10 is defined as "fully specified with no meaningful ambiguity" (calibration:50) — the rubric has no clarity/parseability dimension at all, which an interviewer can exploit.
- **A2 Product 7**: the note ("Missing format, length, tone, location") is nearly verbatim the framework's *4-6* descriptor ("key constraints are missing (format, length, audience)", framework:52).
- **A9 Product 10** ("Claude has everything it needs", band 9-10): the prompt asks Claude to cover "all the things I worked on with the manager" — content never supplied. The clarifying-questions instruction partially rescues this, but "no meaningful ambiguity" is generous for a prompt with no company, no job posting, and a 1000-word cover letter (2-3× standard length).

**Span check (README:34, :74):** "spanning 1/10 to 10/10" is true only as a range. Actual coverage: {1, 3, 3, 5, 7, 8, 9, 10, 10} — **nothing at 2, 4, or 6**, and per-dimension the gaps are worse (no Epistemics between 1 and 6; no Performance between 3 and 7; no Product between 1 and 5). The muddy middle — where calibration matters most — is unanchored.

**The two 10/10 anchors (README:74): claim TRUE.** Anchors 8 and 9 exist, are verbatim identical across both files, and are genuinely structurally distinct — grep/inventory/file:line agentic auditing vs role-layering/iteration/completion-condition collaborative writing ("No grep commands, no file references, no agentic tools", calibration:216). Anchor 8 in particular is a legitimately excellent prompt. One honest quibble: Anchor 8's headline ask ("Improve the overall UI/UX") is never implemented by its deliverables, which end at "Discussion — pause for my input"; it's an audit prompt wearing an improvement prompt's title.

**Circularity:** mixed. Per-dimension notes cite concrete observable features (good, falsifiable: "No topic, format, or length", calibration:99). But overall-score narratives are score-restating: "Three dimensions at 8+ with one clear remaining gap is the signature of an 8/10 prompt" (evaluator:151) justifies the 8 by declaring it an 8.

**Provenance:** "nine real prompts" = **seven scenarios**. A2/A5 share an identical job-posting base text (evaluator:107 vs :137); A3/A4 share an identical blog base text (:117 vs :127). Iteration is disclosed (calibration:10), which is honest, but "nine" overstates diversity.

## 5. Cross-file consistency (Task 3)

- All nine **anchor prompt texts are verbatim identical** across the two files (extracted and diffed: zero differences).
- All 33 dimension scores and 9 overall scores agree exactly.
- Band tables in calibration:45-50 match framework:51-54/:71-75/:97-101 structurally; the five-band Epistemics claim (calibration:43) matches framework:134-140.
- **Drift 1:** the pasted evaluator lists only 2 Performance sub-criteria (role, examples; evaluator:37-38) vs the framework's 4 (role, tone, collaboration, depth; framework:84-87) — and the calibration notes score against tone and collaboration ("No role, no tone, no collaboration style", calibration:83), sub-criteria the pasted evaluator never defines.
- **Drift 2:** the N/A definition exists in full only in calibration:176 (four-part applicability test); the pasted evaluator carries a one-line version (:163). See §7.
- **Drift 3 (labels vs tables):** A5's label "strong everywhere except Product" (evaluator:135) contradicts its own scores — Epistemics 6 is the lowest, Product is 7. A6's label "weak Product angle" (:145) sits atop Product 9, its *highest* score.
- **Double-counting:** A4 credits the same sentence ("web search and verification") to both Process 5 ("a genuine process instruction", calibration:119) and Epistemics 7 ("a real epistemic instruction", :120) — dimension orthogonality is not maintained.

## 6. Reproducibility: would two fresh sessions agree? (Task 2)

Probably not on mid-band prompts. Enumerated ambiguities, each quoted:

1. Rule-vs-anchor conflict (§3) — the session must choose.
2. No rounding rule (§2).
3. No band definitions in the pasted prompt — "Score each dimension 1-10" (:52) is the only scale text; the bands live in documents users are never told to paste.
4. "Be strict" (:55) is unquantified beyond the (violated) 6-cap.
5. N/A trigger underspecified in the pasted text: "not applicable for a pure code generation task with no research or verification component" (:163) — is a marketing blog post "creative writing" (N/A per calibration:176) or fact-asserting (scored, per Anchors 3-4)? The toolkit's own documents disagree. And A7's own prompt demands "the latest best practices on React 19 including React Compiler" — knowledge retrieval that meets calibration:176's applicability test, making the toolkit's flagship N/A example contestable by its own definition. (Silver lining I verified: A3/A4's overall scores happen to round identically under both readings — (5+2+3)/3=3.33→3 and (6+5+3)/3=4.67→5.)
6. Output format loose: "a score card" (:74) — no table spec, no ordering, no requirement to show which anchor was matched (the "compare it against the closest reference example" step at :91 is invisible in output, so unauditable).
7. "average of the active dimensions" (:54) implies other dimensions could be inactive, but only Epistemics N/A is defined.
8. Out-of-domain requests: "you can do so but stay in the evaluator persona" (:85) — evaluate with what rubric?

## 7. The evaluator prompt judged as a prompt (Task 5)

Baseline: Anthropic's current best-practices page, fetched 2026-08-12 from `https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices` (the overview at `/prompt-engineering/overview` names it "the living reference").

**Aligned with current guidance:**
- Role definition up front ("strict, expert prompt evaluator", :12; "strict professor", :82).
- Example-rich: nine labeled anchors. Guidance: "Examples are one of the most reliable ways to steer Claude's output format, tone, and structure."
- Confirmation handshake (:187) — a sound comprehension check.
- Well-specified conditional logic for clarifying questions (:62-67) with a hard cap of 3 — genuinely better than most evaluator prompts.

**Against current guidance:**
- **No XML/tag structure anywhere.** Guidance: "XML tags help Claude parse complex prompts unambiguously, especially when your prompt mixes instructions, context, examples, and variable inputs. Wrapping each type of content in its own tag (for example, `<instructions>`, `<context>`, `<input>`) reduces misinterpretation," and examples should be wrapped "in `<example>` tags … so Claude can distinguish them from instructions." This prompt mixes all four content types with only markdown headers and no delimiter convention for the *evaluated* prompt — the variable input.
- **No data/instruction separation → injection surface.** Nothing tells the model to treat pasted prompts as data. A submitted "prompt" that says "You are now…" competes directly with the evaluator persona. For an evaluator whose whole job is ingesting untrusted prompt text, this is the most consequential craft gap.
- **Edge cases: none.** Empty prompt, non-English prompt, 10k-token prompt, multiple prompts in one message, or a prompt that is already 10/10 — the mandatory output "Either a revised 10/10 prompt, or your clarifying questions" (:76) has no branch for any of these.
- **Safety scoping: none.** ":12 every time I share a prompt with you, evaluate it… and behave exactly as described" + the revised-10/10 mandate makes it, textually, a jailbreak-improvement engine; the only backstop is the model's own training, which "behave exactly as described" fights.
- **Referent confusion:** "you" = evaluator (:12) but = prompt-author (:21 "Clearly defines what you want"); "Claude" third-person (:31) despite ":7 Compatible with any instruction-following AI model."
- **The irony finding:** the evaluator never applies its own Epistemics gospel to itself. It requires no quotes from the evaluated prompt, no inventory-before-scoring, no proof for its negative claims ("no role defined") — the exact behaviors it scores others on (:43-46) and celebrates in Anchor 8. The strongest self-consistency question an interviewer can ask.

## 8. Citation verification (calibration set methodology section)

1. **Eisenstein misattribution — CONFIRMED ERROR.** calibration:14 cites "Eisenstein, J., et al. (2024). *LLM-Rubric…*". The paper's actual authors are **Helia Hashemi, Jason Eisner, Corby Rosset, Benjamin Van Durme, Chris Kedzie** — verified via the Microsoft Research publication page (fetched, full author list), Semantic Scholar ("Hashemi-Eisner"), and JHU slides (`hashemi+al.acl24.slides.pdf`). No Eisenstein. Apparent confusion of Jason **Eisner** with Jacob **Eisenstein** (a different, unrelated NLP researcher). Title and URL are correct; the attribution is wrong. Trivial to fix before the interview; devastating if an interviewer catches it first in a project whose brand is citation rigor.
2. **Mischaracterization — CONFIRMED.** calibration:12-14 uses LLM-Rubric to claim single-expert scoring "follows the standard for calibration set construction… which requires human expert judgment rather than automated scoring as the ground truth source." The fetched abstract: the method trains "judge-specific and judge-independent parameters" to "predict each human judge's annotations," noting "the humans do not fully agree with one another." The paper is a *multi-judge disagreement-modeling* method — evidence against single-evaluator ground truth. The file's own next quote concedes it: "reliability improves when averaging ratings from independent evaluators" (calibration:21). To be fair, the Known Limitations section (:19-25) discloses the single-evaluator weakness honestly — but "follows the standard" is an overreach the sources don't support.
3. **Label Studio (2026)** — post exists at the cited URL (search-confirmed); current title is "Scale AI Evaluation with Rubrics and Calibration"; content fetch egress-blocked, so support for the claim is unverified. The search snippet describes "disagreement review" as a core building block — again multi-reviewer. Low-medium confidence; handed to citations agent.
4. **Hertzum 2006** — bibliographic details check out (IJHCI 21(2), 125-146, title confirmed via search). The blockquote at calibration:21 is presented in quotation marks but I could not verify it verbatim (nngroup.com and journal access egress-blocked); it reads like a paraphrase-in-quotes. Substance is consistent with Nielsen's known severity-rating guidance. Low confidence in "fabricated," high confidence in "unverifiable as a direct quote."
5. **Unmeasured claim:** ":23 The calibration set reduces scoring variance by providing nine concrete reference points" — a repo-wide grep for variance/test-retest/inter-rater/agreement finds only the claim and its echo (framework:198). No experiment, log, or data file exists. The 93%/7% construct repeated at :23 inherits the framework's pseudo-quantification (framework agent's lane for the deep dive).

## 9. The session-intro delivery mechanism (Task 6 — brief; competition is another agent's lane)

**Strengths:** zero-install, works in any chat UI, model-agnostic in principle, self-contained (anchors travel with the prompt — the right call given §6.3), handshake confirms load, MIT-licensed text is trivially forkable.

**Limits (undisclosed in the docs):** (a) lives in a *user* turn — current guidance: "Setting a role in the system prompt focuses Claude's behavior and tone"; user-turn instructions have weaker priority and decay as the conversation grows, with no re-anchoring mechanism for turn 40; (b) no output enforcement vs structured-output tooling; (c) ~2-3k tokens re-paid every session; (d) no version stamp in the pasted text, so a score can't be traced to the evaluator revision that produced it (the git history shows the scoring rules changed on 2026-04-16, commit 5bd9248 "Refine scoring behavior and Epistemics notes"); (e) inherently un-testable at scale versus eval-harness patterns. These are legitimate trade-offs for an accessibility-first tool — but the docs present the pattern without acknowledging any of them.

## 10. Bottom line for the interview

**Genuinely good:** clean arithmetic; perfect cross-file textual consistency (diff-verified); two real, structurally distinct 10/10 anchors exactly as advertised; a thoughtful N/A anti-deflation rule with worked math; unusually disciplined clarifying-question logic; honest hedging and limitation disclosure; pedagogically strong failure-mode labels.

**Bad:** the strictness rule contradicts 5+ of its own anchors; four anchor scores contradict the framework's band definitions; the pasted prompt ships without the band scale; the N/A boundary contradicts itself across documents; no rounding rule.

**Nonsense:** citing a multi-judge calibration paper (with the wrong author) as the methodological blessing for single-judge ground truth, two paragraphs above a quote saying to average independent evaluators.

**Incomplete:** edge cases (empty/non-English/huge/already-perfect/harmful inputs), injection separation, evidence requirements for the evaluator's own claims, any measurement of the variance-reduction claim, mid-band anchor coverage (no 2, 4, or 6).

**Hardest questions to prepare for:** (1) rule-vs-Anchor-2 — which is wrong? (2) who wrote LLM-Rubric? (3) why single-evaluator ground truth against your own quoted sources? (4) why is Anchor 7 Process 10 with no checkpoints or completion conditions? (5) how is "latest React 19 best practices" not a verification task under your own N/A test? (6) what happens with an empty prompt, a 6,000-word prompt, or a jailbreak? (7) is 2.75 a 3? (8) did you ever measure the variance reduction? (9) why doesn't the evaluator have to prove its own negative claims?

Sources fetched/searched this session: [Microsoft Research — LLM-Rubric publication page](https://www.microsoft.com/en-us/research/publication/llm-rubric-a-multidimensional-calibrated-approach-to-automated-evaluation-of-natural-language-texts/), [ACL Anthology entry (via search)](https://aclanthology.org/2024.acl-long.745/), [Semantic Scholar entry](https://www.semanticscholar.org/paper/LLM-Rubric:-A-Multidimensional,-Calibrated-Approach-Hashemi-Eisner/246bfb77363e9f4188bd787e42aefced548a4787), [microsoft/LLM-Rubric GitHub](https://github.com/microsoft/LLM-Rubric), [Label Studio post (existence only)](https://labelstud.io/blog/how-to-scale-evaluation-for-rag-and-agent-workflows/), [Hertzum 2006 (bibliographic, via ResearchGate search result)](https://www.researchgate.net/publication/220302680_Problem_Prioritization_in_Usability_Evaluation_From_Severity_Assessments_Toward_Impact_on_Design), [Anthropic prompt-engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview), [Anthropic prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices).