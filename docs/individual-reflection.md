# Individual Reflection — Customer Lifetime Value & Churn Intelligence

**Intern:** Tharunasri Mogilicharla  
**Project:** DS-01 — Customer Lifetime Value & Churn Intelligence  
**Specialization:** Data Science

## 1. Project Overview

I worked on a Customer Lifetime Value and Churn Intelligence project to analyze customer churn, identify customer segments, compare machine learning models, and explore potential customer retention strategies.

The project uses a telecommunications customer churn dataset containing 7,043 records. I developed an end-to-end workflow that combines data analysis, machine learning, customer analytics, and an interactive Streamlit application.

## 2. My Contributions

My work on this project included:

- Preparing and analyzing the customer churn dataset.
- Training and comparing Logistic Regression and LightGBM classification models.
- Evaluating model performance using accuracy, precision, recall, F1-score, and ROC-AUC.
- Exploring customer segmentation, customer lifetime value summaries, and churn patterns.
- Creating supporting reports and visualizations for the project.
- Developing an interactive Streamlit application to explore hypothetical customer retention campaign outcomes.
- Organizing the project files and documentation in a GitHub repository.
- Deploying the application and checking its behavior by changing the number of targeted customers.
- Preparing architecture, data and model documentation, testing records, and a final presentation.

## 3. Key Results

The LightGBM model achieved an accuracy of approximately 76.01%, an F1-score of 0.6261, and a ROC-AUC of 0.8361 on the recorded evaluation.

The Logistic Regression model achieved an accuracy of approximately 73.31% and a ROC-AUC of 0.8418. Comparing the models helped me understand that accuracy alone does not determine which model is best; precision, recall, F1-score, and ROC-AUC also provide useful information.

I also created a Streamlit simulator that allows users to explore estimated retention campaign costs and returns under different assumptions.

## 4. Challenges and Learning

One important learning experience was understanding how to evaluate classification models using multiple metrics rather than relying only on accuracy. I also learned to interpret customer analytics outputs carefully and to distinguish model predictions from business assumptions.

Building and deploying the Streamlit application helped me understand how a machine learning project can be presented through an interactive interface. Organizing the repository and writing technical documentation also improved my understanding of project structure, reproducibility, and communicating technical work.

Testing the application by changing the number of targeted customers helped me verify that the displayed scenario estimates responded to user inputs.

## 5. Limitations and Responsible Interpretation

The project uses a telecommunications churn dataset, and the retention campaign experiment uses simulated treatment data. Therefore, the estimated campaign effects and ROI are illustrative rather than proven real-world outcomes.

The results should not be interpreted as guaranteed business savings or customer retention improvements. Further validation with real campaign data, better cost estimates, and additional testing would be necessary before using the system for business decisions.

## 6. Future Improvements

Possible improvements include validating the models on additional data, tuning model parameters, improving customer lifetime value estimates, using real retention campaign results to evaluate uplift, and expanding application testing.

## 7. Conclusion

This project helped me apply data science concepts to a practical business problem. I gained experience with Python-based data analysis, machine learning evaluation, customer analytics, Streamlit application development, GitHub project organization, and technical documentation.

It also helped me understand the importance of evaluating models carefully, documenting limitations, testing interactive applications, and communicating results clearly.
