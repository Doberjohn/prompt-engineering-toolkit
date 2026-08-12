# Agent report: hygiene

## Executive summary

Repo hygiene is mostly clean but has one flagship defect: README's primary "Getting started" instruction for the UI/UX evaluator points to prompts/uiux-evaluation-prompts.md, a file deleted on 2026-04-20 (commit f6c1216) — the three real mode files are never path-referenced anywhere in the README. The MIT license coexists with a self-declared "built on top of" relationship to the CC BY-NC-SA 4.0 AI Fluency Framework with no clarifying notice; my (non-lawyer) analysis is that the repo likely stays on the safe "ideas, not expression" side of the line, but the seven-techniques section imports the source's taxonomy plus one verbatim quote, and this is a guaranteed hard interview question. The calibration set's foundational artifact (Doberjohn/inkweave#278) 404s publicly, undercutting the "verifiable/traceable" claims. The LICENSE copyright line names "John Giannelos" (year 2025) while every commit is authored by John Fanidis and the repo started 2026-04-15. Otherwise: 12 of 13 README file paths resolve, every countable README claim I checked verifies exactly (9 anchors, 10 anchors, 25 citations, 20 dimensions, 7 techniques, two 10/10 anchors), the workflow is valid YAML with two recorded successful runs, and CONTRIBUTING is fully consistent with the shipped skills. The repo is a 4-active-day sprint (42 commits, Apr 15-24) followed by 110 days of silence, with zero tags, releases, changelog, issue templates, or CI validation.

## Strengths (with evidence)

- **README file-path accuracy is otherwise high: 12 of 13 referenced repo paths exist exactly as written**
  - Evidence: Verified against the file tree: prompts/issue-evaluator.md (README.md:122), examples/issue-calibration-set.md (:127), prompts/prompt-evaluator.md (:130), skills/draft-issue/SKILL.md (:82,148), skills/implement-issue/SKILL.md (:84,156), framework/ppep-framework.md (:159), examples/prompt-calibration-set.md (:161), CONTRIBUTING.md (:187), LICENSE (:193) — all present; only prompts/uiux-evaluation-prompts.md (:136) is dead
- **Every countable README claim I checked verifies exactly**
  - Evidence: 9 prompt anchors (examples/prompt-calibration-set.md headers ANCHOR 1-9, two 10/10 at lines 184,202 matching README.md:74); 10 issue anchors (grep -cE '^## ANCHOR' = 10, README.md:77); '25+ citations' = exactly 25 (24 URLs in issue-calibration-set.md lines 6-99 + Nielsen 1993 ISBN-only book cite; 3+10+4+5+3=25); '20-dimension scoring system' (README.md:68) = 20 numbered dimensions in prompts/uiux-evaluator/url-mode.md (10 UI + 10 UX); 'seven integrated techniques' section exists at framework/ppep-framework.md:144-169
- **CONTRIBUTING.md is fully consistent with the repo it describes, including an exact match between its required skill frontmatter spec and both shipped skills**
  - Evidence: CONTRIBUTING.md:37-47 mandates name/description/argument-hint/allowed-tools in skills/<skill-name>/SKILL.md; both skills/draft-issue/SKILL.md:1-6 and skills/implement-issue/SKILL.md:1-6 carry exactly those four fields in that layout
- **The GitHub Actions workflow is valid YAML and demonstrably functional — it ran successfully twice on the two post-creation prompts/ commits**
  - Evidence: PyYAML parses .github/workflows/notify-companion.yml cleanly; fetch of https://github.com/Doberjohn/prompt-engineering-toolkit/actions shows 2 runs of 'Trigger companion app rebuild', both successful (8s and 11s), matching commits c80f2e1/c143850 which each touched prompts/uiux-evaluator/url-mode.md
- **AI Fluency attribution hygiene is genuinely good: the upstream license claim is accurate and cited consistently**
  - Evidence: Web search confirms the AI Fluency: Framework and Foundations course by Dakan, Feller & Anthropic is released under CC BY-NC-SA 4.0 (anthropic.skilljar.com/ai-fluency-framework-foundations; aifluencyframework.org); the repo cites it with license named at README.md:9,20,175 and framework/ppep-framework.md:10,169,206
- **Commit message quality is above average for a solo project: imperative, scoped, one concern per commit**
  - Evidence: git log main — e.g. 'Fix typo in URL mode evaluation instructions' (c143850), 'Revise scoring guidance and references in ppep-framework' (f8fda6d), 'Add contributing guidelines for Claude Code skills' (0875ba8); only one generic message ('Update prompt-evaluator.md', a0eb8f0) in 42 commits
- **The README is honest about scope boundaries rather than overclaiming coverage**
  - Evidence: README.md:16-18 explicitly states the issue evaluator is a Discernment tool and that 'The three remaining competencies (Delegation, full Discernment coverage, and Diligence) are not covered by this toolkit'
- **Branch state is clean: no stale feature branches, no divergence**
  - Evidence: git ls-remote --heads origin shows only main and the current audit branch (claude/prompt-toolkit-analysis-jybfdm); working tree clean per git status

## Findings

- **[MAJOR] [readme-accuracy]** README's primary 'Getting started' instruction for the UI/UX evaluator points to a file deleted four months ago, and the three real mode files are never path-referenced anywhere in the README
  - Evidence: README.md:136 'Open `prompts/uiux-evaluation-prompts.md`' — file absent from tree; deleted in commit f6c1216 (2026-04-20, 'Delete prompts/uiux-evaluation-prompts.md', 689 deletions); replacements are prompts/uiux-evaluator/{url,screenshot,codebase}-mode.md; grep of README for 'uiux' shows no mention of the new paths; README was edited afterwards (79514fc, c80f2e1 on Apr 24) without fixing it
  - Confidence: high — verified against tree and git log; nothing could make this wrong
- **[MAJOR] [licensing]** The repo is MIT-licensed while describing itself as 'a practitioner's implementation built on top of' a CC BY-NC-SA 4.0 work, with no notice reconciling the two — a defensible but completely unaddressed legal posture and a guaranteed hard interview question
  - Evidence: README.md:9 ('built on top of the AI Fluency Framework... released under CC BY-NC-SA 4.0') vs LICENSE:1 (MIT, including the right to 'sell copies', LICENSE:8); framework/ppep-framework.md:146-169 imports the source's seven-technique taxonomy and quotes it verbatim ('perhaps the most powerful technique of all', line 165); CC BY-NC-SA 4.0 legalcode defines Adapted Material as derivation 'in a manner requiring permission under the Copyright and Similar Rights' and ShareAlike requires adaptations to carry a same-elements CC license (MIT is not compatible); CC's own guidance confirms ideas/facts/systems are not restricted
  - Confidence: high that the tension is real and unaddressed; medium on the legal-risk call (likely safe under idea/expression, but I could not diff against the source PDF — www-cdn.anthropic.com blocked from this environment — so verbatim overlap beyond the one quote is unverified). I am not a lawyer and this is not legal advice
- **[MAJOR] [verifiability]** The foundational artifact of the issue calibration set — Inkweave issue #278 — is not publicly accessible, contradicting the set's own 'any developer can verify... independently' claim
  - Evidence: WebFetch of https://github.com/Doberjohn/inkweave/issues/278 (linked at examples/issue-calibration-set.md:146) returns HTTP 404, as does https://github.com/Doberjohn/inkweave; the Doberjohn profile's public repo list does not include inkweave; yet examples/issue-calibration-set.md:8 claims 'This section exists so any developer can verify, challenge, or extend the framework independently' and README.md:77 markets it as 'a real implementation plan issue (GitHub issue #278)'
  - Confidence: high that it 404s unauthenticated (private or deleted — cannot distinguish which); cross-cutting with the issue-evaluator agent
- **[MINOR] [licensing]** The LICENSE copyright line names a person ('John Giannelos') who does not match the repo's author of record, and a year (2025) that predates the repository's existence
  - Evidence: LICENSE:3 'Copyright (c) 2025 John Giannelos'; git shortlog shows all 42 main-branch commits by 'John Fanidis <johnfanidis@gmail.com>'; GitHub profile fetch shows 'Doberjohn (John Fanidis)'; initial commit 43cdcc9 is 2026-04-15
  - Confidence: high on the mismatch itself; medium on interpretation (could be a legal-name variant, but more likely a copy-paste from another project) — an easy interviewer 'gotcha' either way
- **[MINOR] [readme-accuracy]** 'Ten controlled degradations' is an off-by-one overstatement: Anchor 1 is explicitly the undegraded reference issue, so the set is 1 reference + 9 degradations
  - Evidence: README.md:77 'Ten controlled degradations of a real implementation plan issue' and examples/issue-calibration-set.md:102 repeat the claim, but examples/issue-calibration-set.md:141 states 'Degradation applied: None. This is the reference issue.'
  - Confidence: high
- **[MINOR] [readme-accuracy]** The model-compatibility table contradicts its own footnote: Claude (chat) is marked 'Full' for UI/UX Codebase Mode while the footnote says codebase mode requires an agentic coding environment that 'standard chat interfaces cannot' provide
  - Evidence: README.md:107 row 'UI/UX Codebase Mode | Full | Partial** | Partial** | Full' vs README.md:113 '**Codebase mode uses grep commands and file:line references that require an agentic coding environment (Claude Code, Cursor, GitHub Copilot Workspace). Standard chat interfaces cannot execute these commands.' — claude.ai chat is a standard chat interface, so by the table's own logic the Claude column should be Partial
  - Confidence: high on the internal inconsistency; capability deep-dive left to the uiux agent
- **[MINOR] [versioning]** Zero versioning of any kind — no tags, no releases, no changelog — for a toolkit whose central promise is calibrated, stable scoring that edits can silently drift
  - Evidence: git tag -l empty; git ls-remote --tags origin empty; no CHANGELOG file in tree; meanwhile README.md:33 claims prompts were 'evaluated, scored, revised, and rescored... until the framework stabilized' and README.md:3 calls templates 'production-ready' — consumers have no way to pin or diff an evaluator version
  - Confidence: high
- **[MINOR] [repo-completeness]** A repo substantially about GitHub issue quality ships no issue templates itself — a direct practice-what-you-preach gap
  - Evidence: .github/ contains only workflows/notify-companion.yml (ls -la .github); no ISSUE_TEMPLATE directory or config; yet the repo ships an eight-section issue rubric (prompts/issue-evaluator.md), a 943-line issue calibration set, and CONTRIBUTING.md:65 asks bug reporters to include 'the AI model you tested with, the prompt you used, and the output you received' — exactly what an issue form would enforce
  - Confidence: high
- **[MINOR] [ci-validation]** There is no automated validation of anything — no markdown lint, no link checker, no formula re-verification — and a trivial link-check CI would have caught the broken README path the day it broke
  - Evidence: The only workflow is .github/workflows/notify-companion.yml (deploy ping); the README:136 dead link has survived since f6c1216 (2026-04-20) through four subsequent commits including two README edits (79514fc); for a repo whose ethos is 'evidence over opinion' (CONTRIBUTING.md:3) and 'formula-verified score' (README.md:77), zero machine verification of its own artifacts is a fair critique, though partially excusable for a docs-only repo
  - Confidence: high
- **[MINOR] [maintenance-signal]** The repo presents as an ongoing community project but shows a 4-day sprint followed by 110 days of silence and near-zero adoption signals
  - Evidence: git log main by day: 2026-04-15 (9), 04-16 (13), 04-20 (13), 04-24 (7) = 42 commits across 4 active days in a 10-day window; nothing since Apr 24 (Apr 24 to Aug 12 = 6+31+30+31+12 = 110 days); GitHub page fetch: 1 star, 0 forks, 0 open issues; yet CONTRIBUTING.md:3 says 'Contributions are welcome' and the README maintains live-demo/deploy-hook infrastructure
  - Confidence: high on the numbers; the interpretation (portfolio sprint vs abandoned) is the owner's to frame
- **[NITPICK] [ci-robustness]** The workflow's curl call cannot fail on HTTP errors, so a dead or rejecting deploy hook still produces a green run
  - Evidence: .github/workflows/notify-companion.yml:12 'run: curl -X POST ${{ secrets.COMPANION_DEPLOY_HOOK }}' — no -f/--fail flag, so 4xx/5xx responses exit 0; the two recorded 'success' runs prove only that curl executed with a non-empty secret (an unset secret would exit 2 with 'no URL specified'), not that Vercel accepted the ping
  - Confidence: high
- **[NITPICK] [git-hygiene]** Git history shows GitHub-web-UI-driven churn: a placeholder file named 'framework' created and deleted 3 minutes later, and three prompt files created without .md extensions then renamed 4 days later
  - Evidence: d3b0817 (13:22:45) adds 1-line file 'framework' with commit body 'created framework folder'; f1d03b1 (13:25:33) deletes it; 4a4560c/7d3d739/ec48871 (Apr 20) create url-mode/screenshot-mode/codebase-mode extensionless; 33a62b4/9b24555/38ec42f (Apr 24) are pure renames adding .md — cosmetic, but it tells an evaluator the repo was largely edited through the GitHub web interface
  - Confidence: high
- **[NITPICK] [readme-accuracy]** The live-demo hostname in the README drops the final 'n' of 'companion' relative to the companion repo's name — either a typo or genuine Vercel truncation, unverifiable within audit scope
  - Evidence: README.md:43 'https://prompt-engineering-toolkit-companio.vercel.app' vs README.md:45 repo name 'prompt-engineering-toolkit-companion' (36 chars vs 35-char host label)
  - Confidence: low — verifying would require fetching the demo, which the owner placed out of scope; flag for the owner to confirm the link works before the interview

## Open questions

- For the skills agent: does the README install path `.claude/commands/draft-issue/SKILL.md` (README.md:148,156) actually work in current Claude Code? Skills conventionally live under `.claude/skills/<name>/SKILL.md` and commands are flat `.claude/commands/<name>.md` files — if the documented path is wrong, both 'Install:' lines in the README are additional broken instructions on top of the uiux one. Also whether `argument-hint`/`allowed-tools` (CONTRIBUTING.md:44-45) are valid SKILL.md frontmatter fields per current docs.
- For the citations agent: (a) README.md:179 attributes LLM-Rubric (ACL 2024) to 'Eisenstein, J., et al.' — verify authorship (I suspect Hashemi/Eisner et al.); (b) the IssuePilot citation in examples/issue-calibration-set.md uses a malformed gist URL (gist.githubusercontent.com/raw/<hash> lacks the required user/gist-id path segments); (c) 'CorsoUX' vs domain 'courseux.com' naming mismatch and its '(2026)' date (README.md:174); (d) the CorsoUX UX-audit checklist is filed under the 'SRE runbook structure' source category in the calibration methodology — miscategorized; (e) whether https://www-cdn.anthropic.com/62df988c101af71291b06843b63d39bbd600bed8.pdf resolves and contains the quoted phrase 'perhaps the most powerful technique of all' (framework/ppep-framework.md:165) — anthropic.com and www-cdn.anthropic.com were egress-blocked from my environment.
- For the framework/citations agents: framework/ppep-framework.md:146 attributes the seven techniques to 'Anthropic's prompting research (Dakan, Feller, & Anthropic, 2025)' — verify the AI Fluency course actually enumerates these techniques; the answer cuts both ways (divergence = attribution inaccuracy; identity = strengthens the CC-adaptation question in my licensing finding).
- Cross-cutting design observation (companion out of scope, noting the trigger only): the workflow's paths filter is `prompts/**` only, so edits to framework/, examples/, or skills/ never trigger a companion rebuild — whether that matters depends on what the companion consumes.
- For the methodology agent: examples/issue-calibration-set.md:143 documents an 'Expert judgment override: formula score 9.44 rounded to 10/10' on Anchor 1 — this resolves the coordinator checkpoint's rounding-anomaly note (analysis/00-first-hand-notes.md item 3) but is itself a formula-override worth scrutiny.
- Presentation note for the owner: the tagline (README.md:3, 'covering the Description competency') is softly contradicted at README.md:16 where the issue evaluator is classified as a Discernment tool; README.md:18's 'full Discernment coverage' hedge shows awareness, but a sharp interviewer may probe the positioning.

---

## Full report

# Repository Hygiene & Packaging Audit — Doberjohn/prompt-engineering-toolkit

Auditor lane: README accuracy, CONTRIBUTING, LICENSE, CI workflow, git history, repo completeness. Audit date 2026-08-12. All paths absolute under `/home/user/prompt-engineering-toolkit`.

## 1. README truthfulness sweep

### 1.1 File paths — 12 of 13 resolve; the 13th is the worst possible one to be broken

Checked every repo path the README references against the actual tree:

| README line | Path | Exists? |
|---|---|---|
| 82, 148 | `skills/draft-issue/SKILL.md` | Yes |
| 84, 156 | `skills/implement-issue/SKILL.md` | Yes |
| 122 | `prompts/issue-evaluator.md` | Yes |
| 127 | `examples/issue-calibration-set.md` | Yes |
| 130 | `prompts/prompt-evaluator.md` | Yes |
| **136** | **`prompts/uiux-evaluation-prompts.md`** | **NO** |
| 159 | `framework/ppep-framework.md` | Yes |
| 161 | `examples/prompt-calibration-set.md` | Yes |
| 187 | `CONTRIBUTING.md` | Yes |
| 193 | `LICENSE` | Yes |

**The broken one is the primary usage instruction for one of the three headline tools.** README.md:135-136: *"To evaluate a UI/UX interface: 1. Open `prompts/uiux-evaluation-prompts.md`"*. That file was deleted in commit f6c1216 (2026-04-20 21:24, "Delete prompts/uiux-evaluation-prompts.md", 689 deletions) and replaced by `prompts/uiux-evaluator/{url,screenshot,codebase}-mode.md` (686 lines total across three files). The README **never mentions the new paths anywhere** — grep for "uiux" in README.md hits only the section blurb (L67-68), the compatibility table (L105-107), and the dead instruction (L136). Worse for the defense: the README was edited twice *after* the deletion (79514fc "Add live demo section", Apr 24; plus bf6c102 the same evening as the delete) without anyone noticing. The instruction's wording ("Choose the mode that matches your available input") also still reflects the old all-modes-in-one-file layout. This is the single most quotable hygiene defect in the repo: the flagship claim is rigor, and the front door to a third of the product is a 404 that survived 114 days and four subsequent commits.

### 1.2 Countable claims — everything I counted checks out

- **"nine anchor prompts spanning the full quality range (1/10 to 10/10)"** (README.md:34, 74): `examples/prompt-calibration-set.md` has exactly ANCHOR 1–9 headers; range 1/10→10/10; **"two distinct 10/10 anchors"** confirmed (Anchor 8 line 184 "Technical agentic", Anchor 9 line 202 "Non-technical collaborative").
- **"Ten controlled degradations"** (README.md:77): 10 `## ANCHOR` headers confirmed — but see §1.3 for the off-by-one.
- **"25+ citations"** (README.md:77): counted in the methodology section (`examples/issue-calibration-set.md:6-99`): 3 (calibration method) + 10 (GitHub issue research) + 4 (Agile) + 5 (SRE) + 3 (severity scale, incl. the URL-less Nielsen 1993 book) = **exactly 25**. Arithmetic: 24 URLs + 1 ISBN citation. "25+" is technically true at the boundary; "25" would have been more honest than "25+".
- **"20-dimension scoring system"** (README.md:68): `prompts/uiux-evaluator/url-mode.md` STEP 2 has exactly dimensions 1–20 (10 UI + 10 UX). Verified by listing them.
- **"seven evidence-based prompting techniques"** (README.md:52): `framework/ppep-framework.md:144-169` has a six-row table + one meta-technique = 7.
- **"Both skills are Claude Code only"** (README.md:80) is consistent with the table's N/A cells (README.md:108-109) and footnote *** (README.md:115).

This is a genuine strength: the README's quantitative self-descriptions are not puffery — they reconcile against the documents.

### 1.3 Claim defects

- **Off-by-one**: "Ten controlled degradations of a real implementation plan issue" (README.md:77; repeated at examples/issue-calibration-set.md:102). Anchor 1 states "**Degradation applied:** None. This is the reference issue." (examples/issue-calibration-set.md:141). So: 1 reference + 9 degradations. Small, but this is a repo that stakes its identity on formula-verified precision.
- **Source artifact 404s**: The "real" issue behind the entire calibration set — `https://github.com/Doberjohn/inkweave/issues/278` (linked at examples/issue-calibration-set.md:146) — returns HTTP 404 unauthenticated, as does the `Doberjohn/inkweave` repo itself (both fetched 2026-08-12; the repo also does not appear on the Doberjohn public profile). The methodology explicitly promises "any developer can verify, challenge, or extend the framework independently" (examples/issue-calibration-set.md:8). No outside reader can verify the anchor artifact. Interview question waiting: *"Your whole calibration set derives from an issue nobody can see?"* (Cross-cutting with the issue-evaluator agent; the dead public link is the hygiene fact.)
- **Compatibility-table self-contradiction**: README.md:107 marks **Claude (chat) as "Full"** for UI/UX Codebase Mode, while the table's own footnote (README.md:113) says codebase mode "uses grep commands... that require an agentic coding environment (Claude Code, Cursor, GitHub Copilot Workspace). **Standard chat interfaces cannot execute these commands.**" claude.ai chat is a standard chat interface; by the footnote's logic, that cell should be Partial (like ChatGPT/Gemini) — or the footnote overclaims. The other rows are internally coherent: footnote * (README.md:111) honestly hedges Partial for cross-model evaluator use; N/A + footnote *** for skills is consistent. (Capability deep-dive is the uiux agent's lane; I flag only the internal logic.)
- **Demo hostname**: README.md:43 gives `https://prompt-engineering-toolkit-companio.vercel.app` — "companio", dropping the final 'n' of the repo name at README.md:45. Could be a typo or legitimate Vercel truncation. **Unverified** (fetching the demo is out of audit scope by owner instruction). Confidence low; the owner should click the link before the interview.
- **Tagline tension** (nitpick): README.md:3 says the toolkit "cover[s] the Description competency," while README.md:16 classifies the issue evaluator as "a Discernment tool." README.md:18's "full Discernment coverage" hedge shows self-awareness, but the positioning is slightly self-contradictory.

## 2. LICENSE analysis — MIT on top of a CC BY-NC-SA 4.0 framework

**Disclaimer: I am not a lawyer; this is a risk read, not legal advice.**

### The facts

- LICENSE is stock MIT — including the explicit right to "sell copies of the Software" (LICENSE:8).
- README.md:9 self-describes: "a practitioner's implementation **built on top of** the AI Fluency Framework... released under CC BY-NC-SA 4.0."
- Upstream license claim **verified**: web search confirms *AI Fluency: Framework and Foundations* (Dakan, Feller & Anthropic) is released under CC BY-NC-SA 4.0 (anthropic.skilljar.com course page; aifluencyframework.org). The README's citation is accurate.
- What the repo actually takes from the CC work: (a) the 4D taxonomy and competency names with one-line paraphrases (README.md:11-14; framework/ppep-framework.md:10); (b) the **seven-technique taxonomy**, explicitly attributed: "The PPEP framework integrates seven evidence-based prompting techniques from Anthropic's prompting research (Dakan, Feller, & Anthropic, 2025)" (framework/ppep-framework.md:146), with technique names in a table (lines 150-157) and one short verbatim quote: "perhaps the most powerful technique of all" (line 165). I found **no multi-sentence verbatim blocks**; the table's "Impact" column phrasing appears original. I could **not** diff against the source PDF (www-cdn.anthropic.com egress-blocked from this environment), so overlap beyond the one quote is unverified.

### The law (verified against CC's published terms)

- CC BY-NC-SA 4.0 defines **Adapted Material** as material derived from the licensed material "in a manner **requiring permission under the Copyright and Similar Rights** held by the Licensor" (legalcode §1.a, via search of creativecommons.org legalcode). The SA/NC obligations attach only to uses of protected *expression* — not ideas.
- **ShareAlike** (§3.b): adaptations must carry a CC license with the same elements (BY-NC-SA, same version or later, or compatible). MIT is not compatible.
- **NonCommercial**: neither the material nor adaptations may be used primarily for commercial advantage.
- CC's own guidance (creativecommons.org FAQ; creativecommonsusa.org "When is my use considered an adaptation?") confirms **facts, ideas, methods, and systems are outside copyright**, and "CC licenses... cannot restrict uses that are otherwise permitted under copyright."

### The assessment

- **Most likely position (defensible)**: the toolkit uses the framework's *ideas* — a four-competency taxonomy, competency names, a list of technique concepts — with attribution, plus one short attributed quote. A taxonomy is a system/method; competency names are unprotectable short phrases; brief attributed quotation is classic de minimis/quotation-right territory. On this reading the repo is **not Adapted Material**, MIT over the author's own text is permissible, and the NC clause does not bind users of this toolkit.
- **The weak point**: the seven-techniques section is where the repo comes closest to the line — it imports the source's pedagogical *selection and arrangement* of techniques wholesale and says so. A maximalist licensor could argue compilation-level expression. I rate this risk low (technique lists in a table, restated in original words, with attribution), but it is the section an interviewer or IP reviewer would poke.
- **If any portion were deemed Adapted Material**: MIT-only licensing of that portion would violate ShareAlike, and NC would prohibit commercial use of it — directly contradicting MIT's "sell copies" grant. That is the worst-case scenario, not the likely one.
- **The real problem is presentational, not legal**: the phrase "built on top of" (README.md:9) rhetorically invites the derivative-work framing that the legal analysis then has to defuse, and the repo contains **no NOTICE or license-scope statement** reconciling MIT with the CC citation. One paragraph — "This toolkit cites and builds on the *concepts* of the AI Fluency Framework; no text from the CC BY-NC-SA-licensed course is incorporated beyond brief attributed quotation; the CC license applies to the original course materials, not to this repository" — would neutralize the question. Its absence is the defect.
- **Interview drill**: *"Your README says this is built on top of a CC BY-NC-SA work, but you licensed it MIT — can a company use your toolkit commercially?"* The correct answer is yes-with-the-idea/expression-argument; the owner should be able to deliver it unprompted.

### Separate LICENSE defect

LICENSE:3 reads "Copyright (c) **2025 John Giannelos**". Every one of the 42 main-branch commits is authored "John Fanidis <johnfanidis@gmail.com>" (git shortlog), and the GitHub profile fetch shows "Doberjohn (John Fanidis)". The initial commit is **2026**-04-15, so the year predates the repo too. Interpretation is uncertain (legal-name variant vs. copy-paste from another project), but as it stands the license file attributes copyright to a name that appears nowhere else in the project, with a wrong year. Trivial to fix; embarrassing to be asked about.

## 3. `.github/workflows/notify-companion.yml`

Full file (12 lines): triggers on `push` to `main` filtered to `paths: ['prompts/**']`; single job runs `curl -X POST ${{ secrets.COMPANION_DEPLOY_HOOK }}`.

- **Validity**: parses cleanly under PyYAML. (The `on:` key parses as boolean `True` under YAML 1.1 — a known, benign GitHub Actions quirk, not a defect.)
- **Demonstrably functional**: the repo's Actions page (fetched) shows exactly 2 runs of "Trigger companion app rebuild," both successful (8s, 11s), matching the only two post-creation commits that touched `prompts/**` (c80f2e1, c143850, both editing `prompts/uiux-evaluator/url-mode.md` on Apr 24). Both green runs also prove the `COMPANION_DEPLOY_HOOK` secret was configured and non-empty at the time (an empty secret makes curl exit 2 → red run).
- **Dependency**: the workflow is inert without the `COMPANION_DEPLOY_HOOK` repository secret; nothing in the repo documents that requirement (a fork would silently fail the job).
- **Silent-failure defect**: `curl` without `-f/--fail` exits 0 on HTTP 4xx/5xx, so a revoked or dead deploy hook still yields a green run. The two "successes" prove curl ran, not that Vercel accepted the ping. One-character-class fix: `curl -fsS -X POST ...`.
- **Paths-filter observation** (companion itself out of scope): only `prompts/**` triggers a rebuild; edits to `framework/`, `examples/`, `skills/`, or README never do. Whether that is a gap depends on what the companion consumes — noting the trigger design only.

## 4. CONTRIBUTING.md

Read in full (71 lines). Verdict: **consistent and above-average for a repo this size.**

- Structure claims match reality: "Skills live in `skills/<skill-name>/SKILL.md`" (CONTRIBUTING.md:37) — true.
- The mandated frontmatter (CONTRIBUTING.md:39-47: `name`, `description`, `argument-hint`, `allowed-tools`) **exactly matches** both shipped skills (skills/draft-issue/SKILL.md:1-6; skills/implement-issue/SKILL.md:1-6). The repo follows its own contribution spec. (Whether that frontmatter matches the *official* Claude Code skills spec is the skills agent's question.)
- Vocabulary is consistent with the toolkit: "four PPEP dimensions" (:11), "eight sections and formula-verified scores" (:12), `**WAIT**` checkpoints (:52) — all real conventions in the shipped files.
- Sensible quality bar: skills must be tested "in at least one real Claude Code session against a real repo" with a failure case (:56-59).
- Includes a minimal but adequate code-of-conduct clause (:69-71), so the absence of a separate CODE_OF_CONDUCT.md is fine at this scale.
- One irony: CONTRIBUTING.md:63-65 tells issue reporters exactly what detail to include — model, prompt, output — and the repo provides **no issue template** to capture it (see §6).

## 5. Git history

42 commits on main, single author (John Fanidis; +1 audit-branch commit by Claude today). Distribution by day (computed from `git log --date=short | sort | uniq -c`):

- 2026-04-15: 9 · 2026-04-16: 13 · 2026-04-20: 13 · 2026-04-24: 7 → **42 commits in 4 active days** within a 10-day window, then **110 days of silence** (Apr 24 → Aug 12 = 6+31+30+31+12).

**Message quality**: genuinely good — imperative, scoped, one concern each ("Revise scoring guidance and references in ppep-framework", "Fix typo in URL mode evaluation instructions"). Only one lazy message in 42 ("Update prompt-evaluator.md", a0eb8f0).

**Churn / tooling tells**:
- d3b0817 (13:22) adds a 1-line file literally named `framework` with commit body "created framework folder"; f1d03b1 deletes it **3 minutes later** (13:25) — the classic create-a-file-to-make-a-folder GitHub-web-UI move.
- The three uiux mode files were created **without .md extensions** (4a4560c, 7d3d739, ec48871, Apr 20) and renamed to add `.md` four days later (33a62b4, 9b24555, 38ec42f, Apr 24) — again a web-UI signature ("Create screenshot-mode").
- The f6c1216 delete (689-line uiux file) was properly done, but its README reference was orphaned (§1.1) — the churn itself is fine; the missing cross-update is the defect.

**What the timeline signals to an evaluator**: a concentrated build sprint, edited largely through the GitHub web interface, with content arriving in large single commits (e.g. 7b42615 adds the whole prompt calibration set) — meaning the claimed "validated through iteration" (README.md:33) happened *outside* git, in AI sessions, and left no auditable trail. Combined with 1 star / 0 forks / 0 issues (repo page fetched) and "Contributions are welcome," the repo reads as a portfolio sprint wearing community-project clothes. That is not damning — but the owner should frame it proactively ("built in a focused sprint, iteration happened in evaluation sessions, here's the evidence trail") rather than let the log frame it for them.

**Branch state**: clean. `git ls-remote --heads` shows only `main` and today's audit branch; no stale branches; working tree clean; initial commit (43cdcc9) sensibly scaffolded README/CONTRIBUTING/LICENSE first.

## 6. Missing standard artifacts — which absences matter

| Artifact | Present? | Verdict |
|---|---|---|
| Tags / releases | No (`git tag -l` and `ls-remote --tags` both empty) | **Matters.** The product is calibrated evaluators; any edit can shift scores. With no versions, no consumer can pin or diff an evaluator. "Production-ready" (README.md:3) without versioning is a fair attack line. |
| CHANGELOG | No | Matters, same reason — score-affecting prompt changes are invisible. |
| Issue templates / `.github/ISSUE_TEMPLATE` | No (`.github/` contains only `workflows/`) | **Matters for credibility more than function**: a repo whose centerpiece is an 8-section GitHub-issue rubric, a 943-line issue calibration set, and a `draft-issue` skill ships zero issue templates, while CONTRIBUTING.md:65 begs reporters for structured detail. The single best practice-what-you-preach fix available. |
| Any CI validation (markdown lint, link check, formula check) | No — only the deploy ping | **Matters**: a stock link-checker (lychee, markdown-link-check) would have caught README:136 on 2026-04-20. For an "evidence over opinion" repo, zero machine verification of its own claims is the sharpest version of this critique. |
| .gitignore | No | Fine — markdown-only repo, nothing to ignore. |
| CODE_OF_CONDUCT.md | No standalone file | Fine — CONTRIBUTING.md:69-71 covers it proportionately. |
| SECURITY.md / PR template | No | Fine at this scale; PR template mildly nice-to-have given CONTRIBUTING:30's PR-description requirements. |

## 7. Model-compatibility table (README.md:100-116)

Assessed for internal consistency only (capability deep-dive belongs to the uiux agent):

- **Coherent**: Framework "Full" everywhere (it's prose — trivially true); Prompt/Issue Evaluator "Partial*" off-Claude with an honest calibration-drift footnote (README.md:111); skills "N/A" in chat + footnote *** (README.md:115) matches the skills' own docs.
- **Incoherent**: Codebase Mode row (README.md:107) — Claude chat marked "Full" while footnote ** (README.md:113) says the mode requires an agentic coding environment and "standard chat interfaces cannot execute these commands." By the table's own logic that cell should be Partial. One cell, but it's the kind of inconsistency a sharp interviewer uses to test whether the author actually stress-tested their own claims.
- URL/Screenshot "Full" across all chat models is plausible (all three major chat products accept URLs/images as of my verification window) — plausibility only; not deep-verified here.

## Hard interview questions from this lane

1. "Walk me through evaluating a UI — your README says open `prompts/uiux-evaluation-prompts.md`. That file doesn't exist. How long has your quickstart been broken, and what does that say about your QA?" (114 days; two README edits since.)
2. "This is MIT-licensed but 'built on top of' a CC BY-NC-SA work. Can I use it at my company? Reconcile the licenses." (§2 — needs the idea/expression answer rehearsed.)
3. "Who is John Giannelos?" (LICENSE:3 vs. commit author.)
4. "Your calibration set derives from Inkweave issue #278 — the link 404s. How do I independently verify anything?"
5. "You wrote 943 lines on what makes a good GitHub issue. Why does your own repo have no issue template?"
6. "Which version of the evaluator scored these anchors? There are no tags, no releases, no changelog."
7. "42 commits in 4 days, then nothing for 4 months, 1 star. Is this maintained?"

## What is genuinely good (this lane)

- Near-perfect path accuracy outside the one (bad) break; every countable README claim reconciles exactly against the documents (§1.2) — rare and worth saying in the interview.
- CONTRIBUTING is specific, testable, and matches the shipped artifacts down to the frontmatter fields.
- Upstream attribution is accurate, consistent, and license-aware (three citations naming CC BY-NC-SA) — the *citation* hygiene is better than the *license-reconciliation* hygiene.
- The CI workflow, however small, is valid and has two verifiable successful runs.
- Clean branch state, disciplined commit messages, scoped commits.

**Bottom line for the defense**: fix before the interview — README:136 (five-minute fix), LICENSE:3 name/year, add a license-scope NOTICE paragraph, tag v1.0.0, add an issue template and a link-check action. Every one is under an hour of work, and together they remove five of the seven hard questions above.