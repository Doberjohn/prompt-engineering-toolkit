# Prompt Calibration Set
## Nine Scored Anchor Prompts for the PPEP Framework

---

## How to use this document

These nine prompts were evaluated and scored during the development of the PPEP framework. They represent real prompts written and iteratively improved in live sessions, not constructed examples.

Use them to calibrate your intuition before evaluating your own prompts. When you score a prompt, compare it against the anchor that most closely resembles it. A prompt with similar gaps to Anchor 3 should score similarly to Anchor 3.

**Important:** These anchors were calibrated against Claude's behavior specifically. Scoring consistency may vary on other models.

---

## Scoring scale reminder

Each dimension (Product, Process, Performance, Epistemics) is scored 1-10. The overall score is the average of the four dimensions.

| Score | Meaning |
|---|---|
| 1-3 | Dimension is absent or so vague it provides no guidance |
| 4-6 | Dimension is partially addressed with meaningful gaps |
| 7-8 | Dimension is well addressed with minor gaps remaining |
| 9-10 | Dimension is fully specified with no meaningful ambiguity |

---

## ANCHOR 1 — Overall: 1/10
### Failure mode: Everything missing

**Prompt:**
> "Make it better."

**Scores:**
| Dimension | Score | Notes |
|---|---|---|
| Product | 1 | No deliverable defined |
| Process | 1 | No process |
| Performance | 1 | No behavioral instruction |
| Epistemics | 1 | No epistemic instruction |

**Why this is the floor:** Zero information across all four dimensions. Claude has nothing to work with except its own assumptions about what "it" is and what "better" means. Use this as the absolute reference point for a 1/10 prompt.

---

## ANCHOR 2 — Overall: 3/10
### Failure mode: Content without structure

**Prompt:**
> "Help me write a job posting for a senior developer position. We are a company looking for developers to work in our client projects. They should have strong knowledge of Modern React, Typescript, JSX, and at least 5 years of experience. They should have good communication skills because they will spend most of the time talking with the client. Experience in AI is highly appreciated."

**Scores:**
| Dimension | Score | Notes |
|---|---|---|
| Product | 7 | Tech stack, experience, soft skills specified. Missing format, length, tone, location. |
| Process | 2 | No process. Claude decides its own approach. |
| Performance | 3 | No role, no tone, no collaboration style. |
| Epistemics | 1 | No verification, no research instruction. |

**Why this score:** Strong domain knowledge in Product but Process, Performance, and Epistemics are almost entirely absent. This is the most common real-world failure pattern — the person knows their domain but does not think about how Claude should approach it. High Product score masks three empty dimensions.

---

## ANCHOR 3 — Overall: 3/10
### Failure mode: Vague content, weak everywhere

**Prompt:**
> "Write something for our company blog. We are a company making athletic footwear and want to target ages 25-30. Be analytical."

**Scores:**
| Dimension | Score | Notes |
|---|---|---|
| Product | 5 | Audience and industry identified. Deliverable ("something") is still vague. No topic, format, or length. |
| Process | 2 | No process. |
| Performance | 3 | "Be analytical" touches Performance but specifies nothing actionable. |
| Epistemics | 1 | Nothing. |

**Why this score:** Different failure profile from Anchor 2. Weaker Product (no specific deliverable) but the same weak Process and Epistemics. The word "analytical" gives a false sense of Performance completeness — it sounds like an instruction but gives Claude no real guidance on depth, approach, or tone. A useful lesson: vague adjectives do not substitute for real Performance instructions.

---

## ANCHOR 4 — Overall: 5/10
### Failure mode: Epistemics added, structure still missing

**Prompt:**
> "Write something for our company blog. We are a company making athletic footwear and want to target ages 25-30. Be analytical and use web to search for what others do and verify your results against theirs. Give a structured report with your findings."

**Scores:**
| Dimension | Score | Notes |
|---|---|---|
| Product | 6 | Format (structured report) added. Topic still unspecified. |
| Process | 5 | Web search and verification is a genuine process instruction. No ordered steps. |
| Performance | 3 | No role, no tone beyond "analytical". |
| Epistemics | 7 | Web search and verification against others is a real epistemic instruction. |

**Why this score:** The notable thing about this prompt is that Epistemics (7) outscores Performance (3). The person naturally reached for verification before thinking about role or tone. This is an unusual but real pattern — strong instinct for evidence, weak instinct for behavioral calibration. The jump in Epistemics from Anchor 3 (1) to this version (7) came from a single addition.

---

## ANCHOR 5 — Overall: 7/10
### Failure mode: Strong everywhere except Product scope

**Prompt:**
> "Help me write a job posting for a senior developer position. We are a company looking for developers to work in our client projects. They should have strong knowledge of Modern React, Typescript, JSX, and at least 5 years of experience. They should have good communication skills because they will spend most of the time talking with the client. Experience in AI is highly appreciated. Compare your posting against others you find online. First create draft questions which you will verify and fine tune with me. If you need extra info ask me first."

**Scores:**
| Dimension | Score | Notes |
|---|---|---|
| Product | 7 | Strong content but missing format, length, tone, and location. |
| Process | 8 | Draft questions first, verify with user, then produce — real iterative process with a checkpoint. |
| Performance | 7 | Ask-first instruction and verification loop are solid. No role defined, no tone specified. |
| Epistemics | 6 | Web search and comparison present. No inventory-before-judging, no negative claims proof. |

**Why this score:** This is what a well-structured prompt with one persistent gap looks like. Process and Performance improved dramatically from earlier versions through the addition of an iterative loop. Product is held back by missing constraints that seem obvious in hindsight (format, location, tone). The lesson: even when you know your domain well, Product gaps about format and constraints are easy to miss.

---

## ANCHOR 6 — Overall: 8/10
### Failure mode: Strong role, weak Product angle

**Prompt:**
> "Act as an experienced tech author working for 10+ years covering tech news. Write a 2000 word detailed technical article about React Server Components for our engineering blog for senior devs that want to get new knowledge. Create a draft version first and verify it with me. Check your answers online for outdated docs."

**Scores:**
| Dimension | Score | Notes |
|---|---|---|
| Product | 9 | Word count, audience, format all specified. Missing specific angle or argument. |
| Process | 7 | Draft and verify present. No outline step before drafting. |
| Performance | 8 | Strong specific role. Missing tone calibration beyond what the role implies. |
| Epistemics | 8 | Mandatory online verification present. Does not cover negative claims or inventory-before-judging. |

**Why this score:** Three dimensions at 8+ with one clear remaining gap in each — this is the signature of an 8/10 prompt. Strong role definition, solid process, good verification. The only meaningful weakness is that no specific angle or argument is defined for the article, leaving Claude to decide what to say about RSC rather than defending a specific position.

---

## ANCHOR 7 — Overall: 9/10
### Failure mode: Strong but missing feature scope

**Prompt:**
> "I want you to create a small tic tac toe web app in React with younger children as the target audience. Use colorful designs and beautiful animations across the board. Include sounds too. I want to be detailed in the approach you follow, by explaining each step you do with code examples. I want to use the latest best practices on React 19 including React Compiler. Present your steps in a structured report. Be analytical and technical."

**Scores:**
| Dimension | Score | Notes |
|---|---|---|
| Product | 9 | Clear deliverable, audience, tech stack, visual direction. Missing game feature list (score tracking, win detection, reset button). |
| Process | 10 | Step by step with code examples, structured report — explicit methodology throughout. |
| Performance | 8 | Technical depth and analytical tone specified. No role defined. |
| Epistemics | N/A | Not applicable for a pure code generation task with no research or verification component. |

**Note on Epistemics N/A:** Do not penalize prompts for missing Epistemics when the task does not require knowledge verification. Code generation, creative writing, and formatting tasks have no meaningful epistemic dimension. Applying the dimension to tasks where it does not fit will artificially deflate scores.

---

## ANCHOR 8 — Overall: 10/10
### Gold standard: Technical agentic context

**Prompt:**
> "Improve the overall UI/UX on Inkweave to make it more engaging with animated segments and graphics. Constraints on analysis: 1. Inventory before judging. Before scoring any area, produce a complete inventory of every page/route in the app, every existing @keyframes animation, every component that uses transition or animation properties, every custom animation hook and where each is imported. Show the grep results or file references as evidence. 2. Per-page analysis. Score each route separately. Every page in the router must appear in the report. 3. Negative claims require proof. If you say something does not exist show the search you ran to confirm it. If you say a component is not used show the import search. 4. Scoring criteria. For each page score current animation quality 1-10, improvement impact potential 1-10, list every existing animation with file:line references. Deliverables in order: 1. Inventory - the raw evidence. 2. Audit report - structured findings per page with scores. 3. Proposed solutions - creative, out of the box, build on existing patterns. 4. Discussion - pause for my input. Process: notify me when each deliverable is complete. If you need clarification ask before proceeding. Do not summarize agent exploration results as facts - verify every claim with direct grep/read."

**Scores:**
| Dimension | Score | Notes |
|---|---|---|
| Product | 10 | Deliverable fully specified: per-page scores, file:line references, ordered deliverables. |
| Process | 10 | Four explicit ordered deliverables, pause for input, notify on completion. |
| Performance | 10 | Collaboration style, verification behavior, and creative direction all defined. |
| Epistemics | 10 | Inventory before judging, negative claims require proof, no summarizing as facts — full epistemic rigor. |

**Why this is the technical 10/10:** The defining characteristic is not just that it covers all four dimensions — it is the depth of the Epistemics dimension. This prompt does not just tell Claude what to do; it tells Claude how to know things and how to prove them. The instruction "do not summarize agent exploration results as facts" is a level of epistemic precision rarely seen in prompts written by anyone.

---

## ANCHOR 9 — Overall: 10/10
### Gold standard: Non-technical collaborative context

**Prompt:**
> "Act as an experienced human resources manager that had a career in academics in the past and was my manager in the previous company. If you have any questions throughout the process ask me clarifying questions before writing anything. Write me a strong 1000 word cover letter for an upcoming senior fashion journalist job I am applying, covering all the things I worked on with the manager and my strengths in a structured report. Break the letter in segments. Create draft versions first so we can go back and forth fixing all the points needed or I give you feedback about missing stuff. We will finalize when everything is in order. I was a senior journalist in the previous company so do a thorough search online about other strong cover letters in my domain and always verify that your structure is the most up to date with what others do. You have to always find and provide proof that what you propose is true and that you don't give negative claims."

**Scores:**
| Dimension | Score | Notes |
|---|---|---|
| Product | 10 | Word count, specific job target, format, structured segments, domain all specified. |
| Process | 10 | Clarifying questions before writing, draft iterations, back-and-forth loop, defined completion condition. |
| Performance | 10 | Role with three layers of context (HR manager + academic background + former direct manager), collaborative and iterative tone fully defined. |
| Epistemics | 10 | Online search, verification against current standards, proof for positive and negative claims. |

**Why this is the non-technical 10/10:** This prompt reaches the same score as Anchor 8 through entirely different means. No grep commands, no file references, no agentic tools — just a precisely specified role, a fully defined iterative process, and explicit epistemic requirements for a collaborative writing task. The two 10/10 anchors together demonstrate that perfect prompts look very different depending on the task type.

---

## Key patterns across the calibration set

**Pattern 1: Product without the others is not enough.**
Anchor 2 scores 7 on Product but only 3 overall. Knowing your domain does not substitute for Process, Performance, and Epistemics.

**Pattern 2: A single addition can jump a dimension.**
Between Anchor 3 and Anchor 4, one addition (web search and verification) jumped Epistemics from 1 to 7. The biggest score improvements often come from a single targeted change to the weakest dimension.

**Pattern 3: Epistemics is the last dimension people think of and the one with the highest leverage.**
No anchor before the 7/10 range has meaningful Epistemics. Yet the difference between a 7/10 and a 10/10 prompt is almost always Epistemics.

**Pattern 4: Two different paths to 10/10.**
Anchors 8 and 9 both score 10/10. One uses grep commands and file references in an agentic codebase context. The other uses role layers and iterative collaboration in a non-technical writing context. The framework is content-agnostic.

**Pattern 5: Epistemics N/A is valid.**
Anchor 7 scores N/A on Epistemics for a code generation task. Do not force a dimension where it does not apply — it will artificially deflate good prompts.
