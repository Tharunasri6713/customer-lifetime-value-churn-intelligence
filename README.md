# Customer Lifetime Value & Churn Intelligence

A machine learning project for customer churn prediction, customer segmentation, survival analysis, and retention campaign ROI simulation.

## Objectives
- Analyze customer churn patterns.
- Compare Logistic Regression and LightGBM.
- Perform survival analysis using Lifelines.
- Explain predictions using SHAP.
- Segment customers with K-Means.
- Demonstrate uplift modeling with simulated treatment data.
- Explore hypothetical retention campaign ROI in Streamlit.

## Technology Stack
Python, Pandas, Scikit-learn, LightGBM, Lifelines, SHAP, CausalML, Matplotlib, Streamlit.

## Dataset
IBM Telco Customer Churn:
https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv

## Model Results

| Model | Accuracy | Precision | Recall | F1 | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 0.7331 | 0.4983 | 0.7914 | 0.6116 | 0.8418 |
| LightGBM | 0.7601 | 0.5340 | 0.7567 | 0.6261 | 0.8361 |

Metrics reflect the current evaluation run and may vary with different configurations.

## Streamlit ROI Simulator
The app lets users adjust customer counts, monthly charges, profit margin, baseline churn, assumed churn reduction, campaign costs, and retained-value duration.

It estimates potential saved customers, campaign costs, net benefit, and ROI. These outputs are hypothetical scenarios, not validated financial forecasts.

## Project Files
- `app.py`: Streamlit ROI simulator
- `requirements.txt`: App dependency
- `data/`: Cleaned customer data and simulated experiment
- `reports/`: Model metrics, CLV summaries, segmentation and uplift outputs
- `models/`: Trained LightGBM pipeline

## Important Limitations
- CLV values are illustrative proxy estimates, not actual realized profit.
- Uplift treatment labels and outcomes are simulated; results do not establish real causal effects.
- SHAP explains model predictions, not causation.
- ROI calculations depend on user-defined assumptions.

## Run Locally
Install dependencies:

    pip install -r requirements.txt

Start the app:

    streamlit run app.py

## Author
Tharunasri Mogilicharla

B.Tech — Computer Science and Engineering (Data Science)
