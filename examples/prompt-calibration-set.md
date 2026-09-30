# Prompt Calibration Set
## Ten Scored Anchor Prompts for the PPEP Framework

---

## Methodology

### How this was built

These ten prompts are real prompts used in live development sessions. They are not synthetic examples. Anchors 1-9 were written and iteratively improved by the framework author; Anchor 10 was written by an AI coding assistant during a real audit of this repository (see its provenance note). Each represents a genuine use case encountered during framework development, and they were scored against the PPEP rubric as the framework was being stabilised.

Scores were assigned by the subject matter expert who developed the PPEP framework — a single evaluator. The LLM evaluation literature below uses human judgment rather than automated scoring as ground truth, typically from multiple raters with adjudication; single-rater scoring is a known limitation of this set:

- Hashemi, H., Eisner, J., Rosset, C., Van Durme, B., & Kedzie, C. (2024). *LLM-Rubric: A Multidimensional, Calibrated Approach to Automated Evaluation of Natural Language Texts*. Proceedings of ACL 2024. https://aclanthology.org/2024.acl-long.745.pdf
- Label Studio. (2026). *How to Scale Evaluation for RAG and Agent Workflows*. https://labelstud.io/blog/how-to-scale-evaluation-for-rag-and-agent-workflows/

### Known limitations

Single-evaluator scoring carries irreducible subjectivity. This is a documented limitation in usability and evaluation research:

Evaluators frequently disagree when assigning severity ratings (Sauro, J. (2014), *Journal of Usability Studies*, 10(1), citing Nielsen, 1993; see also Hertzum, M. (2006), *International Journal of Human-Computer Interaction*, 21(2), 125–146), and Nielsen recommends averaging the ratings of several independent evaluators because a single evaluator's ratings are unreliable (Nielsen, J. (1994), *Severity Ratings for Usability Problems*, Nielsen Norman Group).

The calibration set reduces scoring variance by providing ten concrete reference points, but does not eliminate the underlying subjectivity. `examples/prompt-calibration-agreement.md` measures how well independent raters reproduce these scores: they rank the anchors almost identically (Spearman 0.95 to 1.00) but score the two 10/10 anchors lower when they cannot see the anchors.

These anchors were calibrated against Claude's behavior specifically. Scoring consistency may vary on other models. The model and version used for the original calibration were not recorded; record them when re-running the anchors.

### Revision history

**April 2026:** original scores assigned by the framework author.

**September 2026:** criteria revised for current reasoning models (see "What changed and why" in `framework/ppep-framework.md`) and anchors re-scored against the revised criteria. Only scores affected by a changed criterion were revisited; every other score is the author's original. The re-scored values are proposed changes for the author to confirm.

| Anchor | Dimension | Original | Revised | Reason |
|---|---|---|---|---|
| 6 | Epistemics | 8 | 7 | "Check your answers online for outdated docs" is a specific evidence requirement but does not address negative claims, which the 8-9 band requires (this was already true under the original bands) |
| 7 | Process | 10 | 5 | "Explain each step with code examples" and "a structured report" are output format, not work structure; no checkpoint or completion condition |
| 7 | Epistemics | N/A | 2 | Asking for "the latest best practices on React 19" depends on current facts the prompt does not supply, with no instruction to check them |

**September 2026, later:** Anchor 10 added at 8/10 (see its provenance note). A candidate for a 9/10 anchor was sought; the best available real prompt scored 8.

Overall effect of the re-score: Anchor 6 stays 8/10 (7.75). Anchor 7 moves from 9/10 to 6/10, which leaves the set without a 9/10 anchor; a real prompt at that level should be added. Several notes were also reworded because a missing persona is no longer a gap on its own and tone belongs to Performance, not Product; those changes did not move any score.

### Relationship to the framework

This calibration set is an applied output of the PPEP framework. For the theoretical basis of the four dimensions, the scoring scale justification, and the seven integrated prompting techniques, see `framework/ppep-framework.md`.

---

## How to use this document

Use these anchors to calibrate your intuition before evaluating your own prompts. When you score a prompt, compare it against the anchor that most closely resembles it. A prompt with similar gaps to Anchor 3 should score similarly to Anchor 3.

---

## Scoring scale reminder

Each dimension (Product, Process, Performance, Epistemics) is scored 1-10. The overall score is the average of the active dimensions (see Epistemics N/A note below).

The four bands below correspond to the behavioral anchor pattern used in the PPEP framework for Product, Process, and Performance. They follow the pattern of a behaviorally anchored rating scale, adapted for prompt evaluation. **Epistemics uses a five-band scale** (1-3, 4-5, 6-7, 8-9, 10) defined in the framework document because the progression from implicit to full epistemic rigor is finer-grained. The framework document (`framework/ppep-framework.md`) provides the full theoretical basis for both scales.

| Score | Meaning | Observable signal |
|---|---|---|
| 1-3 | Dimension is absent or so vague it provides no guidance | Claude must guess or invent the missing element entirely |
| 4-6 | Dimension is partially addressed with meaningful gaps | Claude can partially follow the intent but will make assumptions that may not match your needs |
| 7-8 | Dimension is well addressed with minor gaps remaining | Claude will produce a good response but one specific sub-criterion is missing |
| 9-10 | Dimension is fully specified with no meaningful ambiguity | Claude has everything it needs; variance in output comes from the model, not the prompt |

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
| Product | 7 | Tech stack, experience, soft skills specified. Missing format, length, location. |
| Process | 2 | No draft checkpoint or completion condition. The AI delivers one finished posting on its own assumptions. |
| Performance | 3 | No audience depth, tone, or collaboration style. |
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
| Process | 5 | Research-then-report sequence implied. No checkpoint or completion condition. |
| Performance | 3 | No audience depth or collaboration style; no tone beyond "analytical". |
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
| Product | 7 | Strong content but missing format, length, and location. |
| Process | 8 | Draft questions first, verify with user, then produce — real iterative process with a checkpoint. |
| Performance | 7 | Ask-first instruction and verification loop are solid. Tone and depth not specified. |
| Epistemics | 6 | Web search and comparison present. No inventory-before-judging, no negative claims proof. |

**Why this score:** This is what a well-structured prompt with one persistent gap looks like. Process and Performance improved dramatically from earlier versions through the addition of an iterative loop. Product is held back by missing constraints that seem obvious in hindsight (format, length, location). The lesson: even when you know your domain well, Product gaps about format and constraints are easy to miss.

---

## ANCHOR 6 — Overall: 8/10
### Failure mode: Strong audience, weak Product angle

**Prompt:**
> "Act as an experienced tech author working for 10+ years covering tech news. Write a 2000 word detailed technical article about React Server Components for our engineering blog for senior devs that want to get new knowledge. Create a draft version first and verify it with me. Check your answers online for outdated docs."

**Scores:**
| Dimension | Score | Notes |
|---|---|---|
| Product | 9 | Word count, audience, format all specified. Missing specific angle or argument. |
| Process | 7 | Draft checkpoint present. No completion condition; an outline checkpoint would catch a wrong angle earlier. |
| Performance | 8 | Audience (senior developers) and depth (detailed, technical) specified. Tone left to what the persona implies. |
| Epistemics | 7 (originally 8) | Specific evidence requirement (check against current docs). Does not cover negative claims or inventory-before-judging. |

**Why this score:** (9 + 7 + 8 + 7) / 4 = 7.75, rounded to 8. Clear audience and depth, a real checkpoint, and a specific verification source, each with one clear remaining gap. The most consequential weakness is that no specific angle or argument is defined for the article, leaving Claude to decide what to say about RSC rather than defending a specific position.

---

## ANCHOR 7 — Overall: 6/10 (originally 9/10)
### Failure mode: Current-practice claims with no verification, no completion condition

**Prompt:**
> "I want you to create a small tic tac toe web app in React with younger children as the target audience. Use colorful designs and beautiful animations across the board. Include sounds too. I want to be detailed in the approach you follow, by explaining each step you do with code examples. I want to use the latest best practices on React 19 including React Compiler. Present your steps in a structured report. Be analytical and technical."

**Scores:**
| Dimension | Score | Notes |
|---|---|---|
| Product | 9 | Clear deliverable, audience, tech stack, visual direction. Missing game feature list (score tracking, win detection, reset button). |
| Process | 5 (originally 10) | "Explain each step with code examples" and "a structured report" are mainly output format, credited under Product; they imply an order of work. No checkpoint and no completion condition (a playable build, passing tests). |
| Performance | 8 | Technical depth and analytical tone specified. No collaboration style. |
| Epistemics | 2 (originally N/A) | Asks for "the latest best practices on React 19 including React Compiler" with no instruction to check current documentation. |

**Why this score:** (9 + 5 + 8 + 2) / 4 = 6.0. This anchor was originally scored 9/10 with Epistemics N/A and Process 10. Under the revised criteria, a request for step-by-step explanation is output format rather than work structure, and a request for "latest" practices is exactly the kind of claim that needs checking.

**Note on Epistemics N/A:** Do not penalize prompts for missing Epistemics when the task does not require knowledge verification. A task has a meaningful epistemic dimension when it requires the AI to make factual claims, retrieve or verify information, evaluate existing artifacts, or draw conclusions about the state of a system, including claims about current or "latest" practices. Pure code generation from a complete, self-contained specification, creative writing, and formatting tasks have no meaningful epistemic dimension: the AI is producing content from instructions, not asserting facts about the world.

When Epistemics is N/A, the overall score is the average of the active dimensions only. Applying the dimension to tasks where it does not fit will artificially deflate scores and create false incentives to add verification instructions where they add no value.

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

**Why this is the technical 10/10:** The defining characteristic is not just that it covers all four dimensions — it is the depth of the Epistemics dimension. This prompt does not just tell Claude what to do; it tells Claude how to know things and how to prove them. The instruction "do not summarize agent exploration results as facts" anticipates guidance that now appears in official documentation for agentic work: ground every claim in evidence from the session.

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
| Performance | 10 | A role that carries real context (HR manager + academic background + former direct manager who knows the candidate's work), collaborative and iterative tone fully defined. |
| Epistemics | 10 | Online search, verification against current standards, proof for positive and negative claims. |

**Why this is the non-technical 10/10:** This prompt reaches the same score as Anchor 8 through entirely different means. No grep commands, no file references, no agentic tools — just a precisely specified role, a fully defined iterative process, and explicit epistemic requirements for a collaborative writing task. The two 10/10 anchors together demonstrate that perfect prompts look very different depending on the task type.

---

## ANCHOR 10 — Overall: 8/10
### Failure mode: Rigorous agent brief with no stated audience

**Provenance:** Unlike Anchors 1-9, this prompt was not written by the framework author. It was written by an AI coding assistant in September 2026 and sent to a research subagent during a real audit of this repository, which produced the citation corrections now in this toolkit. It is included because it is a real prompt that did real work, and because it shows a failure mode the other anchors do not: an autonomous agent brief. It was added while looking for a 9/10 anchor and scored 8/10, so the set still has no 9/10 anchor.

**Prompt:**
> You are a citation and link verifier for a documentation repo. Today is 2026-09-30. READ-ONLY: do not edit any file.
>
> Task: find EVERY URL, DOI, arXiv ID, and formal citation (Author, Year, Title) across all files in /home/user/prompt-engineering-toolkit (excluding .git). Files: README.md, CONTRIBUTING.md, LICENSE, framework/ppep-framework.md, prompts/prompt-evaluator.md, prompts/issue-evaluator.md, prompts/uiux-evaluator/url-mode.md, prompts/uiux-evaluator/screenshot-mode.md, prompts/uiux-evaluator/codebase-mode.md, examples/prompt-calibration-set.md, examples/issue-calibration-set.md, skills/draft-issue/SKILL.md, skills/implement-issue/SKILL.md, .github/workflows/notify-companion.yml.
>
> Step 1: Use Grep to extract all `http`/`https` URLs, `doi`, `arxiv`, and citation-looking patterns like `(19xx)`/`(20xx)` with author names. Build a deduplicated table.
>
> Step 2: For each URL, fetch it with WebFetch (if WebFetch fails through the proxy, use Bash: `curl -sSIL --cacert /root/.ccr/ca-bundle.crt -o /dev/null -w '%{http_code} %{url_effective}\n' <url>` then fetch body if needed). Record: HTTP status, final URL after redirects, whether the page title/content matches the cited title and authors, and the actual publication year shown on the page.
>
> Step 3: For each formal citation without a URL (e.g. "Nielsen 1993", "Hertzum 2006", "Nielsen 1994 Severity Ratings"), use WebSearch to confirm the work exists with that author/year/title/venue, and note the canonical URL.
>
> Step 4: Specifically double-check these suspicious ones:
> - "CorsoUX. (2026). UX Audit Checklist: 50 Points" at courseux.com (name mismatch CorsoUX vs courseux; year 2026)
> - "Sayagh, M., et al. (2025). What Makes a GitHub Issue Ready for Copilot?" arXiv 2512.21426 (does this arXiv ID resolve to that paper and author list?)
> - "Eisenstein, J., et al. (2024). LLM-Rubric" ACL 2024 aclanthology 2024.acl-long.745 (check the real first author)
> - "Li, X., et al. (2024)" ACM TOSEM DOI 10.1145/3643673 (check the real title and first author)
> - "ReliablePenguin (2025)" blog post dated 2025/10/29
> - GitHub docs URL docs.github.com/en/copilot/tutorials/cloud-agent/get-the-best-results (does it resolve; what is its current title)
> - Anthropic AI Fluency PDF at www-cdn.anthropic.com/62df988c101af71291b06843b63d39bbd600bed8.pdf
> - The live demo https://prompt-engineering-toolkit-companio.vercel.app and the companion repo github.com/Doberjohn/prompt-engineering-toolkit-companion (do they resolve? does the companion app still exist and does its README match "three of the evaluators", "no API key required"?)
> - "GitHub issue #278" referenced as the source of the issue calibration set: which repo is it from, and is that stated anywhere?
>
> Output: a markdown table with columns: Citation/URL as written | File:line(s) | Status (OK / REDIRECTED / DEAD / MISATTRIBUTED / WRONG YEAR / NOT FOUND / UNVERIFIED) | What the source actually is (title, authors, year, final URL) | Recommended fix. Then a short summary counting OK vs problems, and a ranked list of the problems that most damage the repo's "research-backed" credibility. Do not guess: if you cannot fetch a source, mark it UNVERIFIED and say why.

**Scores:**
| Dimension | Score | Notes |
|---|---|---|
| Product | 8 | Every file listed, scope explicit, table columns and status vocabulary fixed, summary and ranked list named. The report's audience is never stated, and the summary length is unbounded. |
| Process | 8 | Ordered deliverables (inventory, fetch, confirm, targeted checks, table) and a completion condition implied by "EVERY" item getting a row. No checkpoint, because it runs unattended. Steps 1-3 prescribe method, which is acceptable here because completeness matters. |
| Performance | 6 | A role only. No audience or depth, no tone, no collaboration style beyond read-only. |
| Epistemics | 10 | Inventory before judging (Step 1 table first), evidence recorded for every item (status, final URL, title match, year), negative results require a check (DEAD, NOT FOUND), and inferences labelled: "Do not guess: if you cannot fetch a source, mark it UNVERIFIED and say why." |

**Why this score:** (8 + 8 + 6 + 10) / 4 = 8.0. The author's pre-registered score was Product 10 and 8.5 overall; all three blind raters (see `examples/prompt-calibration-agreement.md`) independently flagged the missing audience, which the rubric counts under Product, so Product was lowered to 8. Epistemics is as strong as Anchor 8. The lesson is that a prompt can be rigorous about evidence and still leave the reader of the output undefined.

**Note on Process for autonomous briefs:** The Process 9-10 band requires checkpoints. A brief for an agent that runs without a human in the loop cannot have them, so it tops out at 8 however well it structures deliverables and completion. This is a known limitation of the current rubric, not a flaw in the prompt.

---

## Observations from scoring the calibration set

The following patterns were observed during the scoring of Anchors 1-9 by a single subject matter expert (Observation 7 covers Anchor 10). They are not formal research findings — they are heuristics surfaced from this specific set of nine real prompts. They are offered as calibration guidance, not as general claims about all prompts or all users.

**Observation 1: In this set, strong Product without the other dimensions produced low overall scores.**
Anchor 2 scores 7 on Product but only 3 overall. The developer knew their domain well but did not address how Claude should approach the task, behave, or verify its knowledge. Whether this reflects a general pattern in real-world prompts is not claimed here — it is a structural consequence of the four-dimension framework applied to these specific examples.

**Observation 2: In this set, a single addition produced the largest dimension jumps.**
Between Anchor 3 and Anchor 4, one addition — web search and verification — jumped Epistemics from 1 to 7. The largest score improvements in this set came from targeting the single weakest dimension rather than incrementally improving all dimensions simultaneously.

**Observation 3: In this set, Epistemics was consistently the last dimension addressed.**
Apart from Anchor 4, no anchor before the 7/10 range has meaningful Epistemics. Whether this reflects general user behaviour is not claimed here — it reflects the development trajectory of these nine specific prompts.

**Observation 4: Two structurally different prompts reached 10/10.**
Anchors 8 and 9 both score 10/10 through entirely different approaches. One uses grep commands and file references in an agentic codebase context. The other uses role layers and iterative collaboration in a non-technical writing context. This suggests the framework is task-agnostic in its application, though two examples are insufficient to establish this as a general claim.

**Observation 5: Epistemics N/A is valid for some task types, but narrower than it first appears.**
Anchor 7 was originally scored N/A on Epistemics as a code generation task. On re-scoring, its request for "the latest best practices" made the dimension applicable. N/A remains valid for generation from a complete, self-contained specification; forcing the dimension there would artificially deflate the score.

**Observation 6: The revised criteria mostly moved notes, not scores.**
Of 36 dimension scores, three changed in the September 2026 re-score, all in Anchors 6 and 7. The larger shift was in what the notes credit: checkpoints and completion conditions rather than numbered steps, audience and depth rather than a persona, and specific evidence rather than generic verification.

**Observation 7: A prompt can be rigorous about evidence and still leave the audience undefined.**
Anchor 10 matches Anchor 8 on Epistemics (10) but scores 6 on Performance and 8 on Product because it never says who the output is for. Blind raters converged on this gap without seeing the reference scores. It also exposes a rubric limit: autonomous agent briefs cannot have checkpoints, so Process caps at 8 for them.
