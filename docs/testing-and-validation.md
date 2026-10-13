# Testing and Validation

## 1. Purpose

This document describes the testing and validation activities for the Customer Lifetime Value & Churn Intelligence project.

The goal is to verify that the application runs, its inputs are handled appropriately, calculations behave as expected, and machine learning evaluation results are documented accurately.

## 2. Machine Learning Evaluation Results

The following metrics were recorded during model evaluation.

| Metric | Logistic Regression | LightGBM |
|---|---:|---:|
| Accuracy | 0.7331 | 0.7601 |
| Precision | 0.4983 | 0.5340 |
| Recall | 0.7914 | 0.7567 |
| F1-score | 0.6116 | 0.6261 |
| ROC-AUC | 0.8418 | 0.8361 |

These are previously recorded evaluation results, not the results of newly executed tests. They should be interpreted in the context of the project's evaluation data and methodology.

## 3. Application Functional Test Plan

Run each test and record the actual result.

| Test ID | Test | Expected behavior | Actual status |
|---|---|---|---|
| T01 | Open the deployed Streamlit URL | Application loads without an error | Passed — app loaded successfully |
| T02 | Change the customers-targeted input | Scenario results update | Passed — doubling customers from 500 to 1,000 doubled the displayed estimates; restoring 500 returned the original values |
| T03 | Change the churn-reduction assumption | Estimated retained customers update | Pending verification |
| T04 | Change the campaign offer cost | Campaign cost and net benefit update | Pending verification |
| T05 | Change profit margin or retained-value period | Estimated benefit and ROI update | Pending verification |
| T06 | Use different reasonable input values | Calculations remain consistent with the assumptions | Pending verification |
| T07 | Review the application's disclaimer | Hypothetical assumptions and limitations are explained | Pending verification |

## 4. Calculation Validation

The simulator uses assumptions entered by the user. The following relationships can be checked against the application's displayed results.

- Expected churners = customers targeted × baseline churn rate.
- Estimated retained customers = expected churners × assumed relative churn reduction.
- Campaign cost = customers targeted × offer cost per customer.
- Estimated benefit = estimated retained customers × estimated value per retained customer.
- Estimated net benefit = estimated benefit − campaign cost.
- Illustrative ROI = (estimated net benefit ÷ campaign cost) × 100, when campaign cost is greater than zero.

The application should handle a zero campaign cost without a division-by-zero error.

## 5. Interpretation of Model Metrics

- **Accuracy:** Overall proportion of correctly classified observations.
- **Precision:** Proportion of predicted churn cases that were actual churn cases.
- **Recall:** Proportion of actual churn cases identified by the model.
- **F1-score:** Harmonic mean of precision and recall.
- **ROC-AUC:** Ability of the model to rank positive cases above negative cases across classification thresholds.

Metrics should be evaluated together rather than relying on accuracy alone.

## 6. Additional Validation Considerations

- Check that the cleaned dataset contains the expected records and columns.
- Confirm that saved model artifacts can be loaded in the intended environment.
- Inspect generated reports and visualizations for missing or invalid values.
- Verify that the deployed application uses the latest committed source code.
- Confirm that the README setup instructions match the repository's current dependencies.

## 7. Limitations

The recorded model metrics do not guarantee performance on new customer data. The uplift experiment uses simulated treatment data, so it does not establish causal effects. CLV and ROI values are illustrative estimates based on assumptions rather than validated business outcomes.

## 8. Test Execution Record

Update this section after executing the tests.

| Date | Test IDs completed | Outcome | Notes |
|---|---|---|---|
| To be recorded | To be recorded | Pending | Enter actual results after testing |

## 9. Conclusion

This document provides a structured validation plan for the project's machine learning artifacts and interactive application. Final test statuses should be updated only after the corresponding checks have been performed.

## Additional Manual Testing Results

| Test | Action | Observed result | Status |
|---|---|---|---|
| T03 — Churn reduction | Increased assumed relative churn reduction from 10% to 20% | Estimated customers retained increased from 13.5 to 27.0 | Passed |
| T04 — Offer cost | Increased offer cost per customer from ₹10 to ₹20 | Campaign cost increased from ₹5,000 to ₹10,000; estimated net benefit changed to -₹6,598 | Passed |
| T05 — Profit margin | Increased profit margin from 30% to 40% | Estimated net benefit changed to -₹5,464 and illustrative ROI to -54.6% | Passed |
| T06 — Reasonable inputs | Not yet independently verified | Pending | Pending |
| T07 — Disclaimer visibility | Checked the deployed application | Disclaimer was visible and explained that campaign assumptions are not validated predictions | Passed |

**Note:** These are manual checks of the interactive application's displayed calculations. The retention campaign outcomes remain hypothetical and are not validated real-world predictions.
