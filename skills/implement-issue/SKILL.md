---
name: implement-issue
description: Set up a feature branch for a GitHub issue with quality gate and full context. Use when starting work on an issue.
argument-hint: <issue-number>
allowed-tools: Read, Grep, Glob, Bash(git:*), Bash(gh:*)
---

# Implement Issue

Set up a working branch for a GitHub issue, evaluate the issue quality against the
implementation plan rubric, and gather implementation context.

## Step 0: Session hygiene

Run the following checks and present a report before proceeding:

```
git status
git stash list
git branch -vv
gh pr list --state open --author "@me"
```

Check for:
- Uncommitted changes on the current branch
- Stale stashes that may contain relevant work
- Local branches with no remote tracking
- Open PRs awaiting review

If any finding is **blocking** (uncommitted changes on a branch tied to another issue,
open PR awaiting review that the user may have forgotten), **STOP and surface it
explicitly** before proceeding. Ask whether to continue.

If findings are advisory only (stale remote branches, old stashes), note them and proceed.

## Step 1: Resolve the issue

If `$ARGUMENTS` is provided, use it as the issue number.
If not, list open issues and ask the user to pick one:
```
gh issue list --state open --limit 30
```
**WAIT** for the user's response before proceeding.

## Step 2: Fetch issue context

Fetch the issue details including body and recent comments:
```
gh issue view <number> --json title,body,labels,milestone,comments
```

Extract and hold internally (do not present yet):
- Full issue body
- Title and labels
- Last 10 comments — note any design decisions, scope changes, or constraints added
  after the original issue was written
- Linked PRs or related issues mentioned in body or comments

## Step 3: Evaluate issue quality

Read `${CLAUDE_SKILL_DIR}/issue-rubric.md` before scoring. It is the single source of truth for the
section weights, per-section scoring criteria, the weighted formula, severity findings, and
the agent readiness check. Apply it exactly: score each section 0-10, calculate the weighted
overall score, identify severity findings, run the agent readiness check (it does not change
the score), and decide whether to proceed or trigger the soft gate.

If the file cannot be read, stop and tell the user the skill is installed incompletely:
the whole `implement-issue` folder, including `issue-rubric.md`, must be copied.

### Decision after scoring

**If overall_score >= 7.0:**
Present a compact quality note in the Step 6 brief and proceed to Step 4. Format:
```
Issue quality: <score>/10 — <one-line assessment>
Gaps noted: <severity findings if any, or "None">
Agent readiness: <verdict> — <checks that are not Pass or N/A, or "None">
```

**If overall_score < 7.0:**
Stop. Do not proceed to branch setup. Present the full evaluation:

```
## Issue quality gate: <score>/10

This issue does not meet the 7.0 threshold for safe implementation.
Proceeding risks Claude Code making unsafe assumptions in the gaps below.

**Section scores:**
<section> | <score>/10 | <level> | <one-sentence note>
...

**Severity findings:**
Sev <N> | <section> | <description>
...

**Rewritten issue:**
<complete rewritten issue using the eight-section structure, filled with all
available context from the original body, comments, and linked issues. Close agent
readiness gaps inside the existing sections: Out of scope under Context, Environment
and Agent boundaries under Prerequisites, Done when under Testing / Verification>
```

Then ask:
"This rewrite addresses the gaps above. Approve it and I will update the GitHub issue
before creating the branch — or paste your edits and I will apply them."

**WAIT** for explicit approval before proceeding.

On approval:
```
gh issue edit <number> --body "<approved body>"
```

Then proceed to Step 4.

## Step 4: Read project conventions

Read whichever of these repo instruction files exist: `CLAUDE.md`, `AGENTS.md`,
`.github/copilot-instructions.md`. Use them to establish:
- Branch naming convention for this project
- Architecture overview relevant to the issue
- Any workflow rules that affect implementation
- Setup, build, test, lint, and typecheck commands (these close readiness check R2 and
  supply the done-when commands for the brief if the issue has none)

Use the branch naming convention from these files in Step 5. If none of these files specifies
a branch naming convention, fall back to `feature/<number>-<slugified-title>` (lowercase,
hyphens, max 40 chars for slug).

## Step 5: Branch setup

1. Detect the default branch and ensure it is up to date:
```
git remote show origin | grep 'HEAD branch' | awk '{print $NF}'
```
Then:
```
git checkout <default-branch> && git pull origin <default-branch>
```

2. Generate branch name using the convention from Step 4.

3. Check if branch already exists:
```
git branch --list '<prefix>/<number>-*'
git ls-remote --heads origin '<prefix>/<number>-*'
```

4. If exists: `git checkout <branch>` (and pull if remote tracking exists)
5. If new: `git checkout -b <branch>`

## Step 6: Summary

Present the full brief:

```
## Ready to implement #<number>: <title>

**Branch**: `<branch>`
**Labels**: <labels>
**Issue quality**: <score>/10 — <one-line assessment>

**Key requirements**:
<2-4 bullet points from issue body — acceptance criteria and constraints>

**Context from comments**:
<notable decisions, scope changes, or constraints added after the original issue>

**Done when**:
<runnable commands and expected results, from the issue or the repo instruction files;
mark any you proposed yourself as "proposed">

**Out of scope**:
<non-goals from the issue, or "Not stated. Proposed:" followed by your proposal>

**Human-only steps and boundaries**:
<steps you will not perform yourself (production data, secrets, deploys, dashboard
actions) and where you will stop and hand over, or "None">

**Suggested approach**:
<brief suggestion grounded in the issue content and the repo instruction files only>
```

Then ask: "Ready to start, or do you want to discuss the approach first?" If any proposed
done-when commands, out-of-scope items, or boundaries appear above, ask the user to
confirm them in the same question.
