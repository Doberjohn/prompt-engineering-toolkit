# Issue Calibration Set
## Ten Scored Anchor Issues for the Implementation Plan Issue Validator

---

## Methodology and Research Basis

This calibration set was built on a foundation of primary research across four distinct source categories. Every claim in the section weight mapping and scoring scale is traceable to a specific source. This section exists so any developer can verify, challenge, or extend the framework independently.

### How this was built

The calibration set uses controlled degradation of a single real issue (Inkweave #278, produced by Claude Code) rather than synthetic generation. This approach is grounded in NLP evaluation research which shows that synthetic low-quality examples tend to be theatrically bad rather than realistically bad, producing central tendency bias in evaluators. The degradation approach ensures every anchor traces to a real artifact with a known quality baseline.

Scores were assigned by the subject matter expert (the developer who owns the repository and wrote the original prompt) against the eight-section rubric. This follows the standard for ground truth calibration sets in LLM evaluation research, which requires human expert judgment rather than automated scoring.

Sources used to verify this approach:
- Eisenstein, J., et al. (2024). *LLM-Rubric: A Multidimensional, Calibrated Approach to Automated Evaluation of Natural Language Texts*. Proceedings of ACL 2024. https://aclanthology.org/2024.acl-long.745.pdf
- Holterman, B., et al. (2026). *Rulers: Locked Rubrics and Evidence-Anchored Scoring for Robust LLM Evaluation*. arXiv preprint. https://arxiv.org/html/2601.08654
- Label Studio. (2026). *How to Scale Evaluation for RAG and Agent Workflows*. https://labelstud.io/blog/how-to-scale-evaluation-for-rag-and-agent-workflows/

---

### Research basis for the eight sections

The eight sections were derived from three converging research areas: GitHub issue completeness research, Agile task documentation standards, and SRE runbook structure frameworks. All three independently converge on the same core sections, which is why the mapping carries high confidence.

**GitHub issue completeness research**

- GitHub. (2025). *Quickstart for GitHub Issues*. GitHub Docs. https://docs.github.com/en/issues/tracking-your-work-with-issues/learning-about-issues/quickstart
  - Confirms: title, description, acceptance criteria as baseline requirements
- GitHub. (2025). *Best Practices for Projects*. GitHub Docs. https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/best-practices-for-projects
  - Confirms: sub-issues, dependencies, milestones as structural components
- GitHub. (2025). *Best Practices for Using GitHub Copilot to Work on Tasks*. GitHub Docs. https://docs.github.com/en/copilot/tutorials/cloud-agent/get-the-best-results
  - Confirms: "An ideal task includes a clear description, complete acceptance criteria, and directions about which files need to be changed." This is the source for the Files Affected section.
- GitHub Blog. (2025). *How to Create Issues and Pull Requests in Record Time on GitHub*. https://github.blog/developer-skills/github/how-to-create-issues-and-pull-requests-in-record-time-on-github/
  - Confirms: action-forward title, problem description, acceptance criteria / definition of done as the GitHub-recommended checklist
- GitHub Blog. (2025). *From Idea to PR: A Guide to GitHub Copilot's Agentic Workflows*. https://github.blog/ai-and-ml/github-copilot/from-idea-to-pr-a-guide-to-github-copilots-agentic-workflows/
  - Confirms: GitHub Copilot's own planning mode generates four sections: Overview, Requirements, Implementation Steps, Testing. This is the direct source for including Testing/Verification as a mandatory section.
- IssuePilot. (2024). *GitHub CLI Workflow for Task Management — Issue Body Structure*. Community resource. https://gist.githubusercontent.com/raw/c9efc3e0e4fb81b4aefa3bf43d22391b
  - Confirms: the Why/What/How structure — Description (Why), Acceptance Criteria (What), Implementation Plan (How) — as the canonical three-part structure for task issues
- Li, X., et al. (2024). *An Empirical Analysis of Issue Templates Usage in Large-Scale Projects on GitHub*. ACM Transactions on Software Engineering and Methodology. https://dl.acm.org/doi/10.1145/3643673
  - Empirical evidence that structured templates improve issue resolution time, reduce reopening rates, and increase project productivity. Peer-reviewed source confirming that structure matters.
- Wang, Y., et al. (2024). *Empirical Study on GitHub Issue Report Templates*. IEEE Conference Publication. https://ieeexplore.ieee.org/document/10633301/
  - Confirms: adoption of issue templates is associated with increased project productivity and more successful projects across 1,084,300 projects.
- Arya, D., et al. (2018). *An empirical study on the issue reports with questions raised during the issue resolving process*. Empirical Software Engineering. https://link.springer.com/article/10.1007/s10664-018-9636-3
  - Confirms: unnecessary questions raised during issue resolution cause significant delays. Complete upfront context — the why, prerequisites, and acceptance criteria — reduces resolution time.
- Zhang, Y., et al. (2025). *Can We Enhance Bug Report Quality Using LLMs? An Empirical Study of LLM-Based Bug Report Generation*. Proceedings of EASE 2025. https://arxiv.org/pdf/2504.18804
  - Confirms: issue quality evaluated on five dimensions — Atomicity, Conciseness, Completeness, Understandability, Reproducibility. Completeness and Reproducibility map directly to our Acceptance Criteria and Testing/Verification sections.

**Agile task documentation standards**

- Atlassian. (2025). *What is Acceptance Criteria? Definition, Examples, and Tips*. https://www.atlassian.com/work-management/project-management/acceptance-criteria
  - Confirms: acceptance criteria are the specific conditions that must be satisfied for a task to be considered complete. Source for the Definition of Done concept.
- Scrum Alliance. (2023). *What You Need to Know About Acceptance Criteria*. https://resources.scrumalliance.org/Article/need-know-acceptance-criteria
  - Confirms: acceptance criteria must be pass/fail, outcome-oriented, and defined before development begins.
- ArgonDigital. (2023). *User Stories and Technical Stories in Agile Development*. https://argondigital.com/blog/product-management/user-stories-technical-stories-agile-development-productmanagement/
  - Confirms: technical implementation plan issues require a different structure than user stories, with technical acceptance criteria and file-level specificity.
- ZenHub. (2021). *GitHub Best Practices: Taking Issues from Good to Great*. https://www.zenhub.com/blog-posts/best-practices-for-github-issues
  - Confirms: issues should use markdown checklists for acceptance criteria and sub-tasks. Source for the checkbox format recommendation.

**SRE runbook structure**

- OneUptime. (2026). *How to Create Effective Runbooks*. https://oneuptime.com/blog/post/2026-02-02-effective-runbooks/view
  - Confirms: every effective runbook must include metadata header, prerequisites, step-by-step procedure, verification, and rollback. Rollback section described as non-negotiable for any procedure that makes changes.
- ReliablePenguin. (2025). *What Is a Runbook? History, Template, and Best Practices*. https://blogs.reliablepenguin.com/2025/10/29/what-is-a-runbook-history-template-and-best-practices
  - Confirms: include validation steps to confirm success and pair with rollback/recovery instructions. "Close with safety notes and references." Traces the SRE runbook concept to Google's SRE practice.
- Google Cloud. (2019). *How to Start and Assess Your SRE Journey*. Google Cloud Blog. https://cloud.google.com/blog/products/devops-sre/how-to-start-and-assess-your-sre-journey
  - Confirms: Google SRE practice explicitly requires an operational playbook/runbook to exist, with documentation for the release process, service setup, teardown, and rollback mechanism.
- Thesius. (2026). *Runbook Template Library*. DEV Community. https://dev.to/thesius_code_7a136ae718b7/runbook-template-library-50p1
  - Confirms: production SRE frameworks define required sections as Symptoms, Diagnosis, Remediation, Verification, Escalation. Maps directly to our Implementation Steps, Testing/Verification structure.
- CorsoUX. (2026). *UX Audit Checklist: 50 Points*. https://courseux.com/ux-audit-checklist/
  - Confirms: "An audit that does not specify what to do in what order is analysis, not design. The output must be a roadmap." Source for the roadmap/action plan requirement.

---

### Research basis for the severity scale

The severity scale (1-4) is directly derived from Jakob Nielsen's original usability severity rating scale, the most cited severity framework in software engineering.

- Nielsen, J. (1994). *Severity Ratings for Usability Problems*. Nielsen Norman Group. https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/
  - Original source: 0 = not a problem, 1 = cosmetic, 2 = minor, 3 = major, 4 = catastrophic/blocks task completion
  - Our mapping preserves this scale exactly, applied to issue sections rather than UI elements
- Sauro, J. (2013). *Rating the Severity of Usability Problems*. MeasuringU. https://measuringu.com/rating-severity/
  - Confirms: "treat frequency separately from severity" — which is why section absence and section quality are scored independently
- Nielsen, J. (1993). *Usability Engineering*. Academic Press. ISBN: 978-0125184069.
  - Confirms: severity is a combination of frequency, impact, and persistence — the same three factors we used to weight section criticality

The mapping of sections to severity levels was determined by applying Nielsen's impact criterion: how badly does the absence of this section hurt the ability to execute the process? A missing Rollback section on a production process maps to severity 4 (catastrophic/blocks safe completion) by the same logic Nielsen applies to UI elements that block task completion.

---

### Calibration method

Controlled degradation as a method for building evaluation calibration sets is documented in NLP evaluation research as more reliable than synthetic generation for the reasons described above. The specific degradation plan follows a principle of single-change-per-anchor, ensuring each score difference is traceable to exactly one variable. This is consistent with controlled experiment design principles in software engineering research.

The five patterns documented at the end of the calibration set are observations derived from scoring the anchors, not pre-specified claims. They are offered as heuristics for human evaluators, not as formal findings.

---

## How to use this document

These ten issues are controlled degradations of a real 9.5/10 implementation plan issue (Inkweave issue #278) produced by Claude Code. Each anchor removes or degrades specific sections in a traceable way so the scoring rationale is explicit and verifiable.

Use them to calibrate your intuition before evaluating a real issue. When you score an issue, compare it against the anchor that most closely resembles it. An issue with similar gaps to Anchor 6 should score similarly to Anchor 6.

These anchors were scored by the subject matter expert (the developer who authored the original issue) against the eight-section rubric below.

---

## Section weight mapping

Not all sections carry equal weight. Every severity rating in this mapping is derived from Nielsen's usability severity scale (1994) applied to issue sections. See Methodology section above for full citations.

| Section | Severity if absent | Rationale |
|---|---|---|
| Implementation Steps | 4 — Critical | Without steps the issue is not a runbook at all |
| Acceptance Criteria | 4 — Critical | Without this there is no definition of done |
| Rollback | 4 — Critical | Without this a production process is dangerous |
| Context | 3 — Important | Without this future developers cannot understand why the process exists |
| Prerequisites | 3 — Important | Without this the process cannot be safely started |
| Testing / Verification | 3 — Important | Without this there is no way to confirm success |
| Files Affected | 2 — Supporting | Useful but steps partially compensate |
| References | 2 — Supporting | Useful but content partially compensates |

## Scoring scale

Adapted from Nielsen's 0-4 usability severity scale (Nielsen, J. 1994. *Severity Ratings for Usability Problems*. Nielsen Norman Group. https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/), applied to issue section completeness rather than UI elements. The five-band mapping below reflects how severity 4, 3, and 2 findings accumulate across the eight sections.

| Score | Meaning | Nielsen severity equivalent |
|---|---|---|
| 9-10 | All critical and important sections present, well-specified, no meaningful gaps | No severity 3 or 4 findings |
| 7-8 | All critical sections present, supporting sections missing or degraded | Severity 2 findings only |
| 5-6 | All critical sections present, important sections missing or degraded | One or more severity 3 findings |
| 3-4 | One or more critical sections absent or severely degraded | One or more severity 4 findings |
| 1-2 | Multiple critical sections absent, issue is not usable as a runbook | Multiple severity 4 findings |

---

## ANCHOR 1 — Score: 10/10
### All sections present and complete

**Degradation applied:** None. This is the reference issue.

**Failure mode:** None. Minor gap in Prerequisites (missing local environment setup) noted but insufficient to reduce score below 10 in context of a solo developer who owns the repo.

**Source:** https://github.com/Doberjohn/inkweave/issues/278

---

## Context

Set 12 (The Wilds Unknown) introduces Pixar movies (Toy Story, The Incredibles, Brave) to Lorcana. Cards are being revealed gradually during preseason. We need a way to showcase revealed cards immediately and progressively integrate them into the synergy engine — without waiting for the external card database to publish the full set.

**Two-track workflow:**
- **Track 1 — Display** (per-reveal, no deploy): Add card to Supabase -> appears on the reveals page immediately.
- **Track 2 — Engine** (batched, deliberate): When confident about a group of cards' synergies, add them to `previewCards.json` in the repo -> rebuild engine -> deploy.

Cards can be display-only (unclear synergies) or display + engine (known synergies like Shift targets). All cards graduate when the external source publishes the full set 12 `allCards.json`.

## Prerequisites

- [ ] Supabase project access (dashboard for inserts + Storage for images)
- [ ] Understanding of the `allCards.json` card format
- [ ] Familiarity with the synergy engine rebuild pipeline (`pnpm build:engine && pnpm precompute-synergies`)

## Implementation Steps

### Phase 1 — Supabase infrastructure (Display track)

**Step 1: Create `preview_cards` table**

```sql
CREATE TABLE preview_cards (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  full_name TEXT NOT NULL,
  set_code TEXT NOT NULL DEFAULT '12',
  type TEXT NOT NULL CHECK (type IN ('Character', 'Action', 'Item', 'Location')),
  color TEXT NOT NULL,
  cost INTEGER NOT NULL,
  inkwell BOOLEAN NOT NULL DEFAULT false,
  full_text TEXT NOT NULL DEFAULT '',
  full_text_sections JSONB NOT NULL DEFAULT '[]'::jsonb,
  image_url TEXT NOT NULL,
  version TEXT,
  strength INTEGER,
  willpower INTEGER,
  lore INTEGER,
  move_cost INTEGER,
  subtypes TEXT[],
  rarity TEXT,
  number INTEGER,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

ALTER TABLE preview_cards ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Public read" ON preview_cards FOR SELECT USING (true);
CREATE POLICY "Service role write" ON preview_cards FOR ALL USING (auth.role() = 'service_role');
```

**Verify:** Run `SELECT * FROM preview_cards;` in Supabase dashboard — table exists, empty.

**Step 2: Create Supabase Storage bucket**

Create a public bucket `card-previews` in Supabase Storage dashboard.

**Verify:** Upload a test image, confirm it is accessible via public URL.

**Step 3: Regenerate TypeScript types**

```bash
pnpm supabase gen types typescript --project-id <project-id> > apps/web/src/shared/lib/database.types.ts
```

**Verify:** `database.types.ts` includes `preview_cards` table type.

### Phase 2 — Reveals page (Display track)

**Step 4: Create the reveals page route**

Add `/reveals` route in `apps/web/src/router.tsx`.

**Step 5: Build the reveals page component**

Create `apps/web/src/pages/RevealsPage.tsx`. Fetch all rows from `preview_cards` via Supabase client. Display cards in a responsive grid. Cards from Supabase only -> non-clickable. Cards also present in the engine -> clickable.

**Step 6: Add navigation link**

Add "Set 12 Reveals" link to navigation (desktop nav strip + mobile bottom nav).

**Verify:** Dev server shows `/reveals` with test cards inserted into Supabase.

### Phase 3 — Engine integration (Engine track)

**Step 7: Create `previewCards.json`**

Create `apps/web/public/data/previewCards.json` with same format as `allCards.json`.

**Step 8: Update synergy precomputation**

Modify `scripts/precompute-synergies.mjs` to load both `allCards.json` and `previewCards.json`, merge, and compute synergies.

**Step 9: Update card loader**

Modify `apps/web/src/features/cards/loader.ts` to fetch both sources and merge.

**Step 10: Update image download script**

Modify `scripts/download-card-images.mjs` to also read `previewCards.json`.

**Verify:** Add test card to `previewCards.json` -> run `pnpm build:engine && pnpm precompute-synergies` -> confirm synergy files generated.

### Phase 4 — Reveals page engine awareness

**Step 11: Detect engine-integrated cards on reveals page**

Load synergy manifest to get card IDs with computed synergies. Cross-reference with card loader data. Cards in both Supabase AND engine -> clickable. Cards in Supabase only -> non-clickable.

**Verify:** Reveals page shows both clickable and non-clickable cards with visual distinction.

## Files Affected

### Created
| File | Purpose |
|------|---------|
| `supabase/migrations/YYYYMMDD_create_preview_cards.sql` | Table + RLS |
| `apps/web/public/data/previewCards.json` | Engine-track card data |
| `apps/web/src/pages/RevealsPage.tsx` | Reveals page component |
| `apps/web/src/features/cards/hooks/usePreviewCards.ts` | Supabase fetch hook |

### Modified
| File | Change |
|------|--------|
| `apps/web/src/router.tsx` | Add `/reveals` route |
| `apps/web/src/shared/lib/database.types.ts` | Regenerated types |
| `apps/web/src/features/cards/loader.ts` | Merge `previewCards.json` |
| `scripts/precompute-synergies.mjs` | Read both card sources |
| `scripts/download-card-images.mjs` | Read both card sources |
| Navigation components | Add reveals page link |

## Testing / Verification

### Display track
- [ ] Insert card row via Supabase dashboard -> appears on `/reveals` within seconds
- [ ] Upload image to `card-previews` bucket -> renders on reveals page
- [ ] Display-only cards NOT clickable and NOT in browse/search

### Engine track
- [ ] Add card to `previewCards.json` -> `pnpm build:engine && pnpm precompute-synergies` succeeds
- [ ] Engine card appears in browse/search with working synergies
- [ ] Engine card appears on reveals page as clickable

### Graduation
- [ ] After updating `allCards.json` and deleting `previewCards.json`, all cards work as before
- [ ] Clearing Supabase rows removes display-only cards from reveals page

## Acceptance Criteria

- [ ] Revealed Set 12 cards can be added to reveals page without a PR or redeployment
- [ ] Cards with known synergies can be batch-added via `previewCards.json` + deploy
- [ ] Reveals page distinguishes display-only from engine-integrated cards
- [ ] Engine computes synergies across both card pools
- [ ] Graduation path cleanly transitions all cards

## Rollback

- **Display track:** Delete rows from `preview_cards` table -> cards disappear immediately.
- **Engine track:** Empty `cards` array in `previewCards.json` -> rebuild -> deploy.
- **Full rollback:** Drop migration, delete `previewCards.json`, remove reveals route, revert loader/script changes.

## References

- Issue #278: Add set 12 cards in the card pool
- Supabase project: `ttyidjyaxnycbpwngqr` (eu-central-1)
- Card data format: `apps/web/public/data/allCards.json`
- Synergy precomputation: `scripts/precompute-synergies.mjs`
- Card loader: `apps/web/src/features/cards/loader.ts`

---
---

## ANCHOR 2 — Score: 9/10
### References section removed

**Degradation applied:** References section removed entirely.
**Severity finding introduced:** 1x Severity 2 (supporting section absent).
**All critical sections:** Present and complete.
**All important sections:** Present and complete.

---

## Context

Set 12 (The Wilds Unknown) introduces Pixar movies (Toy Story, The Incredibles, Brave) to Lorcana. Cards are being revealed gradually during preseason. We need a way to showcase revealed cards immediately and progressively integrate them into the synergy engine — without waiting for the external card database to publish the full set.

**Two-track workflow:**
- **Track 1 — Display** (per-reveal, no deploy): Add card to Supabase -> appears on the reveals page immediately.
- **Track 2 — Engine** (batched, deliberate): When confident about a group of cards' synergies, add them to `previewCards.json` -> rebuild engine -> deploy.

## Prerequisites

- [ ] Supabase project access (dashboard for inserts + Storage for images)
- [ ] Understanding of the `allCards.json` card format
- [ ] Familiarity with the synergy engine rebuild pipeline (`pnpm build:engine && pnpm precompute-synergies`)

## Implementation Steps

### Phase 1 — Supabase infrastructure

**Step 1: Create `preview_cards` table**

```sql
CREATE TABLE preview_cards (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  full_name TEXT NOT NULL,
  set_code TEXT NOT NULL DEFAULT '12',
  type TEXT NOT NULL CHECK (type IN ('Character', 'Action', 'Item', 'Location')),
  color TEXT NOT NULL,
  cost INTEGER NOT NULL,
  inkwell BOOLEAN NOT NULL DEFAULT false,
  image_url TEXT NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
ALTER TABLE preview_cards ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Public read" ON preview_cards FOR SELECT USING (true);
```

**Verify:** Run `SELECT * FROM preview_cards;` — table exists, empty.

**Step 2: Create Storage bucket**

Create public bucket `card-previews` in Supabase Storage.

**Verify:** Upload test image, confirm public URL accessible.

**Step 3: Regenerate TypeScript types**

```bash
pnpm supabase gen types typescript --project-id <project-id> > apps/web/src/shared/lib/database.types.ts
```

**Verify:** `database.types.ts` includes `preview_cards`.

### Phase 2 — Reveals page

**Step 4:** Add `/reveals` route in `apps/web/src/router.tsx`.

**Step 5:** Create `apps/web/src/pages/RevealsPage.tsx`. Fetch from `preview_cards`, display in grid. Display-only cards non-clickable, engine-integrated clickable.

**Step 6:** Add "Set 12 Reveals" to navigation.

**Verify:** Dev server shows `/reveals` with test cards.

### Phase 3 — Engine integration

**Step 7:** Create `apps/web/public/data/previewCards.json` matching `allCards.json` format.

**Step 8:** Update `scripts/precompute-synergies.mjs` to merge both sources.

**Step 9:** Update `apps/web/src/features/cards/loader.ts` to merge both sources.

**Step 10:** Update `scripts/download-card-images.mjs` to process both sources.

**Verify:** Test card in `previewCards.json` -> run build -> synergy files generated.

### Phase 4 — Engine awareness on reveals page

**Step 11:** Cross-reference synergy manifest with card loader. Engine cards -> clickable. Supabase-only cards -> non-clickable.

**Verify:** Visual distinction between card types on reveals page.

## Files Affected

### Created
| File | Purpose |
|------|---------|
| `supabase/migrations/YYYYMMDD_create_preview_cards.sql` | Table + RLS |
| `apps/web/public/data/previewCards.json` | Engine-track card data |
| `apps/web/src/pages/RevealsPage.tsx` | Reveals page component |
| `apps/web/src/features/cards/hooks/usePreviewCards.ts` | Supabase fetch hook |

### Modified
| File | Change |
|------|--------|
| `apps/web/src/router.tsx` | Add `/reveals` route |
| `apps/web/src/features/cards/loader.ts` | Merge `previewCards.json` |
| `scripts/precompute-synergies.mjs` | Read both sources |
| Navigation components | Add reveals link |

## Testing / Verification

### Display track
- [ ] Insert card row -> appears on `/reveals` without deploy
- [ ] Image upload -> renders on reveals page
- [ ] Display-only cards NOT in browse/search

### Engine track
- [ ] Add card to `previewCards.json` -> build succeeds -> synergies computed
- [ ] Engine card appears in browse/search and on reveals page as clickable

### Graduation
- [ ] After replacing `allCards.json` and deleting `previewCards.json`, all cards work as before

## Acceptance Criteria

- [ ] Cards can be added to reveals page without PR or redeployment
- [ ] Cards with known synergies can be added via `previewCards.json` + deploy
- [ ] Reveals page distinguishes display-only from engine-integrated cards
- [ ] Engine computes synergies across both card pools
- [ ] Graduation path cleanly transitions all cards

## Rollback

- **Display track:** Delete rows from `preview_cards` -> cards disappear immediately.
- **Engine track:** Empty `cards` array in `previewCards.json` -> rebuild -> deploy.
- **Full rollback:** Drop migration, delete `previewCards.json`, remove route, revert loader changes.

---
---

## ANCHOR 3 — Score: 8/10
### References and Files Affected removed

**Degradation applied:** References section removed. Files Affected section removed.
**Severity findings introduced:** 2x Severity 2 (both supporting sections absent).
**All critical sections:** Present and complete.
**All important sections:** Present and complete.

---

## Context

Set 12 (The Wilds Unknown) introduces Pixar movies to Lorcana. Cards are being revealed gradually during preseason. We need a way to showcase revealed cards immediately and integrate them into the synergy engine without waiting for the external database.

**Two-track workflow:**
- **Track 1 — Display** (per-reveal, no deploy): Add card to Supabase -> appears on reveals page immediately.
- **Track 2 — Engine** (batched, deliberate): Add cards to `previewCards.json` -> rebuild -> deploy.

## Prerequisites

- [ ] Supabase project access
- [ ] Understanding of `allCards.json` card format
- [ ] Familiarity with synergy engine rebuild pipeline

## Implementation Steps

**Step 1: Create `preview_cards` table in Supabase**

```sql
CREATE TABLE preview_cards (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  full_name TEXT NOT NULL,
  set_code TEXT NOT NULL DEFAULT '12',
  type TEXT NOT NULL CHECK (type IN ('Character', 'Action', 'Item', 'Location')),
  color TEXT NOT NULL,
  cost INTEGER NOT NULL,
  inkwell BOOLEAN NOT NULL DEFAULT false,
  image_url TEXT NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
ALTER TABLE preview_cards ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Public read" ON preview_cards FOR SELECT USING (true);
CREATE POLICY "Service role write" ON preview_cards FOR ALL USING (auth.role() = 'service_role');
```

**Verify:** `SELECT * FROM preview_cards;` — table exists, empty.

**Step 2: Create public Storage bucket `card-previews`.**

**Verify:** Test image accessible via public URL.

**Step 3: Regenerate TypeScript types.**

```bash
pnpm supabase gen types typescript --project-id <project-id> > apps/web/src/shared/lib/database.types.ts
```

**Verify:** `database.types.ts` includes `preview_cards`.

**Step 4:** Add `/reveals` route to `apps/web/src/router.tsx`.

**Step 5:** Create `apps/web/src/pages/RevealsPage.tsx`. Fetch `preview_cards` from Supabase. Grid display. Display-only cards non-clickable, engine-integrated clickable.

**Step 6:** Add "Set 12 Reveals" to navigation components.

**Verify:** Dev server shows `/reveals` with test cards.

**Step 7:** Create `apps/web/public/data/previewCards.json` matching `allCards.json` format.

**Step 8:** Update `scripts/precompute-synergies.mjs` to merge both card sources.

**Step 9:** Update `apps/web/src/features/cards/loader.ts` to fetch and merge both sources.

**Step 10:** Update `scripts/download-card-images.mjs` to process both sources.

**Verify:** Test card in `previewCards.json` -> `pnpm build:engine && pnpm precompute-synergies` -> synergies generated.

**Step 11:** Cross-reference synergy manifest with card loader on reveals page. Engine cards -> clickable. Supabase-only -> non-clickable.

**Verify:** Both card types visible with clear distinction on reveals page.

## Testing / Verification

### Display track
- [ ] Insert row in Supabase -> card on `/reveals` without deploy
- [ ] Image upload -> renders correctly
- [ ] Display-only cards absent from browse/search

### Engine track
- [ ] `previewCards.json` + build -> synergies computed
- [ ] Engine cards appear in browse/search and reveals as clickable

### Graduation
- [ ] After replacing `allCards.json` and deleting `previewCards.json`, everything works as before

## Acceptance Criteria

- [ ] Cards added to reveals page without PR or redeployment
- [ ] Engine cards added via `previewCards.json` + deploy
- [ ] Reveals page distinguishes display-only from engine-integrated cards
- [ ] Engine computes synergies across both pools
- [ ] Graduation path works cleanly

## Rollback

- **Display track:** Delete rows from `preview_cards` -> immediate removal.
- **Engine track:** Empty `cards` in `previewCards.json` -> rebuild -> deploy.
- **Full rollback:** Drop migration, delete `previewCards.json`, remove route, revert scripts.

---
---

## ANCHOR 4 — Score: 7/10
### References, Files Affected removed. Testing/Verification degraded.

**Degradation applied:** References removed. Files Affected removed. Testing/Verification replaced with a single vague line — no checkboxes, no pass/fail criteria, no track separation.
**Severity findings introduced:** 2x Severity 2, 1x Severity 3.
**All critical sections:** Present and complete.
**Important sections:** Testing/Verification present but insufficient.

---

## Context

Set 12 (The Wilds Unknown) introduces Pixar movies to Lorcana. Cards are being revealed gradually during preseason. We need a way to showcase revealed cards immediately without waiting for the external database.

**Two-track workflow:**
- **Track 1 — Display:** Add card to Supabase -> appears on reveals page.
- **Track 2 — Engine:** Add cards to `previewCards.json` -> rebuild -> deploy.

## Prerequisites

- [ ] Supabase project access
- [ ] Understanding of `allCards.json` format
- [ ] Familiarity with synergy engine rebuild pipeline

## Implementation Steps

**Step 1:** Create `preview_cards` table in Supabase with name, full_name, set_code, type, color, cost, inkwell, image_url fields. Enable RLS with public read and service role write policies.

**Step 2:** Create public Storage bucket `card-previews`.

**Step 3:** Regenerate TypeScript types.

```bash
pnpm supabase gen types typescript --project-id <project-id> > apps/web/src/shared/lib/database.types.ts
```

**Step 4:** Add `/reveals` route to router.

**Step 5:** Create `RevealsPage.tsx`. Fetch from `preview_cards`. Grid display. Display-only non-clickable, engine cards clickable.

**Step 6:** Add navigation link.

**Step 7:** Create `previewCards.json` matching `allCards.json` format.

**Step 8:** Update `precompute-synergies.mjs` to merge both sources.

**Step 9:** Update `loader.ts` to merge both sources.

**Step 10:** Update image download script to process both sources.

**Step 11:** Cross-reference synergy manifest on reveals page for clickability.

## Testing / Verification

Test that the display and engine tracks work as expected before deploying.

## Acceptance Criteria

- [ ] Cards added to reveals page without PR or redeployment
- [ ] Engine cards added via `previewCards.json` + deploy
- [ ] Reveals page distinguishes display-only from engine-integrated cards
- [ ] Engine computes synergies across both pools
- [ ] Graduation path works cleanly

## Rollback

- **Display track:** Delete rows from `preview_cards` -> immediate removal.
- **Engine track:** Empty `cards` in `previewCards.json` -> rebuild -> deploy.
- **Full rollback:** Drop migration, delete `previewCards.json`, remove route, revert scripts.

---
---

## ANCHOR 5 — Score: 6/10
### References, Files Affected removed. Testing/Verification degraded. Prerequisites removed.

**Degradation applied:** References removed. Files Affected removed. Testing/Verification vague. Prerequisites section removed entirely.
**Severity findings introduced:** 2x Severity 2, 2x Severity 3.
**All critical sections:** Present and complete.
**Important sections:** Prerequisites absent. Testing/Verification insufficient.

---

## Context

Set 12 (The Wilds Unknown) introduces Pixar movies to Lorcana. Cards are being revealed gradually. We need to show revealed cards without waiting for the external database.

**Two-track workflow:**
- **Track 1 — Display:** Add card to Supabase -> appears on reveals page.
- **Track 2 — Engine:** Add cards to `previewCards.json` -> rebuild -> deploy.

## Implementation Steps

**Step 1:** Create `preview_cards` table in Supabase with required fields. Enable RLS with public read and service role write.

**Step 2:** Create public Storage bucket `card-previews`.

**Step 3:** Regenerate TypeScript types.

```bash
pnpm supabase gen types typescript --project-id <project-id> > apps/web/src/shared/lib/database.types.ts
```

**Step 4:** Add `/reveals` route to router.

**Step 5:** Create `RevealsPage.tsx`. Fetch from `preview_cards`. Grid display. Display-only non-clickable, engine cards clickable.

**Step 6:** Add navigation link.

**Step 7:** Create `previewCards.json` matching `allCards.json` format.

**Step 8:** Update `precompute-synergies.mjs` to merge both sources.

**Step 9:** Update `loader.ts` to merge both sources.

**Step 10:** Update image download script for both sources.

**Step 11:** Cross-reference synergy manifest on reveals page for clickability.

## Testing / Verification

Test that the display and engine tracks work as expected before deploying.

## Acceptance Criteria

- [ ] Cards added to reveals page without PR or redeployment
- [ ] Engine cards added via `previewCards.json` + deploy
- [ ] Reveals page distinguishes display-only from engine-integrated cards
- [ ] Engine computes synergies across both pools
- [ ] Graduation path works cleanly

## Rollback

- **Display track:** Delete rows from `preview_cards` -> immediate removal.
- **Engine track:** Empty `cards` in `previewCards.json` -> rebuild -> deploy.
- **Full rollback:** Drop migration, delete `previewCards.json`, remove route, revert scripts.

---
---

## ANCHOR 6 — Score: 5/10
### References, Files Affected removed. Testing/Verification degraded. Prerequisites removed. Context removed.

**Degradation applied:** References removed. Files Affected removed. Testing/Verification vague. Prerequisites removed. Context removed entirely.
**Severity findings introduced:** 2x Severity 2, 3x Severity 3.
**All critical sections:** Present and complete.
**Important sections:** Context, Prerequisites, Testing/Verification all absent or insufficient.

---

## Implementation Steps

**Step 1:** Create `preview_cards` table in Supabase with required fields. Enable RLS with public read and service role write.

**Step 2:** Create public Storage bucket `card-previews`.

**Step 3:** Regenerate TypeScript types.

```bash
pnpm supabase gen types typescript --project-id <project-id> > apps/web/src/shared/lib/database.types.ts
```

**Step 4:** Add `/reveals` route to router.

**Step 5:** Create `RevealsPage.tsx`. Fetch from `preview_cards`. Grid display. Display-only non-clickable, engine cards clickable.

**Step 6:** Add navigation link.

**Step 7:** Create `previewCards.json` matching `allCards.json` format.

**Step 8:** Update `precompute-synergies.mjs` to merge both sources.

**Step 9:** Update `loader.ts` to merge both sources.

**Step 10:** Update image download script for both sources.

**Step 11:** Cross-reference synergy manifest on reveals page for clickability.

## Testing / Verification

Test that the display and engine tracks work as expected before deploying.

## Acceptance Criteria

- [ ] Cards added to reveals page without PR or redeployment
- [ ] Engine cards added via `previewCards.json` + deploy
- [ ] Reveals page distinguishes display-only from engine-integrated cards
- [ ] Engine computes synergies across both pools
- [ ] Graduation path works cleanly

## Rollback

- **Display track:** Delete rows from `preview_cards` -> immediate removal.
- **Engine track:** Empty `cards` in `previewCards.json` -> rebuild -> deploy.
- **Full rollback:** Drop migration, delete `previewCards.json`, remove route, revert scripts.

---
---

## ANCHOR 7 — Score: 4/10
### All supporting and important sections removed or degraded. Rollback degraded to single vague sentence.

**Degradation applied:** References removed. Files Affected removed. Testing/Verification vague. Prerequisites removed. Context removed. Rollback degraded to a single vague sentence with no per-track instructions.
**Severity findings introduced:** 2x Severity 2, 3x Severity 3, 1x Severity 4.
**All critical sections:** Implementation Steps and Acceptance Criteria present. Rollback present but insufficient.

---

## Implementation Steps

**Step 1:** Create `preview_cards` table in Supabase with required fields. Enable RLS with public read and service role write.

**Step 2:** Create public Storage bucket `card-previews`.

**Step 3:** Regenerate TypeScript types.

```bash
pnpm supabase gen types typescript --project-id <project-id> > apps/web/src/shared/lib/database.types.ts
```

**Step 4:** Add `/reveals` route to router.

**Step 5:** Create `RevealsPage.tsx`. Fetch from `preview_cards`. Grid display. Display-only non-clickable, engine cards clickable.

**Step 6:** Add navigation link.

**Step 7:** Create `previewCards.json` matching `allCards.json` format.

**Step 8:** Update `precompute-synergies.mjs` to merge both sources.

**Step 9:** Update `loader.ts` to merge both sources.

**Step 10:** Update image download script for both sources.

**Step 11:** Cross-reference synergy manifest on reveals page for clickability.

## Testing / Verification

Test that the display and engine tracks work as expected before deploying.

## Acceptance Criteria

- [ ] Cards added to reveals page without PR or redeployment
- [ ] Engine cards added via `previewCards.json` + deploy
- [ ] Reveals page distinguishes display-only from engine-integrated cards
- [ ] Engine computes synergies across both pools
- [ ] Graduation path works cleanly

## Rollback

Revert all changes if something goes wrong.

---
---

## ANCHOR 8 — Score: 3/10
### Rollback vague. Acceptance Criteria degraded to non-testable statements.

**Degradation applied:** References removed. Files Affected removed. Testing/Verification vague. Prerequisites removed. Context removed. Rollback vague. Acceptance Criteria degraded to two vague non-testable statements without checkboxes.
**Severity findings introduced:** 2x Severity 2, 3x Severity 3, 2x Severity 4.
**Critical sections:** Implementation Steps present. Acceptance Criteria present but non-functional. Rollback present but non-functional.

---

## Implementation Steps

**Step 1:** Create `preview_cards` table in Supabase with required fields. Enable RLS with public read and service role write.

**Step 2:** Create public Storage bucket `card-previews`.

**Step 3:** Regenerate TypeScript types.

```bash
pnpm supabase gen types typescript --project-id <project-id> > apps/web/src/shared/lib/database.types.ts
```

**Step 4:** Add `/reveals` route to router.

**Step 5:** Create `RevealsPage.tsx`. Fetch from `preview_cards`. Grid display. Display-only non-clickable, engine cards clickable.

**Step 6:** Add navigation link.

**Step 7:** Create `previewCards.json` matching `allCards.json` format.

**Step 8:** Update `precompute-synergies.mjs` to merge both sources.

**Step 9:** Update `loader.ts` to merge both sources.

**Step 10:** Update image download script for both sources.

**Step 11:** Cross-reference synergy manifest on reveals page for clickability.

## Testing / Verification

Test that the display and engine tracks work as expected before deploying.

## Acceptance Criteria

The cards should work correctly and the page should look good. The graduation process should be straightforward.

## Rollback

Revert all changes if something goes wrong.

---
---

## ANCHOR 9 — Score: 2/10
### Implementation Steps degraded to vague bullets. Acceptance Criteria non-testable. Rollback vague.

**Degradation applied:** References removed. Files Affected removed. Testing/Verification vague. Prerequisites removed. Context removed. Rollback vague. Acceptance Criteria non-testable. Implementation Steps degraded to three vague high-level bullets with no code blocks, no verification, and no phase structure.
**Severity findings introduced:** 2x Severity 2, 3x Severity 3, 3x Severity 4.
**Critical sections:** All three present but none functional. Implementation Steps cannot be followed. Acceptance Criteria untestable. Rollback uninstructive.

---

## Implementation Steps

- Set up Supabase infrastructure including the preview cards table and storage bucket
- Build the reveals page and update the synergy engine to support preview cards
- Connect everything together and add navigation

## Testing / Verification

Test that the display and engine tracks work as expected before deploying.

## Acceptance Criteria

The cards should work correctly and the page should look good. The graduation process should be straightforward.

## Rollback

Revert all changes if something goes wrong.

---
---

## ANCHOR 10 — Score: 1/10
### Title only. No sections, no structure, no content.

**Degradation applied:** All sections removed. Title and one sentence only.
**Severity findings introduced:** All eight sections absent. Three critical sections absent = three Severity 4 findings.
**Failure mode:** This is the absolute floor. Not usable as a runbook in any sense.

---

Add set 12 cards to the card pool.

---
---

## Observations from scoring the calibration set

The following patterns were observed during the controlled degradation and scoring process. They are not formal research findings — they are heuristics surfaced by a single subject matter expert scoring ten anchors derived from one real issue. They are offered as calibration guidance, not as general claims about all implementation plan issues.

**Observation 1: Supporting section removal barely moves the score.**
In this calibration set, removing References and Files Affected together dropped the score from 10 to 8. These sections add significant value but the issue remained fully actionable without them. This is consistent with their severity 2 weight mapping — useful but compensated by other sections.

**Observation 2: In this calibration set, the 5-6 range reflects missing important sections.**
Anchors 5 and 6 — missing Prerequisites and Context respectively — landed in the 5-6 range. Whether this reflects real-world first-draft issues more broadly is not claimed here; it is a structural consequence of the degradation plan applied to this specific issue.

**Observation 3: A vague Rollback section may be worse than no Rollback.**
Anchor 7 has a Rollback section that says "revert all changes if something goes wrong." This provides false confidence while offering no actionable guidance. The validator should detect the presence of the section separately from its quality — a present-but-vague Rollback is a different failure mode from an absent Rollback. This observation is consistent with SRE runbook research cited in the Methodology section, which states rollback sections must include specific per-track instructions.

**Observation 4: Non-testable Acceptance Criteria make the section functionally absent.**
Anchor 8 has an Acceptance Criteria section with prose statements rather than checkboxes. From a definition-of-done perspective this is effectively a missing section despite technically existing. This aligns with the Scrum Alliance definition of acceptance criteria as pass/fail conditions (https://resources.scrumalliance.org/Article/need-know-acceptance-criteria).

**Observation 5: The gap between scores 2 and 1 is structural, not quality-based.**
Anchor 9 has three sections, each present but non-functional. Anchor 10 has no sections at all. A validator should treat these as fundamentally different failure modes — one is a quality problem, the other is a structural absence. Both score in the 1-2 range but for different reasons that require different feedback.
