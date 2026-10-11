# Data and Model Documentation

## 1. Project Overview

**Project:** Customer Lifetime Value & Churn Intelligence

**Objective:** Analyze customer churn, estimate customer value, identify customer segments, and explore hypothetical customer retention strategies using data science and machine learning.

## 2. Dataset Information

The project uses the IBM Telco Customer Churn dataset.

The dataset contains 7,043 customer records with information about demographics, subscribed services, contract types, billing, tenure, and churn status.

**Target variable:** `Churn`

**Target interpretation:**
- `Yes`: The customer churned.
- `No`: The customer did not churn.

The dataset is used for educational and analytical purposes.

## 3. Important Features

| Feature | Description |
|---|---|
| `customerID` | Customer identifier |
| `gender` | Customer gender category |
| `SeniorCitizen` | Indicates senior-citizen status |
| `Partner` | Whether the customer has a partner |
| `Dependents` | Whether the customer has dependents |
| `tenure` | Number of months with the company |
| `Contract` | Customer contract type |
| `MonthlyCharges` | Monthly customer charges |
| `TotalCharges` | Total charges recorded |
| `InternetService` | Internet service category |
| `PaymentMethod` | Customer payment method |
| `Churn` | Customer churn outcome |

The exact features used by each model depend on the project's preprocessing pipeline.

## 4. Data Preprocessing

The preprocessing workflow includes preparing columns for analysis, handling data types, addressing missing or invalid values where applicable, and encoding features as required by the modeling pipeline.

The cleaned dataset is saved as:

`data/telco_churn_cleaned.csv`

## 5. Machine Learning Models

Two classification models were evaluated:

- Logistic Regression
- LightGBM

The models predict customer churn from the available customer features. Model performance is evaluated using accuracy, precision, recall, F1-score, and ROC-AUC.

## 6. Model Evaluation Results

| Metric | Logistic Regression | LightGBM |
|---|---:|---:|
| Accuracy | 0.7331 | 0.7601 |
| Precision | 0.4983 | 0.5340 |
| Recall | 0.7914 | 0.7567 |
| F1-score | 0.6116 | 0.6261 |
| ROC-AUC | 0.8418 | 0.8361 |

These values are the project's recorded evaluation results. They should be interpreted in the context of the evaluation split and preprocessing used during model development.

## 7. Additional Analytics

### Customer Segmentation
Customer segments are generated using clustering to explore differences in customer behavior and churn rates.

### Customer Lifetime Value
CLV summaries provide estimates based on project-defined assumptions. They should not be treated as verified future revenue.

### Survival Analysis
Survival analysis explores customer retention over time.

### Uplift Analysis
The uplift experiment uses simulated treatment and outcome data because real campaign treatment labels were unavailable. Results are illustrative and do not demonstrate causal campaign effectiveness.

## 8. Generated Artifacts

| File | Purpose |
|---|---|
| `data/telco_churn_cleaned.csv` | Cleaned customer dataset |
| `data/simulated_uplift_experiment.csv` | Simulated campaign experiment data |
| `reports/model_comparison.csv` | Model evaluation summary |
| `reports/churn_by_contract.csv` | Churn analysis by contract |
| `reports/clv_summary.csv` | CLV summary |
| `reports/customer_segments.csv` | Customer segment assignments |
| `reports/customer_segment_summary.csv` | Segment-level summary |
| `reports/shap_feature_importance.png` | Feature-importance visualization |
| `reports/uplift_model_results.csv` | Illustrative uplift analysis results |
| `reports/uplift_model_notes.txt` | Uplift analysis limitations |
| `models/lightgbm_churn_pipeline.joblib` | Saved LightGBM pipeline |

## 9. Streamlit ROI Simulator

The application allows users to change campaign assumptions, such as the number of customers targeted, churn reduction, profit margin, offer cost, and retained-value period.

It calculates estimated retained customers, campaign cost, estimated benefit, net benefit, and illustrative ROI.

The simulator is a scenario-planning tool. Its outputs are not validated predictions of real campaign outcomes.

## 10. Reproducibility and Setup

Clone the repository:

```bash
git clone https://github.com/Tharunasri6713/customer-lifetime-value-churn-intelligence.git
cd customer-lifetime-value-churn-intelligence
```

Create and activate a Python virtual environment if desired, then install the dependencies required by the analysis and application.

Run the Streamlit application:

```bash
pip install -r requirements.txt
streamlit run app.py
```

Note: The current `requirements.txt` is intended for the Streamlit app. Reproducing the full analysis may require additional Python packages used during model development.

## 11. Limitations and Responsible Interpretation

- Model metrics do not guarantee future performance.
- Customer behavior can change over time.
- CLV results depend on the assumptions used.
- Simulated uplift results are not causal evidence.
- ROI outputs are hypothetical scenario estimates.
- Customer data should be handled responsibly and in accordance with applicable privacy requirements.

## 12. Project Links

**GitHub repository:** https://github.com/Tharunasri6713/customer-lifetime-value-churn-intelligence

**Live demo:** https://customer-lifetime-value-churn-intelligence-7hb8hgkxutn7yp7jido.streamlit.app/
