# Prompt Engineering Toolkit

A research-backed toolkit covering the **Description** competency of the AI Fluency 4D Framework — with calibrated evaluation tools, real-world examples, and production-ready prompt templates.

---

## Built on the AI Fluency Framework

This toolkit is a practitioner's implementation built on top of the **AI Fluency Framework** by Rick Dakan, Joseph Feller, and Anthropic (2025), released under CC BY-NC-SA 4.0. The framework defines four competencies for effective, efficient, ethical, and safe collaboration with AI systems — the 4Ds:

- **Delegation** — deciding when and how to involve AI
- **Description** — communicating your intent to AI effectively
- **Discernment** — evaluating AI outputs with critical judgment
- **Diligence** — taking responsibility for AI-assisted work

This toolkit covers **Description** in depth — the competency concerned with writing prompts that produce the results you need. The PPEP framework, prompt evaluator, and calibration sets all operate within this competency. The issue evaluator is a **Discernment** tool — it supports human judgment over AI-destined documents before execution begins.

The three remaining competencies (Delegation, full Discernment coverage, and Diligence) are not covered by this toolkit. The full AI Fluency course is available through Anthropic and covers all four competencies with structured exercises and project-based learning.

> Dakan, R., Feller, J., & Anthropic. (2025). *AI Fluency: Framework and Foundations*. Released under CC BY-NC-SA 4.0. Supported in part by the Higher Education Authority, Ireland, through the National Forum for the Enhancement of Teaching and Learning.

---

## Why this exists

Most prompt engineering guides are opinion-based. They tell you what to do without explaining why, without evidence, and without a way to measure whether your prompts are actually improving.

This toolkit was built differently.

Every decision in this framework was:

- **Grounded in established research** — Nielsen's 10 Usability Heuristics, WCAG 2.2 AA, NN/G studies, peer-reviewed usability literature
- **Validated through iteration** — prompts were evaluated, scored, revised, and rescored against a consistent rubric until the framework stabilized
- **Calibrated against real examples** — a set of ten anchor prompts spanning 1/10 to 8/10 was developed to reduce scoring subjectivity
- **Honest about limitations** — scoring agreement is measured rather than asserted, and the limits of single-evaluator scoring are documented

The result is a framework you can trust, teach, and build on.

---

## Live demo

See the toolkit in action at https://prompt-engineering-toolkit-companio.vercel.app. The companion app ships three of the evaluators as a hosted web app, powered by Claude. No API key required. 

Source: [Doberjohn/prompt-engineering-toolkit-companion](https://github.com/Doberjohn/prompt-engineering-toolkit-companion).

---

## What is in this toolkit

### The Framework
A four-dimension model for evaluating and writing AI prompts, extended with seven evidence-based prompting techniques and mapped to established research.

> **Scope note:** The PPEP framework covers the **Description** competency of the AI Fluency 4D Framework (Dakan, Feller, and Anthropic, 2025). The three peer competencies — Delegation, Discernment, and Diligence — are not covered by this toolkit. Description is the competency concerned with communicating effectively with AI systems. The other three competencies address deciding when to involve AI (Delegation), evaluating AI outputs (Discernment), and responsible use (Diligence).

**Core dimensions:**
- **Product** — what you want: output, format, audience, scope, constraints
- **Process** — how the work should be structured: checkpoints, deliverable order, completion conditions
- **Performance** — how the AI should behave: audience, depth, tone, collaboration style (a persona only when voice matters)
- **Epistemics** — how the AI should know things: inventory before judging, proof for negative claims, evidence shown, inferences labelled

> Product, Process, and Performance are the AI Fluency framework's own Description components; Epistemics is this toolkit's extension. Its content (investigate before answering, show evidence, say what is unverified) now also appears in official prompting guidance; what the toolkit adds is making it scoreable. In the calibration set, it is the dimension that most often separates strong prompts from gold-standard ones.
>
> The criteria were revised in September 2026 for current reasoning models: Process no longer rewards step-by-step thinking instructions, a persona is optional, and generic "verify your answer" lines earn little. See "What changed and why" in `framework/ppep-framework.md`.

### The Prompt Evaluator
A session intro prompt for activating strict, calibrated prompt evaluation. Scores prompts across the four PPEP dimensions using ten scored reference anchors. Works best with Claude, compatible with any instruction-following AI model.

### The UI/UX Evaluation Prompts
Three production-ready evaluation prompts for auditing user interfaces (`prompts/uiux-evaluator/`), one for each evaluation source: URL (`url-mode.md`), Screenshot (`screenshot-mode.md`), and Codebase (`codebase-mode.md`). Built on Nielsen's heuristics, WCAG 2.2 AA, and 20 independently scored dimensions (1-10 each, no aggregate score) covering both UI (objective) and UX (heuristic inference). Every finding carries a confidence label, and AI-generated findings of Severity 3 or 4 that are not verified require human confirmation.

### The Issue Evaluator
A Discernment tool — a session intro prompt for exercising human judgment over GitHub implementation plan issues before delegating execution to AI. Evaluates whether an issue is safe to hand to an AI coding agent by scoring it across eight sections using a weighted formula derived from Nielsen's severity scale. Also runs a separate agent readiness check (runnable done-when command, environment or instruction file, out-of-scope list, boundaries, human-only steps, scope) with a verdict of ready, supervise, or not ready. Produces severity findings and generates targeted improvement suggestions (score >= 7.0), a full revised issue (2.0 <= score < 7.0), or a structured template (score < 2.0) when context is insufficient for a meaningful rewrite. Built on research from GitHub official documentation, Agile acceptance criteria standards, and SRE runbook quality frameworks.

### The Prompt Calibration Set
Ten real prompts, spanning scores from 1/10 to 8/10. The two prompts originally scored 10/10 were lowered to 8/10 and 7/10 after independent blind raters found gaps the rubric defines; the set currently has no 9/10 or 10/10 anchor. Nine were written by the framework author during development; the tenth is an autonomous agent brief from a real audit of this repository. Re-scored in September 2026 against the revised criteria, with the original scores kept for traceability. A companion agreement study (`examples/prompt-calibration-agreement.md`) measures how consistently independent raters reproduce these scores. Included as a learning resource.

### The Issue Calibration Set
A real implementation plan issue ([Doberjohn/inkweave#278](https://github.com/Doberjohn/inkweave/issues/278), formula score 9.44/10) plus nine controlled degradations of it, each with a traceable degradation rationale and formula score. Built by controlled degradation of a known-good artifact, following the logic of perturbation-based meta-evaluation (Karpinska et al., 2022). Includes a full methodology section with 28 citations across GitHub issue quality research, Agile documentation standards, SRE runbook frameworks, and LLM evaluation methods.

### The Claude Code Skills
Both skills and the Issue Evaluator share one rubric, maintained in `rubric/issue-rubric.md` and copied into each of them by `scripts/sync-issue-rubric.py`. A CI check fails if any copy drifts.

Two project-agnostic Claude Code skills that close the write → evaluate → implement loop end to end. Both skills need a repository checkout plus `git` and the GitHub CLI (`gh`), so they run in Claude Code (local, or cloud sessions at claude.ai/code) rather than in plain chat interfaces. The SKILL.md format itself follows the open [Agent Skills](https://agentskills.io) standard.

**`draft-issue`** (`skills/draft-issue/SKILL.md`) — invoke at the end of any Claude Code session where scope has been agreed. Reads context from the conversation, asks up to three clarifying questions when needed, drafts a full eight-section issue, scores it against the weighted rubric, iterates until approved, then publishes via `gh issue create`.

**`implement-issue`** (`skills/implement-issue/SKILL.md`) — invoke when starting work on an issue. Runs session hygiene, fetches the issue, evaluates it against the eight-section rubric with a 7.0 quality gate, rewrites and updates the GitHub issue if it scores below the threshold, reads `CLAUDE.md` for project conventions, creates the branch, and presents a full implementation brief.

---

## Confidence and limitations

Scoring agreement for the PPEP rubric was measured in September 2026 (`examples/prompt-calibration-agreement.md`). In five blind rater runs on the nine calibration prompts:

- **Ranking is reliable:** Spearman correlation with the reference scores was 0.95 to 1.00.
- **Repeat runs agree:** in pairwise comparisons, three runs of the same model gave identical dimension scores 80% of the time (Krippendorff's alpha 0.98).
- **Absolute scores drift without the anchors:** runs averaged 0.5 to 1.4 points from the original reference, and scored the two anchors then rated 10/10 between 6.25 and 9.0. Their reasons identified real gaps, and both anchors were lowered (to 8/10 and 7/10); against the revised reference, the average gap narrows to 0.6 to 1.1 points across both runs (partly by construction, since the revision used the raters' reasons).

Trust the evaluator's ranking of prompts more than any single absolute score, and treat a one-point difference as noise. Single-evaluator scoring is a documented limitation in the usability literature (Nielsen 1993, Hertzum 2006); averaging several runs reduces it. An earlier version of this README stated a 93% "confidence level", which was not measured and has been removed. The issue evaluator's scores have not yet been measured this way.

All research sources are cited inline in the relevant documents.

---

## Model compatibility

| Component | Claude | ChatGPT | Gemini | Claude Code |
|---|---|---|---|---|
| Framework (PPEP) | Full | Full | Full | Full |
| Prompt Evaluator | Full | Partial* | Partial* | Full |
| Issue Evaluator | Full | Partial* | Partial* | Full |
| UI/UX URL Mode | Full**** | Full**** | Full**** | Full |
| UI/UX Screenshot Mode | Full | Full | Full | Full |
| UI/UX Codebase Mode | Partial** | Partial** | Partial** | Full |
| `draft-issue` skill | N/A | N/A | N/A | Full*** |
| `implement-issue` skill | N/A | N/A | N/A | Full*** |

*The calibration anchors were developed and validated using Claude. Scoring consistency may vary on other models.

**Codebase mode uses grep commands and file:line references that require an agentic coding environment with shell and repository access (for example Claude Code, OpenAI Codex, GitHub Copilot coding agent or Copilot CLI, Cursor). Chat interfaces can only approximate it, for example by uploading a repository archive to a code-execution sandbox.

***These two skills depend on a repository checkout, `git`, `gh`, and conversation context, so they run in Claude Code (local or cloud sessions) rather than in chat interfaces. The Agent Skills format itself is an open standard supported beyond Claude Code.

****Chat apps fetch pages as text and generally do not render JavaScript, so visual and performance dimensions are inferred rather than verified. Use a browser-capable agent or screenshots for those.

---

## Getting started

**To evaluate a GitHub implementation plan issue:**
1. Open `prompts/issue-evaluator.md`
2. Copy the full contents
3. Paste into a new AI session
4. The AI will confirm it understands the framework, then you paste your issue content

To understand how the scoring is anchored, read `examples/issue-calibration-set.md` — it contains the ten reference issues used to calibrate the evaluator.

**To evaluate a prompt you have written:**
1. Open `prompts/prompt-evaluator.md`
2. Copy the full contents
3. Paste into a new AI session
4. The AI will confirm it understands the framework, then you paste your prompt

**To evaluate a UI/UX interface:**
1. Open `prompts/uiux-evaluator/`
2. Choose the file that matches your available input: `url-mode.md`, `screenshot-mode.md`, or `codebase-mode.md`
3. Copy that file's prompt
4. Paste into a new AI session alongside your URL, screenshots, or codebase access

**To draft an implementation plan issue from a Claude Code conversation:**
1. In your Claude Code terminal, agree on the scope of the upcoming work
2. Invoke `/draft-issue` (optionally with a brief title hint)
3. The skill reads the conversation, asks clarifying questions if needed, and produces a scored draft
4. Review, request changes, approve
5. The skill publishes the issue via `gh issue create`

Install: copy the whole `skills/draft-issue/` folder (`SKILL.md` and `issue-rubric.md`) to `.claude/skills/draft-issue/` in your repo, or to `~/.claude/skills/draft-issue/` for global access. (Do not place it under `.claude/commands/`: a file in a subfolder there is invoked as `/<folder>:<filename>`, so it would become `/draft-issue:SKILL`.)

**To start implementing an issue with the quality gate:**
1. In your Claude Code terminal, invoke `/implement-issue <number>`
2. The skill evaluates the issue against the eight-section rubric
3. If the score is >= 7.0 it proceeds to branch setup with an implementation brief
4. If the score is < 7.0 it produces a rewrite, asks for approval, updates the GitHub issue, then branches

Install: copy the whole `skills/implement-issue/` folder (`SKILL.md` and `issue-rubric.md`) to `.claude/skills/implement-issue/` in your repo, or to `~/.claude/skills/implement-issue/` for global access.

**To learn the framework before using the tools:**
1. Start with `framework/ppep-framework.md`
2. Read through the seven integrated techniques and "What changed and why"
3. Study `examples/prompt-calibration-set.md` to calibrate your intuition

---

## References and sources

This toolkit draws on the following established research and standards:

- Nielsen, J. (1994). [10 Usability Heuristics for User Interface Design](https://www.nngroup.com/articles/ten-usability-heuristics/). Nielsen Norman Group.
- Nielsen, J. (1994). [Severity Ratings for Usability Problems](https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/). Nielsen Norman Group.
- W3C. (2023). [Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/).
- Hertzum, M. (2006). Problem prioritization in usability evaluation: From severity assessments toward impact on design. *International Journal of Human-Computer Interaction*, 21(2), 125–146.
- Sauro, J. (2013). [Rating the Severity of Usability Problems](https://measuringu.com/rating-severity/). MeasuringU.
- CorsoUX. (2026). [UX Audit Checklist: 50 Points](https://courseux.com/ux-audit-checklist/).
- Dakan, R., Feller, J., & Anthropic. (2025). [AI Fluency: Framework and Foundations](https://www-cdn.anthropic.com/62df988c101af71291b06843b63d39bbd600bed8.pdf). CC BY-NC-SA 4.0.
- Sülün, E., Saçakçı, M., & Tüzün, E. (2024). [An Empirical Analysis of Issue Templates Usage in Large-Scale Projects on GitHub](https://dl.acm.org/doi/10.1145/3643673). ACM Transactions on Software Engineering and Methodology, 33(5).
- Sayagh, M. (2025). [What Makes a GitHub Issue Ready for Copilot?](https://arxiv.org/abs/2512.21426) arXiv preprint.
- GitHub. (2025). [Best Practices for Using GitHub Copilot to Work on Tasks](https://docs.github.com/en/copilot/tutorials/cloud-agent/get-the-best-results). GitHub Docs.
- Hashemi, H., Eisner, J., Rosset, C., Van Durme, B., & Kedzie, C. (2024). [LLM-Rubric: A Multidimensional, Calibrated Approach to Automated Evaluation of Natural Language Texts](https://aclanthology.org/2024.acl-long.745.pdf). Proceedings of ACL 2024.
- ReliablePenguin. (2025). [What Is a Runbook? History, Template, and Best Practices](https://blogs.reliablepenguin.com/2025/10/29/what-is-a-runbook-history-template-and-best-practices).
- Atlassian. (n.d.). [What is Acceptance Criteria?](https://www.atlassian.com/work-management/project-management/acceptance-criteria)
- Karpinska, M., Raj, N., Thai, K., Song, Y., Gupta, A., & Iyyer, M. (2022). [DEMETR: Diagnosing Evaluation Metrics for Translation](https://aclanthology.org/2022.emnlp-main.649/). Proceedings of EMNLP 2022.

---

## Contributing

See `CONTRIBUTING.md` for guidelines. Contributions that include evidence, citations, or calibrated examples are strongly preferred over opinion-based additions.

---

## License

MIT. See `LICENSE`.
