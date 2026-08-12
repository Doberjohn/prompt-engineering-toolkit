# Agent report: framework

## Executive summary

The PPEP framework is a competently written, well-structured operationalization of Anthropic's AI Fluency "Description" competency — but its originality and rigor claims are substantially overstated, and that is the owner's biggest interview risk. Verified via web search: the three dimensions Product/Process/Performance are the AI Fluency course's own three named components of Description (near-verbatim glosses), so the framework's sole novel dimension is Epistemics — and even one of its Epistemics techniques ("Ask It to Think First") is imported from the same Anthropic handout the README says the dimension was "independently surfaced" apart from. The "93% confidence" figure is pseudo-quantification: no metric, procedure, or data exists anywhere in the repo, the promised "confidence intervals documented throughout" appear zero times, and the cited Nielsen/Hertzum literature actually documents single-evaluator unreliability far worse than 7% — it undercuts rather than supports the number. The "seven evidence-based techniques" are faithfully reproduced from a 2025 Anthropic course handout titled "6 Techniques for Effective Prompt Engineering" (verified at the exact cited URL), which is pedagogy, not research, and the framework's own impact claims (e.g. role prompting as "one of the most impactful single-line additions") are contradicted for factual tasks by peer-reviewed work (EMNLP 2024 Findings). Genuine strengths survive scrutiny: the Epistemics dimension's audit-grade criteria (negative claims require proof, no summarizing as facts) are sharp, concrete, and genuinely rare as named scoring criteria in major guides; the 4D attribution, licensing note, and HEA Ireland support note are all accurate; and the diagnostic per-dimension design with calibration anchors is real design work the course itself does not provide.

## Strengths (with evidence)

- **The AI Fluency 4D framework is represented faithfully and attributed accurately: the README's one-line definitions of Delegation, Description, Discernment, and Diligence match Anthropic's official definitions, and the 'Supported in part by the Higher Education Authority, Ireland, through the National Forum for the Enhancement of Teaching and Learning' note is verified real.**
  - Evidence: README.md:11-14 vs Anthropic course definitions confirmed via web search (anthropic.skilljar.com/ai-fluency-framework-foundations; anthropic.com/ai-fluency/description); HEA/National Forum support confirmed at https://www.teachingandlearning.ie/2025/05/28/supporting-ai-fluency-in-higher-education/ and https://www.educationawards.ie/news/anthropic-and-university-partners-develop-ai-fluency-courses-for-irish-higher-education
- **The seven techniques faithfully reproduce the cited Anthropic handout, including the meta-technique framing and the quoted phrase 'perhaps the most powerful technique of all' (which is real: the handout says of asking the AI for prompting help, 'This is perhaps the most powerful technique of all!').**
  - Evidence: framework/ppep-framework.md:150-165 vs the PDF at the exact cited URL https://www-cdn.anthropic.com/62df988c101af71291b06843b63d39bbd600bed8.pdf, whose indexed title is '6 Techniques for Effective Prompt Engineering' and whose six techniques (context, examples, constraints, steps, think-first, role) plus the ask-AI-for-help closing tip were confirmed via two independent web searches
- **The Epistemics dimension is a genuine practice-derived contribution: 'negative claims require proof' and 'no summarizing as facts' are sharp, actionable, audit-grade criteria that do not appear as named scoring criteria in Anthropic's or OpenAI's guides, and the paired weak/strong example ('There are no entrance animations' vs the grep-inventory version) is the best pedagogy in the document.**
  - Evidence: framework/ppep-framework.md:110-127; contrast verified: Anthropic 'Reduce hallucinations' docs cover allow-I-don't-know/citations/direct-quotes and OpenAI's guide covers reference-text/citations/time-to-think, but neither names inventory-before-judging or proof-for-negative-claims as scoring criteria (https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations)
- **The diagnostic decomposition design is practically useful and goes beyond the source course: per-dimension 1-10 scoring bands, a task-type criticality table, and an Epistemics N/A provision that avoids penalizing pure code-generation prompts are real operationalization work the AI Fluency course does not provide.**
  - Evidence: framework/ppep-framework.md:29 ('Understanding which dimension is failing tells you exactly how to fix it'), :50-54/:71-75/:97-101/:132-140 (band rubrics), :177-186 (task-type table); N/A rule at prompts/prompt-evaluator.md:159-163 and examples/prompt-calibration-set.md:176-180
- **The scope note honestly delimits PPEP to the Description competency and explicitly names the three uncovered competencies — accurate self-positioning that survives verification.**
  - Evidence: framework/ppep-framework.md:10: 'The PPEP framework covers the Description competency of the AI Fluency 4D Framework... The three peer competencies — Delegation..., Discernment..., and Diligence... — are not covered by this framework.'
- **The calibration set (referenced by the framework) practices better epistemic hygiene than the framework doc itself, explicitly refusing to generalize from nine examples.**
  - Evidence: examples/prompt-calibration-set.md:231: 'Whether this reflects general user behaviour is not claimed here — it reflects the development trajectory of these nine specific prompts.'

## Findings

- **[CRITICAL] [originality-overclaim]** The framework's three dimensions Product/Process/Performance are the AI Fluency course's own three named components of the Description competency (Product Description, Process Description, Performance Description) with near-verbatim glosses, yet the framework presents the four-dimension model as its own creation ('developed through iterative testing') and never discloses the component-level provenance — making the true novel contribution only the Epistemics dimension plus the scoring rubrics/anchors.
  - Evidence: framework/ppep-framework.md:8 ('It was developed through iterative testing') and :14-17 ('Product — what you want; Process — how the AI should approach it; Performance — how the AI should behave') vs Anthropic's official page (https://www.anthropic.com/ai-fluency/description, verified via web search): 'Product Description (clearly defining what you want the AI to create), Process Description (guiding how the AI approaches your request), Performance Description (defining how you want the AI to behave during your collaboration)'. The scope note (:10) attributes only the competency, not the triad.
  - Confidence: high — confirmed by two independent searches quoting anthropic.com/ai-fluency/description; could be softened only if the owner can show the P/P/P naming predates their reading of the course, which the repo gives no evidence of
- **[CRITICAL] [pseudo-quantification]** 'Framework confidence: 93%' is pseudo-quantification dressed as rigor: no metric definition, measurement procedure, or data exists anywhere in the repo; 93% = 100% − 7% where the '7% irreducible subjectivity' is asserted, not derived; and the cited Nielsen/Hertzum literature quantifies nothing at 7% — it documents single-evaluator unreliability far LARGER than 7%, so the citation undercuts the number it is offered to support.
  - Evidence: framework/ppep-framework.md:192-198; README.md:90 ('built with explicit confidence tracking. Current confidence level in the framework: 93%') — no tracking artifact exists in the repo (grep for confidence/93%/7% returns only the claims themselves). NN/G (Nielsen), verified: 'severity ratings from a single evaluator are too unreliable to be trusted' (https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/); Hertzum 2006 documents substantial evaluator disagreement (https://www.researchgate.net/publication/220302680); search-summarized inter-expert severity correlations (~r=.33) imply subjective variance far above 7%.
  - Confidence: high on the absence of any derivation (exhaustive local grep); medium on the exact correlation figures (from search summaries, source pages unfetchable through this environment's egress proxy)
- **[MAJOR] [false-claim]** README claims 'confidence intervals... are documented throughout' but zero confidence intervals exist anywhere in the repository — the word 'interval' appears exactly once, in that sentence itself.
  - Evidence: README.md:35: 'confidence intervals, epistemic uncertainty, and the 7% irreducible subjectivity... are documented throughout'; grep -rn 'interval' over the whole repo returns only README.md:35.
  - Confidence: high — exhaustive grep shown
- **[MAJOR] [citation-mischaracterization]** The 'seven evidence-based prompting techniques from Anthropic's prompting research' are actually the six techniques plus one closing tip from a CC-licensed course handout titled '6 Techniques for Effective Prompt Engineering' — pedagogy, not research — and the reference mislabels that handout URL as the full 'AI Fluency: Framework and Foundations' document.
  - Evidence: framework/ppep-framework.md:146 ('seven evidence-based prompting techniques from Anthropic's prompting research') and :169/:206 (citation titled 'AI Fluency: Framework and Foundations' linking https://www-cdn.anthropic.com/62df988c101af71291b06843b63d39bbd600bed8.pdf); two independent web searches return that exact URL indexed under the title '6 Techniques for Effective Prompt Engineering 1. Provide context Before…', a handout from the course's Deep Dive 2 lesson (https://www.anthropic.com/ai-fluency/deep-dive-2-effective-prompting-techniques).
  - Confidence: medium-high — the PDF itself is unfetchable through this environment's egress proxy, but the URL-to-title match was confirmed by two independent search results; whether the handout carries any internal research citations could not be verified
- **[MAJOR] [unsupported-claims]** The framework makes strong empirical impact claims with zero citations, and its flagship role-prompting claim is contradicted for factual performance by peer-reviewed research: 'Role definition is one of the most impactful single-line additions to any prompt' vs EMNLP 2024 Findings showing personas in system prompts do not improve LLM performance on 2,410 factual questions across 162 roles.
  - Evidence: framework/ppep-framework.md:90; also :48 ('Format specification is one of the highest-leverage additions to any prompt'), :93 ('the most commonly underused technique') — no citations anywhere. Counter-evidence: Zheng et al., 'When "A Helpful Assistant" Is Not Really Helpful: Personas in System Prompts Do Not Improve Performances of Large Language Models', Findings of EMNLP 2024 (https://arxiv.org/abs/2311.10054, https://aclanthology.org/2024.findings-emnlp.888/).
  - Confidence: high; fairness note: the framework maps role to tone/depth/vocabulary (where role prompting is defensible), but 'one of the most impactful' is stated unconditionally
- **[MAJOR] [unsupported-claims]** 'Guided by decades of research on how structured instructions improve AI reasoning (and human performance)' is uncited hand-waving: no such citation exists in the repo, and 'decades of research' on AI reasoning via prompting is anachronistic (LLM prompting research is roughly 2020+; the parenthetical about humans carries the sentence).
  - Evidence: framework/ppep-framework.md:69; the framework's reference list (:204-206) contains only Nielsen 1994, Hertzum 2006, and the Dakan/Feller/Anthropic handout — none about instruction structure and reasoning.
  - Confidence: high
- **[MAJOR] [broken-reference]** The overall-scoring section contains a dangling internal cross-reference: it says 'When Epistemics is N/A (see Epistemics scoring guidance above for when this applies)' but the framework's Epistemics scoring guidance never defines any N/A condition — the definition exists only in prompts/prompt-evaluator.md and the calibration set.
  - Evidence: framework/ppep-framework.md:175 vs :132-140 (bands 1-3 through 10 only, no N/A); definition actually at prompts/prompt-evaluator.md:159-163 and examples/prompt-calibration-set.md:176-180 ('Epistemics is not applicable for a pure code generation task…').
  - Confidence: high
- **[MAJOR] [novelty-overclaim]** The claim that Epistemics 'was independently surfaced during iterative development and is not found in most prompting guides' is overstated and internally contradicted: PPEP's own entry-level Epistemics technique ('Ask It to Think First') is imported from the same Anthropic handout, and the two most prominent guides — Anthropic's own docs and OpenAI's prompt engineering guide — prominently cover the equivalent concepts (allow 'I don't know', verify with citations, ground in direct quotes; provide reference text/answer with citations, give the model time to think).
  - Evidence: README.md:62 and framework/ppep-framework.md:107 ('most absent from standard prompting guides') vs framework/ppep-framework.md:157 ('Ask It to Think First | Epistemics' sourced from Dakan/Feller/Anthropic per :146); Anthropic 'Reduce hallucinations' docs (https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations, techniques verified via search); OpenAI guide strategies 'Provide reference text — instruct the model to answer with citations' and 'Give the model time to think' (verified via search of the official guide's six strategies).
  - Confidence: high for the two major guides; the literal wording 'most prompting guides' is technically defensible, but the framing ('independently surfaced', 'most absent') does not survive comparison
- **[MAJOR] [self-consistency]** The framework violates its own Epistemics standard: it mandates 'No summarizing as facts' and 'Negative claims require proof' (with shown evidence, e.g. grep output), yet its headline claims — 93% confidence, 'not found in most prompting guides', 'evidence-based techniques', 'opinion-based' competitors — are exactly the kind of unverified assertions and unproven negative claims it instructs Claude never to make; no survey/inventory of prompting guides is shown anywhere.
  - Evidence: framework/ppep-framework.md:111-113 ('Negative claims require proof: if Claude says something does not exist, it must show the search or check that confirmed it'; 'No summarizing as facts') vs README.md:26 ('Most prompt engineering guides are opinion-based' — no inventory shown), README.md:62, README.md:90.
  - Confidence: high — this is the sharpest interview attack vector because it uses the framework's own words
- **[MINOR] [taxonomy-overlap]** The four dimensions are not a clean partition — three overlaps create double-counting risk when scoring: audience appears in both Product ('Target audience identified') and Performance ('Role defined: … for what audience'); check-ins appear in both Process ('Checkpoints defined: when Claude should pause, verify, or check in') and Performance ('Collaboration style: … check in between steps'); and verification appears in both Process checkpoints ('verify') and Epistemics (whose 6-7 band is 'Explicit verification step present').
  - Evidence: framework/ppep-framework.md:40 vs :84; :66 vs :86; :66 vs :138. No tie-breaking rule for which dimension owns an instruction exists anywhere in the doc.
  - Confidence: high
- **[MINOR] [citation-integrity]** The block quotation supporting the 93% section is attributed to 'Nielsen (1993), as discussed in Hertzum (2006)' but the sentence could not be located verbatim in either source (exact-phrase search surfaces a MeasuringU practitioner blog instead), and the in-text 'Nielsen (1993)' has no matching entry in the reference list, which cites only Nielsen (1994).
  - Evidence: framework/ppep-framework.md:196 ('There tends to be disagreement between evaluators when assigning severity, and reliability improves when averaging ratings from independent evaluators') vs :204 ('Nielsen, J. (1994). Heuristic evaluation…'); README.md:92 also says 'Nielsen 1993'. Exact-phrase web search hits https://measuringu.com/severity-ratings/, not Hertzum/Nielsen. Substance is genuine Nielsen doctrine (NN/G verified), but the quotation-marks-plus-attribution format implies a verbatim quote that cannot be confirmed.
  - Confidence: medium — Hertzum 2006 full text and MeasuringU pages are unfetchable through this environment's egress; the quote may exist in the paywalled paper, but presenting an unlocatable sentence as a quotation is itself the defect
- **[MINOR] [unvalidated-claim]** The composite score is claimed to 'predict how useful the AI's response will be' with no predictive validation anywhere in the repo, and the framework then walks the composite back ('apply judgment about which dimensions matter most'), leaving an unweighted average that is effectively decorative — inconsistent with the toolkit's own issue evaluator, which has an explicit 4/4/4/3/3/3/2/2 weighting scheme.
  - Evidence: framework/ppep-framework.md:19 ('Together they produce a composite quality score that predicts how useful the AI's response will be') and :175 ('Use the overall average as a starting point, then apply judgment'); weighted contrast at prompts/issue-evaluator.md (weights summing to 25). No outcome data linking scores to response quality exists in any file.
  - Confidence: high
- **[MINOR] [citation-integrity]** The claim of being 'grounded in established research from usability, communication, and epistemology' is two-thirds empty: the repo contains zero communication-studies references and zero epistemology references — 'epistemolog*' appears exactly once, in that sentence.
  - Evidence: framework/ppep-framework.md:8; grep -rin 'epistemolog' returns only that line; reference lists (framework:204-206, README:169-181) contain no communication or epistemology sources.
  - Confidence: high
- **[NITPICK] [naming]** The acronym PPEP does not match the framework's own dimension order — dimensions are presented as Product, Process, Performance, Epistemics (PPPE), and the acronym is never expanded letter-by-letter anywhere.
  - Evidence: framework/ppep-framework.md:12-17 lists '1. Product… 2. Process… 3. Performance… 4. Epistemics'; no expansion of 'PPEP' exists in the doc or README.
  - Confidence: high
- **[NITPICK] [arbitrary-design]** The justification for Epistemics using five scoring bands instead of four is asserted, not argued: 'Scores 4-5 and 6-7 are distinct in this dimension in a way they are not in Product, Process, or Performance' gives no reason why.
  - Evidence: framework/ppep-framework.md:134.
  - Confidence: high

## Open questions

- License conflict (license agent's lane): the toolkit is MIT (README.md:193) but is a self-described derivative 'built on top of' a CC BY-NC-SA 4.0 work (README.md:9) whose ShareAlike clause may require compatible licensing of adaptations — the framework doc reproduces the handout's technique set and quotes it directly.
- The 6-techniques handout PDF (www-cdn.anthropic.com/62df988c...) is unfetchable through this environment's egress proxy; if any agent has wider egress, fetching it would settle (a) whether it carries any internal research citations (bearing on 'evidence-based') and (b) its exact title/footer (bearing on the mislabeled-reference finding).
- Evaluator agents should check whether the taxonomy overlaps I found (audience in Product+Performance, check-ins in Process+Performance, verification in Process+Epistemics) produce actual double-counting in the nine calibration anchors' dimension scores.
- The '93%' claim propagates into examples/prompt-calibration-set.md:23 — methodology agent should treat it as a single unsourced figure repeated in three files, not three corroborating statements.
- Stale README path prompts/uiux-evaluation-prompts.md (README.md:136) — already logged in the coordinator's checkpoint notes; not duplicated in my findings.
- Interview-prep note for synthesis: the strongest defensible pitch is 'I operationalized Anthropic's Description competency into a scoreable rubric and added an Epistemics dimension for agentic work' — every stronger originality or quantification claim in the current README/framework text is attackable with the evidence above.

---

## Full report

# PPEP Framework Audit (framework/ppep-framework.md + README framing)

**Auditor lane:** The PPEP framework itself. **Date:** 2026-08-12. **Repo state:** commit c143850 (2026-04-24).

**Verification environment note:** This sandbox's egress proxy blocks most direct page fetches (anthropic.com, www-cdn.anthropic.com, nngroup.com, measuringu.com, researchgate.net, dev.to all EGRESS_BLOCKED; attempted with curl via proxy and WebFetch). GitHub raw fetches and WebSearch work. All web claims below were verified through WebSearch result content, in several cases via two independent queries; confidence is marked accordingly.

---

## 1. Internal consistency of the four-dimension taxonomy

### 1.1 The taxonomy is mostly coherent but not a clean partition

Three overlaps create double-counting risk for a scorer:

| Concept | Dimension A | Dimension B |
|---|---|---|
| **Audience** | Product: \"Target audience identified: who the output is for\" (ppep-framework.md:40) | Performance: \"Role defined: who Claude is acting as, at what level of expertise, **for what audience**\" (:84) |
| **Check-ins** | Process: \"Checkpoints defined: when Claude should pause, verify, or **check in**\" (:66) | Performance: \"Collaboration style: ask clarifying questions, **check in between steps**\" (:86) |
| **Verification** | Process: \"Checkpoints defined: when Claude should pause, **verify**, or check in\" (:66) | Epistemics: band 6-7 = \"Explicit verification step present\" (:138) |

No tie-breaking rule exists anywhere: a prompt saying \"verify each step before proceeding\" is scoreable under Process or Epistemics, and the doc gives no guidance on which dimension owns it. Also note the framework's own re-filing choice: \"Ask It to Think First\" (:129-130, :157) is classed as Epistemics, but \"think through tradeoffs **before** recommending\" is an ordering instruction — in the source AI Fluency course, guiding \"how the AI approaches your request\" is the definition of *Process* Description. Defensible, but it blurs the Process/Epistemics boundary the moment you look closely.

### 1.2 Dangling internal cross-reference (verified defect)

ppep-framework.md:175: \"When Epistemics is N/A **(see Epistemics scoring guidance above for when this applies)**\" — but the Epistemics scoring guidance (:132-140) defines bands 1-3 through 10 and **never mentions N/A**. The N/A condition is defined only in `prompts/prompt-evaluator.md:159-163` and `examples/prompt-calibration-set.md:176-180` (\"Epistemics is not applicable for a pure code generation task with no research or verification component\"). The framework doc — the theoretical source — points to a definition it does not contain.

### 1.3 Other internal inconsistencies

- **Acronym/order mismatch:** dimensions are presented \"1. Product … 2. Process … 3. Performance … 4. Epistemics\" (:12-17) = PPPE; the acronym is PPEP and is never expanded letter-by-letter anywhere in the repo.
- **Five-bands note is asserted, not argued** (:134): \"Scores 4-5 and 6-7 are distinct in this dimension in a way they are not in Product, Process, or Performance\" — no reason given.
- **Composite claim vs. composite retraction:** :19 claims the composite \"predicts how useful the AI's response will be\" (a predictive-validity claim with zero validation data anywhere in the repo), then :175 immediately undermines it: \"Use the overall average as a starting point, then apply judgment about which dimensions matter most.\" The composite is decorative. Contrast: the toolkit's own issue evaluator has an explicit weighting scheme (4+4+4+3+3+3+2+2=25, `prompts/issue-evaluator.md`). Obvious interviewer question: *why does the flagship framework get no weights when your issue rubric does?*
- **README vs framework:** the dimension glosses match (README:56-60 vs framework:12-17); the scope notes match (README:54 vs framework:10). The main README/framework contradiction is at the claims level, covered in §3 and §4 below. One dating inconsistency: README:92 cites \"Nielsen 1993\" while the framework's reference list (:204) contains only \"Nielsen, J. (1994). Heuristic evaluation.\" The in-text \"Nielsen (1993)\" (:196) has **no matching reference entry**.

---

## 2. The \"seven evidence-based prompting techniques\"

The seven, as listed (:150-165): (1) Provide Context → Product; (2) Specify Output Constraints → Product; (3) Break Complex Tasks into Steps → Process; (4) Define the AI's Role → Performance; (5) Show Examples of What Good Looks Like → Performance; (6) Ask It to Think First → Epistemics; (7) meta-technique: Ask the AI for help with prompting.

**Source verification.** The sole citation for all seven is \"Dakan, R., Feller, J., & Anthropic. (2025). AI Fluency: Framework and Foundations\" with URL `https://www-cdn.anthropic.com/62df988c101af71291b06843b63d39bbd600bed8.pdf` (:169, :206). The PDF is unfetchable from this sandbox, but **two independent web searches return that exact URL indexed under the title \"6 Techniques for Effective Prompt Engineering 1. Provide context Before…\"** — i.e., the cited URL is a **course handout listing six techniques**, from the AI Fluency \"Deep Dive 2: Effective Prompting Techniques\" lesson (https://www.anthropic.com/ai-fluency/deep-dive-2-effective-prompting-techniques), not the full \"Framework and Foundations\" document. Search-confirmed handout contents: giving context, showing examples, specifying constraints, breaking complex tasks into steps, asking the AI to think first, defining the AI's role — plus a closing tip that asking the AI to help improve your prompt \"is perhaps the most powerful technique of all!\"

Per-technique verdict:

| Technique | In cited source? | Independent evidence base |
|---|---|---|
| Provide Context | Yes (handout #1) | Reasonable, uncited |
| Specify Output Constraints | Yes (\"specifying constraints\") | Reasonable, uncited; \":48 'one of the highest-leverage additions'\" is asserted |
| Break Tasks into Steps | Yes | Real support exists in the literature (task decomposition), but the framework cites none; :69's \"**decades of research** on how structured instructions improve **AI reasoning**\" is anachronistic hand-waving — LLM prompting research is ~2020+ |
| Define the AI's Role | Yes (\"defining the AI's role or tone\") | **Contradicted for factual performance**: Zheng et al., *When \"A Helpful Assistant\" Is Not Really Helpful: Personas in System Prompts Do Not Improve Performances of Large Language Models*, Findings of EMNLP 2024 (arxiv.org/abs/2311.10054; aclanthology.org/2024.findings-emnlp.888) — 4 LLMs, 2,410 factual questions, 162 personas: no improvement over no-persona control. The framework's \":90 'one of the most impactful single-line additions to any prompt'\" is unconditional and wrong for accuracy tasks (defensible only for tone/style/depth, which is what Performance covers — but the claim doesn't say that) |
| Show Examples | Yes | Strong real evidence exists (few-shot prompting), uncited; \":93 'the most commonly underused technique'\" is an unsourced empirical claim about user behavior |
| Ask It to Think First | Yes | Real support exists (CoT literature), uncited |
| Meta: Ask AI for help | Yes (closing tip; quote verified) | Faithful to source |

**Verdicts:** (a) The techniques are **faithfully reproduced** from the handout — good. (b) Calling them \"**evidence-based** … from **Anthropic's prompting research**\" (:146) is mischaracterization: the source is a pedagogical handout, not research, and no empirical citation for any technique appears anywhere in the repo. (c) The **reference is mislabeled**: the URL is the 6-techniques handout, cited under the full course title. (d) \"Seven\" is a repackaging of the handout's \"6 + closing tip\" — fine, but the handout's own title says six, which an interviewer holding the handout will notice.

---

## 3. \"Not found in most prompting guides\" (README:62) and \"independently surfaced\"

README:62: \"[Epistemics] was **independently surfaced** during iterative development and is **not found in most prompting guides**. It is the single biggest differentiator between a 7/10 and a 10/10 prompt.\" Framework :107: \"the one **most absent from standard prompting guides**.\"

**Web check of major guides (verified via search):**
- **Anthropic's own docs** — \"Reduce hallucinations\" (platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations): *allow Claude to say \"I don't know\"*, *verify with citations (find supporting quote, retract claim if none found)*, *ground in direct quotes*. That retract-if-no-quote rule is functionally \"claims require proof.\"
- **OpenAI's prompt engineering guide** — six strategies including *\"Provide reference text… instruct the model to answer with citations from a reference text\"* (motivated explicitly by models \"confidently inventing fake answers\") and *\"Give the model time to think\"* (chain-of-thought) — the latter being the exact content of PPEP's own Epistemics technique.
- **The AI Fluency handout itself** contains \"asking the AI to think first\" — which PPEP maps into Epistemics (:157). So the dimension the README says was \"independently surfaced\" imports one of its techniques **from the same Anthropic handout the other three dimensions come from**.

**Verdict:** The *letter* of \"not found in most prompting guides\" survives — as a **named scoring dimension** bundling inventory-before-judging + proof-for-negative-claims + no-summarizing-as-facts, Epistemics is genuinely unusual, and those audit-grade criteria are the best original content in the framework. The *spirit* does not survive: equivalent concepts are prominent in the two most-read guides on earth (one of them Anthropic's own documentation), and \"independently surfaced\" is contradicted by the framework's own technique table. Also note: \"the single biggest differentiator between a 7/10 and a 10/10 prompt\" is another unsourced empirical claim; the only support is the framework's own 9-anchor set, whose calibration doc explicitly declines to generalize (`examples/prompt-calibration-set.md:231`).

**Self-consistency problem (the sharpest attack available to an interviewer):** the Epistemics dimension itself demands \"Negative claims require proof: if Claude says something does not exist, it must **show the search or check that confirmed it**\" (:111) and \"No summarizing as facts\" (:113). \"Not found in most prompting guides\" is a negative claim with **no shown survey**. \"Most prompt engineering guides are opinion-based\" (README:26) likewise. The framework fails its own test, in its own words.

---

## 4. The 93% / 7% framing (README:88-92, framework:190-198)

**What the sources establish (verified):**
- Nielsen (NN/G, \"Severity Ratings for Usability Problems\"): *\"severity ratings from a single evaluator are too unreliable to be trusted\"*; the mean of ratings from **three** evaluators is satisfactory for many practical purposes (nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/, verified via search).
- Hertzum (2006), *Problem prioritization in usability evaluation*, IJHCI 21(2):125-146 — real paper, documents substantial evaluator disagreement on severity (researchgate.net/publication/220302680). Search-level summaries of the adjacent literature report inter-expert severity correlations around r=.33-.46 and cross-method evaluator agreement of 5-65% (medium confidence; pages unfetchable).

**What the framework does with them:** \"Framework confidence: **93%**. The remaining **7%** reflects the irreducible subjectivity inherent in single-evaluator heuristic assessment\" (:192-194), and README:90: \"built with **explicit confidence tracking**.\"

**Assessment — this is pseudo-quantification, precisely:**
1. **No metric.** \"Confidence in the framework\" is never defined — confidence *of what, measured how*? It is not a confidence interval, not an inter-rater statistic, not predictive accuracy.
2. **No procedure or data.** \"Explicit confidence tracking\" implies a tracked artifact; exhaustive grep shows the 93%/7% figures appear only as bare assertions in three files (README:90-92, framework:192-194, prompt-calibration-set.md:23 — one number repeated, not three corroborations).
3. **The citations don't contain the number.** Neither Nielsen nor Hertzum quantifies subjectivity at 7% or anything like it. The literature is cited for the *existence* of evaluator subjectivity, then a precise magnitude is invented and formatted as a measurement.
4. **The citations point the other way.** If single-evaluator severity ratings are \"too unreliable to be trusted\" (Nielsen) and inter-expert correlations sit near r=.33, the subjective residual of a single-evaluator method is far larger than 7%. The literature undercuts the claim it decorates. And the method choice compounds it: the framework cites literature recommending **averaging 3+ evaluators on a 5-point scale**, then ships a **single-evaluator, 10-point** rubric.
5. **False adjacent claim.** README:35: \"**confidence intervals** … are documented throughout.\" The word \"interval\" appears **exactly once in the entire repository — in that sentence**. There are zero confidence intervals.
6. **Quote integrity.** The supporting block quote (:196, \"There tends to be disagreement between evaluators when assigning severity…\") is attributed \"Nielsen (1993), as discussed in Hertzum (2006)\" but could not be located verbatim in either source; an exact-phrase search surfaces a MeasuringU practitioner article instead (measuringu.com/severity-ratings/). The substance is genuine Nielsen doctrine; the quotation-marks-plus-double-attribution format implies a verbatim quote that cannot be confirmed (medium confidence — Hertzum's full text is paywalled/unfetchable). And \"Nielsen (1993)\" has no matching entry in the reference list (which cites Nielsen 1994).

**Fair credit:** acknowledging single-evaluator subjectivity *at all*, and citing real usability literature for it, is more epistemic honesty than most prompt-engineering repos attempt. The failure is attaching a fabricated precision (\"93%\") to it — which converts a genuine limitation acknowledgment into the report's clearest example of rigor-theater. The honest version costs one sentence: *\"Single-evaluator scoring is subjective (Nielsen; Hertzum 2006); the calibration set reduces but cannot eliminate this.\"*

---

## 5. AI Fluency 4D representation, attribution, licensing note

**Could not fetch the cited PDF** (www-cdn.anthropic.com blocked at every attempted route: direct curl, proxied curl, WebFetch). Verified via multiple searches instead:

- **4D definitions — faithful.** README:11-14 (\"Delegation — deciding when and how to involve AI; Description — communicating your intent to AI effectively; Discernment — evaluating AI outputs with critical judgment; Diligence — taking responsibility for AI-assisted work\") match Anthropic's official definitions (Delegation: \"setting goals and deciding whether, when and how to engage with AI\"; Description: \"effectively describing goals to prompt useful AI behaviors and outputs\"; Discernment: \"accurately assessing the usefulness of AI outputs and behaviours\"; Diligence: \"taking responsibility for what we do with AI\") — confirmed via anthropic.skilljar.com/ai-fluency-framework-foundations and coursera.org/learn/ai-fluency-framework-foundations search results. Attribution to Dakan (Ringling College) and Feller (University College Cork) + Anthropic: correct.
- **Support note — verified accurate.** README:20's \"Supported in part by the Higher Education Authority, Ireland, through the National Forum for the Enhancement of Teaching and Learning\" is confirmed by teachingandlearning.ie/2025/05/28/supporting-ai-fluency-in-higher-education/ and educationawards.ie coverage.
- **License note** — CC BY-NC-SA 4.0 for the AI Fluency materials is consistent with all search results; the MIT-vs-ShareAlike derivative question is another agent's lane (flagged in open questions).
- **The big one — Description's own sub-components.** Anthropic's course page (anthropic.com/ai-fluency/description, verified via two searches) defines Description's three components as: \"**Product Description** (clearly defining what you want the AI to create), **Process Description** (guiding how the AI approaches your request), **Performance Description** (defining how you want the AI to behave during your collaboration).\" Compare ppep-framework.md:14-16: \"**Product** — what you want; **Process** — how the AI should approach it; **Performance** — how the AI should behave.\" **Three of PPEP's four dimensions, including their names and glosses, are the source course's own decomposition of Description.** Nowhere in the repo is this component-level provenance disclosed. The scope note (:10) attributes the *competency*; framework:8 then claims the model \"was developed through iterative testing\"; README:62 claims only Epistemics was \"independently surfaced\" — quietly implying the rest was too, when it was adopted. This is not plagiarism — global attribution to the course is prominent and repeated — but it is **under-attribution combined with originality overclaim**, and it is the single most dangerous gap for an interview with anyone who has taken the (300,000+ enrollment) AI Fluency course.

---

## 6. Framework-design assessment: what a senior practitioner would say

**Genuinely good:**
1. **Epistemics as a named, scoreable dimension** for agentic work. \"Inventory before judging,\" \"negative claims require proof (show the grep),\" \"no summarizing as facts\" are sharp, operational, and rare as *scoring criteria* even in Aug-2026. The weak/strong example pair (:119-127, \"no entrance animations\" vs. the grep-inventory version) is excellent, concrete pedagogy — the best passage in the repo.
2. **Diagnostic decomposition.** \"Understanding which dimension is failing tells you exactly how to fix it\" (:29) is a genuinely more useful mental model than checklist guides; the calibration set demonstrates it (Anchor 3→4: one added verification instruction moves Epistemics 1→7).
3. **Real operationalization work the course doesn't provide:** per-dimension 1-10 bands, task-type criticality table (:177-186), the N/A rule for Epistemics (right idea, wrong file), and nine calibration anchors — anchored-rubric practice consistent with the LLM-Rubric direction (Eisenstein et al. 2024, cited in README:179).
4. **Honest scoping** (:10) and the calibration doc's refusal to generalize from nine examples (prompt-calibration-set.md:231, :234) — better epistemic hygiene than the framework doc's own headline claims.

**What they would tear apart:**
1. The originality framing (§5). The defensible pitch is *\"I operationalized Anthropic's Description competency into a scoreable rubric and added an Epistemics dimension for agentic work\"* — genuinely respectable. The current text claims more, and every increment beyond that pitch is attackable with public sources.
2. The 93% (§4) — pseudo-quantification, contradicted by its own citations.
3. \"Evidence-based\" with zero empirical citations, a mislabeled reference, one claim contradicted by EMNLP 2024 findings, and \"decades of research\" on AI reasoning (§2).
4. Single evaluator + 10-point ordinal scale immediately after citing literature that recommends the opposite (multiple evaluators, coarser scale).
5. Composite score that the doc itself retracts; no weights despite the sibling issue-evaluator having them.
6. Taxonomy overlaps with no ownership rules (§1.1); dangling N/A reference (§1.2).
7. Self-consistency: the framework flunks its own Epistemics rubric — its unproven negative claims (\"not found in most guides,\" \"most guides are opinion-based\") come with no shown inventory, exactly what :111 forbids.

**Hard interviewer questions to prepare for:**
1. \"The AI Fluency course already defines Product, Process, and Performance Description. What exactly did you create?\"
2. \"Where does 93% come from? Show me the measurement. What would make it 91%?\"
3. \"You quote Nielsen that single-evaluator ratings are 'too unreliable to be trusted' — then built a single-evaluator 10-point rubric. Reconcile that.\"
4. \"'Evidence-based' — cite one empirical study for any of the seven techniques. Are you aware personas don't improve factual accuracy (EMNLP 2024)?\"
5. \"Your framework says negative claims require shown proof. Which guides did you survey before writing 'not found in most prompting guides'?\"
6. \"When is Epistemics N/A? Your framework doc references a definition it doesn't contain.\"
7. \"A prompt says 'verify each step' — Process checkpoint or Epistemics? Show me the tie-break rule.\"
8. \"Why does your issue evaluator have section weights but your flagship framework averages equally and then tells me to ignore the average?\"
9. \"What does PPEP stand for, in order? Your doc lists Product, Process, Performance, Epistemics — that's PPPE.\"
10. \"How would you validate that the composite score 'predicts how useful the AI's response will be'?\"

---

## Key sources (all accessed 2026-08-12 via WebSearch; direct fetches blocked by sandbox egress)
- https://www.anthropic.com/ai-fluency/description — Description's three components (Product/Process/Performance Description)
- https://www-cdn.anthropic.com/62df988c101af71291b06843b63d39bbd600bed8.pdf — cited URL; indexed title \"6 Techniques for Effective Prompt Engineering\"
- https://www.anthropic.com/ai-fluency/deep-dive-2-effective-prompting-techniques ; https://anthropic.skilljar.com/ai-fluency-framework-foundations ; https://www.coursera.org/learn/ai-fluency-framework-foundations
- https://www.teachingandlearning.ie/2025/05/28/supporting-ai-fluency-in-higher-education/ ; https://www.educationawards.ie/news/anthropic-and-university-partners-develop-ai-fluency-courses-for-irish-higher-education
- https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/ — single-evaluator unreliability, average of three
- https://www.researchgate.net/publication/220302680_Problem_Prioritization_in_Usability_Evaluation_From_Severity_Assessments_Toward_Impact_on_Design — Hertzum 2006
- https://measuringu.com/severity-ratings/ — exact-phrase hit for the framework's \"quote\"
- https://arxiv.org/abs/2311.10054 ; https://aclanthology.org/2024.findings-emnlp.888/ — personas don't improve factual performance
- https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations — Anthropic's epistemics-equivalent guidance
- OpenAI prompt engineering guide six strategies (verified via search: \"provide reference text / answer with citations\", \"give the model time to think\")