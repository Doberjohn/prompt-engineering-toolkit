# Prompt Engineering Toolkit

A research-backed, iteratively developed framework for writing better AI prompts — with calibrated evaluation tools, real-world examples, and production-ready prompt templates.

---

## Why this exists

Most prompt engineering guides are opinion-based. They tell you what to do without explaining why, without evidence, and without a way to measure whether your prompts are actually improving.

This toolkit was built differently.

Every decision in this framework was:

- **Grounded in established research** — Nielsen's 10 Usability Heuristics, WCAG 2.2 AA, NN/G studies, peer-reviewed usability literature
- **Validated through iteration** — prompts were evaluated, scored, revised, and rescored against a consistent rubric until the framework stabilized
- **Calibrated against real examples** — a set of nine anchor prompts spanning the full quality range (1/10 to 10/10) was developed to reduce scoring subjectivity
- **Honest about limitations** — confidence intervals, epistemic uncertainty, and the 7% irreducible subjectivity inherent in single-evaluator heuristic assessment are documented throughout

The result is a framework you can trust, teach, and build on.

---

## What is in this toolkit

### The Framework
A four-dimension model for evaluating and writing AI prompts, extended with six evidence-based prompting techniques and mapped to established research.

**Core dimensions:**
- **Product** — what you want: output, format, audience, scope, constraints
- **Process** — how the AI should approach the task: steps, order, methodology
- **Performance** — how the AI should behave: tone, role, collaboration style, depth
- **Epistemics** — how the AI should know things: inventory before judging, proof for negative claims, reasoning before concluding

> The Epistemics dimension is the most advanced and the most impactful. It was independently surfaced during iterative development and is not found in most prompting guides. It is the single biggest differentiator between a 7/10 and a 10/10 prompt.

### The Prompt Evaluator
A session intro prompt you paste at the start of any AI conversation to activate strict, calibrated prompt evaluation with nine scored reference anchors. Works best with Claude, compatible with any instruction-following AI model.

### The UI/UX Evaluation Prompts
Three production-ready evaluation prompts for auditing user interfaces — one for each evaluation source: URL, Screenshot, and Codebase. Built on Nielsen's heuristics, WCAG 2.2 AA, and a 20-dimension scoring system covering both UI (objective) and UX (heuristic inference).

### The Issue Evaluator
A session intro prompt and standalone HTML app for evaluating GitHub implementation plan issues. Scores issues across eight sections using a weighted formula derived from Nielsen's severity scale, produces severity findings, and generates either targeted improvement suggestions (score >= 7.0) or a full revised issue (score < 7.0). Built on research from GitHub official documentation, Agile acceptance criteria standards, and SRE runbook quality frameworks.

### The Prompt Calibration Set
Nine real prompts evaluated and scored during framework development, spanning scores from 1/10 to 10/10 with two distinct 10/10 anchors (technical agentic and non-technical collaborative). Included as a learning resource.

### The Issue Calibration Set
Ten controlled degradations of a real 9.5/10 implementation plan issue (GitHub issue #278), each with a traceable degradation rationale and formula-verified score. Built using the same controlled degradation methodology recommended by NLP evaluation research to avoid central tendency bias. Includes a full methodology section with 25+ citations across GitHub issue quality research, Agile documentation standards, SRE runbook frameworks, and LLM evaluation methods.

---

## Confidence and limitations

This toolkit was built with explicit confidence tracking. Current confidence level in the framework: **93%**.

The remaining 7% is the irreducible subjectivity inherent in single-evaluator heuristic assessment, documented in peer-reviewed literature (Nielsen 1993, Hertzum 2006). This is not a failure of the framework — it is an honest acknowledgment of the limits of any expert-led evaluation method without multi-evaluator aggregation.

All research sources are cited inline in the relevant documents.

---

## Model compatibility

| Component | Claude | ChatGPT | Gemini | Claude Code |
|---|---|---|---|---|
| Framework (PPEP) | Full | Full | Full | Full |
| Prompt Evaluator | Full | Partial* | Partial* | Full |
| Issue Evaluator | Full | Partial* | Partial* | Full |
| UI/UX URL Mode | Full | Full | Full | Full |
| UI/UX Screenshot Mode | Full | Full | Full | Full |
| UI/UX Codebase Mode | Full | Partial** | Partial** | Full |

*The calibration anchors were developed and validated using Claude. Scoring consistency may vary on other models.

**Codebase mode uses grep commands and file:line references that require an agentic coding environment (Claude Code, Cursor, GitHub Copilot Workspace). Standard chat interfaces cannot execute these commands.

---

## Getting started

**To evaluate a GitHub implementation plan issue:**
1. Open `prompts/issue-evaluator.md`
2. Copy the full contents
3. Paste into a new AI session
4. The AI will confirm it understands the framework, then you paste your issue content

Alternatively, use the `issue-evaluator.html` standalone app which includes URL fetching, a progress bar, and structured rendering of section scores and severity findings.

**To evaluate a prompt you have written:**
1. Open `prompts/prompt-evaluator.md`
2. Copy the full contents
3. Paste into a new AI session
4. The AI will confirm it understands the framework, then you paste your prompt

**To evaluate a UI/UX interface:**
1. Open `prompts/uiux-evaluation-prompts.md`
2. Choose the mode that matches your available input (URL, Screenshot, or Codebase)
3. Copy that mode's prompt
4. Paste into a new AI session alongside your URL, screenshots, or codebase access

**To learn the framework before using the tools:**
1. Start with `framework/ppep-framework.md`
2. Read through the six integrated techniques
3. Study `examples/prompt-calibration-set.md` to calibrate your intuition

---

## References and sources

This toolkit draws on the following established research and standards:

- Nielsen, J. (1994). [10 Usability Heuristics for User Interface Design](https://www.nngroup.com/articles/ten-usability-heuristics/). Nielsen Norman Group.
- Nielsen, J. (1994). [Severity Ratings for Usability Problems](https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/). Nielsen Norman Group.
- W3C. (2023). [Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/).
- Hertzum, M. (2006). Problem prioritization in usability evaluation. *International Journal of Human-Computer Interaction*, 21(2), 125–146.
- MeasuringU. (2013). [Rating the Severity of Usability Problems](https://measuringu.com/rating-severity/).
- CorsoUX. (2026). [UX Audit Checklist: 50 Points](https://courseux.com/ux-audit-checklist/).
- Dakan, R., Feller, J., & Anthropic. (2025). [6 Techniques for Effective Prompt Engineering](https://www-cdn.anthropic.com/62df988c101af71291b06843b63d39bbd600bed8.pdf). CC BY-NC-SA 4.0.
- Li, X., et al. (2024). [An Empirical Analysis of Issue Templates Usage in Large-Scale Projects on GitHub](https://dl.acm.org/doi/10.1145/3643673). ACM Transactions on Software Engineering and Methodology.
- Sayagh, M., et al. (2025). [What Makes a GitHub Issue Ready for Copilot?](https://arxiv.org/pdf/2512.21426) arXiv preprint.
- GitHub. (2025). [Best Practices for Using GitHub Copilot to Work on Tasks](https://docs.github.com/en/copilot/tutorials/cloud-agent/get-the-best-results). GitHub Docs.
- Eisenstein, J., et al. (2024). [LLM-Rubric: A Multidimensional, Calibrated Approach to Automated Evaluation of Natural Language Texts](https://aclanthology.org/2024.acl-long.745.pdf). Proceedings of ACL 2024.
- ReliablePenguin. (2025). [What Is a Runbook? History, Template, and Best Practices](https://blogs.reliablepenguin.com/2025/10/29/what-is-a-runbook-history-template-and-best-practices).
- Atlassian. (2025). [What is Acceptance Criteria?](https://www.atlassian.com/work-management/project-management/acceptance-criteria)

---

## Contributing

See `CONTRIBUTING.md` for guidelines. Contributions that include evidence, citations, or calibrated examples are strongly preferred over opinion-based additions.

---

## License

MIT. See `LICENSE`.
