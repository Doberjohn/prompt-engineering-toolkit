# The PPEP Framework
## A Research-Backed Model for Writing and Evaluating AI Prompts

---

## Overview

The PPEP Framework (Product, Process, Performance, Epistemics) is a four-dimension model for writing and evaluating prompts for AI language models. It was developed through iterative testing, scored against real examples, and grounded in established research from usability, communication, and epistemology.

> **Scope note:** The PPEP framework covers the **Description** competency of the AI Fluency 4D Framework (Dakan, Feller, and Anthropic, 2025). The three peer competencies — Delegation (deciding when and how to involve AI), Discernment (evaluating AI outputs), and Diligence (responsible use) — are not covered by this framework. PPEP addresses the question: once you have decided to use AI for a task, how do you communicate your intent effectively?

The four dimensions are:

1. **Product** — what you want
2. **Process** — how the work should be structured
3. **Performance** — how the AI should behave
4. **Epistemics** — how the AI should know things

**Attribution:** Dimensions 1-3 are the three components of the Description competency defined by the AI Fluency Framework (Product Description, Process Description, Performance Description). This toolkit adds sub-criteria, scoring bands, and calibration anchors to them. Dimension 4, Epistemics, is this toolkit's extension.

Each dimension is independently scoreable from 1-10. Together they produce a composite quality score that predicts how useful the AI's response will be.

> **Revision note (September 2026):** The Process, Performance, and Epistemics criteria were revised to match current guidance for reasoning models, which think before answering by default. The main changes: Process rewards checkpoints and deliverable order rather than step-by-step thinking instructions; a persona is optional rather than required; "ask it to think first" is replaced by asking for tradeoffs and evidence in the answer; and generic "verify your answer" instructions no longer earn Epistemics credit. See "What changed and why" at the end of this document.

---

## Why four dimensions?

Most prompting guides treat a prompt as a single thing to optimize. The PPEP framework treats a prompt as four communication problems, each of which can succeed or fail independently.

A prompt can have a perfect Product description (crystal clear deliverable) but no checkpoints, so the AI delivers a finished draft built on a wrong assumption you would have caught at the outline. A prompt can have good checkpoints but weak Performance (the AI pauses at the right moments but pitches the answer at the wrong depth). A prompt can score well on all three and still fail because it has no Epistemics — it asks the AI to know things without telling it what evidence to show.

Understanding which dimension is failing tells you exactly how to fix it.

### Where each dimension lives

In a one-off chat, all four dimensions live in the prompt. In agentic or repeated use, much of them belongs elsewhere: standing context and conventions in a system prompt or a repository instruction file (such as CLAUDE.md or AGENTS.md), reusable procedures in skills, and verification in runnable checks. When evaluating a prompt written for such a setting, credit what the surrounding context already supplies, and keep stable content ahead of the part that changes per request so it can be cached.

---

## Dimension 1: Product Description

**What it covers:** The output you want. Everything the AI needs to know about the deliverable before starting.

**Sub-criteria:**
- Scope defined: what is included and what is not
- Target audience identified: who the output is for
- Format specified: structured report, bullet list, code, prose, table, etc.
- Length or constraints specified: word count, file type, column definitions
- Specific deliverables named when the output has multiple parts

**Technique: Provide Context**
Before specifying what you want, give the AI the parameters that shape it — geography, timeframe, domain, technical environment — and the reason you need it. Without context, the AI fills gaps with assumptions that may not match your situation.

**Technique: Specify Output Constraints**
Define the exact format. Not just "a report" but "a structured report with sections for findings, scores per area, and a prioritized roadmap." Format specification is one of the highest-leverage additions to a chat prompt. When a prompt is called through an API and the output must be machine-readable, enforce the format with the provider's structured output feature rather than prose instructions.

**Scoring guidance:**
- 1-3: Deliverable is vague or undefined. The AI will guess.
- 4-6: Deliverable is implied but key constraints are missing (format, length, audience).
- 7-8: Deliverable is clear with most constraints specified. Minor assumptions remain.
- 9-10: Deliverable is fully specified. The AI has zero ambiguity about what to produce.

---

## Dimension 2: Process Description

**What it covers:** How the work should be structured: which intermediate deliverables come first, where the AI should stop for your input, and what done looks like. It does not cover how the AI should think.

**Sub-criteria:**
- Checkpoints defined: where the AI should pause for input, show a draft, or confirm before anything irreversible
- Deliverable order specified where it matters: inventory before analysis, outline before draft, draft before final
- Completion conditions stated: what done looks like, ideally something checkable
- Method left to the model where it plans well: ordered steps are prescribed only where order or completeness matters

**Technique: Structure the Work, Not the Thinking**
Current models plan and reason before answering. Anthropic's guidance for its current models is to prefer general instructions over prescriptive steps, because the model's own reasoning frequently exceeds a hand-written step-by-step plan, and prompts written for older models are often too prescriptive and can degrade output. What still pays off is structure the model cannot infer: the checkpoints where you want to steer, the order of deliverables you want to review, and the condition that ends the task.

**Scoring guidance:**
- 1-3: The task needs checkpoints or ordered deliverables and none are given. The AI will deliver one finished answer built on its own assumptions.
- 4-6: Some structure implied but not explicit. The AI may skip a stage you wanted to review.
- 7-8: Checkpoints or deliverable order defined. Completion condition missing or vague.
- 9-10: Checkpoints, deliverable order, and completion conditions all present, with the method left to the model where it can plan well.

**Process N/A:** Only when the task is fully specified and so small that the answer is a single short output with nothing to review in stages: a one-line answer, a rewrite of text supplied in the prompt, a factual lookup. A vague or underspecified prompt is never Process N/A, because its missing structure is exactly what should be scored; a request for a document, posting, article, report, or code is never Process N/A. When in doubt, score it. Average the active dimensions when it applies.

**Autonomous briefs (no human in the loop):** When the prompt is written for an agent that runs without anyone available to answer (a background task, a subagent, a scheduled run), the checkpoint sub-criterion is N/A: score deliverable order, completion conditions, and method only, so such a brief can reach 9-10. A stop condition (when to halt and report instead of continuing, such as before an irreversible action or when blocked) counts toward the completion condition. Only apply this when the prompt itself makes clear no human will be available; an ordinary chat prompt with no checkpoints is not autonomous.

**No credit for thinking choreography:** Instructions that dictate how to reason ("first think about X, then consider Y, then decide") earn no Process credit. Note them as a risk: on current models they are redundant at best and can lower quality.

---

## Dimension 3: Performance Description

**What it covers:** How the AI should behave during your collaboration: depth, tone, and interaction style.

**Sub-criteria:**
- Audience and depth calibrated: who the answer is for, how technical, how detailed, how exhaustive
- Tone or voice specified where it matters: analytical, concise, challenging, supportive, or a named voice
- Collaboration style: ask clarifying questions, check in between stages, or proceed and state assumptions
- Examples provided where the desired style is hard to describe in words

**Technique: Define the Audience (and a Role Only When Voice Matters)**
Stating who the output is for and how deep to go does most of the work a persona used to do. A role ("act as a senior mobile architect briefing mid-level developers") still helps set voice, vocabulary, and assumed knowledge, but research finds that expert personas do not improve factual accuracy, and current guidance treats heavy-handed role prompting as usually unnecessary. A missing persona is not a gap on its own.

**Technique: Show Examples of What Good Looks Like**
When the desired output style, tone, or quality is hard to describe in words, provide examples. Examples calibrate the AI's output in ways that descriptions alone cannot. Provide three to five varied examples and say they are illustrative: current models follow a single example closely, including its length and structure, so one example tends to be copied rather than generalized. This is the most commonly underused technique for subjective output types (writing style, UI aesthetic, communication tone).

> If you find yourself unable to describe what good looks like in words, stop and find examples instead. They will do more work than any description.

**Scoring guidance:**
- 1-3: No audience, depth, tone, or collaboration guidance. The AI defaults to generic assistant mode.
- 4-6: Some of these are implied by the content but not stated.
- 7-8: Audience and depth stated, and either tone or collaboration style defined. One element missing.
- 9-10: Audience, depth, tone, and collaboration style all defined. Examples provided where style is subjective.

---

## Dimension 4: Epistemics

**What it covers:** How the AI should know things and how it should show that it knows them. This is the toolkit's addition to the AI Fluency Description components. Its content (investigate before answering, ground claims in evidence, say what is unverified) now also appears in official prompting guidance, but it is rarely packaged as something a prompt can be scored on.

**Sub-criteria:**
- Inventory before judging: the AI gathers evidence before drawing conclusions, not concluding and then justifying
- Negative claims require proof: if the AI says something does not exist, it shows the search or check that confirmed it
- Evidence shown: sources, searches, quotes, or file:line references accompany the claims they support, and tradeoffs are laid out in the answer
- Inferences labelled: the AI does not present inferences as verified findings and says what it could not verify

**Why this dimension exists**

Without epistemic instructions, models can state inferences as facts and claim things do not exist without checking, especially on long agentic runs. Current models are better calibrated than earlier ones and often check their own work unprompted, so the value of this dimension has shifted: generic "double-check your answer" instructions are now redundant, while specific evidence requirements (show the search, cite the source, label what is unverified) remain valuable. The Epistemics dimension makes the AI's conclusions checkable by you.

**The clearest example of weak Epistemics:**
> "There are no entrance animations in this codebase."

The AI said this after a visual scan of a few files. It had not grepped for `@keyframes`, had not checked CSS files, and had not verified the claim. The statement was presented as a fact. It was an inference at best, and potentially wrong.

**The same claim with strong Epistemics:**
> "Grep for @keyframes across all CSS and JS files returned zero results (output shown). Grep for animation: returned zero results. Grep for transition: returned 3 files (listed). Based on this inventory, no keyframe animations are present, though CSS transitions are used in [file:line]."

The second version is verifiable, honest about scope, and actionable.

**Technique: Ask for Tradeoffs and Evidence in the Answer**
For architecture decisions, technical comparisons, and strategic recommendations, ask the AI to lay out the options, the tradeoffs, and the evidence behind its recommendation in the answer itself. Do not ask it to "think step by step" or to write out its reasoning: models with built-in thinking already reason before answering, and on some current models an instruction to reproduce internal reasoning in the response can trigger a refusal. If you need more deliberation, use the model's thinking or effort setting rather than prose.

**Scoring guidance:**

> Note: Epistemics uses five bands rather than four because the progression from implicit to full epistemic rigor is meaningfully finer-grained.

- 1-3: No epistemic instruction. The AI may assert without evidence.
- 4-5: Generic verification only ("check online", "verify your answer", "double-check"). Earns little: current models already do this, and it does not tell the AI what evidence to show.
- 6-7: A specific evidence requirement: named sources to check against, comparison with current documentation, or evidence to show. Negative claims not addressed.
- 8-9: Evidence required and negative claims require proof.
- 10: Full epistemic rigor. Inventory before judging. Negative claims require proof with shown evidence. Inferences labelled; nothing summarized as fact without evidence.

**Epistemics N/A:** Epistemics is N/A when the prompt supplies everything the output depends on and the task is to generate or transform from it (code from a complete specification, creative writing, formatting). It is applicable whenever the output depends on facts the prompt does not supply: current or "latest" practices, the state of a codebase or system, market norms, or claims about the world. A prompt too vague to tell what the output depends on is never Epistemics N/A.

---

## The seven integrated techniques

The PPEP framework integrates the six prompting techniques taught in the AI Fluency course (Dakan, Feller, & Anthropic, 2025), plus the course's meta-technique. Two of the six have been adapted for current reasoning models; the table notes how.

### Dimension-mapped techniques

| Technique | Dimension | How it is applied here |
|---|---|---|
| Provide Context | Product | Scopes the deliverable with real-world parameters and the reason for the request |
| Specify Output Constraints | Product | Locks format, length, and structure; use structured outputs for machine-readable API output |
| Break Complex Tasks into Steps | Process | Adapted: structure the deliverables and checkpoints, not the model's thinking |
| Define the AI's Role | Performance | Adapted: state audience and depth; add a persona only when voice matters |
| Show Examples of What Good Looks Like | Performance | Three to five varied examples for subjective output |
| Ask It to Think First | Epistemics | Adapted: ask for tradeoffs and evidence in the answer, not a reasoning transcript |

### The meta-technique

**Ask the AI for help with prompting.**

When you are unsure which dimension is failing or how to fix it, ask the AI directly: "I am trying to get you to help me with [goal]. I am not sure how to phrase my request to get the best results. Can you help me craft an effective prompt for this?"

This technique does not map to a single dimension because it operates across all four simultaneously — the AI diagnoses which Product, Process, Performance, or Epistemic instructions are missing and suggests how to add them. The source authors describe it as "perhaps the most powerful technique of all."

It is most useful as a diagnostic tool: reach for it when the six dimension-mapped techniques have not produced the result you need, and you cannot identify which dimension is the source of the failure.

> Source: Dakan, R., Feller, J., & Anthropic. (2025). [AI Fluency: Framework and Foundations](https://www-cdn.anthropic.com/62df988c101af71291b06843b63d39bbd600bed8.pdf). CC BY-NC-SA 4.0.

---

## Scoring the overall prompt

The overall score is the average of the active dimension scores. When Process or Epistemics is N/A (see the N/A rules in those dimensions), average the remaining active dimensions only. However, dimension scores are not equally weighted in practice — a prompt with Epistemics at 1/10 on a research or verification task is not a 7/10 prompt regardless of other scores. Use the overall average as a starting point, then apply judgment about which dimensions matter most for the task type.

**Task type guidance:**

| Task type | Most critical dimension |
|---|---|
| Research, audit, analysis | Epistemics |
| Code generation, technical implementation | Product, Process (especially a checkable completion condition) |
| Writing, content creation | Performance (especially examples) |
| Architecture, strategy | Epistemics, Process |
| Iterative collaboration | Performance |
| One-shot deliverable | Product |

---

## Confidence and limitations

**Measured agreement (September 2026).** Five blind rater runs scored the nine calibration prompts using only the rubric, without the anchors (full method and data in `examples/prompt-calibration-agreement.md`):

- The rubric orders prompts reliably: Spearman correlation with the reference overall scores was 0.95 to 1.00 in every run.
- Scores are highly repeatable within one model: in pairwise comparisons, three runs of the same model gave identical dimension scores 80% of the time (Krippendorff's alpha 0.98).
- Absolute scores vary: without anchors, runs were 0.5 to 1.4 points from the reference overall scores on average, and scored the two anchors then rated 10/10 between 6.25 and 9.0. A follow-up run with reasons showed real gaps in both, and they were lowered to 8/10 and 7/10; against the revised reference, the average gap narrows to 0.6 to 1.1 points across both runs (partly by construction, since the revision used the raters' reasons).

In practice: trust the evaluator's ranking of prompts more than any single absolute score, keep the calibration anchors in the evaluator, and treat differences of about one point as noise.

A single evaluator's scores remain a known limitation. Evaluators frequently disagree when assigning severity ratings (Sauro, 2014, citing Nielsen, 1993; see also Hertzum, 2006), and Nielsen recommends averaging the ratings of several independent evaluators because a single evaluator's ratings are unreliable (Nielsen, 1994b). Averaging several runs of one model reduces run-to-run noise but does not remove that model's shared biases; independent raters (different models, or people) are closer to what Nielsen recommends.

Earlier versions of this document stated a "framework confidence" of 93%. That figure was not measured and has been replaced by the results above.

Since this framework uses a single AI evaluator, some scoring variance is unavoidable by definition. The calibration set (see `examples/prompt-calibration-set.md`) reduces this variance by providing ten concrete reference points, but does not eliminate it.

**Model dependence:** Prompting guidance differs between model generations, and the model used for the original calibration was not recorded. When you re-run the calibration anchors, record the model and date alongside the scores.

---

## What changed and why (September 2026)

| Area | Before | After | Why |
|---|---|---|---|
| Process | Rewarded numbered, ordered steps as the quality bar | Rewards checkpoints, deliverable order, and completion conditions; adds Process N/A; no credit for thinking choreography | Current guidance: prefer general instructions over prescriptive steps; prompts written for older models are often too prescriptive (Anthropic, n.d.-a, n.d.-b) |
| Performance | Role required for a high score | Audience and depth required; persona optional | Personas do not improve factual accuracy (Zheng et al., 2024); heavy role prompting usually unnecessary (Anthropic, n.d.-a) |
| Examples | One example | Three to five varied examples | Current guidance recommends 3-5 examples; models follow a single example closely (Anthropic, n.d.-a) |
| Epistemics technique | "Ask it to think first"; "reasoning before answering" sub-criterion | "Ask for tradeoffs and evidence in the answer"; "evidence shown" sub-criterion | Current models reason before answering by default; asking for a reasoning transcript can trigger refusals on some models (Anthropic, n.d.-b) |
| Epistemics scoring | Generic "verify your answer" scored 4-5 as partial rigor | Earns little; specific evidence requirements score higher | Current models verify their own work unprompted, and generic re-check instructions cause over-verification (Anthropic, n.d.-c) |
| Epistemics N/A | Defined only in the calibration set | Defined here; "latest/current" requirements make it applicable | Claims about fast-moving practice are exactly what needs checking |
| Confidence | Unmeasured "93% framework confidence" | Measured agreement from five blind rater runs | The figure had no measurement or source behind it |
| Process N/A | "Small enough that no checkpoint would add anything" | Only fully specified single-output tasks; vague prompts and requests for documents or code are never N/A | Blind raters applied the looser rule to vague prompts, hiding their missing structure |
| Autonomous briefs | Process 9-10 required checkpoints, capping unattended agent briefs at 8 | Checkpoints N/A when the prompt makes clear no human is available; stop conditions count toward completion | Current agentic guidance favours stating boundaries and when to stop over pausing for input (Anthropic, n.d.-b) |
| Attribution | Four dimensions presented as original | Dimensions 1-3 attributed to AI Fluency; Epistemics as the extension | Accurate attribution of a CC BY-NC-SA source |

The effect on the calibration anchors is documented in `examples/prompt-calibration-set.md`.

---

## References

- Anthropic. (n.d.-a). [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices). Claude Docs.
- Anthropic. (n.d.-b). [Prompting Claude Fable 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5). Claude Docs.
- Anthropic. (n.d.-c). [Prompting Claude Opus 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5). Claude Docs.
- Zheng, M., Pei, J., Logeswaran, L., Lee, M., & Jurgens, D. (2024). [When "A Helpful Assistant" Is Not Really Helpful: Personas in System Prompts Do Not Improve Performances of Large Language Models](https://aclanthology.org/2024.findings-emnlp.888/). Findings of EMNLP 2024.
- Nielsen, J. (1994a). Heuristic evaluation. In Nielsen, J. & Mack, R.L. (Eds.), *Usability Inspection Methods*. John Wiley & Sons.
- Nielsen, J. (1993). *Usability Engineering*. Academic Press.
- Nielsen, J. (1994b). [Severity Ratings for Usability Problems](https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/). Nielsen Norman Group.
- Sauro, J. (2014). [The Relationship Between Problem Frequency and Problem Severity in Usability Evaluations](https://uxpajournal.org/the-relationship-between-problem-frequency-and-problem-severity-in-usability-evaluations/). *Journal of Usability Studies*, 10(1).
- Hertzum, M. (2006). Problem prioritization in usability evaluation: From severity assessments toward impact on design. *International Journal of Human-Computer Interaction*, 21(2), 125–146.
- Dakan, R., Feller, J., & Anthropic. (2025). [AI Fluency: Framework and Foundations](https://www-cdn.anthropic.com/62df988c101af71291b06843b63d39bbd600bed8.pdf). Released under CC BY-NC-SA 4.0.
