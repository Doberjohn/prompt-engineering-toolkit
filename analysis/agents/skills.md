# Agent report: skills

## Executive summary

The two Claude Code skills are the strongest-engineered prompt artifacts in the repo: valid frontmatter per the current (Aug 2026) official spec, disciplined step/gate structure, and rubric weights/formula that exactly match the issue-evaluator. Critically, I empirically tested the README's contested install path (".claude/commands/draft-issue/SKILL.md") on Claude Code v2.1.228 in a sandbox: /draft-issue and /implement-issue DO resolve and load the skill content (and /SKILL does not), so the documented install works today — but it is an undocumented legacy layout that the official docs' own command-naming table would predict to fail, and the canonical location is .claude/skills/. The real defects are elsewhere: implement-issue lacks the evaluator's out-of-scope guard and collapses its three-tier output policy into two tiers (mandating a "complete rewrite" even below 2.0, where the evaluator says rewrites are meaningless — then writing it back to GitHub); both side-effectful skills omit disable-model-invocation and pre-approve overly broad Bash(git:*)/Bash(gh:*) grants; and despite the toolkit's "calibrated, validated" thesis, the skills ship with zero evaluations, contradicting the official best-practices checklist ("At least three evaluations created"). "Close the write → evaluate → implement loop end to end" overstates: implement-issue stops at branch setup and a brief; it never implements, tests, or PRs.

## Strengths (with evidence)

- **The README-documented install path actually works on current Claude Code (v2.1.228, Aug 2026) — empirically verified, not assumed: /draft-issue and /implement-issue resolve and load real skill content from .claude/commands/<name>/SKILL.md (project) and ~/.claude/commands/<name>/SKILL.md (global).**
  - Evidence: Sandbox test: `claude -p '/draft-issue'` returned skill-specific behavior ('pulling the problem, agreed approach, constraints, and scope from a preceding discussion'); `claude -p '/totally-nonexistent-xyz'` returned 'Unknown command'; `claude -p '/SKILL'` returned 'Unknown command: /SKILL'; `/implement-issue` executed Step 0 hygiene (git status etc.) and correctly halted on missing gh. Global probe: ~/.claude/commands/audit-probe-xyz/SKILL.md → '/audit-probe-xyz' returned the planted token PROBE-LOADED-91544.
- **All four frontmatter fields used (name, description, argument-hint, allowed-tools) are valid per the current official Claude Code skills spec, and skill names comply with naming rules (lowercase/hyphens, ≤64 chars, action-oriented form is an 'acceptable alternative' per official best practices).**
  - Evidence: skills/draft-issue/SKILL.md:1-6 and skills/implement-issue/SKILL.md:1-6 vs. code.claude.com/docs/en/skills frontmatter reference table (name, description, argument-hint, allowed-tools all listed; 'All fields are optional. Only `description` is recommended') and platform.claude.com best-practices ('Acceptable alternatives: ... Action-oriented: `process-pdfs`').
- **Descriptions follow the official 'what it does + when to use it' convention, closely matching the docs' own examples.**
  - Evidence: draft-issue SKILL.md:3 'Draft, evaluate, and publish a GitHub implementation plan issue from the current conversation context. Use when you have agreed on scope...' mirrors the official example pattern 'Extract text and tables from PDF files... Use when working with PDF files...' (platform.claude.com best-practices, 'Writing effective descriptions').
- **Rubric weights, scoring formula, floor, severity scale, and the three severity-4 triggers in implement-issue are character-for-character consistent with prompts/issue-evaluator.md — genuine cross-file coherence on the load-bearing numbers.**
  - Evidence: implement-issue SKILL.md:71-80 (weights 4/4/4/3/3/3/2/2) and 134-147 (formula /25, max(...,0.5)) match issue-evaluator.md:28-37 and 98-110 exactly; severity definitions SKILL.md:155-158 match evaluator:120-123; the three severity-4 triggers SKILL.md:161-163 match evaluator:128-130. Arithmetic checks: 4+4+4+3+3+3+2+2=25; max = 10×25/25 = 10.
- **The interaction design is genuinely above community average: explicit WAIT gates before every irreversible action, a bounded clarifying-questions protocol (max 3, with criteria for when asking is allowed), deterministic output templates, and a cross-skill quality-gate handoff.**
  - Evidence: draft-issue SKILL.md:41 ('Maximum 3 questions'), :54 ('**WAIT** for answers'), :232 ('**WAIT** for the user's response'), :244-249 (sub-7.0 publish warning explicitly referencing 'The quality gate in `implement-issue`'); implement-issue SKILL.md:200 ('**WAIT** for explicit approval before proceeding').
- **draft-issue's 'reads context from the conversation' is architecturally sound, not hand-wavy: as an inline (non-forked) skill its content is injected into the live conversation, so the history is genuinely in context; the authors correctly did not use context:fork, which would have broken it.**
  - Evidence: code.claude.com/docs/en/skills: 'When you or Claude invoke a skill, the rendered SKILL.md content enters the conversation as a single message' and (for fork) 'It won't have access to your conversation history.' draft-issue SKILL.md:14-16 relies on exactly this.
- **implement-issue has thoughtful deterministic fallbacks: default-branch detection instead of hardcoding main, and a specified branch-name fallback when CLAUDE.md lacks a convention.**
  - Evidence: SKILL.md:224 (`git remote show origin | grep 'HEAD branch' | awk '{print $NF}'`) and :216-218 ('fall back to `feature/<number>-<slugified-title>` (lowercase, hyphens, max 40 chars for slug)').
- **Both files respect the official size guidance and the allowed-tools syntax works in practice (git commands executed without permission prompts in headless mode).**
  - Evidence: wc -l: 266 and 263 lines vs. docs 'Keep `SKILL.md` under 500 lines'; sandbox /implement-issue run executed git status/branch checks under `allowed-tools: ... Bash(git:*), Bash(gh:*)` (SKILL.md:5) with no prompt.

## Findings

- **[MAJOR] [install-docs]** README installs the skills into the legacy, undocumented `.claude/commands/<name>/SKILL.md` layout instead of the canonical `.claude/skills/<name>/SKILL.md`; it works on current Claude Code only by grace of undocumented loader behavior that the official docs' own command-naming table predicts should fail (filename → /SKILL).
  - Evidence: README.md:148,156 ('copy `skills/draft-issue/SKILL.md` to `.claude/commands/draft-issue/SKILL.md`'). Official docs (code.claude.com/docs/en/skills): skills live at '`.claude/skills/<skill-name>/SKILL.md`' / '`~/.claude/skills/<skill-name>/SKILL.md`'; the command-name table says for 'File under `.claude/commands/`' the name comes from 'File name without extension' (SKILL.md → /SKILL); the `commands/<dir>/SKILL.md` layout appears nowhere in the docs; docs add 'New commands should usually be skills instead; commands remain supported' (code.claude.com/docs/en/claude-directory). Empirical: works today on v2.1.228 (see strengths), but /SKILL returning 'Unknown command' proves the behavior is special-cased, not the documented rule.
  - Confidence: high that the path is non-canonical and undocumented (direct doc quotes + test); medium that it could regress — I cannot verify Anthropic's compatibility guarantees for undocumented layouts, and I could not test April-2026-era Claude Code versions.
- **[MAJOR] [cross-file-consistency]** implement-issue lacks the issue-evaluator's out-of-scope guard: it applies the implementation-plan rubric to ANY issue number, so running /implement-issue on a bug report or feature request scores it low and then offers to rewrite it as a runbook and push that back to GitHub via `gh issue edit`.
  - Evidence: issue-evaluator.md:18 ('If you receive a bug report, feature request, or question, tell me it is out of scope and explain which type it appears to be') and :7-8 ('Scoped to implementation plan issues only. For other issue types... a different rubric is required'). implement-issue SKILL.md:59-207 contains no issue-type check; Step 3 evaluates whatever Step 2 fetched, and :202-204 writes the approved rewrite back with `gh issue edit <number> --body`.
  - Confidence: high — the guard is verbatim in the evaluator and verbatim absent from the skill; failure scenario follows directly from the instructions as written.
- **[MAJOR] [cross-file-consistency]** implement-issue collapses the evaluator's three-tier output policy into two tiers: any score <7.0 triggers a 'complete rewritten issue', including scores <2.0 where the toolkit's own evaluator mandates a placeholder template because context is insufficient for a meaningful rewrite — so the skill instructs Claude to fabricate runbook content (commands, rollback steps, file paths) from a near-empty issue and then update GitHub with it.
  - Evidence: issue-evaluator.md:155-159 ('If overall_score >= 7.0 — Improvement suggestions... If overall_score < 7.0 AND overall_score >= 2.0 — Revised issue... If overall_score < 2.0 — Template: Produce a structured template with [PLACEHOLDER] notation... Clearly label it as a starting template, not a verified runbook') vs implement-issue SKILL.md:174-194 ('If overall_score < 7.0: ... **Rewritten issue:** <complete rewritten issue using the eight-section structure, filled with all available context...>') with no <2.0 branch; write-back at :202-204.
  - Confidence: high — direct quote comparison; both files are in-repo.
- **[MAJOR] [safety-config]** Neither skill sets `disable-model-invocation: true`, so Claude can auto-trigger these side-effectful workflows (branch checkout/pull, GitHub issue creation/editing) whenever their descriptions match the conversation — exactly the case the official docs say to flag, and both descriptions ('Use when starting work on an issue') actively invite auto-invocation.
  - Evidence: skills/draft-issue/SKILL.md:1-6 and skills/implement-issue/SKILL.md:1-6 have no disable-model-invocation field. Official docs (code.claude.com/docs/en/skills): '`disable-model-invocation: true`: Only you can invoke the skill. Use this for workflows with side effects or that you want to control timing, like `/commit`, `/deploy`... You don't want Claude deciding to deploy because your code looks ready.' implement-issue Step 5 runs `git checkout <default-branch> && git pull` (SKILL.md:228) before any user-approval gate.
  - Confidence: high on the deviation (doc quote vs file); medium on real-world frequency of spurious auto-invocation, which I did not measure.
- **[MAJOR] [test-coverage]** The skills ship with zero evaluations or recorded testing, directly failing the official skill-authoring checklist ('At least three evaluations created') — a pointed contradiction for a toolkit whose core pitch is 'validated through iteration' and calibrated measurement, and in an ecosystem where Anthropic's skill-creator plugin automates exactly this (evals.json, benchmark.json, with/without-skill comparison).
  - Evidence: Repo listing: skills/draft-issue/ and skills/implement-issue/ contain only SKILL.md (ls output; no evals/ anywhere). platform.claude.com best-practices checklist: 'Testing: [ ] At least three evaluations created; [ ] Tested with Haiku, Sonnet, and Opus'. code.claude.com/docs/en/skills documents `/plugin install skill-creator@claude-plugins-official` storing 'prompts, input files, and expected behavior in `evals/evals.json` inside the skill directory'. README.md:33 claims the toolkit was 'Validated through iteration — prompts were evaluated, scored, revised, and rescored'.
  - Confidence: high — absence verified by directory listing; the validation claim at README.md:33 covers the prompts generally and no skill-specific validation artifact exists anywhere in the repo.
- **[MINOR] [overclaim]** README's 'close the write → evaluate → implement loop end to end' overstates: implement-issue never implements — it stops at branch setup plus a brief and asks 'Ready to start, or do you want to discuss the approach first?'; there is no implementation, testing, PR, or feedback leg, and the skill name itself ('implement-issue') oversells what is really issue-triage-and-branch-setup.
  - Evidence: README.md:80 ('close the write → evaluate → implement loop end to end') vs implement-issue SKILL.md:242-263 (final step is presenting a brief and asking the question); no step after Step 6 exists.
  - Confidence: high — the file simply ends there.
- **[MINOR] [overclaim]** 'Project-agnostic' (README.md:80) is true mechanically but false editorially: the embedded rubric hard-codes an ops/runbook ideology (Rollback weighted 4 as 'production process is dangerous without it', per-step commands/SQL, dashboard actions), so in projects whose issues are ordinary feature work, the 7.0 gate plus rewrite machinery pushes every issue toward runbook form; also the remote name 'origin' is hardcoded.
  - Evidence: implement-issue SKILL.md:76 ('Rollback | 4 | Yes — production process is dangerous without it'), :224,228,236 (hardcoded 'origin'); math: an otherwise-perfect issue with no Rollback section scores (250-40)/25 = 8.4 so it passes the gate, but any rewrite triggered must include Rollback/Prerequisites/Testing per the eight-section structure (SKILL.md:191-193).
  - Confidence: high on the textual evidence; the practical impact assessment is judgment.
- **[MINOR] [cross-file-consistency]** Rubric drift #1: implement-issue drops the evaluator's frequency dimension (Always/Frequent/Occasional/Rare) from severity findings, so the two tools report findings in different formats despite claiming the same rubric.
  - Evidence: issue-evaluator.md:125 ('Report frequency separately from severity: Always / Frequent / Occasional / Rare') has no counterpart in implement-issue SKILL.md:153-163.
  - Confidence: high.
- **[MINOR] [cross-file-consistency]** Rubric drift #2: draft-issue scores its own draft per-section out of 10 with Strong/Acceptable/Poor/Absent labels but never defines the numeric bands (Strong 8-10, Acceptable 5-7, Poor 1-4, Absent 0) that implement-issue and the evaluator define — so the score the drafting skill reports and the score the implementing skill's gate recomputes rest on different specifications, undermining the 7.0-gate handoff the two skills advertise; draft-issue also adds novel criteria absent from the evaluator (e.g. Prerequisites 'executor can confirm readiness in under two minutes').
  - Evidence: draft-issue SKILL.md:209-218 (scorecard asks for '<n>/10' and 'Strong/Acceptable/Poor/Absent' with no band definitions; the bands appear only in implement-issue SKILL.md:84-130 and issue-evaluator.md:45-91); draft-issue SKILL.md:80 ('Strong: executor can confirm readiness in under two minutes') has no equivalent in issue-evaluator.md:70.
  - Confidence: high on the textual gap; medium on practical score divergence (untested).
- **[MINOR] [robustness]** The publish/edit commands model fragile shell quoting: `gh issue create --title "<title>" --body "<approved body>"` inlines a full multi-line markdown body containing backticks, code fences, and double quotes into one double-quoted argument; a body with a double quote or command substitution breaks or injects. The robust documented gh pattern is --body-file.
  - Evidence: draft-issue SKILL.md:255-257 and implement-issue SKILL.md:202-204. Every issue the skill drafts is guaranteed to contain fenced code blocks and quotes by its own template (draft-issue SKILL.md:92-108).
  - Confidence: high on the fragility as written; medium on real-world failure rate since Claude typically improvises heredocs/temp files when the literal command fails.
- **[MINOR] [robustness]** No dependency or failure handling exists in the skill text: no gh-installed/gh-auth check, no GitHub-remote check, network-dependent default-branch detection, and no instruction for a missing CLAUDE.md (only for a CLAUDE.md missing the branch convention) — the graceful degradation I observed in testing came from the model, not from the instructions.
  - Evidence: implement-issue SKILL.md:13-58 and 209-241 contain no `gh auth status`, no remote existence check; :224 uses network-calling `git remote show origin`; :209-215 says 'Read `CLAUDE.md`' unconditionally. Sandbox run of /implement-issue in a repo with no gh and no remote: Claude itself halted and reported cleanly — competence, not spec.
  - Confidence: high on absence (grep-verified); the observed graceful behavior is one data point on one model.
- **[NITPICK] [dead-config]** implement-issue pre-approves Grep and Glob in allowed-tools but no step ever instructs their use, and Step 6 restricts the suggested approach to 'the issue content and CLAUDE.md architecture only' — the granted tools are dead weight and the 'gather implementation context' promise never touches the codebase.
  - Evidence: SKILL.md:5 ('allowed-tools: Read, Grep, Glob, ...') vs. grep for Grep/Glob in the body: only line 5; SKILL.md:260 ('grounded in the issue content and CLAUDE.md architecture only').
  - Confidence: high.
- **[MINOR] [security]** allowed-tools grants are over-broad for the stated tasks: Bash(gh:*) pre-approves every gh subcommand (gh repo delete, gh api, gh pr merge) and Bash(git:*) every git subcommand (push --force, reset --hard) without prompting during the invoking turn; least-privilege scoping (e.g. Bash(gh issue:*), Bash(git status:*)) was available.
  - Evidence: draft-issue SKILL.md:5, implement-issue SKILL.md:5. Docs warn: 'Review project skills before trusting a repository, since a skill can grant itself broad tool access' (code.claude.com/docs/en/skills, Pre-approve tools for a skill).
  - Confidence: high on breadth; mitigating: the grant is turn-scoped per docs ('The grant clears when you send your next message').
- **[NITPICK] [spec-semantics]** $ARGUMENTS is written as a runtime variable to test ('If `$ARGUMENTS` is provided, use it as the issue number') but per spec it is substituted before Claude sees the content, rendering as 'If `123` is provided...' — works in practice (verified) but is semantically sloppy against the documented substitution model.
  - Evidence: draft-issue SKILL.md:29, implement-issue SKILL.md:38 vs docs: '`$ARGUMENTS` — All arguments passed when invoking the skill. If `$ARGUMENTS` is not present in the content, arguments are appended as `ARGUMENTS: <value>`' (code.claude.com/docs/en/skills). Sandbox run with no arguments proceeded correctly.
  - Confidence: high.
- **[NITPICK] [portability]** The argument-hint field is a Claude Code-only extension excluded from the Agent Skills open standard; uploading these skills to claude.ai/Skills API (including personal-skill sync for Cowork/cloud sessions) fails with a hard error — the docs' own example error message literally names this field. README's 'Claude Code only' framing makes this fair, but the skills are one line away from spec compliance.
  - Evidence: Docs: allowed fields outside Claude Code are 'name, description, license, compatibility, metadata, allowed-tools' and the example error is 'Unexpected key(s) in SKILL.md frontmatter: argument-hint' (code.claude.com/docs/en/skills, Using skill frontmatter outside Claude Code). README.md:115 already disclaims chat interfaces.
  - Confidence: high.
- **[NITPICK] [formatting]** draft-issue's scoring formula block lost its indentation (flush-left) relative to the identically-defined formula in implement-issue and the evaluator — cosmetic copy drift that hints the three rubric copies are maintained by hand.
  - Evidence: draft-issue SKILL.md:183-195 (unindented) vs implement-issue SKILL.md:135-147 and issue-evaluator.md:98-110 (indented).
  - Confidence: high.
- **[MINOR] [distribution]** In the Aug 2026 ecosystem, manual file-copy install is a generation behind: the standard distribution paths are committing .claude/skills/ to the repo, or shipping a plugin installable via the marketplace system; the repo's skills/ directory has no .claude-plugin/plugin.json and no marketplace manifest, so users cannot `/plugin install` it.
  - Evidence: Docs 'Share skills': 'Project skills: Commit `.claude/skills/` to version control; Plugins: Create a `skills/` directory in your plugin' (code.claude.com/docs/en/skills); ecosystem scale per search: official claude-plugins-official marketplace ~256 entries, community aggregators (tonsofskills.com: 2,800+ skills), Agent Skills standard at agentskills.io published Dec 2025 and adopted by Microsoft, OpenAI, Cursor, GitHub (simonwillison.net/2025/Dec/19/agent-skills/, github.com/anthropics/skills). Repo: skills/ contains only two SKILL.md files (ls -R).
  - Confidence: medium-high — ecosystem numbers come from search-result summaries of third-party sources I did not individually fetch; the absence of plugin manifests in-repo is verified.

## Open questions

- Did the .claude/commands/<dir>/SKILL.md layout already work on Claude Code versions current in April 2026 (when README was committed), or did the unified loader make it work later? I verified v2.1.228 (Aug 2026) only; historical CLI versions were not testable in the sandbox.
- Cross-cutting for the evaluator-lane agent: issue-evaluator.md:113 claims 'The floor of 0.5 applies only when all sections are entirely absent' — mathematically false (e.g. References=1, all else 0 gives 2/25 = 0.08 → floored to 0.5); the same max(...,0.5) formula is copied into both skills without the (incorrect) explanatory claim.
- Cross-cutting for the README-lane agent: README.md:82 'invoke at the end of any Claude Code session where scope has been agreed' understates a real failure mode — after auto-compaction the conversation draft-issue 'reads' is a summary, and the skill's 'Do not ask the user to repeat themselves' (SKILL.md:17) then works against it.
- For the owner to prepare: why maintain three hand-synced copies of the rubric (evaluator, implement-issue full, draft-issue abbreviated) instead of one canonical source — and is the visible drift (frequency dimension, tier policy, score bands, formula indentation) acknowledged?
- Sharp-interviewer questions this audit would ask: (1) Why .claude/commands/ in April 2026, six months after .claude/skills/ became canonical — and can you defend it working? (2) Your toolkit's thesis is measurement — where are the skill evals, given skill-creator automates exactly that? (3) Why does implement-issue mandate a full rewrite below 2.0 when your own evaluator says that produces a fake runbook? (4) What happens when /implement-issue is pointed at a bug report? (5) Why are side-effectful skills model-invocable with blanket Bash(git:*)/Bash(gh:*) grants? (6) Does `gh issue create --body "..."` survive a body full of backticks and quotes? (7) 'End to end' — where is the implement leg? (8) Why not ship as a plugin?

---

## Full report

# Audit: Claude Code Skills (`skills/draft-issue/SKILL.md`, `skills/implement-issue/SKILL.md`) + README §§79-84, 141-156

**Auditor lane:** the two Claude Code skills and the README's description/install instructions for them.
**Method:** full file reads; cross-check against the *current* official docs fetched live (code.claude.com/docs/en/skills, code.claude.com/docs/en/claude-directory, platform.claude.com skill-authoring best practices); **empirical install-path testing with the actual Claude Code CLI v2.1.228** available in the audit sandbox; web search of the Aug 2026 skills ecosystem.

---

## 1. Verdict on the headline question: does the documented install path work at all?

**Yes — verified empirically — but it relies on undocumented legacy behavior, and the canonical path is different.**

README.md:148: *"Install: copy `skills/draft-issue/SKILL.md` to `.claude/commands/draft-issue/SKILL.md` in your repo, or to `~/.claude/commands/draft-issue/SKILL.md` for global access."* (mirrored at :156 for implement-issue).

**What the official docs say (fetched Aug 12, 2026):**
- Skills live at `.claude/skills/<skill-name>/SKILL.md` (project) / `~/.claude/skills/<skill-name>/SKILL.md` (personal) — the "Where skills live" table lists **no** commands/ location for SKILL.md.
- The "How a skill gets its command name" table: *"File under `.claude/commands/` → File name without extension → `.claude/commands/deploy.md` → `/deploy`"*. Read literally, `.claude/commands/draft-issue/SKILL.md` should produce `/SKILL` — and both skills installed this way would collide on that name.
- *"Custom commands have been merged into skills. A file at `.claude/commands/deploy.md` and a skill at `.claude/skills/deploy/SKILL.md` both create `/deploy`."* And: *"New commands should usually be skills instead; commands remain supported"* (claude-directory page).
- The `commands/<dir>/SKILL.md` hybrid layout the README prescribes is **described nowhere** in the official docs.

**What actually happens (empirical, Claude Code v2.1.228, clean sandbox repo):**

| Test | Result |
|---|---|
| `.claude/commands/draft-issue/SKILL.md` + `claude -p '/draft-issue'` | **Loads the skill** — response referenced skill-specific content ("pulling the problem, agreed approach, constraints, and scope from a preceding discussion"; later run referenced "title hint" and "scored implementation-plan issue") |
| `claude -p '/SKILL'` | `Unknown command: /SKILL` — filename does **not** become the command |
| `claude -p '/totally-nonexistent-xyz'` | `Unknown command` — control case, proving /draft-issue was genuinely resolved |
| `.claude/commands/implement-issue/SKILL.md` + `claude -p '/implement-issue'` | **Loads and executes Step 0** — ran git checks under the `allowed-tools` grant without permission prompts, correctly reported "gh (GitHub CLI) is not installed", "no remote configured", "no commits yet", and stopped |
| `~/.claude/commands/audit-probe-xyz/SKILL.md` (global variant) | Probe token `PROBE-LOADED-91544` returned — global path works too |

**Fair conclusion:** the install instructions are *functional* on current Claude Code — the unified skills/commands loader evidently treats a directory-with-SKILL.md under `commands/` like a skill directory (directory name → command name). But this is (a) undocumented, (b) contrary to the docs' own naming table, (c) the legacy location the docs steer away from, and (d) needless: the repo's own source layout `skills/<name>/SKILL.md` maps 1:1 onto the canonical `.claude/skills/<name>/SKILL.md`. One-line README fix. I could not test whether this worked on April-2026 CLI versions (unverifiable in sandbox — flagged low confidence on the historical question).

An interviewer who reads the docs but doesn't test will conclude the install is broken; an interviewer who tests will conclude the README author didn't know the canonical location. Neither is a good look; the fix is trivial and should happen before the interview.

---

## 2. Spec compliance (current Aug 2026 spec)

| Item | draft-issue | implement-issue | Spec status |
|---|---|---|---|
| `name` (SKILL.md:2) | `draft-issue` | `implement-issue` | Valid: lowercase/hyphens, ≤64 chars, no reserved words; matches directory name. "Action-oriented" naming is an "acceptable alternative" per best practices (gerund form is the recommendation) |
| `description` (:3) | what + "Use when…" | what + "Use when…" | Matches the official example pattern almost exactly ("Extract text and tables from PDF files… Use when working with PDF files…"). Best practices warn "Always write in third person"; these open imperative — but so do Anthropic's own examples, so I don't ding it |
| `argument-hint` (:4) | `[optional: brief title hint]` | `<issue-number>` | Valid Claude Code field, correct format. **Not** in the Agent Skills open standard: claude.ai upload/packaging fails hard — the docs' example error is literally *"Unexpected key(s) in SKILL.md frontmatter: argument-hint"*. Acceptable given README:115 says Claude Code-only |
| `allowed-tools` (:5) | `Read, Bash(gh:*)` | `Read, Grep, Glob, Bash(git:*), Bash(gh:*)` | Valid syntax (comma-separated accepted; `:*` prefix-wildcard worked empirically). See §5 for breadth concerns |
| Body size | 266 lines | 263 lines | Under the 500-line guidance |
| `$ARGUMENTS` | :29 | :38 | Supported. Written as a variable to *test* ("If `$ARGUMENTS` is provided…") when spec substitutes it before Claude sees content — renders as "If `123` is provided…". Sloppy but empirically harmless |
| `disable-model-invocation` | **absent** | **absent** | **Deviation** — see §5 |
| Supporting files / evals | none | none | See §6 |

---

## 3. Rubric consistency with `prompts/issue-evaluator.md` (task 6)

**The load-bearing numbers are perfectly consistent — a genuine strength:**
- Weights 4/4/4/3/3/3/2/2 (implement-issue:71-80 = evaluator:28-37). Sum = 25; formula `Σ(score×weight)/25` with `max(…, 0.5)` floor identical in all three files (draft-issue:182-196, implement-issue:134-147, evaluator:98-110). Max = 250/25 = 10 ✓.
- Severity scale wording identical (implement-issue:155-158 = evaluator:120-123); same three severity-4 triggers (:161-163 = :128-130). The 7.0 gate matches everywhere, and draft-issue:244-247 explicitly warns that a sub-7.0 publish "will trigger a rewrite prompt when this issue is picked up" by implement-issue — real cross-skill coherence.

**The drift (all verified by quote):**
1. **Tier policy contradiction (major).** Evaluator:155-159 defines three tiers: ≥7.0 → suggestions; 2.0-7.0 → revised issue; **<2.0 → placeholder template, "not a verified runbook"**, because context is insufficient. implement-issue:174-194 has only two tiers: any score <7.0 → *"Rewritten issue: <complete rewritten issue using the eight-section structure, filled with all available context>"*. For a title-only 0.5/10 issue, the skill mandates fabricating steps, rollback commands, and file paths — the exact hallucinated-runbook failure the evaluator's third tier exists to prevent — and then `gh issue edit` (:202-204) writes it to GitHub on approval.
2. **Missing out-of-scope guard (major).** Evaluator:18: *"If you receive a bug report, feature request, or question, tell me it is out of scope."* implement-issue has no issue-type check anywhere in :59-207; it rubric-scores whatever issue number it is given.
3. **Frequency dimension dropped (minor).** Evaluator:125 requires "Always / Frequent / Occasional / Rare" per finding; absent from implement-issue:153-163.
4. **draft-issue's bands undefined (minor).** It demands `<n>/10` + Strong/Acceptable/Poor/Absent per section (:209-218) but never defines the 8-10/5-7/1-4/0 bands (those live only in implement-issue and the evaluator), and invents criteria the evaluator lacks ("executor can confirm readiness in under two minutes", :80). The draft-side score and the gate-side score rest on different specs.
5. **Cosmetic:** draft-issue's formula block lost its indentation (:183-195) vs the other two copies — a tell that three rubric copies are hand-synced.

---

## 4. Prompt-quality assessment (task 3)

**Genuinely well-engineered relative to typical community skills:**
- Deterministic step machine with explicit **WAIT** gates before every irreversible action (draft-issue:54, 232, 249; implement-issue:43, 200) — publishing and issue-editing are always behind explicit user approval *in the prompt* (though not at the permission layer, see §5).
- Bounded clarifying-question protocol: max 3, with three crisp admissibility criteria and a required format tying each question to the rubric section it unblocks (draft-issue:34-52). This is better question-discipline than most production prompts.
- Output templates are fully specified (scorecard table, brief format, gate report), making behavior testable.
- "Reads context from the conversation" (README:82) is **architecturally sound, not hand-wavy**: as an inline (non-fork) skill, the SKILL.md content "enters the conversation as a single message" (docs), so the history genuinely is in context. The authors correctly avoided `context: fork`, which the docs say "won't have access to your conversation history". Caveat nobody handled: post-compaction the "conversation" is a summary, and ":17 Do not ask the user to repeat themselves" then fights reality.
- "Session hygiene" (implement-issue:13-34) is implementable and sensible (git status/stash/branch -vv/gh pr list with a blocking-vs-advisory triage), though "a branch tied to another issue" requires fuzzy inference the prompt doesn't operationalize.
- Thoughtful determinism details: default-branch detection instead of assuming `main` (:224); specified fallback branch convention "feature/<number>-<slug> (lowercase, hyphens, max 40 chars)" (:216-218).

**Weaknesses:**
- `gh issue create --title "<title>" --body "<approved body>"` (draft-issue:255-257) and `gh issue edit … --body` (:202-204) model fragile quoting: every body this skill produces is guaranteed by its own template to contain fenced code blocks, backticks, and quotes (:92-108). `--body-file` is the robust pattern. In practice the model will likely improvise a heredoc when the literal command breaks — but the instruction as written is the fragile form.
- implement-issue grants `Grep, Glob` (:5) that **no step ever uses**, while Step 6 explicitly restricts the suggested approach to "the issue content and CLAUDE.md architecture only" (:260). The intro's "gather implementation context" (:11-12) never touches the codebase.
- Vague quality exhortations coexist with the deterministic machinery ("do not produce acceptable when strong is achievable", :60-61) — harmless but unfalsifiable.

---

## 5. Dependencies, failure handling, and safety posture (task 4)

**In the text: nothing.** No `gh auth status`/installation check, no GitHub-remote existence check, hardcoded remote name `origin` (:224, 228, 236), network-dependent `git remote show origin` (:224), unconditional "Read `CLAUDE.md`" (:209) — the fallback at :216-218 covers a CLAUDE.md *lacking a convention*, not a missing file.

**In practice: graceful — I tested it.** `/implement-issue` in a repo with no gh, no remote, no commits produced a precise, correct halt report ("gh (GitHub CLI) is not installed… no remote configured… I can't complete Step 1"). Credit where due — but that resilience came from the model, not the skill. An unauthenticated-gh repo would similarly surface gh's own error and the model would recover; the skill contributes zero guidance for it.

**Safety posture — the more serious issue:**
- **No `disable-model-invocation: true`** on either skill. The docs are explicit: *"Use this for workflows with side effects… You don't want Claude deciding to deploy because your code looks ready."* implement-issue's description ("Use when starting work on an issue") is a broad auto-invocation magnet, and its Step 5 runs `git checkout && git pull` with **no user gate before it** (the WAIT gates cover clarifications and rewrites, not branch mutation).
- **Over-broad `allowed-tools`:** `Bash(gh:*)` pre-approves *every* gh subcommand (`gh repo delete`, `gh api`, `gh pr merge`); `Bash(git:*)` includes `push --force` and `reset --hard`. My test confirmed the grant works (git ran unprompted in headless mode). Turn-scoped per docs, but least-privilege scoping (`Bash(gh issue:*)`, `Bash(git status:*)`, …) was available and is what the docs' own examples model (`Bash(git add *) Bash(git commit *)`). Docs: *"Review project skills before trusting a repository, since a skill can grant itself broad tool access."*
- Combined: Claude may auto-invoke a skill that can then create/edit GitHub issues and mutate branches without a single permission prompt in that turn. The only guardrails are prompt-level WAITs.

---

## 6. README claims (task 5) and testing debt

- **"Project-agnostic" (README:80):** mechanically true — no hardcoded repo/paths, CLAUDE.md convention discovery, gh repo auto-detection. Editorially false: the rubric bakes in a runbook/SRE ideology (Rollback weight 4, "production process is dangerous without it", per-step SQL/commands). The gate itself is survivable without Rollback (perfect-otherwise issue scores (250-40)/25 = **8.4**), but every triggered rewrite imposes the full eight-section runbook form on any project. And the skills are GitHub/gh-only (fair — stated).
- **"Close the write → evaluate → implement loop end to end" (README:80):** overclaim. The loop delivered is *write → evaluate → prepare-to-implement*. implement-issue ends at a brief plus "Ready to start, or do you want to discuss the approach first?" (:263). No implementation, no tests, no PR, no link-back, no retro. The skill's own name oversells it.
- **Per-feature claims check out:** "asks up to three clarifying questions" (README:82) = :41; the step lists at README:82/:84 accurately mirror the skills' actual steps; "Invoke `/draft-issue`" (README:143) verified working.
- **Testing debt (the interview-killer):** the official checklist requires *"At least three evaluations created"* and testing across models; Anthropic's skill-creator plugin automates with/without-skill benchmarking into `evals/evals.json`/`benchmark.json`. The skills directories contain **only SKILL.md** — zero evals, zero recorded testing — in a repo whose entire pitch (README:31-37) is "validated through iteration… evaluated, scored, revised, and rescored". The skills are the one component of the toolkit with no calibration artifact at all.

---

## 7. Aug 2026 ecosystem context (task 7)

Since these skills were committed (2026-04-24), and mostly *before* (skills shipped Oct 2025; the Agent Skills open standard was published at agentskills.io on Dec 18, 2025 and adopted by Microsoft, OpenAI, Atlassian, Figma, Cursor, and GitHub — per Simon Willison's Dec 19, 2025 write-up and ecosystem coverage):
- **Distribution norm** is marketplaces/plugins: official `claude-plugins-official` marketplace (~256 entries per July 2026 coverage), community aggregators (tonsofskills.com claims 2,800+ skills), `anthropics/skills` as the first-party repo. This repo's "copy one file by hand" install — into the legacy directory — reads as pre-ecosystem. No `.claude-plugin/plugin.json`, no marketplace.json, so no `/plugin install` path exists.
- **What would impress a power user:** the WAIT-gate discipline; the correct inline-context architecture; rubric-consistent scoring across three files; clean frontmatter; empirically the things just work.
- **What would concern them:** legacy install path; no `disable-model-invocation` on side-effectful skills; blanket `Bash(git:*)`/`Bash(gh:*)`; no evals in a "measurement" toolkit; three hand-synced rubric copies already drifting; single-file skills that ignore the supporting-files/progressive-disclosure model (defensible for copy-install, but that constraint exists only because of the copy-install choice); `--body` quoting.

**Sources used** (fetched or searched this session): [Claude Code skills docs](https://code.claude.com/docs/en/skills), [.claude directory docs](https://code.claude.com/docs/en/claude-directory), [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices), [anthropics/skills](https://github.com/anthropics/skills), [agentskills.io spec repo](https://github.com/agentskills/agentskills), [Simon Willison on Agent Skills](https://simonwillison.net/2025/Dec/19/agent-skills/), [tonsofskills marketplace repo](https://github.com/jeremylongshore/claude-code-plugins-plus-skills), [ecosystem guide](https://www.alexcloudstar.com/blog/claude-code-plugin-marketplace-skills-2026/), [Unite.ai on the standard](https://www.unite.ai/anthropic-opens-agent-skills-standard-continuing-its-pattern-of-building-industry-infrastructure/). Ecosystem scale figures come from search-result summaries of these third-party sources (not individually fetched) — marked medium confidence; all doc quotes are from pages fetched in full.

---

## 8. Hard questions a sharp interviewer will ask (with the honest answers)

1. **"Walk me through installing draft-issue."** Path works but is legacy/undocumented; canonical is `.claude/skills/`. Fix the README first; if asked, own it: "commands and skills were merged; I've corrected it to the canonical skills path."
2. **"Where are the evals for these skills?"** There are none. Indefensible given the repo's thesis — either run skill-creator evals before the interview or pre-concede this as known debt.
3. **"Your evaluator says a sub-2.0 issue can't be meaningfully rewritten. Why does implement-issue rewrite it anyway — and push it to GitHub?"** Genuine contradiction; the honest answer is the tier logic wasn't ported.
4. **"What happens if I run /implement-issue on a bug report?"** It gets rubric-scored as an implementation plan and offered a runbook rewrite; the evaluator's out-of-scope guard was not ported.
5. **"Why can Claude auto-invoke a skill that checks out branches and edits issues, with git and gh blanket-pre-approved?"** Missing `disable-model-invocation: true`; over-broad grants. Two-line fix.
6. **"Does `gh issue create --body \"…\"` survive a body full of backticks and quotes?"** As written, no reliably; `--body-file` is the fix.
7. **"'End to end' — where's the implement leg?"** It stops at branch + brief. Rename the claim or extend the skill.
8. **"Three copies of the rubric — how do you keep them in sync?"** Manually, and they've already drifted (frequency, tiers, bands, indentation).

## 9. Pre-interview fix list (highest leverage first)
1. README:148,156 → `.claude/skills/…` (one line each).
2. Add `disable-model-invocation: true` to both skills; narrow `allowed-tools` to `Bash(gh issue:*)` / scoped git rules; switch to `--body-file`.
3. Port the <2.0 template tier and the out-of-scope issue-type guard into implement-issue.
4. Run skill-creator evals on both skills and commit `evals/` — converts the biggest weakness into a story that matches the toolkit's thesis.
5. Optional: add `.claude-plugin/plugin.json` to make the repo `/plugin install`-able.