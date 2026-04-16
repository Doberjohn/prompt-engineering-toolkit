# The PPEP Framework
## A Research-Backed Model for Writing and Evaluating AI Prompts

---

## Overview

The PPEP Framework is a four-dimension model for writing and evaluating prompts for AI language models. It was developed through iterative testing, scored against real examples, and grounded in established research from usability, communication, and epistemology.

> **Scope note:** The PPEP framework covers the **Description** competency of the AI Fluency 4D Framework (Dakan, Feller, and Anthropic, 2025). The three peer competencies — Delegation (deciding when and how to involve AI), Discernment (evaluating AI outputs), and Diligence (responsible use) — are not covered by this framework. PPEP addresses the question: once you have decided to use AI for a task, how do you communicate your intent effectively?

The four dimensions are:

1. **Product** — what you want
2. **Process** — how the AI should approach it
3. **Performance** — how the AI should behave
4. **Epistemics** — how the AI should know things

Each dimension is independently scoreable from 1-10. Together they produce a composite quality score that predicts how useful the AI's response will be.

---

## Why four dimensions?

Most prompting guides treat a prompt as a single thing to optimize. The PPEP framework treats a prompt as four independent communication problems, each of which can succeed or fail independently.

A prompt can have a perfect Product description (crystal clear deliverable) but zero Process instruction (Claude will pick its own approach). A prompt can have a perfect Process but weak Performance (Claude follows the steps but answers in the wrong tone or depth). A prompt can score well on all three and still fail because it has no Epistemics — it asks Claude to know things without telling it how to verify them.

Understanding which dimension is failing tells you exactly how to fix it.

---

## Dimension 1: Product Description

**What it covers:** The output you want. Everything Claude needs to know about the deliverable before starting.

**Sub-criteria:**
- Scope defined: what is included and what is not
- Target audience identified: who the output is for
- Format specified: structured report, bullet list, code, prose, table, etc.
- Length or constraints specified: word count, file type, column definitions
- Specific deliverables named when the output has multiple parts

**Technique: Provide Context**
Before specifying what you want, give Claude the parameters that shape it — geography, timeframe, domain, technical environment. Without context, Claude fills gaps with assumptions that may not match your situation.

**Technique: Specify Output Constraints**
Define the exact format. Not just "a report" but "a structured report with sections for findings, scores per area, and a prioritized roadmap." Format specification is one of the highest-leverage additions to any prompt.

**Scoring guidance:**
- 1-3: Deliverable is vague or undefined. Claude will guess.
- 4-6: Deliverable is implied but key constraints are missing (format, length, audience).
- 7-8: Deliverable is clear with most constraints specified. Minor assumptions remain.
- 9-10: Deliverable is fully specified. Claude has zero ambiguity about what to produce.

---

## Dimension 2: Process Description

**What it covers:** How Claude should approach the task. The order of operations, the methodology, the steps.

**Sub-criteria:**
- Steps defined: numbered, ordered, explicit
- Methodology specified: research first then recommend, draft then verify, inventory then evaluate
- Checkpoints defined: when Claude should pause, verify, or check in
- Completion conditions stated: what done looks like at each stage

**Technique: Break Complex Tasks into Steps**
Guided by decades of research on how structured instructions improve AI reasoning (and human performance), breaking a complex task into explicit numbered steps is one of the most reliable ways to improve output quality. The step order matters — it prevents Claude from collapsing multiple stages into a single response.

**Scoring guidance:**
- 1-3: No process. Claude picks its own approach, which may not match what you need.
- 4-6: Some structure implied but not explicit. Claude may combine steps you wanted separate.
- 7-8: Steps defined and ordered. Checkpoints may be missing.
- 9-10: Full process defined. Ordered steps, checkpoints, and completion conditions all present.

---

## Dimension 3: Performance Description

**What it covers:** How Claude should behave during your collaboration. Tone, depth, role, and interaction style.

**Sub-criteria:**
- Role defined: who Claude is acting as, at what level of expertise, for what audience
- Tone specified: analytical, creative, concise, detailed, challenging, supportive
- Collaboration style: ask clarifying questions, check in between steps, proceed and state assumptions
- Depth calibrated: how technical, how detailed, how exhaustive

**Technique: Define the AI's Role**
Assigning a specific role — "act as a senior mobile architect briefing a team of mid-level developers" — shapes not just tone but depth, vocabulary, assumed knowledge, and what Claude considers relevant to include. Role definition is one of the most impactful single-line additions to any prompt.

**Technique: Show Examples of What Good Looks Like**
When the desired output style, tone, or quality is hard to describe in words, provide an example. Examples calibrate Claude's output in ways that descriptions alone cannot. This is the most commonly underused technique and the one most likely to close the gap between a 7/10 and a 10/10 prompt for subjective output types (writing style, UI aesthetic, communication tone).

> If you find yourself unable to describe what good looks like in words, stop and find an example instead. It will do more work than any description.

**Scoring guidance:**
- 1-3: No role, no tone, no collaboration style. Claude defaults to generic assistant mode.
- 4-6: Tone partially implied by content. Role absent or generic.
- 7-8: Role defined. Tone specified. Collaboration style partially addressed.
- 9-10: Role fully specific with layered context. Tone, depth, and collaboration style all defined. Examples provided where style is subjective.

---

## Dimension 4: Epistemics

**What it covers:** How Claude should know things and how it should prove them. This is the most advanced dimension and the one most absent from standard prompting guides.

**Sub-criteria:**
- Inventory before judging: Claude must gather evidence before drawing conclusions, not conclude and then justify
- Negative claims require proof: if Claude says something does not exist, it must show the search or check that confirmed it
- Reasoning before answering: Claude should think through tradeoffs before making recommendations, not jump to conclusions
- No summarizing as facts: Claude must not present inferences as verified findings

**Why this dimension exists**

Claude is confident by default. Without epistemic instructions, it will state things as facts that are actually inferences, skip verification steps, and claim things do not exist without checking. The Epistemics dimension forces Claude to earn its conclusions rather than assert them.

**The clearest example of weak Epistemics:**
> "There are no entrance animations in this codebase."

Claude said this after a visual scan of a few files. It had not grepped for `@keyframes`, had not checked CSS files, and had not verified the claim. The statement was presented as a fact. It was an inference at best, and potentially wrong.

**The same claim with strong Epistemics:**
> "Grep for @keyframes across all CSS and JS files returned zero results (output shown). Grep for animation: returned zero results. Grep for transition: returned 3 files (listed). Based on this inventory, no keyframe animations are present, though CSS transitions are used in [file:line]."

The second version is verifiable, honest about scope, and actionable.

**Technique: Ask It to Think First**
Instructing Claude to reason through tradeoffs before recommending is an accessible entry point to the Epistemics dimension. It prevents shallow, fast answers on complex questions and is particularly valuable for architecture decisions, technical comparisons, and strategic recommendations.

**Scoring guidance:**
- 1-3: No epistemic instruction. Claude will assert without verifying.
- 4-5: Some verification implied ("check online", "verify your answer") but not rigorous.
- 6-7: Explicit verification step present. Negative claims not explicitly addressed.
- 8-9: Verification required. Negative claims require proof. Reasoning before answering.
- 10: Full epistemic rigor. Inventory before judging. Negative claims require proof with shown evidence. No summarizing as facts. Reasoning before concluding.

---

## The seven integrated techniques

The PPEP framework integrates seven evidence-based prompting techniques from Anthropic's prompting research (Dakan, Feller, & Anthropic, 2025). Six map directly to PPEP dimensions. The seventh is a meta-technique that operates across all dimensions simultaneously.

### Dimension-mapped techniques

| Technique | Dimension | Impact |
|---|---|---|
| Provide Context | Product | Scopes the deliverable with real-world parameters |
| Specify Output Constraints | Product | Locks format, length, and structure |
| Break Complex Tasks into Steps | Process | Defines order and prevents step collapse |
| Define the AI's Role | Performance | Shapes depth, vocabulary, and assumed knowledge |
| Show Examples of What Good Looks Like | Performance | Calibrates style when words cannot describe it |
| Ask It to Think First | Epistemics | Entry-level epistemic instruction preventing shallow answers |

### The meta-technique

**Ask the AI for help with prompting.**

When you are unsure which dimension is failing or how to fix it, ask the AI directly: "I am trying to get you to help me with [goal]. I am not sure how to phrase my request to get the best results. Can you help me craft an effective prompt for this?"

This technique does not map to a single dimension because it operates across all four simultaneously — the AI diagnoses which Product, Process, Performance, or Epistemic instructions are missing and suggests how to add them. The source authors describe it as "perhaps the most powerful technique of all."

It is most useful as a diagnostic tool: reach for it when the six dimension-mapped techniques have not produced the result you need, and you cannot identify which dimension is the source of the failure.

> Source: Dakan, R., Feller, J., & Anthropic. (2025). [AI Fluency: Framework and Foundations](https://www-cdn.anthropic.com/62df988c101af71291b06843b63d39bbd600bed8.pdf). CC BY-NC-SA 4.0.

---

## Scoring the overall prompt

The overall score is the average of the four dimension scores. However, dimension scores are not equally weighted in practice — a prompt with Epistemics at 1/10 on a research or verification task is not a 7/10 prompt regardless of other scores. Use the overall average as a starting point, then apply judgment about which dimensions matter most for the task type.

**Task type guidance:**

| Task type | Most critical dimension |
|---|---|
| Research, audit, analysis | Epistemics |
| Code generation, technical implementation | Product, Process |
| Writing, content creation | Performance (especially examples) |
| Architecture, strategy | Epistemics, Process |
| Iterative collaboration | Performance |
| One-shot deliverable | Product |

---

## Confidence and limitations

**Framework confidence: 93%**

The remaining 7% reflects the irreducible subjectivity inherent in single-evaluator heuristic assessment. This is a documented limitation in the usability research literature:

> "There tends to be disagreement between evaluators when assigning severity, and reliability improves when averaging ratings from independent evaluators." — Nielsen (1993), as discussed in Hertzum (2006)

Since this framework uses a single AI evaluator, some scoring variance is unavoidable by definition. The calibration set (see `examples/prompt-calibration-set.md`) reduces this variance by providing nine concrete reference points, but does not eliminate it.

---

## References

- Nielsen, J. (1994). Heuristic evaluation. In Nielsen, J. & Mack, R.L. (Eds.), *Usability Inspection Methods*. John Wiley & Sons.
- Hertzum, M. (2006). Problem prioritization in usability evaluation: From severity assessments toward impact on design. *International Journal of Human-Computer Interaction*, 21(2), 125–146.
- Dakan, R., Feller, J., & Anthropic. (2025). [6 Techniques for Effective Prompt Engineering](https://www-cdn.anthropic.com/62df988c101af71291b06843b63d39bbd600bed8.pdf). Released under CC BY-NC-SA 4.0.
