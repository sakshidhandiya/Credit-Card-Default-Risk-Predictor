# Credit-Card-Default-Risk-Predictor
To build, evaluate, and deploy an interpretable credit risk model that predicts the probability of credit card default and converts it into actionable risk categories, using industry-aligned modeling and deployment practices.

1️⃣ PROBLEM STATEMENT

Financial institutions must identify customers who are likely to default before losses occur.
The challenge is to:

Capture behavioral risk patterns

Maintain model interpretability

Ensure governance & deployment readiness

This project simulates a real banking risk analytics workflow, from raw data to a deployed application.

2️⃣ DATASET

Dataset: UCI Credit Card Default Dataset

Records: 30,000 customers

Target Variable: DEFAULT (1 = default, 0 = non-default)

Key Feature Groups

Exposure: Credit limit

Behavior: Payment delays, repayment volatility

Utilization: Credit usage vs limit

Demographics: Age, education, marital status

3️⃣ DATA CLEANING & PREPROCESSING

Steps Performed

Renamed target variable for clarity

Removed non-informative ID column

Cleaned invalid categorical values

Validated age and payment fields

Ensured no missing values

Important Design Choice

Behavior > Demographics

Behavioral variables were prioritized, aligning with real credit risk policy.

4️⃣ FEATURE ENGINEERING (CORE STRENGTH)

Created domain-driven features instead of using raw monthly data:

Feature	Description

CREDIT_UTILIZATION	Avg bill / credit limit

PAYMENT_RATIO	Avg payment / avg bill

MAX_DELAY	Worst delinquency

AVG_DELAY	Persistent delinquency

DELINQUENCY_TREND	Worsening vs improving behavior

DELAY_STD	Payment volatility

👉 These features make the model interpretable and stable.

5️⃣ MODELING STRATEGY

Why Logistic Regression (Primary Model)

Interpretable coefficients

Regulator-friendly

Stable and explainable

Industry standard in credit risk

Challengers Evaluated

Decision Tree

Random Forest

Voting Ensemble

Stacking Ensemble

Key Finding:
Ensembles marginally improved ROC-AUC but did not justify loss of interpretability.

✔ Logistic Regression retained as production model

✔ Trees & ensembles used for benchmarking only

6️⃣ MODEL EVALUATION

Metrics Used

ROC-AUC (primary)

Default Recall (business-critical)

Precision, Accuracy (secondary)

Final Logistic Regression Performance

ROC-AUC: ~0.73

Default Recall: ~61%

Interpretation: Risk-conservative and business-aligned

7️⃣ THRESHOLD & RISK BUCKETING

Instead of raw probabilities, predictions were mapped to actionable risk buckets:

Probability -	Risk - Level -	Business Action
< 0.35 -	Low -	Normal - monitoring
0.35 – 0.60 -	Medium -	Reminders & monitoring
> 0.60 -	High -	Proactive risk controls

This converts ML output → decision support.

8️⃣ DEPLOYMENT ARCHITECTURE

Deployment Principles

Deploy only Logistic Regression

Keep preprocessing inside pipeline

Ensure version compatibility

Business-friendly UI

Tech Stack

Python

scikit-learn

Streamlit

joblib

9️⃣ STREAMLIT APPLICATION

App Features

Human-readable inputs (Education, Marital Status, Gender)

Probability-based prediction

Clear risk classification

Business action recommendations

Output Example

Default Probability: 50.3%

Risk: Medium

Action: Monitor closely

🔟 FINAL OUTCOME

✔ End-to-end ML lifecycle

✔ Bank-grade modeling decisions

✔ Deployed & usable application

✔ Interview-ready project
