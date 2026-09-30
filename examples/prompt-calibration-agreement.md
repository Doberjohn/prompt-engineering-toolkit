# Prompt Calibration Agreement Study
## Measured scoring agreement for the PPEP rubric (September 2026)

This study replaces the former "93% framework confidence" figure, which had no measurement behind it. It measures how consistently the PPEP rubric scores the nine calibration prompts, and how closely independent scores match the reference scores in `examples/prompt-calibration-set.md`.

---

## Method

**Raters.** Five independent AI rater runs, each in a fresh context with no access to the repository, the calibration set, or the web:
- Three runs of the same large Claude model (to measure run-to-run repeatability).
- One run of a mid-size Claude model and one run of a small Claude model (to measure how much scores shift between models).

**Material.** Each rater received only the EVALUATION FRAMEWORK and SCORING BEHAVIOR sections of `prompts/prompt-evaluator.md` (September 2026 revision) and the nine calibration prompts in a shuffled order under neutral labels. They did not see the anchor scores, the anchor notes, or which prompts were anchors. This is a **blind** test of the rubric alone; the shipped evaluator also includes the calibration anchors, which this test deliberately withholds.

**Instruction.** Score each prompt on the four dimensions exactly as the rubric defines (1-10, or N/A where the rubric allows it), judging each prompt on its own text, and return JSON only.

**Reference.** The September 2026 scores in `examples/prompt-calibration-set.md`. The overall score is the average of the active dimensions, unrounded.

**Metrics.**
- Rank agreement: Spearman correlation between each run's overall scores and the reference overall scores.
- Absolute agreement: mean absolute difference between each run's overall score and the reference, and the share of dimension scores within ±1 of the reference.
- Repeatability: agreement among the three same-model runs, including Krippendorff's alpha (interval) on dimension scores.
- Pooled reliability: Krippendorff's alpha (interval) across all five runs, and across all five runs plus the reference. N/A is treated as missing.

**Limitations.** Nine prompts is a small sample. All raters are models from one provider. The test is blind to the anchors, so it measures the rubric text, not the evaluator as shipped. The model names are not recorded here; the owner should record them when re-running.

---

## Results

### Overall scores per anchor

| Anchor | Reference | Same model, run 1 | Run 2 | Run 3 | Mid-size model | Small model |
|---|---|---|---|---|---|---|
| 1 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.25 |
| 2 | 3.25 | 4.00 | 4.00 | 4.00 | 3.00 | 4.00 |
| 3 | 2.75 | 2.25 | 2.75 | 2.50 | 2.25 | 2.75 |
| 4 | 5.25 | 3.50 | 4.25 | 3.75 | 3.75 | 5.00 |
| 5 | 7.00 | 5.75 | 5.75 | 5.75 | 5.50 | 6.75 |
| 6 | 7.75 | 7.00 | 7.00 | 7.00 | 5.75 | 7.00 |
| 7 | 6.00 | 4.25 | 4.50 | 4.25 | 5.00 | 5.50 |
| 8 | 10.00 | 7.50 | 7.75 | 8.25 | 7.50 | 9.00 |
| 9 | 10.00 | 6.25 | 6.50 | 6.25 | 6.75 | 9.00 |

### Agreement metrics

| Run | Spearman vs reference | Mean abs. overall difference | Dimension scores within ±1 |
|---|---|---|---|
| Same model, run 1 | 0.95 | 1.44 | 55% |
| Same model, run 2 | 0.97 | 1.22 | 53% |
| Same model, run 3 | 0.95 | 1.31 | 58% |
| Mid-size model | 1.00 | 1.39 | 44% |
| Small model | 1.00 | 0.53 | 86% |

- **Repeatability (three same-model runs):** 80% of pairwise comparisons of dimension scores were identical, the mean absolute difference between runs was 0.20 points, the mean standard deviation of the overall score was 0.12 points, and Krippendorff's alpha was 0.98.
- **Pooled reliability:** alpha 0.88 across the five model runs; 0.85 across the five runs plus the reference.
- **N/A use:** the same-model runs marked Epistemics N/A on Anchors 1 and 2 and Process N/A on Anchor 1 in some runs, where the reference scores 1. The other two models never used N/A. The rubric's N/A rules leave room for this on prompts with little content.

---

## What the results show

1. **The rubric orders prompts reliably.** Every run ranked the nine prompts in nearly the same order as the reference (Spearman 0.95 to 1.00).
2. **Scores are highly repeatable within one model.** Re-running the same model changes an overall score by about a tenth of a point on average.
3. **Absolute scores depend on the model and on the anchors.** Without anchors, runs sat 0.5 to 1.4 points from the reference on average, and different models disagreed with each other by similar amounts.
4. **The gold-standard anchors are where blind raters disagree most.** Anchors 8 and 9 (reference 10/10) scored 6.25 to 8.25 in the same-model runs. The largest and most consistent drops were Anchor 9's Performance and Epistemics (6 in every same-model run, against a reference of 10) and Anchor 8's Performance (5 or 6, against 10). Raters returned scores only, so their reasons are not recorded; a follow-up run that asks for one-line notes would show which sub-criteria they judged missing. Either the written rubric is stricter than the reference at the top of the scale, or the reference is generous there; the owner should decide which, and adjust either the rubric text or the two anchors.
5. **The calibration anchors are doing essential work.** Because blind scores drift at the top of the scale, the anchors in the shipped evaluator are what keep absolute scores comparable. Do not remove them.

---

## Follow-up run: ten prompts, with reasons (September 2026)

A second blind run added a candidate anchor and asked raters for a one-line reason for every dimension scored below 9, which the first run lacked.

**Setup:** three runs of the same large Claude model, each given the same rubric and the nine anchor prompts plus the candidate (now Anchor 10), shuffled under new labels. As before, no scores, notes, or repository access. The candidate's reference scores (Product 10, Process 8, Performance 6, Epistemics 10; 8.5 overall) were recorded before the runs.

| Anchor | Reference | Run 1 | Run 2 | Run 3 |
|---|---|---|---|---|
| 1 | 1.00 | 1.00 | 1.00 | 1.00 |
| 2 | 3.25 | 4.00 | 3.50 | 4.00 |
| 3 | 2.75 | 2.00 | 2.67 | 2.67 |
| 4 | 5.25 | 3.25 | 3.50 | 3.25 |
| 5 | 7.00 | 5.25 | 5.25 | 5.25 |
| 6 | 7.75 | 6.00 | 6.50 | 6.75 |
| 7 | 6.00 | 4.00 | 4.00 | 4.25 |
| 8 | 10.00 | 7.50 | 7.50 | 7.75 |
| 9 | 10.00 | 6.50 | 6.50 | 6.25 |
| 10 | 8.00 | 7.25 | 7.50 | 7.25 |

Anchor 10's reference is shown after the correction described below. Spearman against the reference: 0.96, 0.96, 0.94. Mean absolute overall difference: 1.57, 1.36, 1.41. Every run ranked Anchor 8 first and Anchor 10 second.

**What the reasons showed:**

1. **Anchor 10 was over-scored on Product.** All three runs noted that the prompt never states who the report is for. Audience is a Product sub-criterion, and a missing sub-criterion rules out 9-10, so the reference Product score was corrected from 10 to 8 (overall 8.5 to 8.0). The candidate was sought as a 9/10 anchor and was added at 8/10 instead.
2. **The gold-standard anchors have real gaps.** For Anchor 9, all three runs flagged the contradiction between "cover letter" and "a structured report", and read "you don't give negative claims" as a garbled version of the negative-claims rule rather than a requirement to prove them. For Anchor 8, all three flagged that audience, depth, and tone are never stated. These are gaps the rubric defines, which suggests the 10/10 reference scores for Anchors 8 and 9 are generous rather than the rubric being too strict. Whether to lower them is the author's decision.
3. **Autonomous briefs cap at Process 8.** The Process 9-10 band requires checkpoints; a brief for an agent that runs unattended cannot have them. Two runs also called Anchor 10's numbered steps over-prescribed. A future revision could make checkpoints N/A when no human is in the loop.
4. **N/A use varies.** Runs marked Process N/A on Anchors 2, 3, or 1 in some cases, where the reference scores 1 or 2. The N/A rule for "small tasks" is being read more broadly than intended.

---

## How to re-run

1. Copy the EVALUATION FRAMEWORK and SCORING BEHAVIOR sections from `prompts/prompt-evaluator.md` into a file, followed by all anchor prompts in a shuffled order under neutral labels (P1, P2, ...). Do not include scores or notes. Asking for a one-line reason for every dimension scored below 9 makes disagreements interpretable.
2. Give that file, and nothing else, to at least three fresh sessions of the model you care about, plus any other models you want to compare. Ask for JSON scores only.
3. Map labels back to anchors and compute the metrics above. Record the model names, the date, and the rubric revision.

A second useful variant is leave-one-out: give the full evaluator with eight anchors and ask it to score the ninth. That measures the evaluator as shipped, which this study does not.

---

## Raw scores

Label key used in this run: P1 = Anchor 1, P2 = Anchor 5, P3 = Anchor 4, P4 = Anchor 3, P5 = Anchor 2, P6 = Anchor 9, P7 = Anchor 6, P8 = Anchor 7, P9 = Anchor 8.

Dimension scores by anchor, in the order Product / Process / Performance / Epistemics:

| Anchor | Reference | Same model, run 1 | Run 2 | Run 3 | Mid-size model | Small model |
|---|---|---|---|---|---|---|
| 1 | 1/1/1/1 | 1/NA/1/NA | 1/1/1/NA | 1/NA/1/NA | 1/1/1/1 | 1/2/1/1 |
| 2 | 7/2/3/1 | 6/3/3/NA | 6/3/3/NA | 6/3/3/NA | 5/2/3/2 | 7/4/4/1 |
| 3 | 5/2/3/1 | 3/2/3/1 | 3/2/4/2 | 3/2/3/2 | 3/2/2/2 | 4/2/4/1 |
| 4 | 6/5/3/7 | 4/2/4/4 | 4/3/5/5 | 4/2/4/5 | 4/3/3/5 | 5/3/5/7 |
| 5 | 7/8/7/6 | 6/7/5/5 | 6/7/5/5 | 6/7/5/5 | 5/6/6/5 | 7/7/6/7 |
| 6 | 9/7/8/7 | 8/7/7/6 | 8/7/7/6 | 8/7/7/6 | 7/5/6/5 | 8/7/7/6 |
| 7 | 9/5/8/2 | 7/3/5/2 | 7/3/6/2 | 7/3/5/2 | 6/4/5/5 | 8/6/7/1 |
| 8 | 10/10/10/10 | 8/8/5/9 | 8/8/6/9 | 8/9/6/10 | 5/9/6/10 | 9/10/7/10 |
| 9 | 10/10/10/10 | 6/7/6/6 | 7/7/6/6 | 6/7/6/6 | 6/7/7/7 | 9/9/8/10 |
