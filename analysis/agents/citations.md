# Agent report: citations

## Executive summary

I verified all 31 unique external citations across README.md, framework/, prompts/, and examples/. The good news: 30 of 31 sources demonstrably exist, every cited URL/DOI/arXiv ID resolves to a real, topically relevant document, several verbatim quotes check out exactly, and the "25+ citations" count is numerically accurate (exactly 25 in the methodology section). The bad news is serious: 6 of the 14 author-named academic citations (43%) carry fabricated author names — "Eisenstein", "Li", "Wang", "Arya", "Zhang (Y.)", and "Holterman" are not authors of the papers cited (real first authors: Hashemi, Sülün, Zhang (Jin), Huang, Acharya, Hong) — the classic signature of unverified AI-generated bibliography. Additionally, the flagship "93% confidence / 7% irreducible subjectivity" figure is presented as "documented in peer-reviewed literature" but no cited source contains any such number; a block quote attributed to "Nielsen (1993), as discussed in Hertzum (2006)" appears three times but could not be found as a verbatim sentence anywhere; the calibration set's core "controlled degradation" methodology is attributed to three sources none of which discuss it; and the Anthropic PDF link cited as "AI Fluency: Framework and Foundations" actually resolves to a handout Google indexes as "6 Techniques for Effective Prompt Engineering". Verdict: "research-backed" is roughly 70% honest — the sources are real and well-chosen, but the scholarly apparatus (author names, quotations, quantified confidence) would not survive a spot-check by a sharp interviewer.

## Strengths (with evidence)

- **Zero fully fabricated sources: 30 of 31 unique external citations verifiably exist at the given URL/ID, including every obscure one checked (blog posts, gist, dev.to, arXiv preprints)**
  - Evidence: Web-verified: nngroup.com both articles, w3.org/TR/WCAG22/, measuringu.com/rating-severity/, courseux.com/ux-audit-checklist/, arXiv 2512.21426, arXiv 2601.08654, dl.acm.org/doi/10.1145/3643673, ieeexplore 10633301, springer s10664-018-9636-3, arXiv 2504.18804, aclanthology 2024.acl-long.745, blogs.reliablepenguin.com/2025/10/29/..., oneuptime.com/blog/post/2026-02-02-effective-runbooks/view, dev.to/thesius_code_7a136ae718b7/runbook-template-library-50p1, labelstud.io blog, atlassian.com acceptance-criteria, scrumalliance, argondigital, zenhub, docs.github.com x3, github.blog x2, gist c9efc3e0e4fb81b4aefa3bf43d22391b (curl 302 -> gist.github.com/shanelindsay/..., HTTP 200). Only github.com/Doberjohn/inkweave/issues/278 could not be confirmed (network-blocked), though the repo itself is real (dependabot.ecosyste.ms indexes Doberjohn/inkweave).
- **The GitHub Copilot 'ideal task' quotation at examples/issue-calibration-set.md:34 is verbatim-accurate against the live GitHub Docs page**
  - Evidence: issue-calibration-set.md:34 quotes 'An ideal task includes a clear description, complete acceptance criteria, and directions about which files need to be changed'; web search of docs.github.com/en/copilot/tutorials/cloud-agent/get-the-best-results returned: 'An ideal task includes: A clear description of the problem... complete acceptance criteria... directions about which files need to be changed'
- **Nielsen's 0-4 severity scale is reproduced faithfully, and the frequency/impact/persistence trio is real Nielsen doctrine**
  - Evidence: issue-calibration-set.md:81 ('0 = not a problem, 1 = cosmetic, 2 = minor, 3 = major, 4 = catastrophic/blocks task completion') matches NN/g severity article scale confirmed by search (0='I don't agree...' through 4='Usability catastrophe'); the article also confirms 'frequency... impact... persistence' as the three severity factors
- **The suspicious-looking 'CorsoUX (2026)' citation is real: the site's brand is CorsoUX on domain courseux.com, and the toolkit's quote is on the page nearly verbatim**
  - Evidence: Search returned 'UX Audit Checklist: 50 Points & Free Template | CorsoUX' at courseux.com/ux-audit-checklist/, and the snippet: 'An audit that doesn't specify "what to do in what order" is analysis, not design. The output must be a roadmap.' vs issue-calibration-set.md:72's quote — near-exact match
- **The 'What Makes a GitHub Issue Ready for Copilot?' citation (README.md:177) is correct on author surname, title, ID and date — a fully real, on-point Dec 2025 paper**
  - Evidence: arXiv 2512.21426 confirmed via search: exact title, author Mohammed Sayagh (École de Technologie Supérieure), submitted 24 Dec 2025, 32-criteria issue-quality study for Copilot
- **The IEEE paper's headline statistic is quoted accurately: '1,084,300 projects' appears verbatim in the real paper's abstract**
  - Evidence: issue-calibration-set.md:44 ('across 1,084,300 projects') matches IEEE Xplore 10633301 abstract snippet: 'the relationship with project characteristics were analyzed for 1,084,300 projects... adoption of IRT was associated with increased project productivity'
- **The 'From Idea to PR' four-section planning claim is supported: the plan chatmode featured by GitHub generates exactly Overview, Requirements, Implementation Steps, Testing**
  - Evidence: issue-calibration-set.md:38 claim vs github/awesome-copilot plan.chatmode.md (found via search): 'a Markdown document that includes: Overview... Requirements... Implementation Steps... Testing'
- **The 'Includes a full methodology section with 25+ citations' claim is numerically exact**
  - Evidence: grep -cE '^- [A-Z]' over issue-calibration-set.md lines 6-98 returns exactly 25 citation bullets (computed in-session)
- **No future-dated or post-hoc-impossible citations relative to the owner's commits (2026-04-15 to 2026-04-24), with one exception noted in findings**
  - Evidence: git log: owner content committed 2026-04-15..24; latest cited sources: Rulers arXiv Jan 2026, OneUptime 2026-02-02, dev.to Thesius 2026-03-23 — all before 2026-04-24
- **Core peer-reviewed backbone (Nielsen 1994 x2, Nielsen 1993 ISBN, Hertzum 2006, WCAG 2.2, Sauro 2013) is bibliographically flawless**
  - Evidence: Hertzum 2006 confirmed as IJHCI 21(2), 125-146 exactly as cited (README.md:172); Nielsen 1993 ISBN 978-0125184069/Academic Press confirmed via book databases; WCAG 2.2 confirmed as W3C Recommendation 5 Oct 2023 matching 'W3C. (2023)' at README.md:171

## Findings

- **[CRITICAL] [fabricated-authors-pattern]** Six of the fourteen author-named academic citations (43%) attribute real papers to fabricated author names — the signature pattern of AI-generated, unverified bibliography — directly undermining the repo's core claim of 'proof of every decision'
  - Evidence: Eisenstein→Hashemi et al. (aclanthology 2024.acl-long.745); Li→Sülün/Saçakçı/Tüzün (ACM 10.1145/3643673, confirmed by @acm_tosem tweet); Wang→Jin Zhang/Maoqi Peng/Yang Zhang (IEEE 10633301); Arya→Huang/Costa/Zhang/Zou (Springer s10664-018-9636-3); Zhang→Acharya/Ginde (arXiv 2504.18804); Holterman→Hong/Yao/Wei/Shen/Dong/Xu (arXiv 2601.08654, ADS index 2026arXiv260108654H). In every case the title, venue, year, and URL are correct — only the humans are invented.
  - Confidence: high — each author list confirmed via at least one authoritative web source (ACL Anthology, TOSEM's own announcement, IEEE/COMPSAC listing, Springer, arXiv/ADS); could only be wrong if all six search-result snapshots were simultaneously wrong
- **[MAJOR] [citation-misattribution]** The LLM-Rubric paper (ACL 2024) is cited three times as 'Eisenstein, J., et al.' but no author named Eisenstein exists on it; real authors are Helia Hashemi, Jason Eisner, Corby Rosset, Benjamin Van Durme, Chris Kedzie
  - Evidence: README.md:179, examples/prompt-calibration-set.md:14, examples/issue-calibration-set.md:17 all read 'Eisenstein, J., et al. (2024)'; ACL Anthology 2024.acl-long.745 and microsoft/LLM-Rubric GitHub confirm Hashemi as first author, Eisner (not Eisenstein) as second — likely conflation of Jason Eisner with Jacob Eisenstein, a different NLP researcher
  - Confidence: high
- **[MAJOR] [citation-misattribution]** 'Li, X., et al.' is not an author of the TOSEM issue-templates paper cited at README.md:176 and examples/issue-calibration-set.md:41; real authors are Emre Sülün, Metehan Saçakçı, Eray Tüzün (Bilkent University)
  - Evidence: dl.acm.org/doi/10.1145/3643673 'An Empirical Analysis of Issue Templates Usage in Large-Scale Projects on GitHub'; ACM TOSEM's own X/Twitter announcement: 'Sülün et al. just got their paper... accepted at #goTOSEM'
  - Confidence: high
- **[MAJOR] [citation-misattribution]** 'Holterman, B., et al. (2026)' does not exist on the RULERS paper (arXiv 2601.08654) cited at examples/issue-calibration-set.md:18; real authors are Yihan Hong, Huaiyuan Yao, Hua Wei, Bolin Shen, Yushun Dong, Wanpeng Xu
  - Evidence: Search results for arXiv 2601.08654 (HuggingFace papers page, ResearchGate, NASA ADS bibcode 2026arXiv260108654H — the trailing 'H' encodes first-author Hong); no Holterman on any listing. Note the paper was also retitled 'From Rubrics to Reliable Scores...' in a later arXiv revision; the toolkit cites the v1 title, which is fine
  - Confidence: high
- **[MAJOR] [citation-misattribution]** 'Wang, Y., et al. (2024)' is not an author of IEEE 10633301 'Empirical Study on GitHub Issue Report Templates' cited at examples/issue-calibration-set.md:43; real authors are Jin Zhang, Maoqi Peng, Yang Zhang (COMPSAC 2024)
  - Evidence: IEEE Xplore document 10633301 plus ResearchGate/computer.org CSDL listings confirm Zhang/Peng/Zhang; ironically the toolkit assigns the name 'Zhang, Y.' to a different paper where it is wrong
  - Confidence: high
- **[MAJOR] [citation-misattribution]** 'Arya, D., et al. (2018)' is not an author of Springer s10664-018-9636-3 cited at examples/issue-calibration-set.md:45; real authors are Yonghui Huang, Daniel Alencar da Costa, Feng Zhang, Ying Zou
  - Evidence: link.springer.com/article/10.1007/s10664-018-9636-3 'An empirical study on the issue reports with questions raised during the issue resolving process' — author list confirmed via search; Deepika Arya is a real researcher on GitHub-issue-discussion papers (2019), making this a plausible-looking but wrong attribution an interviewer could catch
  - Confidence: high
- **[MAJOR] [citation-misattribution]** 'Zhang, Y., et al. (2025)' is not an author of arXiv 2504.18804 (EASE 2025) cited at examples/issue-calibration-set.md:47; real authors are Jagrit Acharya and Gouri Ginde
  - Evidence: arXiv 2504.18804 'Can We Enhance Bug Report Quality Using LLMs?...' — authors confirmed via arXiv/ResearchGate search: 'authored by Jagrit Acharya and Gouri Ginde... EASE 2025 (17–20 June, Istanbul)'. The 'five dimensions: Atomicity, Conciseness, Completeness, Understandability, Reproducibility' claim maps to the CTQRS rubric the paper uses but was not verifiable verbatim
  - Confidence: high on authors; medium on the five-dimensions detail
- **[MAJOR] [unsupported-claim]** The README asserts the '7% irreducible subjectivity' is 'documented in peer-reviewed literature (Nielsen 1993, Hertzum 2006)' — but no cited source contains any 7% (or 93%) figure; the number is self-assigned and dressed as literature-backed
  - Evidence: README.md:90-92: 'Current confidence level in the framework: 93%. The remaining 7% is the irreducible subjectivity... documented in peer-reviewed literature (Nielsen 1993, Hertzum 2006)'; Nielsen's severity article and Hertzum 2006 document evaluator disagreement and averaging benefits (verified via search) but quantify nothing resembling 7%; framework/ppep-framework.md:192-198 repeats the figure
  - Confidence: high that no source states 7%; the sources do support the existence (not magnitude) of single-evaluator subjectivity
- **[MAJOR] [fabricated-quote]** A block quotation used three times — 'There tends to be disagreement between evaluators when assigning severity, and reliability improves when averaging ratings from independent evaluators.' attributed to 'Nielsen (1993), as discussed in Hertzum (2006)' — could not be found as a verbatim sentence in either source and reads as a synthesized paraphrase presented in quotation marks
  - Evidence: framework/ppep-framework.md:196, examples/prompt-calibration-set.md:21 (and echoed at README.md:92). Targeted exact-phrase web search found the underlying doctrine (NN/g: single-evaluator ratings 'too unreliable to be trusted', mean of 3-4 evaluators satisfactory) but no verbatim match in Nielsen 1993 or Hertzum 2006
  - Confidence: medium — full text of Hertzum 2006 is paywalled and could not be fetched from this environment; substance is accurate Nielsen doctrine even if wording is invented
- **[MAJOR] [unsupported-claim]** The calibration set's foundational methodology claim — that 'NLP evaluation research... shows that synthetic low-quality examples tend to be theatrically bad rather than realistically bad, producing central tendency bias' and that controlled degradation is the 'recommended' remedy — is attributed to three sources (LLM-Rubric, RULERS, Label Studio) none of which discusses controlled degradation, 'theatrically bad' synthetic examples, or that causal chain
  - Evidence: examples/issue-calibration-set.md:12-19 and :94; README.md:77 ('the same controlled degradation methodology recommended by NLP evaluation research'). LLM-Rubric is about calibrating LLM judges to individual human raters; RULERS about locked rubrics/evidence anchoring; the Label Studio post about rubric+ground-truth+calibration workflow (all confirmed via abstracts/snippets). Central tendency bias in LLM raters IS real in the literature (e.g., arXiv 2605.16386), but not in the works cited
  - Confidence: medium-high — based on abstracts and indexed content, not full texts; none of the three mention degradation methodology anywhere visible
- **[MINOR] [citation-mislabeling]** The repeatedly-cited Anthropic CDN PDF (README.md:175, framework/ppep-framework.md:169 and :206) is labeled 'AI Fluency: Framework and Foundations' but the document at that hash is indexed by Google as '6 Techniques for Effective Prompt Engineering' — a course handout, not the framework document the citation names
  - Evidence: Two independent search results render the PDF's indexed title/first line as '6 Techniques for Effective Prompt Engineering 1. Provide context Before' at www-cdn.anthropic.com/62df988c101af71291b06843b63d39bbd600bed8.pdf; the AI Fluency framework itself (Dakan/Feller/Anthropic, CC BY-NC-SA 4.0, HEA Ireland/National Forum support) is fully real and verified via teachingandlearning.ie and anthropic.skilljar.com — only the link/title pairing is wrong
  - Confidence: medium-high — could not fetch the PDF directly (egress-blocked); title evidence is Google's index of the file content, seen in two separate searches
- **[MINOR] [impossible-date]** The 'IssuePilot. (2024)' gist citation is dated a year before the gist existed — the gist was created 2025-07-11 — and the named author 'IssuePilot' is just the document's own heading; the gist owner is github user shanelindsay
  - Evidence: examples/issue-calibration-set.md:39; curl of gist.github.com/c9efc3e0e4fb81b4aefa3bf43d22391b → 302 to /shanelindsay/...; page HTML: aria-label 'created by shanelindsay on 10:39AM on July 11, 2025', file line 1: '# GitHub CLI Workflow for Task Management - IssuePilot'. The Why/What/How content claim itself IS verified in the gist body (Description (Why), Acceptance Criteria (What), implementation steps (How))
  - Confidence: high
- **[MINOR] [standard-misreading]** The UI/UX evaluator prompts misstate WCAG 2.2 SC 1.4.12: they present 'minimum 1.5 line height for body text' as a WCAG 1.4.12 requirement, but 1.4.12 (Text Spacing) only requires that content survive USER-applied spacing overrides (line height to 1.5x) without loss — it imposes no authored line-height minimum
  - Evidence: prompts/uiux-evaluator/url-mode.md:49 ('sufficient line height (minimum 1.5 for body text per WCAG 1.4.12)') and codebase-mode.md:86; W3C Understanding SC 1.4.12 (confirmed via search): 'no loss of content or functionality occurs by setting line height... to at least 1.5 times the font size' — an adaptability requirement, not a design minimum. The adjacent 'minimum 16px body text' sub-criterion is likewise no WCAG criterion (not attributed to WCAG, so lesser issue)
  - Confidence: high
- **[MINOR] [weak-support]** The GitHub Issues Quickstart is cited as confirming 'title, description, acceptance criteria as baseline requirements', but the Quickstart covers titles, descriptions, task lists, labels, and milestones — acceptance criteria do not appear in it
  - Evidence: examples/issue-calibration-set.md:29-30; search of docs.github.com quickstart content surfaces 'creating new issues, adding task lists, and adding labels, milestones, assignees' with no acceptance-criteria mention. Also the cited path (.../learning-about-issues/quickstart) now lives at .../configuring-issues/quickstart on current docs (old path survives on enterprise-server versions/redirects)
  - Confidence: medium — based on indexed summaries of the page, not a full fetch
- **[MINOR] [source-quality]** Several load-bearing 'research' citations are marketing/SEO blog content or anonymous posts, which sits uneasily under the 'research-backed'/'established research' banner even though all are honestly attributed: CorsoUX (course-selling UX site), ReliablePenguin (hosting-company blog), Thesius (auto-generated dev.to handle 'thesius_code_7a136ae718b7' promoting an 'SRE Platform Pro' toolkit, published 2026-03-23), OneUptime (vendor blog)
  - Evidence: README.md:167 frames the References as 'established research and standards'; issue-calibration-set.md:63-72 cites all four under the methodology's 'research areas'; dev.to article confirmed as March 23, 2026 vendor-toolkit promo via search
  - Confidence: high on the characterization of each source; the defect is framing, not existence
- **[NITPICK] [citation-misattribution]** 'Sayagh, M., et al.' implies co-authors, but arXiv 2512.21426 is sole-authored by Mohammed Sayagh
  - Evidence: README.md:177; two independent searches report the single author ('published... by Mohammed Sayagh from École de Technologie Supérieure')
  - Confidence: medium-high — based on search-result author listings, not the arXiv page itself (egress-blocked)
- **[NITPICK] [paraphrase-as-quote]** The Sauro/MeasuringU citation puts quotation marks around 'treat frequency separately from severity', which is a paraphrase of the article's point, not its verbatim text
  - Evidence: examples/issue-calibration-set.md:84; the real article (measuringu.com/rating-severity/) argues frequency and severity 'should be treated as distinct measures' per search snippets — same substance, different words
  - Confidence: medium
- **[NITPICK] [category-error]** CorsoUX's UX-audit checklist — a UX source — is filed under the calibration set's 'SRE runbook structure' research category, where it is used to justify the roadmap/action-plan requirement
  - Evidence: examples/issue-calibration-set.md:61 (heading '**SRE runbook structure**') with CorsoUX as its final bullet at :71-72
  - Confidence: high
- **[NITPICK] [title-drift]** Two minor title mismatches: Scrum Alliance article is actually titled 'Acceptance Criteria: Everything You Need to Know Plus Examples' (cited as 'What You Need to Know About Acceptance Criteria'); the Label Studio post's live title is 'Scale AI Evaluation with Rubrics and Calibration' (cited by its slug-title 'How to Scale Evaluation for RAG and Agent Workflows')
  - Evidence: examples/issue-calibration-set.md:54 and :19/prompt-calibration-set.md:15 vs search-confirmed live titles at resources.scrumalliance.org/Article/need-know-acceptance-criteria and labelstud.io/blog/how-to-scale-evaluation-for-rag-and-agent-workflows/ (both URLs valid)
  - Confidence: high
- **[NITPICK] [unverifiable-citation]** The calibration set's anchor source, github.com/Doberjohn/inkweave/issues/278, could not be verified to exist (only the repo could), and the Google Cloud (2019) claim that Google SRE 'explicitly requires' a playbook with release/setup/teardown/rollback documentation was not confirmable in the article's indexed content
  - Evidence: examples/issue-calibration-set.md:146 and :67-68; Doberjohn/inkweave confirmed real via dependabot.ecosyste.ms (tracks its PR #244), but direct fetch of issue 278 was network-blocked (github.com 403 via proxy; add_repo denied); cloud.google.com/blog/products/devops-sre/how-to-start-and-assess-your-sre-journey confirmed to exist ('Do you have an SRE team yet? How to start and assess your journey') but its checklist details were not retrievable
  - Confidence: low — these are verification gaps caused by my environment, not demonstrated defects; flagged so the owner verifies before the interview

## Open questions

- Cross-cutting (hygiene agent's lane): the analysis/ directory containing this audit fleet's own checkpoint reports was committed to the repo today (commits 42cd405, a94ac16, 2026-08-12) — should those ship in a repo the owner is about to defend?
- Cross-cutting (issue-evaluator agent's lane): the '9.44/10 formula score' for Inkweave #278 (issue-calibration-set.md:139-146) rests on an issue I could not fetch; someone with GitHub access should confirm the issue exists and matches the reproduced content.
- Cross-cutting (framework agent's lane): framework/ppep-framework.md:146 says the seven techniques come from 'Anthropic's prompting research (Dakan, Feller, & Anthropic, 2025)', and :165 quotes 'perhaps the most powerful technique of all' from 'the source authors' — the linked handout lists six techniques and the course does teach ask-AI-for-help as a powerful 'secret weapon', but the exact quoted phrase could not be verified; the owner should locate the verbatim source before quoting it aloud.
- README.md:137 tells users to open 'prompts/uiux-evaluation-prompts.md', a file deleted in commit f6c1216 (2026-04-20) — broken internal reference adjacent to my lane; hygiene agent should confirm.
- Whether the owner can regenerate/download the cited Anthropic CDN PDF to confirm what it actually contains (my access was egress-blocked; Google's index says its title is '6 Techniques for Effective Prompt Engineering').

---

## Full report

# Citation Verification Audit — prompt-engineering-toolkit

**Auditor lane:** every external citation in the owner's files (README.md references, framework/, prompts/, examples/). The `analysis/` directory was committed by the audit fleet itself today (git log: `42cd405`, `a94ac16`, dated 2026-08-12) and is not owner content; it was excluded. Owner content spans commits 2026-04-15 → 2026-04-24.

**Method and constraints:** This environment's egress proxy blocked direct fetches of most domains (arxiv.org, aclanthology.org, nngroup.com, anthropic.com CDN, docs.github.com, archive.org, semanticscholar.org all returned EGRESS_BLOCKED/403). Verification therefore combined: WebSearch (worked; snippets quoted below are from indexed page content), and direct curl where permitted (gist.github.com worked). Every verdict below states its evidence channel. Where full text was unreachable, confidence is marked down explicitly.

---

## 1. The headline numbers

- **31 unique external citations** across the owner's files (13 in README's References; 25 bullets in the calibration-set methodology — `grep -cE '^- [A-Z]'` over lines 6-98 returns exactly 25, so README:77's "25+ citations" is numerically true; the two lists overlap on 7 items; plus framework-only items: Nielsen 1994 book chapter, Nielsen 1993 book, the gist, GitHub docs/blog pages, etc.).
- **30 of 31 confirmed to exist** (the one holdout — Inkweave issue #278 — is a network-access gap, not a demonstrated fabrication; the repo itself is real per dependabot.ecosyste.ms).
- **6 of 14 author-named academic citations (43%) have fabricated author names.** Every one of those six papers is real, at the exact URL/DOI/arXiv ID given, with correct title, venue, and year. Only the author names are wrong.
- **0 not-found sources. 0 future-dated sources** relative to the owner's last commit (2026-04-24). One internally impossible date (gist cited "2024", created 2025-07-11).

## 2. Verdict table

| # | Citation (location) | Verdict | Key evidence |
|---|---|---|---|
| 1 | Nielsen 1994, 10 Usability Heuristics (README:169) | **VERIFIED** | URL live per search; 1994 refinement of 249-problem factor analysis; canonical citation year correct |
| 2 | Nielsen 1994, Severity Ratings (README:170; issue-cal:80-82,127) | **VERIFIED** | 0-4 scale reproduced faithfully (0 not-a-problem → 4 catastrophe); frequency/impact/persistence trio confirmed on page |
| 3 | W3C 2023, WCAG 2.2 (README:171) | **VERIFIED** | W3C Recommendation 5 Oct 2023 at w3.org/TR/WCAG22/ |
| 4 | Hertzum 2006, IJHCI 21(2) 125-146 (README:172; framework:205) | **VERIFIED** | Exact bibliographic match confirmed (ResearchGate/journal listings) |
| 5 | MeasuringU/Sauro 2013 (README:173; issue-cal:83) | **VERIFIED** | URL live; 2013; frequency-vs-severity-as-distinct-measures content confirmed. Caveat: the quoted string "treat frequency separately from severity" is paraphrase-in-quotes |
| 6 | CorsoUX 2026 (README:174; issue-cal:71-72) | **VERIFIED (existence+quote)** | Brand "CorsoUX" on domain courseux.com — the name/domain mismatch is the site's own branding, not an error. Quote near-verbatim on page: 'An audit that doesn't specify "what to do in what order" is analysis, not design. The output must be a roadmap.' Date "2026" unverifiable. It is a course-marketing site, not research |
| 7 | Dakan, Feller & Anthropic 2025, AI Fluency PDF (README:175; framework:169,206) | **EXISTS-BUT-MISLABELED** | Framework real (Dakan=Ringling, Feller=UCC, CC BY-NC-SA 4.0, HEA Ireland/National Forum — all confirmed via teachingandlearning.ie & skilljar). But the linked hash-PDF is Google-indexed as **"6 Techniques for Effective Prompt Engineering"** — a handout, not the titled framework document (2 independent search confirmations; direct fetch blocked) |
| 8 | "Li, X., et al." 2024, ACM 3643673 (README:176; issue-cal:41) | **EXISTS-BUT-MISATTRIBUTED** | Real authors: **Sülün, Saçakçı, Tüzün** (TOSEM's own announcement: "Sülün et al."). Content claim (templates ↔ resolution time/reopens) consistent with the paper's abstract |
| 9 | "Sayagh, M., et al." 2025, arXiv 2512.21426 (README:177) | **VERIFIED** (nit: sole author, so "et al." is wrong) | Exact title; Mohammed Sayagh, ÉTS; submitted 24 Dec 2025; 32-criteria Copilot-readiness study — the single most on-point academic source in the repo |
| 10 | GitHub 2025, Copilot best practices (README:178; issue-cal:33-34) | **VERIFIED** | Page live; the toolkit's quoted "ideal task" sentence matches the page nearly verbatim — the strongest citation in the repo |
| 11 | "Eisenstein, J., et al." 2024, LLM-Rubric ACL (README:179; prompt-cal:14; issue-cal:17) | **EXISTS-BUT-MISATTRIBUTED** | Real authors: **Hashemi, Eisner, Rosset, Van Durme, Kedzie** (ACL Anthology + microsoft/LLM-Rubric). "Eisenstein" is a different NLP researcher; likely Eisner→Eisenstein confusion |
| 12 | ReliablePenguin 2025 (README:180; issue-cal:65-66) | **VERIFIED** | URL with 2025/10/29 date live; history-to-Google-SRE narrative confirmed. Exact sub-quote "Close with safety notes and references" unverified verbatim |
| 13 | Atlassian 2025 (README:181; issue-cal:52-53) | **VERIFIED** | Page live; "definition of done" framing confirmed |
| 14 | "Holterman, B., et al." 2026, RULERS arXiv 2601.08654 (issue-cal:18) | **EXISTS-BUT-MISATTRIBUTED** | Real authors: **Hong, Yao, Wei, Shen, Dong, Xu** (HF papers, ResearchGate, ADS bibcode 2026arXiv260108654**H**). No Holterman anywhere. Paper also does not discuss the degradation methodology it is cited for |
| 15 | Label Studio 2026 (prompt-cal:15; issue-cal:19) | **VERIFIED** | URL live; rubric + ground-truth + calibrated scoring content confirmed; live page title now differs slightly |
| 16 | GitHub Quickstart (issue-cal:29-30) | **EXISTS / WEAK SUPPORT** | Page exists (path since moved); its content (task lists, labels, milestones) does not mention acceptance criteria, which the toolkit says it "confirms" |
| 17 | GitHub Best Practices for Projects (issue-cal:31-32) | **VERIFIED** | Page live; sub-issues + blocked-by/blocking dependencies confirmed |
| 18 | GitHub Blog "record time" (issue-cal:35-36) | **VERIFIED** | Page live; action-forward title + acceptance-criteria/definition-of-done checklist confirmed in page content |
| 19 | GitHub Blog "From Idea to PR" (issue-cal:37-38) | **VERIFIED** | Page live; the four-section plan (Overview/Requirements/Implementation Steps/Testing) confirmed via the plan.chatmode.md the post features (github/awesome-copilot). Nuance: it's a custom chat mode GitHub promotes, not a built-in "planning mode" |
| 20 | "IssuePilot (2024)" gist (issue-cal:39-40) | **EXISTS-BUT-MISDATED** | curl: gist real (302 → gist.github.com/**shanelindsay**/c9efc...; HTTP 200); created **2025-07-11** (cited 2024 — impossible); "IssuePilot" is the document's own H1, not the author; Why/What/How structure claim **verified in the gist body**. Cited raw-URL form (gist.githubusercontent.com/raw/<id>) is nonstandard |
| 21 | "Wang, Y., et al." 2024, IEEE 10633301 (issue-cal:43-44) | **EXISTS-BUT-MISATTRIBUTED** | Real authors: **Jin Zhang, Maoqi Peng, Yang Zhang** (COMPSAC 2024). The "1,084,300 projects" figure is verbatim-accurate |
| 22 | "Arya, D., et al." 2018, Springer s10664-018-9636-3 (issue-cal:45-46) | **EXISTS-BUT-MISATTRIBUTED** | Real authors: **Huang, Costa, Zhang, Zou**. Title exact. Content claim (questions during resolution → delays) consistent with abstract |
| 23 | "Zhang, Y., et al." 2025, arXiv 2504.18804 / EASE (issue-cal:47-48) | **EXISTS-BUT-MISATTRIBUTED** | Real authors: **Acharya & Ginde**. Venue (EASE 2025, Istanbul) correct. "Five dimensions" claim maps to the paper's CTQRS metric — plausible, unverified verbatim |
| 24 | Scrum Alliance 2023 (issue-cal:54-55) | **VERIFIED** (title drift) | URL live; real title "Acceptance Criteria: Everything You Need to Know Plus Examples"; pass/fail checklist confirmed |
| 25 | ArgonDigital 2023 (issue-cal:56-57) | **VERIFIED** | URL + title exact; technical-stories-need-technical-AC confirmed; "file-level specificity" is the toolkit's own gloss |
| 26 | ZenHub 2021 (issue-cal:58-59) | **VERIFIED** | URL + title + markdown-checklist claim all confirmed |
| 27 | OneUptime 2026 (issue-cal:63-64) | **VERIFIED** | Exact dated URL (2026-02-02) live; metadata/prerequisites/rollback structure and "every runbook that makes changes should include a rollback procedure" confirmed |
| 28 | Google Cloud 2019 SRE journey (issue-cal:67-68) | **VERIFIED (existence)** | Real article "Do you have an SRE team yet? How to start and assess your journey"; the specific playbook-requirement detail not confirmable from indexed content |
| 29 | Thesius 2026, dev.to (issue-cal:69-70) | **VERIFIED (existence+structure)** | URL live; symptoms/diagnosis/remediation/verification structure confirmed ("Escalation" unconfirmed); published 2026-03-23; author handle is auto-generated ("thesius_code_7a136ae718b7") promoting a paid toolkit — weak authority |
| 30 | Nielsen 1993, Usability Engineering, ISBN 978-0125184069 (issue-cal:85-86) | **VERIFIED** | ISBN + Academic Press confirmed via book databases. The frequency/impact/persistence trio is stated on the NN/g 1994 severity page; attributing it specifically to the 1993 book is loose but defensible |
| 31 | Nielsen 1994 chapter, Usability Inspection Methods (Wiley) (framework:204) | **VERIFIED** | Canonical, standard bibliography entry (high confidence; not fetched) |

## 3. The five landmines (what a sharp interviewer will find in 10 minutes)

1. **Fabricated author names on six academic citations.** "Eisenstein", "Li", "Wang", "Arya", "Zhang (Y.)", "Holterman" — none is an author of the cited paper. Real first authors: Hashemi, Sülün, Jin Zhang, Huang, Acharya, Hong. This is the textbook signature of an LLM writing a bibliography from memory: correct titles/venues/IDs, invented humans. For a project whose README (line 26-37) attacks "opinion-based" guides and promises decisions "grounded in established research," this is the single most damaging discoverable fact. The saving grace: because every URL is right, the *claims* mostly survive; the *scholarship* does not.
2. **The 93%/7% figure** (README:90-92, framework:192-198, prompt-cal:23). Presented as though the 7% is "documented in peer-reviewed literature (Nielsen 1993, Hertzum 2006)." The literature documents *that* single-evaluator assessment is unreliable; it contains no 7% quantification. "Documented" here means "we picked a number and cited the field." An interviewer who asks "where does 7% come from?" has no good answer available.
3. **The Nielsen-via-Hertzum quotation** (framework:196; prompt-cal:21; README:92 paraphrase). Used three times, in quotation marks, with a scholarly-looking chain attribution. I could not find the sentence verbatim anywhere; it reads as a synthesized summary. Substance is genuinely Nielsen (NN/g: single-rater severity "too unreliable to be trusted"; mean of 3-4 raters within half a point 95% of the time) — the owner should quote *that*, which is real and checkable.
4. **The controlled-degradation methodology's citation trail** (issue-cal:12, :94; README:77). "Synthetic low-quality examples tend to be theatrically bad… producing central tendency bias" is attributed to LLM-Rubric + RULERS + a Label Studio post. None of the three contains this. Central-tendency bias in LLM raters is real in *other* literature, and controlled degradation is a perfectly defensible design choice — but as cited, it is an invented provenance. Defend it as engineering judgment, not as "recommended by NLP evaluation research."
5. **The AI Fluency PDF link** (README:175; framework:169,206). The hash-PDF at www-cdn.anthropic.com is indexed as "6 Techniques for Effective Prompt Engineering," not "AI Fluency: Framework and Foundations." The framework, its authors, the license, and the Irish HEA support are all real — but if an interviewer clicks the link, they get a handout whose title doesn't match the citation, and the framework file's "seven evidence-based techniques" (framework:146) rests on a six-technique handout plus a course-taught meta-technique with an unverifiable quote ("perhaps the most powerful technique of all", framework:165).

## 4. Secondary issues

- **WCAG 1.4.12 misread** (url-mode.md:49, codebase-mode.md:86): 1.4.12 requires content to *survive user-applied* line-height 1.5, not that body text ship at 1.5. An accessibility-literate interviewer will catch this. (The contrast thresholds 4.5:1/3:1 are correctly stated everywhere.)
- **Gist citation** (issue-cal:39): year impossible (2024 vs created 2025-07-11), author is the doc's own heading, raw URL nonstandard. Content claim itself verified.
- **Quickstart over-claim** (issue-cal:29-30): quickstart doesn't cover acceptance criteria.
- **Category error**: CorsoUX (UX site) filed under "SRE runbook structure" (issue-cal:61-72).
- **Source-quality framing**: CorsoUX, ReliablePenguin, OneUptime, Thesius are vendor/SEO blogs; honest attributions, but they sit under a "research" banner. Thesius in particular is an anonymous auto-generated handle promoting a paid product.
- **Title drift**: Scrum Alliance and Label Studio live titles differ from cited titles (URLs correct).

## 5. What genuinely holds up (say these aloud with confidence)

- Nielsen's 10 heuristics, Nielsen's 0-4 severity scale (reproduced *exactly*), frequency/impact/persistence, Hertzum 2006's bibliographic details, Sauro/MeasuringU 2013, WCAG 2.2 (Rec, Oct 2023), Nielsen 1993 ISBN — flawless.
- The GitHub Copilot "ideal task" quote — verbatim-accurate against live GitHub Docs. This is the best single citation in the repo and directly underpins the Files Affected section.
- Sayagh 2025 (say "Sayagh 2025", not "Sayagh et al.") — a real, extremely on-point Dec-2025 paper on issue-readiness for Copilot with 32 quality criteria; it is striking that the *most relevant* paper in the References is one of the correctly-attributed ones.
- The 1,084,300-projects statistic (IEEE paper) and the four-section Copilot plan structure (Overview/Requirements/Implementation Steps/Testing) — both verified.
- The CorsoUX roadmap quote — real, near-verbatim.
- "25+ citations" — exactly 25, verified by count.
- All dates internally consistent (sources ≤ 2026-03-23 vs commits 2026-04-15..24), except the gist's "2024".

## 6. Bottom line for the interview

**Is "research-backed" honest?** Partially. Existence-wise: 30/31 sources check out — far better than typical hallucinated bibliographies, and clearly the product of real searching. Scholarship-wise: 43% of academic author attributions are fabricated, the flagship confidence number has no literature basis, one quotation appears synthesized, and one methodology attribution is invented. The honest framing the owner can defend: *"every source is real and I can show you each one — but I generated the reference list with AI assistance and did not verify author names; here are the corrections."* Fixing the six author lists, relabeling the Anthropic PDF, dropping the "(Nielsen 1993, Hertzum 2006)" prop from the 7% figure, and re-quoting Nielsen from the actual NN/g severity page are a ~1-hour patch that would convert the biggest landmines into a good story about Discernment — which is, ironically, the toolkit's own vocabulary.

**Pre-interview checklist (concrete fixes):**
1. README:179, prompt-cal:14, issue-cal:17 → "Hashemi, H., Eisner, J., Rosset, C., Van Durme, B., & Kedzie, C. (2024)".
2. README:176, issue-cal:41 → "Sülün, E., Saçakçı, M., & Tüzün, E. (2024)".
3. issue-cal:18 → "Hong, Y., et al. (2026)".
4. issue-cal:43 → "Zhang, J., Peng, M., & Zhang, Y. (2024)".
5. issue-cal:45 → "Huang, Y., Costa, D. A., Zhang, F., & Zou, Y. (2019)".
6. issue-cal:47 → "Acharya, J., & Ginde, G. (2025)".
7. README:177 → drop "et al." (sole author).
8. README:92 / framework:192-198 → stop citing literature for the 7% number; own it as self-assessment.
9. framework:196 / prompt-cal:21 → replace the quotation with NN/g's real, checkable sentence about averaging 3-4 evaluators.
10. README:175 / framework:169,206 → label the CDN link as the "6 Techniques" handout or link the actual framework document/course page.
11. issue-cal:39 → "shanelindsay (2025), 'GitHub CLI Workflow for Task Management (IssuePilot)', gist".
12. url-mode:49 / codebase-mode:86 → rephrase 1.4.12 as an adaptability criterion.