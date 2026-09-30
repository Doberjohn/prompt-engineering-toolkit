<!-- Generated from rubric/issue-rubric.md in the Prompt Engineering Toolkit. Edit the source and run scripts/sync-issue-rubric.py. -->

# Implementation Plan Issue Rubric

## EVALUATION FRAMEWORK

Implementation plan issues are evaluated across eight sections. Not all sections carry equal weight.

### Section weights (derived from Nielsen severity scale)

| Section | Weight | Severity if absent |
|---|---|---|
| Implementation Steps | 4 | Critical — without steps the issue is not a runbook |
| Acceptance Criteria | 4 | Critical — without this there is no definition of done |
| Rollback | 4 | Critical — without this a production process is dangerous |
| Context | 3 | Important — without this future developers cannot understand why |
| Prerequisites | 3 | Important — without this the process cannot be safely started |
| Testing / Verification | 3 | Important — without this there is no way to confirm success |
| Files Affected | 2 | Supporting — steps partially compensate |
| References | 2 | Supporting — content partially compensates |

---

### Scoring criteria per section

Score each section 0-10. A section that does not exist scores 0.

**Implementation Steps**
- Strong (8-10): Numbered imperative steps. Code block for every command, file path, or SQL statement. Expected output per step. Verification instruction per step. Logically ordered.
- Acceptable (5-7): Numbered and ordered but missing one or more of: code blocks, expected output, or per-step verification. Followable with moderate inference.
- Poor (1-4): Prose bullets or high-level descriptions with no commands, no expected output, no verification. Cannot be followed safely without prior knowledge.
- Absent (0): Section does not exist.

**Acceptance Criteria**
- Strong (8-10): Checkboxes. Outcome-oriented and pass/fail verifiable. No implementation details. Covers all primary success conditions including explicit constraints from the issue context.
- Acceptable (5-7): Checkboxes present but one or more criteria are vague, implementation-focused, or a primary constraint is missing.
- Poor (1-4): Prose statements. No checkboxes. No pass/fail structure. Not independently testable.
- Absent (0): Section does not exist.

**Rollback**
- Strong (8-10): Separate rollback instruction per track or phase. Each instruction names the exact command, file, or dashboard action. Covers partial and full rollback.
- Acceptable (5-7): Present but covers only one track when multiple exist, or partially specific.
- Poor (1-4): Single vague sentence such as "revert all changes." Provides false confidence with no actionable guidance. When the plan includes irreversible or out-of-repository operations, this is worse than absent — flag it explicitly as a severity 4 finding.
- Absent (0): Section does not exist.
- Code-only changes: when the change touches only code, has a single track, and is delivered as one pull request (no migrations, data changes, infrastructure, or dashboard actions), naming the revert of that PR plus a check that confirms the revert worked scores Strong. Multi-track plans still need a rollback per track, because one PR revert cannot undo a single track on its own. The vague-rollback severity 4 rule applies to issues that include irreversible or out-of-repo operations.

**Context**
- Strong (8-10): States why the process exists. States when to trigger it with specific conditions. States what outcome the process achieves.
- Acceptable (5-7): Covers why and when but one element is missing or vague.
- Poor (1-4): Single sentence or vague paragraph. No trigger conditions and no motivation stated.
- Absent (0): Section does not exist.

**Prerequisites**
- Strong (8-10): Checkboxes covering required access (specific roles named), required tools (specific tool names), required knowledge. Nothing left to assumption.
- Acceptable (5-7): Checkboxes present but one category is missing or items are vague.
- Poor (1-4): General statement without checkboxes and without specific named requirements.
- Absent (0): Section does not exist.

**Testing / Verification**
- Strong (8-10): Pass/fail checkboxes grouped by track or phase. Observable, objective outcomes. Covers success and failure scenarios.
- Acceptable (5-7): Checkboxes present but one or more use subjective language or a major track is missing.
- Poor (1-4): Single vague sentence or general instruction with no checkboxes and no observable outcomes.
- Absent (0): Section does not exist.

**Files Affected**
- Strong (8-10): Split into Created and Modified. Each entry has an exact file path and a purpose statement.
- Acceptable (5-7): Files listed but paths partial, purpose statements absent, or Created/Modified split not made.
- Poor (1-4): Component names or directory names without file paths.
- Absent (0): Section does not exist.
- Note: coding agents can search a codebase, so exact paths mainly save exploration time and reduce the chance of editing the wrong file. This is why the section carries supporting weight.

**References**
- Strong (8-10): Links to related issues or PRs and specific internal files, plus official documentation for any external system the executor cannot learn from the repository. All links specific.
- Acceptable (5-7): Present but incomplete — some links too general or key documentation missing.
- Do not reward link volume. Prefer in-repository artifacts over external links; an issue that depends on many external sources is harder for an agent to execute.
- Poor (1-4): One or two vague links that do not materially help an executor.
- Absent (0): Section does not exist.

---

## SCORING FORMULA

```
overall_score = max(
  (
    (Implementation Steps × 4) +
    (Acceptance Criteria  × 4) +
    (Rollback             × 4) +
    (Context              × 3) +
    (Prerequisites        × 3) +
    (Testing/Verification × 3) +
    (Files Affected       × 2) +
    (References           × 2)
  ) / 25,
  0.5
)
```

Round to two decimal places. The 0.5 floor applies whenever the weighted score falls below 0.5.

---

## AGENT READINESS CHECK

The section score measures whether the plan is complete. It does not measure whether an AI coding agent can execute it safely without a human filling gaps. Run this check separately on every issue. It does not change the section scores or the overall score.

Rate each check Pass, Partial, or Fail (or N/A where stated), with a one-line note citing where in the issue the evidence is or is not.

| # | Check | Pass means |
|---|---|---|
| R1 | Executable done-when | At least one command the agent can run (tests, build, lint, typecheck, or a script) with its expected result, covering the primary acceptance criteria. Manual-only checks are Partial at best. |
| R2 | Environment and instructions | Setup, build, and test commands are stated, or the issue points to a repo instruction file that holds them (CLAUDE.md, AGENTS.md, `.github/copilot-instructions.md`). |
| R3 | Out of scope | Explicit non-goals: what the agent must not change or add, even if it seems related. |
| R4 | Boundaries | What the agent must not do without a human: production data, secrets, deploys, migrations against shared environments, dashboard actions. N/A only if the issue touches none of these. |
| R5 | Human-only steps marked | Steps that need access or judgment the agent lacks (dashboards, credentials, approvals) are labelled as human steps. N/A if there are none. |
| R6 | Scoped for one change | The work is one coherent change that fits a single reviewable PR, or the issue says how to split it. |

**Readiness verdict:**
- **Ready to delegate:** overall_score >= 7.0 and every check is Pass or N/A.
- **Delegate with supervision:** overall_score >= 7.0, and R1 and R4 are not Fail. A human performs the human-only steps and reviews the PR.
- **Not ready to delegate:** overall_score < 7.0, or R1 is Fail, or R4 is Fail.

Why these checks: current guidance for coding agents converges on a runnable check the agent can use to prove it is done, stated scope and non-goals, and repository instructions for setup and testing. Well-scoped, shorter issues are also associated with more merged agent PRs. Sources are listed in `examples/issue-calibration-set.md` in the Prompt Engineering Toolkit repository.

---

## SEVERITY FINDINGS

In addition to section scores, identify severity findings using Nielsen's severity scale:
- Severity 4 — Catastrophic: blocks safe execution or creates production risk
- Severity 3 — Major: causes significant confusion or requires unsafe inference
- Severity 2 — Minor: causes inconvenience but does not block execution
- Severity 1 — Cosmetic: does not affect execution

Report frequency separately from severity: Always / Frequent / Occasional / Rare.

Key severity 4 cases:
- Rollback present but single vague sentence, on a plan with irreversible or out-of-repository operations — false confidence, no actionable guidance
- Acceptance Criteria written as prose — no definition of done
- Implementation Steps as bullets without commands — cannot be followed
