# Contributing

Contributions are welcome. This toolkit was built on a principle of evidence over opinion — please bring the same standard to any additions or changes.

---

## What makes a good contribution

**Preferred:**
- Changes backed by citations from established UX, accessibility, or prompting research
- New prompt calibration examples with full scoring rationale across all four PPEP dimensions
- New issue calibration anchors with full section scoring rationale across all eight sections and formula-verified scores
- Corrections with evidence showing why the current version is wrong
- New prompt templates that have been tested and iterated on, not first drafts
- Translations of the framework or prompts into other languages
- New Claude Code skills following the format and quality standards described below

**Discouraged:**
- Opinion-based additions without evidence ("I think this would work better")
- Untested prompt templates added without real-world validation
- Changes to calibration anchor scores without a detailed scoring rationale

---

## How to contribute

1. Fork the repository
2. Create a branch named after what you are adding or fixing
3. Make your changes
4. In your pull request description, explain what you changed and why, including any sources or evidence
5. Submit the pull request

---

## Contributing a Claude Code skill

Skills live in `skills/<skill-name>/SKILL.md`. Each skill must follow this structure:

**Frontmatter (required):**
```
---
name: <skill-name>
description: <one sentence describing what it does and when to invoke it>
argument-hint: <what arguments it accepts, if any>
allowed-tools: <comma-separated list of permitted tools>
---
```

**Quality standards for skills:**
- Skills must be project-agnostic — no hardcoded repo names, branch names, or project-specific tooling
- Every step must have a clear action and an explicit outcome
- Human checkpoints must use `**WAIT**` so Claude Code pauses for input rather than proceeding autonomously
- Conditional logic (if score < threshold, stop; if branch exists, checkout) must be explicit, not inferred
- Failure modes must be handled — every step that can fail must have an instruction for what to do when it does

**Before submitting a skill:**
- Test it in at least one real Claude Code session against a real repo
- Confirm correct behaviour at both the happy path and at least one failure case
- Describe the test in your pull request

---

## Reporting issues

If you find a scoring inconsistency, a claim that is not supported by evidence, or a prompt that does not behave as documented, open an issue with as much detail as possible including the AI model you tested with, the prompt you used, and the output you received.

---

## Code of conduct

Be direct, be evidence-based, and be respectful of the work others have put in.
