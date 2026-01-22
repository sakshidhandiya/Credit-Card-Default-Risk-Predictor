import streamlit as st
from model import predict_default_probability

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(
    page_title="Credit Card Default Risk Predictor",
    layout="centered"
)

# -----------------------------
# Title & description
# -----------------------------
st.title("💳 Credit Card Default Risk Predictor")
st.write(
    "This app predicts the probability of credit card default "
    "using an interpretable **Logistic Regression** model."
)

# -----------------------------
# Category mappings (UI → Model)
# -----------------------------
SEX_MAP = {
    "Male": 1,
    "Female": 2
}

EDUCATION_MAP = {
    "Graduate School": 1,
    "University": 2,
    "High School": 3,
    "Other / Unknown": 4
}

MARRIAGE_MAP = {
    "Married": 1,
    "Single": 2,
    "Other": 3
}

# -----------------------------
# Sidebar inputs
# -----------------------------
st.sidebar.header("Customer Information")

LIMIT_BAL = st.sidebar.number_input(
    "Credit Limit", min_value=1000, value=50000, step=1000
)

AGE = st.sidebar.number_input(
    "Age", min_value=18, max_value=100, value=35
)

sex_label = st.sidebar.selectbox("Gender", list(SEX_MAP.keys()))
SEX = SEX_MAP[sex_label]

education_label = st.sidebar.selectbox(
    "Education Level", list(EDUCATION_MAP.keys())
)
EDUCATION = EDUCATION_MAP[education_label]

marriage_label = st.sidebar.selectbox(
    "Marital Status", list(MARRIAGE_MAP.keys())
)
MARRIAGE = MARRIAGE_MAP[marriage_label]

st.sidebar.header("Payment Behavior")

MAX_DELAY = st.sidebar.slider("Max Payment Delay (months)", -1, 8, 0)
AVG_DELAY = st.sidebar.slider("Average Payment Delay", -1.0, 8.0, 0.0)
DELINQUENCY_TREND = st.sidebar.slider("Delinquency Trend", -8, 8, 0)
DELAY_STD = st.sidebar.slider("Payment Volatility", 0.0, 4.0, 0.0)

CREDIT_UTILIZATION = st.sidebar.slider(
    "Credit Utilization Ratio", 0.0, 1.5, 0.3
)
PAYMENT_RATIO = st.sidebar.slider(
    "Payment Ratio", 0.0, 5.0, 0.5
)

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict Risk"):
    input_data = {
        "LIMIT_BAL": LIMIT_BAL,
        "CREDIT_UTILIZATION": CREDIT_UTILIZATION,
        "PAYMENT_RATIO": PAYMENT_RATIO,
        "MAX_DELAY": MAX_DELAY,
        "AVG_DELAY": AVG_DELAY,
        "DELINQUENCY_TREND": DELINQUENCY_TREND,
        "DELAY_STD": DELAY_STD,
        "AGE": AGE,
        "SEX": SEX,
        "EDUCATION": EDUCATION,
        "MARRIAGE": MARRIAGE
    }

    probability = predict_default_probability(input_data)

    st.subheader("📊 Prediction Result")
    st.metric("Default Probability", f"{probability:.2%}")

    # -----------------------------
    # Risk Buckets
    # -----------------------------
    if probability < 0.35:
        st.success("🟢 **Low Risk**: Normal monitoring recommended.")
    elif probability < 0.60:
        st.warning("🟡 **Medium Risk**: Monitor closely and send reminders.")
    else:
        st.error("🔴 **High Risk**: Consider proactive risk control actions.")

    st.caption(
        "Model: Logistic Regression | Built for explainable credit risk analysis"
    )
