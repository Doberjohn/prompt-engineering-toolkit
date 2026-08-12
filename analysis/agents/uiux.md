# Agent report: uiux

## Executive summary

The three UI/UX evaluator prompts are structurally the strongest prompt-engineering work in the repo — 20 identically-named dimensions across all three modes exactly as the README claims, a genuinely good three-tier confidence-labeling system (VERIFIED/INFERRED/SUSPECTED), mandatory "what this mode cannot assess" disclosures, and codebase-mode epistemic rules (negative claims require shown grep output) that target real LLM failure modes; all embedded grep commands are syntactically valid (I executed them). However, the research grounding has verifiable defects: WCAG SC 1.4.12 is misquoted as mandating 1.5 line-height, a 16px minimum font size is presented as WCAG-compliant (no such requirement exists), the 44x44px tap-target figure is the AAA/Apple-HIG number while the actual WCAG 2.2 AA criterion (2.5.8, 24x24px) never appears — indeed none of the nine new-in-2.2 criteria appear anywhere, making the "2.2" label decorative — and the debunked 3-click rule (NN/g: "The 3-Click Rule for Navigation Is False") is a scoring sub-criterion in a framework marketed as NN/g-grounded. The capability-realism problem is concentrated in URL mode: chat AIs fetch pages as markdown text (verified for Claude's web-fetch tool), so its demands to judge load time, layout shift, animation smoothness, blur tests, and color appearance have zero signal to infer from, yet the README compatibility table rates URL mode "Full" on all four surfaces. Additionally, the README's getting-started instructions point at `prompts/uiux-evaluation-prompts.md`, a file deleted on 2026-04-20, and the UI/UX evaluator is the only evaluator in the toolkit with no calibration set, no weights, no aggregate score, and no example outputs.

## Strengths (with evidence)

- **The '20-dimension' claim is exactly accurate and perfectly consistent: all three modes contain the same 20 dimensions with identical names, numbering, and UI(1-10)/UX(11-20) split — zero drift in dimension identity across modes**
  - Evidence: Verified by extracting all numbered headings from the three files (grep -oP '^\*\*\d+\. ' on /home/user/prompt-engineering-toolkit/prompts/uiux-evaluator/{url,screenshot,codebase}-mode.md): each yields the identical list '1. Visual Hierarchy' through '20. Flexibility for Different User Types (Nielsen H7)', matching README.md:68
- **The three-tier confidence-labeling system (VERIFIED/INFERRED/SUSPECTED) with mandatory per-finding format including 'To verify:' instructions is genuinely good epistemic design, rare in prompt engineering**
  - Evidence: url-mode.md:134-145 ('Present every finding using one of three confidence labels. This is mandatory for every single finding - no exceptions'), mirrored at screenshot-mode.md:140-151 and codebase-mode.md:202-213
- **Codebase mode's 'CORE EPISTEMIC RULES' directly target documented LLM failure modes — hallucinated absence claims — by requiring shown grep output for every negative claim**
  - Evidence: codebase-mode.md:11-19: 'Negative claims require proof. If you state something does not exist (e.g. "no focus styles"...), show the grep command you ran and its output to confirm this' and 'Do not summarize exploration results as facts'
- **Each mode carries a mandatory limitations-disclosure section and a cross-mode handoff protocol — the prompts largely DO acknowledge their limits, which is the fair answer to 'does it acknowledge limits?'**
  - Evidence: url-mode.md:168-188 ('EVALUATION GAPS - WHAT THIS MODE CANNOT ASSESS' + 'HANDOFF: [finding] → Verify using [Codebase Mode / Screenshot Mode]'), screenshot-mode.md:174-195, codebase-mode.md:236-254
- **The severity scale is a faithful rendering of Nielsen's real 0-4 severity ratings**
  - Evidence: url-mode.md:153-158 ('0: Not a usability problem... 4: Critical... fix before release') matches Nielsen's published scale (0='not a usability problem', 1='cosmetic problem only', 2='minor', 3='major... high priority', 4='usability catastrophe: imperative to fix before release') per nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/ and measuringu.com/rating-severity/ (web-searched; nngroup.com direct fetch blocked by egress proxy)
- **All eleven embedded grep commands in codebase mode are syntactically valid and return correct matches — none error out**
  - Evidence: Executed every grep from codebase-mode.md:45-47,51-54,67,151-153,162,167,197 verbatim against a scratch fixture repo (/tmp/.../scratchpad/greptest); all exited 0 and matched the planted fixtures (e.g. the dark-pattern pattern 'urgency\|countdown\|limited\|only.*left\|expires' correctly caught 'only 3 left in stock')
- **Correct WCAG AA contrast thresholds are cited (4.5:1 normal text, 3:1 large text and UI components), matching real SC 1.4.3 and 1.4.11**
  - Evidence: url-mode.md:53, screenshot-mode.md:57, codebase-mode.md:91; values confirmed against multiple WCAG references via web search (w3.org direct fetch blocked by proxy)
- **Sub-criteria are deliberately and mostly consistently adapted per mode — screenshot mode softens claims to 'appears', codebase mode adds evidence requirements — showing intentional design rather than copy-paste**
  - Evidence: Compare typography: url-mode.md:49 (hard numbers), screenshot-mode.md:52-54 ('sufficient apparent line height... cannot verify exact font sizes... Flag technical typography findings as Inferred'), codebase-mode.md:85-88 ('Evidence required: File:line references for font definitions')
- **LLM-based heuristic evaluation is a credible emerging instrument, so the concept is not inherently nonsense — peer-reviewed work exists showing moderate consistency**
  - Evidence: 'Catching UX Flaws in Code: Leveraging LLMs to Identify Usability Flaws at the Development Stage' (arXiv 2512.04262, IEEE VL/HCC 2025): GPT-4o applying Nielsen's heuristics to 30 sites, 850+ evaluations — issue detection Cohen's kappa 0.50, 84% exact agreement, severity weighted kappa 0.63, 'requires human oversight' (arxiv.org fetch blocked; results from search)

## Findings

- **[MAJOR] [capability-nonsense]** URL mode instructs the AI to make visual and temporal observations that a chat AI with URL access has zero signal for: page load within 2.5s (LCP), visible layout shift (CLS), smooth transitions, blur tests, F/Z-pattern scanning, and color appearance — chat AI 'browsing' fetches pages as text/markdown without rendering, CSS, JS execution, or timing
  - Evidence: url-mode.md:75 ('Page appears to load within 2.5 seconds (LCP threshold), no visible layout shift after initial load (CLS)'), :80 ('transitions feel smooth and intentional'), :45 ('blur test: primary actions and groupings remain distinguishable when mentally blurred'), :53 (contrast appearance). Anthropic's web-fetch tool 'Fetches a URL, converts the page to markdown' with no rendering (verified via the claude-api skill's server-tools reference and the WebFetch tool contract in this environment). The 'Inferred' hedge (url-mode.md:77) misrepresents zero-signal as weak-signal: there is nothing to infer LOAD TIME from in fetched markdown.
  - Confidence: high for Claude (vendor tool contract verified); medium for ChatGPT/Gemini default chat (vendor docs unreachable through the egress proxy, but their default browsing is also search/text-fetch based; agent modes with visual browsers exist but are not the default surface)
- **[MAJOR] [accuracy]** README model-compatibility row rates UI/UX URL Mode as 'Full' on Claude, ChatGPT, and Gemini — an overclaim, since no default chat surface renders pages visually, which most of URL mode's UI dimensions require
  - Evidence: README.md:105 ('| UI/UX URL Mode | Full | Full | Full | Full |'). Contrast with the honest double-asterisk footnote given to codebase mode (README.md:113) — URL mode gets no equivalent caveat despite needing one more.
  - Confidence: high that 'Full' is unjustified for the visual dimensions; the table has no footnote mechanism engaged for this row
- **[MAJOR] [citation-error]** WCAG SC 1.4.12 is misattributed: the prompts cite it as requiring 'minimum 1.5 line height for body text', but the real SC 1.4.12 (Text Spacing, AA) only requires no loss of content/functionality when the USER overrides line height to 1.5x — it mandates no default line height at all
  - Evidence: url-mode.md:49 ('sufficient line height (minimum 1.5 for body text per WCAG 1.4.12)'), codebase-mode.md:86 ('line height minimum 1.5 for body text (WCAG 1.4.12)'). Real text confirmed via W3C WAI Understanding page and Deque/DigitalA11Y (web search; w3.org direct fetch blocked): 'no loss of content or functionality occurs by setting... line height... to at least 1.5 times the font size'.
  - Confidence: high
- **[MAJOR] [citation-error]** A 16px minimum body-text size is presented as part of WCAG compliance ('10/10: All sub-criteria verified... WCAG-compliant'), but WCAG has no minimum font size at any level — 16px is an industry convention; the real requirement is 200% resize without loss (SC 1.4.4)
  - Evidence: codebase-mode.md:86-87 ('body text minimum 16px... 10/10 definition: All sub-criteria verified from code. Typography is consistent and WCAG-compliant'), url-mode.md:49 ('readable font sizes (minimum 16px body text)'). Multiple accessibility references confirm 'WCAG never specifies a hard minimum pixel size' (web search: a11y-collective, wildandfreetools, section508.gov).
  - Confidence: high
- **[MAJOR] [citation-error]** The 44x44px tap-target minimum is a level conflation: 44x44 is WCAG SC 2.5.5 Target Size (Enhanced), Level AAA (or Apple HIG) — the actual WCAG 2.2 AA criterion is SC 2.5.8 Target Size (Minimum) at 24x24 CSS px, which never appears in a framework branded 'WCAG 2.2 AA'
  - Evidence: url-mode.md:70 ('tap targets minimum 44x44px'), screenshot-mode.md:76, codebase-mode.md:119-121 ('tap targets minimum 44x44px... All tap targets meet minimum size'). Real levels confirmed: 2.5.8 (AA) = 24x24 CSS px with exceptions; 2.5.5 (AAA) = 44x44 (silktide.com, wcag22aa.org, wcag.com via web search). Grep for '24' / '2.5.8' across prompts/uiux-evaluator: zero matches.
  - Confidence: high
- **[MAJOR] [citation-error]** 'WCAG 2.2' is name-dropped, not implemented: none of the nine success criteria new in WCAG 2.2 (2.4.11 Focus Not Obscured, 2.5.7 Dragging Movements, 2.5.8 Target Size Minimum, 3.2.6 Consistent Help, 3.3.7 Redundant Entry, 3.3.8 Accessible Authentication, etc.) appear in any of the three prompts — every listed accessibility check is WCAG 2.0/2.1-era
  - Evidence: Grep across /home/user/prompt-engineering-toolkit/prompts/uiux-evaluator for '2\.4\.11|2\.5\.7|2\.5\.8|3\.2\.6|3\.3\.7|3\.3\.8|Focus Not Obscured|Dragging|Redundant Entry|Accessible Authentication|Consistent Help' (case-insensitive): 'No matches found'. WCAG 2.2's new-criteria list confirmed via web search (vispero.com, testparty.ai, w3.org/TR/WCAG22 in search results).
  - Confidence: high
- **[MAJOR] [debunked-research]** The 3-click rule is embedded as a scoring sub-criterion in a framework marketed as 'grounded in established research — Nielsen's... NN/G studies', but NN/g itself published 'The 3-Click Rule for Navigation Is False' and the only empirical test (Porter/UIE 2003, 44 users, 620 tasks) found no correlation between click count and success or satisfaction
  - Evidence: url-mode.md:113-114 ('any target user can reach any primary content within 3 clicks from the homepage... Primary content reachable within 3 clicks'), codebase-mode.md:176-177 ('Verify that primary content is reachable within 3 clicks from root... Evidence required: Route map with click depth'). README.md:32 makes the research-grounding claim. nngroup.com/articles/3-click-rule/ title and Porter findings confirmed via web search.
  - Confidence: high
- **[MAJOR] [documentation]** The README's getting-started instructions for the UI/UX evaluator point at a file that was deleted ~4 months ago: `prompts/uiux-evaluation-prompts.md` was removed in commit f6c1216 (2026-04-20) when the content was split into the three mode files, but README step 1 still says to open it
  - Evidence: README.md:137 ('1. Open `prompts/uiux-evaluation-prompts.md`'); git show f6c1216 --stat: '2026-04-20 Delete prompts/uiux-evaluation-prompts.md | 689 deletions'; find confirms only prompts/uiux-evaluator/{url,screenshot,codebase}-mode.md exist; last repo commit before the audit was 2026-04-24, so the break has stood since then
  - Confidence: high
- **[MAJOR] [incomplete]** Only 7 of Nielsen's 10 heuristics are mapped into the 20 dimensions (H1, H2, H3, H5, H6, H7, H9); H4 Consistency and Standards is covered by dimension 5 but unattributed, and H8 Aesthetic and Minimalist Design and H10 Help and Documentation are absent entirely — with no acknowledgment, despite the persona claiming 'deep knowledge of Nielsen's 10 Usability Heuristics' and the README claiming the prompts are 'Built on Nielsen's heuristics'
  - Evidence: Dimension extraction shows Nielsen tags only on dimensions 11 (H1), 12 (H2), 13 (H3), 14 (H5+H9), 15 (H6), 20 (H7). No dimension addresses help/documentation (H10). Real 10-heuristic list confirmed via web search of nngroup.com/articles/ten-usability-heuristics/ (direct fetch blocked). Persona claim at url-mode.md:9, screenshot-mode.md:9, codebase-mode.md:9; README.md:68.
  - Confidence: high
- **[MAJOR] [incomplete]** The UI/UX evaluator is the only evaluator in the toolkit with no calibration set, no example outputs, no weights, no aggregation formula, and no overall score — in a toolkit whose central differentiator is calibration ('Calibrated against real examples') and whose two sibling evaluators both ship calibration sets; the LLM heuristic-eval literature (kappa=0.50 issue-detection agreement for GPT-4o) predicts 20 independent 1-10 scores will not be reproducible run-to-run without anchors
  - Evidence: examples/ contains only prompt-calibration-set.md and issue-calibration-set.md (find output); README.md:34 (calibration claim), README.md:73-77 (both sibling calibration sets described); no aggregation/weighting instruction anywhere in the three mode files (the only formulas in the repo belong to the issue evaluator). Reliability figure from arXiv 2512.04262 / IEEE VL/HCC 2025 (web search).
  - Confidence: high for the absence; medium for the reproducibility prediction (inferred from published GPT-4o results, not tested on these prompts)
- **[MAJOR] [internal-contradiction]** Codebase mode's section header asserts 'UI DIMENSIONS (All verifiable from code)' but its own Step 5 disclosure contradicts this — visual hierarchy, 'generous negative space', crowdedness, and the 'blur test' cannot be verified from unrendered code, as the prompt itself admits five sections later
  - Evidence: codebase-mode.md:76 ('### UI DIMENSIONS (All verifiable from code)') vs codebase-mode.md:241 ('Actual visual rendering (colors, spacing, typography render differently in browser than in code)'); also :79 asks to 'Apply the blur test mentally' to source code
  - Confidence: high
- **[MINOR] [capability]** Codebase mode requires shown contrast-ratio calculations for every text/background pair but never instructs the agent to compute them with a script — WCAG relative luminance involves nonlinear sRGB math (per-channel ^2.4 gamma expansion) that LLMs are unreliable at via mental arithmetic, even though the target environment (Claude Code) could trivially run the computation in code; it also assumes design tokens reveal which color pairs actually co-occur, which they don't
  - Evidence: codebase-mode.md:91-95 ('Calculate contrast ratios against WCAG 2.2 AA thresholds... Contrast ratio calculation shown for each combination... This is the only mode that can produce VERIFIED contrast findings') — no mention of writing/running a script anywhere in the file
  - Confidence: high that no script instruction exists; medium on practical impact (a strong agent may write a script unprompted)
- **[MINOR] [tooling]** All eleven embedded grep commands lack --exclude-dir for node_modules/dist/build, so in real JS/TS repos they traverse dependencies and return noise; several patterns are also extremely low-precision ('error' matches nearly every source file, 'role' matches 'roles', 'limited' matches 'unlimited')
  - Evidence: Executed codebase-mode.md:151 ('grep -r "loading\|isLoading\|spinner\|skeleton" --include="*.tsx" ... -l') and :152 in a fixture repo containing node_modules/somepkg/src/index.tsx — both returned the node_modules file. Patterns at codebase-mode.md:152 ('error\|ErrorBoundary'), :197 ('shortcut\|hotkey\|advanced\|role\|permission'), :67 ('limited')
  - Confidence: high (reproduced in sandbox)
- **[MINOR] [capability-nonsense]** Screenshot mode's accessibility sub-criterion 'Images appear to have alt text context (though cannot verify)' is incoherent — alt text is invisible in rendered pixels, so there is nothing for it to 'appear' as; the parenthetical concedes the criterion is unevaluable while still listing it for scoring
  - Evidence: screenshot-mode.md:71 ('Images appear to have alt text context (though cannot verify)')
  - Confidence: high
- **[MINOR] [capability]** Screenshot mode asks whether 'tap targets appear minimum 44x44px', but a screenshot carries no CSS-pixel scale — device pixel ratio and capture resolution are unknown — so a vision model cannot estimate 44px even approximately without an in-image reference
  - Evidence: screenshot-mode.md:76 ('tap targets appear minimum 44x44px'); no instruction anywhere to ask the user for viewport size or DPR
  - Confidence: high on the physics; the 'appear' hedge partially mitigates
- **[NITPICK] [internal-consistency]** URL mode's gap list claims exact contrast values 'require codebase mode for hex verification', but for public sites the CSS containing those hex values is fetchable in URL mode itself — the mode boundary is overstated
  - Evidence: url-mode.md:174 ('Exact contrast ratio values (requires codebase mode for hex verification)')
  - Confidence: medium (minified/bundled CSS makes it harder in practice, so the simplification is defensible)
- **[NITPICK] [drift]** The only output-format drift between modes: codebase mode's Step 7 roadmap adds a File:line field and quantifies effort in hours ('Low (CSS/copy change, < 1 hour)') while URL/screenshot modes use unquantified Low/Medium/High — plausibly intentional, but undocumented
  - Evidence: codebase-mode.md:265-267 vs url-mode.md:196-200 and screenshot-mode.md:201-207
  - Confidence: high (direct comparison)
- **[MINOR] [professional-practice]** The prompts never mention the professional deterministic instruments for the mechanical half of the work — axe-core, WAVE, or pa11y — even though those compute contrast, alt-text, and ARIA checks exactly and for free; Lighthouse is referenced only for performance. A sharp interviewer will ask why an LLM should eyeball what axe-core measures; the defensible answer (LLM covers the heuristic-judgment dimensions automation cannot) is never articulated in the prompts. Professional heuristic evaluation also uses 3-5 independent evaluators (a single evaluator finds roughly a third of problems per Nielsen); the prompts run one evaluator with no aggregation guidance.
  - Evidence: Grep for 'axe|WAVE|pa11y' in prompts/uiux-evaluator: no matches; 'Lighthouse' appears only at url-mode.md:176 and codebase-mode.md:243,247 (performance context). Multi-evaluator practice per Nielsen's heuristic-evaluation methodology (nngroup, via search).
  - Confidence: high on the absence; the README's separate single-evaluator acknowledgment (README.md:92) partially covers this but sits outside these prompts

## Open questions

- Cross-cutting (README agent's lane): README.md:137's broken `prompts/uiux-evaluation-prompts.md` path and the README.md:105-107 compatibility rows are README defects surfaced here because they gate access to my lane's files — flag to the README/sibling auditor to avoid double-counting.
- Cross-cutting (framework agent's lane): the '93% confidence / 7% irreducible subjectivity' claim (README.md:90-92) cites Nielsen 1993 and Hertzum 2006 — whether those sources support a quantified 93% is outside my lane but interacts with my finding that the UI/UX evaluator has zero validation evidence.
- Unverifiable through the egress proxy: nngroup.com, w3.org, arxiv.org, docs.anthropic.com, and OpenAI/Google docs were all blocked; Nielsen's heuristics list, severity scale, WCAG SC details, and the VL/HCC 2025 paper results were verified via multiple concordant secondary sources in web search instead — confidence remains high for the WCAG/Nielsen facts (stable, multiply-attested), but ChatGPT/Gemini default-chat rendering capabilities specifically could not be vendor-verified and are marked medium confidence.
- Could not test the prompts end-to-end against a real site/screenshot/repo within audit scope — the reproducibility concern (20 unanchored 1-10 scores) is grounded in published GPT-4o reliability figures, not a measured run-to-run variance on these exact prompts; a defender could counter by running the same input twice and showing score stability.
- Interview-prep note for synthesis: the highest-yield hostile questions in this lane are (1) 'Name one success criterion that is new in WCAG 2.2' (none appear in the prompts; the 44px figure is AAA), (2) 'What does the model actually receive when you give it a URL?', (3) 'Which of Nielsen's 10 heuristics does your 20-dimension system NOT cover?' (H8, H10), (4) 'Why not axe-core for the objective half?', and (5) 'Where is the calibration set for this evaluator?'

---

## Full report


# Audit: UI/UX Evaluator Prompts (url-mode.md, screenshot-mode.md, codebase-mode.md)

**Auditor lane:** the three UI/UX evaluation prompts in `/home/user/prompt-engineering-toolkit/prompts/uiux-evaluator/`.
**Files:** `url-mode.md` (205 lines), `screenshot-mode.md` (212 lines), `codebase-mode.md` (272 lines). Last substantive commits 2026-04-24; audited 2026-08-12.

**Verification constraints:** the sandbox egress proxy blocked direct fetches of nngroup.com, w3.org, arxiv.org, docs.anthropic.com. Nielsen's heuristics/severity scale, WCAG 2.2 SC details, and the cited arXiv paper were verified via multiple concordant secondary sources through WebSearch (marked below). Claude's web-fetch behavior was verified from the authoritative claude-api skill reference and the WebFetch tool contract in this environment. All grep-command tests were executed in a sandbox.

---

## 1. The 20-dimension claim (README.md:68) — TRUE, and perfectly consistent

README.md:68: *"a 20-dimension scoring system covering both UI (objective) and UX (heuristic inference)"*.

Verified by extracting every numbered dimension heading from all three files: **each mode contains exactly 20 dimensions, identically named and numbered**, split 1–10 UI / 11–20 UX:

1. Visual Hierarchy · 2. Typography · 3. Color and Contrast · 4. Spacing and Layout · 5. Component and Design System Consistency · 6. Accessibility (WCAG 2.2 AA) · 7. Responsive and Mobile Behavior · 8. Performance Indicators · 9. Motion and Animation Quality · 10. Dark Pattern Detection · 11. System Status Visibility (Nielsen H1) · 12. Real-World Language Match (Nielsen H2) · 13. User Control and Freedom (Nielsen H3) · 14. Error Prevention and Recovery (Nielsen H5 + H9) · 15. Cognitive Load and Recognition over Recall (Nielsen H6) · 16. Information Architecture · 17. Task Flow Clarity · 18. Microcopy and Content Quality · 19. Trust Signals and Conversion Path Clarity · 20. Flexibility for Different User Types (Nielsen H7)

**Drift across modes:** dimension identity has zero drift. Sub-criteria are deliberately adapted per mode (URL mode uses hard numbers, screenshot mode softens to "appears"/"apparent", codebase mode adds "Evidence required" clauses) — this is intentional design, and it is done consistently. Scales (1–10) and severity (0–4) are identical across modes. The *only* output-format drift found: codebase mode's Step 7 roadmap adds a `File:line reference` field and quantifies effort in hours (`Low (CSS/copy change, < 1 hour)`, codebase-mode.md:265–267) where URL/screenshot use unquantified `Low (CSS/copy change)` (url-mode.md:200, screenshot-mode.md:207). Nitpick-level, plausibly intentional.

**No weights exist.** The README claims a "scoring system", not a weighted one, so this is not a contradiction — but there is **no aggregation formula, no overall score, and no weighting** anywhere in the three files, in contrast to the issue evaluator's weighted formula. Twenty independent 1–10 scores with no roll-up is a real gap for actionability (see §6).

## 2. Nielsen verification — scale faithful; heuristic coverage incomplete

Real list (verified via WebSearch of nngroup.com/articles/ten-usability-heuristics/ and multiple mirrors; direct fetch blocked): 1 Visibility of System Status · 2 Match Between System and the Real World · 3 User Control and Freedom · 4 Consistency and Standards · 5 Error Prevention · 6 Recognition Rather than Recall · 7 Flexibility and Efficiency of Use · 8 Aesthetic and Minimalist Design · 9 Help Users Recognize, Diagnose, and Recover from Errors · 10 Help and Documentation.

**Correct:** every Nielsen tag used in the prompts maps to the right heuristic number — H1→dim 11, H2→dim 12, H3→dim 13, H5+H9→dim 14 (a legitimate pairing), H6→dim 15, H7→dim 20. No invented or misnumbered heuristics. The 0–4 severity scale (url-mode.md:153–158 and identical in the other modes) is a faithful paraphrase of Nielsen's real scale (0 "not a usability problem" … 4 "usability catastrophe: imperative to fix before release" — nngroup severity article + measuringu.com/rating-severity, via search). Reporting frequency as a separate field is a deviation from Nielsen (whose severity *combines* frequency/impact/persistence) but a defensible, arguably cleaner one.

**Incomplete:** only **7 of 10 heuristics** are mapped (H1, H2, H3, H5, H6, H7, H9). **H4 Consistency and Standards** is functionally covered by dimension 5 but never attributed. **H8 Aesthetic and Minimalist Design** and **H10 Help and Documentation** are absent — no dimension anywhere evaluates help/documentation. This is unacknowledged while the persona claims "deep knowledge of Nielsen's 10 Usability Heuristics" (all three files, line 9) and README:68 says "Built on Nielsen's heuristics". Interview question waiting to happen.

## 3. WCAG verification — the weakest research grounding in the lane

Verified against secondary sources mirroring w3.org/TR/WCAG22 (direct fetch blocked; sources: W3C WAI Understanding pages surfaced in search, Deque, Silktide, wcag22aa.org, Vispero, TestParty):

| Prompt claim | Reality | Verdict |
|---|---|---|
| 4.5:1 normal / 3:1 large text & UI components (url:53, screenshot:57, codebase:91) | SC 1.4.3 (AA) + SC 1.4.11 (AA) | **Correct** |
| "minimum 1.5 line height for body text per WCAG 1.4.12" (url:49, codebase:86) | SC 1.4.12 Text Spacing (AA) requires **no loss of content when the user overrides** line height to 1.5×; it mandates **no default** line height | **Misattributed** |
| "body text minimum 16px" under a 10/10 defined as "WCAG-compliant" (codebase:86–87; url:49) | WCAG has **no minimum font size** at any level; the real requirement is 200% resize (SC 1.4.4). 16px is browser-default convention | **False as WCAG** |
| "tap targets minimum 44x44px" (url:70, screenshot:76, codebase:119–121) | 44×44 is SC **2.5.5 Target Size (Enhanced), Level AAA** (and Apple HIG). The **WCAG 2.2 AA** criterion is SC **2.5.8 Target Size (Minimum): 24×24** CSS px | **Level conflation** |
| "no content flashes more than 3 times per second" (url:65) | SC 2.3.1 (Level A) | Correct-ish (A, included in AA conformance) |
| prefers-reduced-motion expected for a 10/10 (codebase:130–134) | Maps to SC 2.3.3 Animation from Interactions, **AAA** | Beyond-AA requirement, unlabeled |
| "meaningful title" (url:65) | SC 2.4.2 (A) | Correct |

**The headline finding:** grep across all three prompts for any WCAG-2.2-specific criterion — `2.4.11, 2.5.7, 2.5.8, 3.2.6, 3.3.7, 3.3.8, Focus Not Obscured, Dragging, Redundant Entry, Accessible Authentication, Consistent Help` — returns **zero matches**. Every accessibility check listed is WCAG 2.0/2.1-era. "WCAG 2.2 AA" is name-dropped as a brand, not implemented as a checklist; the one place a 2.2-specific number could have appeared (target size), the prompt uses the AAA figure instead. A prepared interviewer who asks "name one thing that's new in WCAG 2.2" lands a direct hit.

**Also in this bucket:** the **3-click rule** is a scoring sub-criterion (url:113–114 "any target user can reach any primary content within 3 clicks from the homepage"; codebase:176–177 requires a click-depth route map as evidence). NN/g's own article is titled *"The 3-Click Rule for Navigation Is False"* (nngroup.com/articles/3-click-rule/, via search), and the only empirical test (Porter/UIE 2003: 44 users, 620 tasks) found **no correlation** between clicks and success or satisfaction. For a framework whose README claims grounding in "Nielsen's 10 Usability Heuristics, WCAG 2.2 AA, NN/G studies" (README:32), embedding a rule NN/g explicitly debunked is a credibility problem. (The "5 seconds to understand the product" criterion in dim 19, by contrast, echoes the legitimate five-second-test method — no flag.)

## 4. Capability realism — where the nonsense lives

### URL mode — the weakest mode by far
What a chat AI actually receives from a URL: **text/markdown extraction**. Verified for Claude — the web-fetch tool "Fetches a URL, converts the page to markdown"; no rendering, no CSS application, no JS execution, no timing, no screenshots (claude-api skill server-tools reference + this environment's WebFetch contract). ChatGPT/Gemini default chat browsing is likewise search/text-fetch based (vendor docs unreachable through proxy — medium confidence; their *agent* modes with visual browsers exist but are not the paste-a-prompt chat surface this file targets: "paste it into a new AI session", url-mode.md:5).

Against that reality, URL mode asks the model to score:
- **Dim 8 Performance:** "Page appears to load within 2.5 seconds (LCP threshold), no visible layout shift after initial load (CLS)" (url:75). A text fetch has **no notion of load time or layout** — there is nothing to infer from. The hedge "All performance findings are Inferred" (url:77) misframes zero-signal as weak-signal.
- **Dim 9 Motion:** "transitions feel smooth and intentional" (url:80). Nothing moves in markdown.
- **Dim 1 Visual Hierarchy:** "blur test: primary actions... remain distinguishable when mentally blurred" (url:45). There is no rendered visual to blur.
- **Dims 2–5** (typography appearance, contrast appearance, spacing, component consistency) all presuppose seeing the rendered page.
- Dim 10 dark patterns, dims 11–20 UX language/flow analysis, and the accessibility checks that live in HTML attributes **are** partially feasible from fetched HTML/text — the mode is not uniformly nonsense.

To be fair: URL mode's Step 1 pre-flight and Step 5 gaps list hedge many things (hover/focus states as inaccessible, CWV as imprecise). But the hedging systematically says "imprecise/Inferred" where the honest statement is "not observable at all", and the README then rates the mode "Full" everywhere (§5).

### Screenshot mode — mostly honest, two incoherent criteria
Vision models genuinely can assess hierarchy, spacing, copy, consistency, dark patterns from screenshots, and this file's hedging is the best of the three ("Screenshot mode cannot measure exact contrast ratios. All contrast findings are Inferred", screenshot:59 — accurate: JPEG/AA artifacts and perception make pixel-precise ratios unreliable). Two exceptions:
- "Images appear to have alt text context (though cannot verify)" (screenshot:71) — **alt text is invisible in pixels**; the criterion is meaningless as written.
- "tap targets appear minimum 44x44px" (screenshot:76) — a screenshot has **no CSS-px scale** (unknown DPR/capture resolution); 44px cannot be estimated without a reference, and the prompt never asks for viewport metadata.

### Codebase mode — deployable and mostly feasible, with three defects
This is the strongest mode: repo access + grep is a real capability, the epistemic rules (codebase:11–19) are excellent, and README footnote ** correctly restricts it to agentic environments.
- **Grep commands: all syntactically valid.** I executed every one of the eleven commands (codebase:45–47, 51–54, 67, 151–153, 162, 167, 197) verbatim in a fixture repo — all ran clean and matched planted content (GNU grep BRE `\|` alternation works as written).
- **But no `--exclude-dir`:** the same test confirmed the greps match files inside `node_modules/` (fixture `node_modules/somepkg/src/index.tsx` was returned by the dim-11 and dim-14 greps). In any real JS repo with installed deps these commands are slow and noisy. Several patterns are also low-precision by construction: `error` (dim 11/14) matches nearly every file, `role` (dim 20) matches "roles", `limited` (dim 10) matches "unlimited".
- **Internal contradiction:** header "UI DIMENSIONS (All verifiable from code)" (codebase:76) vs its own Step 5 admission "Actual visual rendering (colors, spacing, typography render differently in browser than in code)" (codebase:241). Visual hierarchy, "generous negative space", crowdedness, and "Apply the blur test mentally" (codebase:79) are not verifiable from unrendered source.
- **Contrast math:** dim 3 demands "Contrast ratio calculation shown for each combination" (codebase:94) with "This is the only mode that can produce VERIFIED contrast findings" (codebase:95). WCAG relative luminance requires per-channel nonlinear sRGB math (( (c+0.055)/1.055 )^2.4) — unreliable as LLM mental arithmetic — and the prompt never says "write a script", even though its target environment (Claude Code) makes that trivial. Also, design tokens don't record which text/background pairs actually co-occur, so "every combination verified" overstates what token files can prove.

## 5. README compatibility table (README.md:105–107)

| Row | Claim | Verdict |
|---|---|---|
| 105 UI/UX URL Mode | Full / Full / Full / Full | **Overclaimed.** No default chat surface renders pages; most UI dimensions (1–5, 8, 9) are unevaluable as specified. Verified for Claude; medium confidence for ChatGPT/Gemini. The row deserves at least the asterisk treatment codebase mode gets. |
| 106 UI/UX Screenshot Mode | Full / Full / Full / Full | **Roughly fair** — all four surfaces accept images; within-mode limitations are (mostly) self-disclosed. |
| 107 UI/UX Codebase Mode | Full / Partial** / Partial** / Full | **Accurate and honestly footnoted** (README:113: grep + file:line require an agentic environment). The one caveat: "Claude | Full" for codebase mode is odd since plain Claude chat cannot run grep either — the footnote logic applied to ChatGPT/Gemini applies equally to non-Code Claude. |

Related: README:137 tells users to "Open `prompts/uiux-evaluation-prompts.md`" — that file was **deleted in commit f6c1216 on 2026-04-20** (689 lines) when the content was split into the three mode files; the README was never updated. The primary user path to this lane's deliverable has been broken for ~4 months.

## 6. Is an LLM prompt a credible instrument here? (vs. axe-core/Lighthouse/professional practice)

- **The concept is defensible.** Peer-reviewed precedent exists: *"Catching UX Flaws in Code: Leveraging LLMs to Identify Usability Flaws at the Development Stage"* (arXiv 2512.04262, IEEE VL/HCC 2025) ran GPT-4o Nielsen-heuristic evaluations on 30 open-source sites (850+ evaluations): issue-detection consistency was **moderate** (mean pairwise Cohen's κ=0.50, 84% exact agreement), severity κ_w=0.63, conclusion "requires human oversight". So codebase-style LLM heuristic evaluation is a real, publishable direction — and its measured reliability is exactly why 20 unanchored 1–10 scores per run should not be presented as stable measurements.
- **The mechanical half belongs to deterministic tools.** Professionals run axe-core/WAVE/pa11y/Lighthouse for contrast, alt text, ARIA, target size, CWV — exact, free, reproducible. The prompts never mention axe-core, WAVE, or pa11y (grep: zero matches); Lighthouse appears only in performance gap notes (url:176, codebase:243/247). The strong defense — "the LLM covers heuristic-judgment dimensions no automated tool can, and should delegate the mechanical checks" — is never articulated. As written, the prompts have the LLM eyeball what axe-core computes.
- **Single-evaluator design.** Nielsen's own methodology calls for 3–5 independent evaluators because one evaluator finds roughly a third of problems. The prompts are single-run with no aggregation guidance. (The README's general "single-evaluator" acknowledgment at README:92 partially covers this, but sits outside these prompts and belongs to another auditor's lane.)
- **No validation artifacts for this evaluator.** `examples/` contains calibration sets for the prompt evaluator and issue evaluator only. The UI/UX evaluator — three files, ~690 lines, a fifth of the repo — has zero anchors, zero example outputs, zero scoring-consistency evidence. For a toolkit whose "Why this exists" section is *"prompts were evaluated, scored, revised, and rescored... Calibrated against real examples"* (README:33–34), this is the biggest incompleteness in the lane.

## 7. What is genuinely good (don't undersell in the interview)

1. **Dimension architecture is real and disciplined** — 20 dimensions, identical across modes, with mode-appropriate sub-criteria adaptation. The README's structural claim checks out exactly.
2. **The confidence-label system (VERIFIED/INFERRED/SUSPECTED)** with mandatory per-finding formats and "To verify:" pointers is better epistemic hygiene than most professional prompt work.
3. **Codebase mode's epistemic rules** ("Negative claims require proof... show the grep command you ran and its output"; "Do not summarize exploration results as facts") directly counter the most common LLM audit failure — confidently asserting absence. This is the strongest single piece of prompt engineering in the repo.
4. **Mandatory limitations disclosure + cross-mode handoffs** (Steps 5–6 in every mode) — the prompts do largely acknowledge their limits, and the triage design (URL → screenshot → codebase → user testing) is genuinely sensible system thinking.
5. **Nielsen severity scale is faithful**, contrast thresholds are correct, and all grep commands execute.

## 8. Hard interviewer questions this lane exposes

1. "Your accessibility dimension says WCAG 2.2 AA. Name one success criterion that's new in 2.2." (None appear; the 44px figure is the AAA number; the actual new AA target-size criterion is 24px.)
2. "Walk me through what the model actually receives when I paste your URL-mode prompt plus a URL into Claude. How does it measure a 2.5-second LCP from markdown?"
3. "Which of Nielsen's 10 heuristics does your 20-dimension system not cover?" (H8, H10; H4 unattributed.)
4. "NN/g published 'The 3-Click Rule for Navigation Is False.' Why is it a scoring criterion in your NN/g-grounded framework?"
5. "Why would I use this instead of axe-core for contrast and ARIA? Where do you tell the model to delegate to deterministic tools?"
6. "Your README says everything is calibrated against real examples. Where's the UI/UX calibration set? If I run the same screenshot twice, do I get the same 20 scores?"
7. "How do 20 scores become a decision? There's no weighting or overall score."
8. "Your README's getting-started step points at a file you deleted in April."

## Findings index (atomic, most severe first)
1. **major/capability-nonsense** — URL mode demands unobservable visual/temporal judgments (LCP, CLS, motion, blur test, contrast appearance) from a text-fetch surface; "Inferred" hedging misframes zero signal (url:45,53,75-77,80-82).
2. **major/accuracy** — README:105 rates URL mode "Full" on all four surfaces.
3. **major/citation-error** — SC 1.4.12 misquoted as mandating 1.5 line-height (url:49, codebase:86).
4. **major/citation-error** — 16px minimum presented as WCAG-compliant (codebase:86-87, url:49); WCAG has no minimum font size.
5. **major/citation-error** — 44×44px is AAA/HIG, not 2.2 AA; real AA is 2.5.8 @ 24×24, never mentioned (url:70, screenshot:76, codebase:119-121).
6. **major/citation-error** — zero WCAG-2.2-specific criteria anywhere; "2.2" is decorative (grep verified).
7. **major/debunked-research** — 3-click rule as scoring criterion vs NN/g's own debunking (url:113-114, codebase:176-177; README:32).
8. **major/documentation** — README:137 points at file deleted 2026-04-20 (commit f6c1216).
9. **major/incomplete** — only 7/10 Nielsen heuristics mapped; H8, H10 absent, H4 unattributed; unacknowledged.
10. **major/incomplete** — no calibration set, weights, aggregate score, or example outputs for this evaluator; reliability unaddressed (κ=0.50 precedent).
11. **major/internal-contradiction** — "All verifiable from code" (codebase:76) vs codebase:241's own disclaimer; mental blur test on source code (codebase:79).
12. **minor/capability** — contrast calculations demanded without instructing script use; token pairs don't prove co-occurrence (codebase:91-95).
13. **minor/tooling** — greps lack --exclude-dir (node_modules noise reproduced in sandbox); low-precision patterns (`error`, `role`, `limited`).
14. **minor/capability-nonsense** — "Images appear to have alt text context" in a screenshot (screenshot:71).
15. **minor/capability** — 44px tap-target estimation from a scale-less screenshot (screenshot:76).
16. **nitpick/internal-consistency** — URL mode claims hex verification needs codebase mode though CSS is fetchable (url:174).
17. **nitpick/drift** — codebase roadmap adds file:line + hour-quantified effort vs other modes (codebase:265-267).
18. **minor/professional-practice** — axe-core/WAVE/pa11y never mentioned; single-evaluator with no aggregation guidance; the LLM-vs-automation division of labor never articulated.
