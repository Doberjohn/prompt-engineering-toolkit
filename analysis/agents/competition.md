# Agent report: competition

## Executive summary

Against the August-2026 landscape, this toolkit is a well-constructed but zero-adoption artifact (1 GitHub star, 0 forks, unmaintained for ~110 days) competing in five categories that are each dominated by massively adopted, better-resourced alternatives: prompt guides (dair-ai 77.4k stars, official Anthropic/OpenAI/Google docs), eval tooling (promptfoo 24.2k stars, Braintrust's $80M Series B, Anthropic Console evals built by the acquired Humanloop team), AI issue tooling (GitHub's own 3-element official guidance, spec-kit 126.4k stars), UX auditing (axe-core/Lighthouse plus productized AI auditors like Baymard UX-Ray), and Claude Code skills (anthropics/skills 168.5k stars; 15,360 SKILL.md files on GitHub already contain "gh issue create"). Its genuine differentiators are real but narrow: anchored calibration sets that mirror 2026 LLM-as-judge best practice, an "Epistemics" scoring dimension that no named prompt framework (CO-STAR/RISEN/CRISPE/TCREI) has, honest Verified/Inferred labeling, and a scored quality-gate loop from issue drafting to implementation that does not exist as a packaged unit elsewhere. The fatal weaknesses for an interview are the absence of any human-agreement validation (industry practice is 100-300 labeled samples with Cohen's kappa; the toolkit self-scores 9-10 anchors with the same model it evaluates), the unfalsifiable "93% confidence" number, the stale "Claude Code only" skills claim (SKILL.md became an open standard in Dec 2025), and the fact that the repo never once engages with or even names a single competitor. The strongest honest positioning is "a calibration-first evaluation-methodology demonstration, portable into real eval tooling," and the comparison an interviewer will most likely throw is promptfoo/Anthropic Console evals ("why a paste-in prompt?") followed by spec-kit ("why an 8-section runbook rubric?").

## Strengths (with evidence)

- **The anchored calibration-set approach (one scored exemplar per band, controlled degradations) is exactly what 2026 LLM-as-judge best-practice guidance recommends, and is rare in paste-in prompts — the toolkit implemented it before/independently of most practitioner content.**
  - Evidence: prompts/prompt-evaluator.md:89-183 (9 scored anchors with failure-mode labels) and prompts/issue-evaluator.md:175-192 (10 formula-scored degradation anchors) vs futureagi.com/blog/llm-as-judge-best-practices-2026 and deepeval.com/blog/llm-as-a-judge guidance found via search: "Anchor each score level with a concrete criterion and add examples—one per score level"
- **The Epistemics dimension as a *scored dimension* is genuinely absent from every named prompt-structure framework in circulation (CO-STAR, CRISPE, RISEN, RACE, RTF, APE, TAG, CRAFT, TCREI) — the packaging is original even though the content is not.**
  - Evidence: framework/ppep-framework.md:105-141 vs framework surveys (promptary.dev/frameworks/, promptquorum.com/blog/prompt-frameworks, Google TCREI = Task/Context/References/Evaluate/Iterate per nicolaziady.com/tcrei-framework/) — none includes a verification/proof dimension; WebSearch for "PPEP Product Process Performance Epistemics" returns no colliding or prior framework
- **The closed loop — same 8-section rubric drives an evaluator prompt, a drafting skill, and an implement-time quality gate with a 7.0 threshold and auto-rewrite — does not exist as a packaged unit in the official or community skills ecosystem, despite issue-creation skills being commodity.**
  - Evidence: skills/draft-issue/SKILL.md:1-62 + skills/implement-issue/SKILL.md + prompts/issue-evaluator.md:95-113 (shared weighted formula); GitHub code search "gh issue create" repo:anthropics/skills → 0 results; broad search → 15,360 SKILL.md hits but none surfaced with a scored gate + rewrite loop
- **The toolkit's key external citations in my lane are real and correctly characterized: GitHub's official Copilot coding-agent issue guidance exists, and the arXiv paper on Copilot-ready issues exists.**
  - Evidence: README.md:177-178 citations verified via search: docs.github.com/copilot/how-tos/agents/copilot-coding-agent/best-practices-for-using-copilot-to-work-on-tasks (problem statement + acceptance criteria + file pointers) and arxiv.org/abs/2512.21426 "What Makes a GitHub Issue Ready for Copilot?" (32 criteria, merged-vs-closed PR comparison)
- **The UI/UX prompts' epistemic labeling discipline (Accessible/Inaccessible inventory, findings flagged Inferred/Suspected when not verifiable) is more honest than typical LLM audit prompts and aligns with how practitioners criticize LLM UX audits.**
  - Evidence: prompts/uiux-evaluator/url-mode.md:22-34 (pre-flight inventory) and :67,72,77,82 ("Flag all accessibility findings as Inferred", "Flag mobile findings as Suspected", "All performance findings are Inferred")
- **The AI Fluency 4D framing is real, current, and correctly attributed, giving the toolkit a legitimate intellectual lineage to an Anthropic-backed framework.**
  - Evidence: README.md:7-20 vs anthropic.skilljar.com/ai-fluency-framework-foundations and coursera.org/learn/ai-fluency-framework-foundations (Dakan/Feller/Anthropic 4Ds confirmed via search, Aug 2026)

## Findings

- **[MAJOR] [adoption]** The toolkit has effectively zero adoption in every category it competes in: 1 star, 0 forks, created 2026-04-15, last pushed 2026-04-24 (9 days of activity, then ~110 days idle), while its nearest named competitors have 4-6 orders of magnitude more traction.
  - Evidence: GitHub API via MCP on 2026-08-12: Doberjohn/prompt-engineering-toolkit stars=1, forks=0, created 2026-04-15, pushed 2026-04-24. Comparators same day: dair-ai/Prompt-Engineering-Guide 77,437 stars; anthropics/prompt-eng-interactive-tutorial 37,637; anthropics/skills 168,477; github/spec-kit 126,393; promptfoo 24,171. Arithmetic: Apr 24 → Aug 12 = 110 days with no push.
  - Confidence: high — live API numbers; only caveat is stars are an imperfect adoption proxy.
- **[MAJOR] [validation-gap]** The toolkit's calibration has no human-agreement validation, which is the table-stakes standard for LLM-as-judge rubrics in 2026: anchors were authored and scored by the same person/model being calibrated (circular), with 9-10 samples vs the practitioner norm of 100-300 human-labeled samples and Cohen's kappa > 0.6.
  - Evidence: prompts/prompt-evaluator.md:89-183 (9 anchors, no human raters mentioned); framework/ppep-framework.md:192-198 (admits single-evaluator variance but offers no measurement). Industry norm per futureagi.com/blog/llm-as-judge-best-practices-2026 (via search): "Hand-label 100-300 samples, measure Cohen's kappa, and iterate the prompt until kappa > 0.6."
  - Confidence: high — the repo contains no agreement data anywhere; the norm is corroborated by multiple 2026 sources (futureagi, confident-ai, deepeval).
- **[MAJOR] [positioning]** The repo never names or engages a single competitor in any category — no promptfoo, no CO-STAR/RISEN/CRISPE, no LangSmith/Braintrust, no spec-kit, no axe-core — and its only competitive framing is the unsupported straw man "Most prompt engineering guides are opinion-based," which is false for the official Anthropic/OpenAI/Google guidance that dominates the category.
  - Evidence: Grep for promptfoo|LangSmith|Braintrust|CO-STAR|CRISPE|RISEN|spec-kit|competitor|alternative across the repo: zero hits outside the audit's own analysis/ folder. README.md:26: "Most prompt engineering guides are opinion-based." Counter-evidence: platform.claude.com prompting docs (fetched 2026-08-12) include model-specific empirical guidance for Fable 5/Opus 5/Sonnet 5; Google's Boonstra whitepaper (400k+ downloads per leeboonstra.dev via search) is technique-surveyed, not opinion.
  - Confidence: high for the absence (grep shown); high for the counter-evidence (fetched/searched).
- **[MAJOR] [competitive-obsolescence]** As a prompt-evaluation tool, the paste-in evaluator lacks every table-stakes feature of the 2026 eval stack — versioned prompts, datasets, CI/regression runs, model comparison, cost/latency tracking, structured outputs, position-bias controls — and the exact function it performs (rubric-graded prompt scoring) is a built-in one-liner in promptfoo (llm-rubric assertion) and a hosted product in Anthropic's own Console (Evaluations built by the acquired Humanloop team) and OpenAI's Evals API graders.
  - Evidence: prompts/prompt-evaluator.md is chat-paste only (:4-5 "Copy everything... paste into a new conversation"). promptfoo.dev/docs/configuration/expected-outputs/model-graded/llm-rubric/ (via search): "llm-rubric sends the output to another LLM and asks it to grade the response against your rubric," returns {pass, score, reason}. TechCrunch 2025-08-13 (via search): Anthropic hired the Humanloop founders/team; platform sunset 2025-09-08; "Humanloop's DNA lives on as the Workbench and Evaluations tabs within Anthropic's enterprise suite." Braintrust raised $80M Series B at ~$800M valuation Feb 2026 (atlan.com/respan.ai via search).
  - Confidence: high — multiple independent sources; the Humanloop-to-Anthropic timeline is corroborated by TechCrunch, W&B, and PromptLayer migration posts.
- **[MAJOR] [overclaim]** README's flagship differentiation claim — the Epistemics dimension "is not found in most prompting guides" — overreaches: the *content* (verification, grounding, source-checking, hallucination minimization) is standard in Anthropic's own current official prompting docs and an emerging academic topic ("epistemic prompting," arXiv July 2026); only the packaging as a scored rubric dimension is novel.
  - Evidence: README.md:62 ("not found in most prompting guides"). Fetched platform.claude.com prompting docs (2026-08-12) contain a "Minimizing hallucinations in agentic coding" section, "Ground responses in quotes," "Encourage source verification: Ask Claude to verify information across multiple sources," and "Provide verification tools." arxiv.org/abs/2607.11680 "From Prompt Engineering to Epistemic Prompting" (July 2026, via search).
  - Confidence: high — direct quotes from fetched official docs; the claim is defensible only against mnemonic frameworks, which the README does not specify.
- **[MAJOR] [competitive-obsolescence]** The issue-quality lane is already served by better-backed alternatives the toolkit ignores: GitHub's official Copilot guidance defines an AI-ready issue in 3 elements (problem statement, acceptance criteria, file pointers), the arXiv paper the toolkit itself cites offers 32 criteria, GitHub has shipped native AI triage for low-quality issues, and spec-kit (126,393 stars) owns the upstream 'plan before agent execution' workflow — while the toolkit's mandatory Rollback section (weight 4, severity-4 if vague) imports runbook standards that GitHub's own issue guidance does not require, penalizing ordinary feature issues.
  - Evidence: prompts/issue-evaluator.md:29-38 (Rollback weight 4: "Critical — without this a production process is dangerous") and :168 (vague rollback = automatic severity 4). GitHub official doc via search (docs.github.com .../best-practices-for-using-copilot-to-work-on-tasks): ideal issue = clear problem description + acceptance criteria + file pointers — no rollback element. github/spec-kit: 126,393 stars (API, 2026-08-12). GitHub AI triage: "GitHub shipped AI triage tools to filter low-quality submissions" (danilchenko.dev 2026-04-11 via search).
  - Confidence: high for the sources; medium for the 'penalizing ordinary issues' inference — the evaluator scopes itself to 'implementation plan issues' (:18), but the skills apply the same rubric to all drafted issues.
- **[MAJOR] [competitive-obsolescence]** The UI/UX evaluator competes against free deterministic tooling and productized AI auditors without any measurement capability: axe-core/Lighthouse/WAVE verify a11y and performance in CI for free, Baymard's UX-Ray runs 346 research-derived heuristics with a vendor-claimed 95%+ accuracy on URLs and screenshots, and generation-plus-review tools (UX Pilot, ~1M users) bundle audit into design workflows — while this prompt admits it cannot measure contrast, Core Web Vitals, or keyboard navigation and has no validated heuristic base beyond Nielsen's 10 + WCAG citations.
  - Evidence: prompts/uiux-evaluator/url-mode.md:67 ("cannot verify semantic HTML, keyboard navigation, or screen reader compatibility"), :77 ("URL mode cannot measure Core Web Vitals precisely. All performance findings are Inferred"). Comparators via API/search 2026-08-12: dequelabs/axe-core 7,394 stars; GoogleChrome/lighthouse 30,650 stars; baymard.com/blog/ai-heuristic-evaluations (search snippet): "automated heuristic evaluation using 346 UX heuristics with a 95% Accuracy Rate or higher, based on either live URLs or screenshots"; UX Pilot "over 1M users" (aufaitux.com review via search).
  - Confidence: high for tool existence and the prompt's own admissions; medium for UX-Ray accuracy (vendor claim, site egress-blocked so verified only via search snippet) and UX Pilot user count (single third-party review).
- **[MAJOR] [staleness]** The README's compatibility claims are stale against the Aug-2026 ecosystem: it asserts skills are "Claude Code only" and "cannot run in any chat interface," but SKILL.md became an open standard (Dec 2025) supported by OpenAI Codex, Cursor, Gemini CLI, Windsurf and others — all of which have the git/gh tool access the README says only Claude Code provides.
  - Evidence: README.md:80 ("Both skills are Claude Code only") and :115 ("Skills are Claude Code only."). designrevision.com/blog/awesome-claude-code-skills via search: "Anthropic introduced the format in October 2025 and released it as an open standard in December 2025; it's now supported by Claude Code, Claude.ai, the Claude API, OpenAI Codex, Cursor, Gemini CLI, Antigravity, and Windsurf." Note the open-standard date (Dec 2025) precedes the repo's creation (2026-04-15), so the claim was arguably already wrong when written.
  - Confidence: medium-high — open-standard support corroborated by multiple secondary sources (designrevision, awesomeclaude.ai, claudeskills.info) but not verified against a primary Anthropic announcement in this session.
- **[MAJOR] [validation-gap]** The "93% confidence / 7% irreducible subjectivity" framing has no counterpart in evaluation practice and will not survive interviewer scrutiny: practitioners quantify evaluator reliability with inter-rater agreement statistics (kappa/alpha) against human labels, not a self-declared percentage, and the 7% figure is not derived from any computation shown in the repo.
  - Evidence: README.md:90-92 ("Current confidence level in the framework: 93%. The remaining 7% is the irreducible subjectivity..."); framework/ppep-framework.md:192-198 cites Nielsen/Hertzum qualitatively but shows no arithmetic producing 7%. Practice norm via search (futureagi.com, confident-ai.com): "Calibration is the process of measuring whether the judge agrees with humans on a labeled gold-set... typically using Cohen's kappa... or Krippendorff's alpha."
  - Confidence: high — the number is asserted, not computed, anywhere in the repo.
- **[MINOR] [discoverability]** The repo name is maximally generic and unfindable: 58 GitHub repos are named "prompt-engineering-toolkit," including teknium1's with 452 stars, and the PPEP brand appears in zero third-party sources.
  - Evidence: GitHub repo search 'prompt-engineering-toolkit in:name' → total_count 58; top hit teknium1/Prompt-Engineering-Toolkit 452 stars (API, 2026-08-12). WebSearch for "PPEP Product Process Performance Epistemics" returns no reference to this framework by any third party.
  - Confidence: high.
- **[MINOR] [staleness]** Four months of no maintenance spans a period in which the ground truth moved: the model landscape rolled over (GPT-5.2/5.4/5.5-era models; Claude Fable 5/Opus 5/Sonnet 5 with model-specific prompting docs), OpenAI's Evals platform was scheduled for deprecation (read-only Oct 31, 2026), and the Claude skills ecosystem exploded — none reflected in the toolkit, whose calibration was "developed and validated using Claude" models of early 2026 or earlier.
  - Evidence: Last push 2026-04-24 (API). GPT-5.2/5.4/5.5 Wikipedia pages surfaced in search results (en.wikipedia.org/wiki/GPT-5.2 etc.); fetched platform.claude.com docs list per-model guidance for Claude Fable 5/Opus 5/Sonnet 5; qaskills.sh/blog/openai-evals-api-reference-2026 via search: Evals platform "read-only on October 31, 2026, and shut down on November 30, 2026." prompt-evaluator.md:7-8: "calibration anchors were scored against Claude's behavior specifically."
  - Confidence: high for repo staleness and Claude docs (fetched); medium for the OpenAI deprecation dates (single secondary source).
- **[MINOR] [adoption]** Even the toolkit's parent framework is a niche adoption story, weakening the "built on the AI Fluency Framework" appeal-to-authority: the Coursera course has ~5,114 enrollments (4.7 rating), versus 77k+ stars for dair-ai's guide and 37k+ for Anthropic's interactive tutorial — the 4D framework is real but not the industry's shared vocabulary.
  - Evidence: Search result for coursera.org/learn/ai-fluency-framework-foundations: "5,114 students already enrolled... 4.7 out of 5 based on 100 reviews." Comparators: dair-ai 77,437 stars; anthropics/prompt-eng-interactive-tutorial 37,637 stars (API, 2026-08-12).
  - Confidence: medium — Coursera number from search snippet, not a direct fetch (coursera.org egress-blocked); Skilljar/enterprise distribution numbers are not public, so total course reach may be higher.
- **[MINOR] [competitive-obsolescence]** Issue-creation Claude Code skills are commodity — 15,360 SKILL.md files on GitHub contain "gh issue create", and marketplace listings (mcpmarket, claudeskills.info, claudemarketplaces) carry multiple GitHub-issue creator/fixer skills — so the skills' defensible novelty reduces to the scored quality gate alone, which nothing in the distribution story surfaces (not a plugin, in no marketplace, and installed via manual file copy).
  - Evidence: GitHub code search '"gh issue create" filename:SKILL.md' → total_count 15,360 (2026-08-12). Marketplace listings via search: mcpmarket.com/tools/skills/github-issues, claudeskills.info/skills/openclaw/openclaw/gh-issues, claudepluginhub.com/skills/feiskyer-claude-code-settings/github-fix-issue. README.md:148,156: install by copying SKILL.md to .claude/commands/.
  - Confidence: high for the counts; the 15,360 figure includes duplicates/forks, so treat as order-of-magnitude.
- **[NITPICK] [positioning]** The scale of the skills ecosystem the toolkit entered is understated by its framing: community skill frameworks created after Sept 2025 reached six-figure star counts within months (superpowers 271k, ECC 240k, mattpocock/skills 215k, ComposioHQ list 72k), and superpowers already ships brainstorming/writing-plans skills covering the pre-implementation planning territory draft-issue occupies — though star-count authenticity in 2026 AI repos is questionable.
  - Evidence: API 2026-08-12: obra/superpowers 271,156 stars (created 2025-10-09); affaan-m/ECC 239,686 (created 2026-01-18); mattpocock/skills 214,829; ComposioHQ/awesome-claude-skills 72,353. Code search repo:obra/superpowers filename:SKILL.md 'issue' → includes skills/writing-plans/SKILL.md and skills/brainstorming/SKILL.md.
  - Confidence: medium — numbers are live API but their organic authenticity is unverifiable (e.g., ultraworkers/claw-code shows 195k stars with 109k forks, an anomalous pattern suggesting inflated metrics circulate in this niche).

## Open questions

- License compatibility (hygiene agent's lane): the toolkit is MIT (README.md:192) but presents itself as 'built on top of' the AI Fluency Framework released CC BY-NC-SA 4.0 (README.md:9) — if PPEP is a derivative work, ShareAlike would forbid MIT relicensing; if it is merely 'inspired by', the 'covers the Description competency' framing overstates the relationship. Worth a crisp answer before the interview.
- Skills agent's lane: README.md:148,156 instructs installing SKILL.md files into .claude/commands/<name>/SKILL.md — as of Aug 2026 the documented location for skills is .claude/skills/ (commands are separate .md slash-command files); whether these instructions actually work in current Claude Code should be tested.
- Prompt-evaluator agent's lane: whether the 9 anchors' scores reproduce on today's Claude models (Fable 5/Sonnet 5 era) — my landscape finding that calibration was scored against early-2026 Claude behavior (prompt-evaluator.md:7-8) makes drift plausible but I did not test it.
- Framework agent's lane: whether the 'seven integrated techniques' faithfully match the AI Fluency course's technique list — I verified the course exists and its 4D structure, not the technique mapping.
- The README's live-demo URL (README.md:43) is a Vercel link with an apparent typo ('companio') — out of scope per owner instruction, but someone should confirm the link works before the interview.
- I could not verify Baymard UX-Ray's accuracy claim beyond its own marketing (baymard.com egress-blocked; search snippet only) and could not fetch docs.github.com or arxiv.org directly (egress-blocked; both verified via multiple search results instead).

---

## Full report

# Competitive Landscape Audit — Doberjohn/prompt-engineering-toolkit (as of 2026-08-12)

**Auditor lane:** Category-by-category competitive landscape, August 2026. All GitHub star counts were pulled live from the GitHub API (via MCP search) on 2026-08-12. All post-Jan-2026 claims were verified by web search/fetch this session. Where a source could not be fetched directly (arxiv.org, docs.github.com, baymard.com, coursera.org are egress-blocked in this environment), I verified via multiple independent search results and say so.

**Baseline adoption of the audited repo** (GitHub API, 2026-08-12): `Doberjohn/prompt-engineering-toolkit` — **1 star, 0 forks**, created 2026-04-15, last pushed 2026-04-24. Arithmetic: Apr 24 → Aug 12 = **110 days with zero commits**, in the fastest-moving tooling niche of 2026. The repo also never names a single competitor anywhere (grep for `promptfoo|LangSmith|Braintrust|CO-STAR|CRISPE|RISEN|spec-kit|competitor|alternative` returns zero hits outside the audit's own `analysis/` folder).

---

## Category 1 — Prompt-engineering guides & frameworks

### The incumbents (verified 2026-08-12)

| Competitor | Signal | Backing |
|---|---|---|
| Anthropic platform prompting docs | Official; fetched live — now organized as **model-specific guidance** (Claude Fable 5, Opus 5, Sonnet 5, Opus 4.8...), plus agentic-systems techniques and a "Minimizing hallucinations in agentic coding" section | Anthropic |
| Anthropic interactive tutorial / courses | 37,637 / 22,604 stars | Anthropic |
| Anthropic Console prompt improver + generator | Built-in, free to all Console users (chain-of-thought injection, XML structuring, example enhancement) | Anthropic |
| AI Fluency course (the toolkit's parent) | Coursera: **~5,114 enrolled**, 4.7★ (search snippet; Skilljar/enterprise reach not public) | Anthropic + Dakan/Feller |
| dair-ai/Prompt-Engineering-Guide (promptingguide.ai) | **77,437 stars**, 8,506 forks, 3M+ learners claimed, 13 languages | DAIR.AI |
| Google: Boonstra 68-page whitepaper; Prompting Essentials (TCREI) | 400k+ downloads claimed (leeboonstra.dev); TCREI = Task/Context/References/Evaluate/Iterate, still actively discussed Jul 2026 | Google |
| OpenAI: GPT-5.x prompting guides + Prompt Optimizer | Cookbook guides per model incl. Codex models; Playground optimizer | OpenAI |
| Learn Prompting | 4,726 stars; large Discord | Learn Prompting Inc. |
| Named structure frameworks: CO-STAR (Sheila Teo/GovTech Singapore), CRISPE, RISEN, RACE, RTF, APE, TAG, CRAFT, CREATE, STOKE... | 20+ catalogued in 2026 roundups (promptary.dev lists 20; aipromptsx lists 23+) | none — folk frameworks |

### Table stakes PPEP lacks
- **Model-specific guidance.** The Anthropic docs' center of gravity in Aug 2026 is *per-model* behavioral guidance (verbosity, over-verification, subagent control for Opus 5, etc.). PPEP is model-agnostic in a period when official guidance stopped being so.
- **Technique coverage.** No CoT/few-shot/structured-output/XML/ReAct/thinking-budget material — the entire technical core of the dair-ai and Google guides.
- **Maintenance and community.** All major guides updated in 2026; toolkit frozen since April.

### Genuine differentiators
- **It is a scored rubric, not a mnemonic.** CO-STAR/RISEN/CRISPE/TCREI are unscored checklists. PPEP has per-dimension 1-10 bands, failure-mode-labeled anchors, and an N/A rule. Nothing in the named-framework field has that.
- **Epistemics as a dimension.** No named framework has a verification/proof dimension (verified by inspecting framework roundups). **But** — the README:62 claim that this is "not found in most prompting guides" overreaches: Anthropic's own current docs instruct "Ground responses in quotes," "Encourage source verification," "Investigate before answering... give grounded and hallucination-free answers" (direct quotes from fetched docs), and academia now has "epistemic prompting" (arXiv 2607.11680, Jul 2026). Novel *packaging*, mainstream *content*.
- **Lineage to AI Fluency** is real and correctly cited — but the parent's Coursera adoption (~5k) means "built on the 4D framework" is a credibility argument, not a distribution argument.

### Verdict
Who chooses PPEP over the alternatives: an individual or team that wants to *grade* prompts in review (learning/teaching context), rather than *write* better prompts for a specific model. That is a real but tiny niche. Anyone optimizing production prompts uses the official model-specific docs plus an optimizer; anyone learning breadth uses dair-ai or a course. PPEP has zero third-party mentions (searching the acronym finds nothing), so today it competes on substance alone, and its substance is one genuinely good idea (anchored scoring + epistemics dimension) inside an otherwise thin framework.

---

## Category 2 — Prompt evaluation / testing tooling

### The incumbents (verified 2026-08-12)

| Competitor | Signal | Notes |
|---|---|---|
| **promptfoo** | **24,171 stars**; repo description: "Used by OpenAI and Anthropic"; pushed same day | `llm-rubric`, `g-eval`, model-graded assertions; CI/CD; red-teaming |
| **Anthropic Console Evaluations/Workbench** | Humanloop founders + ~a dozen staff hired by Anthropic Aug 2025 (TechCrunch 2025-08-13); Humanloop platform sunset 2025-09-08 | The "paste-in evaluator vs the platform" question now has Anthropic itself on the platform side |
| **Braintrust** | **$80M Series B, ~$800M valuation, Feb 2026**; customers incl. Notion, Stripe, Vercel | eval-first platform |
| **LangSmith** | Sequoia/Benchmark/IVP-backed; customers incl. Vercel, Notion | LangChain ecosystem |
| **Langfuse** | **32,972 stars** (OSS, YC W23) | self-host evals + observability |
| **OpenAI Evals** | 19,153 stars; platform Evals UI **scheduled read-only 2026-10-31, shutdown 2026-11-30** (qaskills.sh — single source, medium confidence); ten built-in grader types incl. model-graded | |
| DeepEval | 17,553 stars | G-Eval etc. |
| PromptLayer, Vellum, Helicone, Adaline, Maxim, Arize | active 2026 roundup fixtures (marktechpost 2026-08-09) | LLM-observability market est. ~$2.69B in 2026 (secondary source) |
| Humanloop | **dead** — acquired/sunset | migration guides published by every competitor |

### Table stakes the paste-in evaluator lacks
Versioning, datasets, batch runs, CI/regression gates, cross-model comparison, cost/latency tracking, structured output, tracing, human-review queues, position-bias controls, variance measurement across runs. Every one of these is standard in the table above. The toolkit's own README concedes scoring "may vary" off-Claude (README.md:111) — with no way to measure the variance.

### Genuine differentiators
- **Zero infrastructure.** No account, no API key, no YAML. Paste and go. For a PM or writer with only a chat window, none of the platforms above serve them as directly.
- **Transparency.** The entire rubric is human-readable; a promptfoo `llm-rubric` string is typically a one-liner. The 9 anchors *are* what 2026 best practice prescribes ("one example per score level" — futureagi/deepeval guidance) and most practitioners' judge prompts are far lazier.
- **It teaches while it grades** — the strict-professor interaction loop (prompt-evaluator.md:80-85) has no analogue in eval tooling.

### Verdict
As *tooling*, this is not in the same sport as promptfoo/Braintrust — no one running evals at work would choose it, and the interviewer will know that. As a *judge prompt* (an asset that could be loaded INTO those tools), it is above-average quality. The honest move is to position it as the latter and note the port is trivial (PPEP as a promptfoo rubric config). Right now the repo does not even mention that world exists.

---

## Category 3 — LLM-as-judge / rubric evaluation practice (Aug 2026)

What practitioners actually do (multiple 2026 sources: futureagi, confident-ai, deepeval, Braintrust articles):
- **Calibrate against humans:** hand-label 100-300 samples, compute Cohen's kappa (target > 0.6), iterate the judge prompt.
- **Anchored rubrics:** concrete criterion + example per score level. ✅ *The toolkit does this.*
- **CoT judging** (+10-20% agreement), **pairwise with position-swap** to control 5-15% position bias, **distilled judges** for volume + frontier judges for calibration anchors.
- Newer 2026 work: recursive rubric decomposition (Prometheus lineage).

### Where the toolkit stands
- **Aligned:** anchoring, per-dimension decomposition, evidence-referencing notes, controlled degradation for the issue set (a legitimately clever way to get monotonic anchors and avoid central-tendency bias).
- **Missing the non-negotiable:** *no human gold-set, no agreement statistic, no repeated-run variance data.* The anchors were written and scored by the toolkit's own author with the model being calibrated — circular by construction. n=9 and n=10 vs the 100-300 norm.
- **The "93% confidence" number** (README.md:90) is not a statistic — no computation in the repo produces it, and no practitioner metric corresponds to it. Nielsen/Hertzum are cited for the *existence* of evaluator disagreement, not for a 7% figure. An interviewer who knows evals will go straight here.

### Verdict
Methodologically literate at the design level, unvalidated at the measurement level. One weekend of work (5 humans × 20 prompts, kappa) would convert the weakest claim in the repo into its strongest evidence — that gap is the single most actionable pre-interview fix.

---

## Category 4 — GitHub issue quality / AI-readiness tooling

### The incumbents
- **GitHub official guidance** (docs.github.com .../best-practices-for-using-copilot-to-work-on-tasks — verified via search): an AI-ready issue = **problem statement + acceptance criteria + pointers to files**. Three elements. The toolkit cites this doc (README.md:178) and then requires eight sections.
- **arXiv 2512.21426** "What Makes a GitHub Issue Ready for Copilot?" (verified) — **32 criteria**, derived from comparing issues leading to merged vs closed Copilot PRs. Also cited by the toolkit (README.md:177).
- **github/spec-kit** — **126,393 stars** in ~12 months. The dominant "structure work before handing to an agent" tool (constitution/specify/plan/tasks). The draft-issue skill's territory.
- **GitHub native AI triage** for low-quality issues/PRs shipped amid the 2026 agent-volume crunch (secondary sources: danilchenko.dev, hackread on Black Hat USA 2026 — the latter also showing malicious GitHub issues as an attack vector on coding agents, which makes issue *vetting* topical).
- Repo-level AI-readiness scorers exist (kodustech/agent-readiness, f/check-ai 0-10 score) — adjacent but repo-level, not issue-level.

### Table stakes / gaps
- **No automation.** Competitors ship as Actions/bots/CLIs; this is a paste-in prompt + two locally-installed skills. Nothing runs on `issues.opened`.
- **Rubric misalignment with the AI-ready definition it cites.** Rollback carries weight 4 and a vague rollback is an automatic severity-4 "catastrophic" finding (issue-evaluator.md:29-38,168) — but rollback appears nowhere in GitHub's own guidance, and most feature issues have a trivial rollback (revert the PR). The evaluator scopes itself to "implementation plan issues" (:18), which is honest, but the skills then apply the same rubric to every issue they draft — importing SRE runbook standards into ordinary dev workflow.
- The cited arXiv paper's 32 empirical criteria were *not* incorporated — the 8 sections predate/parallel it, and no mapping is shown.

### Genuine differentiators
- A **weighted, formula-scored issue rubric with a calibration set of controlled degradations** genuinely does not exist elsewhere as a packaged artifact — I searched (2,384 SKILL.md files mention acceptance-criteria+rollback+score, none surfaced with an anchored scoring formula; no issue-level AI grader product found).
- **Merged-vs-closed evidence exists for the thesis** (the arXiv paper found detailed, well-scoped issues correlate with merged agent PRs) — so "issue quality gates before agent execution" is a defensible, current thesis.

### Verdict
Right thesis, wrong weight table, no distribution. Someone wanting this today would use GitHub's 3 bullets + an issue form template, or spec-kit for anything big. The toolkit's rubric is the most rigorous *scoring* treatment of the niche I found — and nobody knows it exists.

---

## Category 5 — AI-assisted UI/UX auditing

### The incumbents
- **Deterministic, free, CI-integrated:** axe-core (7,394 stars, Deque), Lighthouse (30,650 stars, Google), WAVE (WebAIM). These *measure* — contrast ratios, ARIA, CWV.
- **Productized AI heuristic review:** **Baymard UX-Ray** — 346 research-derived UX heuristics, vendor-claimed **95%+ accuracy**, URL or screenshot input (baymard.com blog via search snippet; site egress-blocked, so vendor claim unverified independently). Baymard is *the* research brand in this space — a direct, better-armed analogue of the toolkit's approach.
- **Design-tool-native:** UX Pilot (~1M users claimed, generation + automated design review), Figma AI UX Audit plugins, Attention Insight/VisualEyes (predictive attention heatmaps), Pixelait (screenshot UI linting), uxaudit.dev.
- Academic benchmarks for multimodal LLM UX reasoning now exist (arXiv 2606.13192).

### Table stakes the prompts lack
Actual measurement (contrast, CWV, keyboard nav — the prompts admit all of this is "Inferred": url-mode.md:67,77,82), a validated heuristic database, screenshot annotation, CI integration, tracked re-audits.

### Genuine differentiators
- **Three explicit input modes** (URL/screenshot/codebase) with mode-appropriate epistemic caveats — the codebase mode (grep-driven, file:line evidence) has no direct analogue among the products above, which are all surface-level.
- **The inference-labeling discipline** (Verified/Inferred/Suspected, pre-flight accessible/inaccessible inventory) is genuinely better epistemics than typical "AI UX audit" content and answers the standard criticism of LLM audits.
- Free and transparent vs Baymard's paywall.

### Verdict
For a developer wanting a fast qualitative audit with zero tooling — plausible choice. For anyone who needs defensible a11y/perf findings, axe-core + Lighthouse are free and objective, and for heuristic depth Baymard has 346 heuristics to this prompt's ~20 dimensions. The honest framing: this is a *triage* instrument, and its codebase mode is the interesting one.

---

## Category 6 — Claude Code skills ecosystem

### The landscape (API numbers, 2026-08-12)
- **anthropics/skills: 168,477 stars** (created 2025-09-22 → ~15.7k stars/month). No issue-creation skill in it (`"gh issue create" repo:anthropics/skills` → 0 hits).
- SKILL.md became an **open standard Dec 2025**, supported by Claude Code, Claude.ai, API, OpenAI Codex, Cursor, Gemini CLI, Antigravity, Windsurf (multiple secondary sources).
- Community: ComposioHQ/awesome-claude-skills **72,353**; hesreallyhim/awesome-claude-code **52,200**; obra/superpowers **271,156** (incl. `writing-plans` and `brainstorming` skills — the pre-implementation planning territory); mattpocock/skills **214,829**; affaan-m/ECC **239,686**. *Caveat:* several of these curves are historically anomalous (claw-code: 195k stars/109k forks), so treat community star counts as inflated-prone; the anthropics number is the safest signal.
- Multiple marketplaces (claudeskills.info, awesomeskill.ai claiming 69k+ skills, mcpmarket, plugin marketplaces via `/plugin marketplace add`).
- **Issue skills are commodity:** GitHub code search `"gh issue create" filename:SKILL.md` → **15,360 files** (order-of-magnitude; includes forks). Marketplace listings for GitHub-issue creators and `/fix-issue`-style implementers are numerous (mcpmarket "GitHub Issues" skill, feiskyer's `github-fix-issue`, openclaw `gh-issues`...).

### Table stakes / gaps
- **Distribution:** not a plugin, in no marketplace, no `npx skills add` path; install is "copy SKILL.md to `.claude/commands/...`" (README.md:148,156) — which is the *slash-command* directory, not the documented `.claude/skills/` location (flagged for the skills agent).
- **Staleness:** "Skills are Claude Code only... cannot run in any chat interface" (README.md:80,115) was already questionable when written (open standard Dec 2025 predates repo creation Apr 2026) and is wrong by Aug 2026 — Codex/Cursor/Gemini CLI all run SKILL.md with shell access.

### Genuine differentiators
- The **scored quality gate** (evaluate → 7.0 threshold → rewrite → update GitHub issue → then branch) is real novelty. Commodity issue skills create issues; superpowers writes plans; none I found *score* the artifact against an anchored rubric and gate execution on the score.
- The draft-issue skill's conversation-context extraction incl. **rejected alternatives** (SKILL.md:22) is a thoughtful touch uncommon in the commodity skills.

### Verdict
The differentiator is real but invisible: in a 69k-skill ecosystem, an unlisted two-skill repo with wrong install paths has zero discovery surface. The idea (quality-gated agent execution) is exactly on-trend for 2026 (GitHub's own triage push, the Black Hat issue-injection findings make issue vetting security-relevant) — the packaging is three distribution decisions away from viable.

---

## Cross-cutting: the four-month staleness problem

Between the last commit (2026-04-24) and today: Claude's docs reorganized around Fable 5/Opus 5/Sonnet 5 model-specific guidance; the GPT-5.2/5.4/5.5-era arrived on the OpenAI side; OpenAI's platform Evals got a deprecation date (per one source); the skills ecosystem roughly doubled and consolidated into marketplaces; Braintrust raised $80M. The toolkit's calibration is explicitly tied to Claude-of-then (prompt-evaluator.md:7-8). Nothing in the repo dates its claims or defines a revalidation cadence — for a project whose brand is "calibrated," that is a structural weakness an interviewer can reach in one question.

---

## Interview framing

### Strongest honest positioning statement
> "This is a calibration-first evaluation methodology, demonstrated end-to-end at small scale — not a platform. The 2026 LLM-as-judge literature says a judge needs anchored rubrics with an exemplar per score level; I actually built those, twice, including a controlled-degradation set that gives monotonic anchors — which is more calibration discipline than most production judge prompts have. Then I closed the loop: the same rubric that scores an issue gates whether an agent is allowed to start work on it, which is where the industry went in 2026 with GitHub's own AI triage. The deliberate trade-off is zero infrastructure — everything is readable markdown that runs in a chat window — and the obvious next steps are porting the rubrics into promptfoo/Console evals as judge assets and validating against human labels with kappa. What I'd defend is the methodology; what I wouldn't claim is adoption."

Supporting facts the owner can safely cite: anchor-per-score-level is prescribed 2026 practice (futureagi/deepeval); no named prompt framework has a scored epistemics dimension (verified against 2026 framework roundups); no issue-level anchored scoring gate exists in anthropics/skills or surfaced anywhere in a 15k-file search; the AI-ready-issue thesis has empirical backing (arXiv 2512.21426); GitHub's official guidance and Copilot merge-rate findings agree directionally with the rubric's core sections (acceptance criteria, scoping, file pointers).

### The comparison an interviewer is most likely to throw
1. **"Why wouldn't I just use promptfoo — or Anthropic's own Console, which now has the Humanloop team's Evaluations product and a free prompt improver?"** This is the kill-shot question because Anthropic both wrote the framework the toolkit builds on *and* ships the tooling that obsoletes its paste-in form factor. The only honest answer is the positioning above: zero-infrastructure niche + portable judge asset + pedagogy, not tooling.
2. Close second: **"Your calibration is nine prompts you scored yourself. Where's the human agreement data?"** (no kappa, n=9, circular self-scoring, unfalsifiable "93% confidence").
3. For the issue half: **"GitHub says an AI-ready issue is three things and spec-kit has 126k stars — why eight sections with mandatory rollback?"**
4. Sleeper question: **"It's been untouched since April. Which of these numbers still hold on current models?"**

### What is genuinely good, bad, nonsense, terrible, incomplete (this lane's ledger)
- **Genuinely good:** anchored calibration sets; controlled degradation methodology; epistemics-as-scored-dimension packaging; Verified/Inferred labeling; the scored quality-gate loop; real, checkable citations.
- **Bad:** zero engagement with any competitor; form factor (paste-in) already obsoleted for professional use; stale "Claude Code only" claim; generic unfindable name (58 identically-named repos; teknium1's has 452 stars).
- **Nonsense:** "93% confidence" as a number; "most prompt engineering guides are opinion-based" as a market description of 2026.
- **Terrible:** nothing in this lane rises to terrible — the work is honest; the positioning is merely absent.
- **Incomplete:** human validation (kappa), distribution (marketplace/plugin/Action), currency (post-April model landscape), and any acknowledgment that a competitive landscape exists.