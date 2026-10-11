
import streamlit as st

st.set_page_config(
    page_title="Customer Retention ROI Simulator",
    page_icon="📊",
    layout="wide"
)

st.title("Customer Lifetime Value & Churn Intelligence")
st.write(
    "Explore hypothetical retention campaign outcomes. "
    "All campaign effects and costs are assumptions."
)

st.sidebar.header("Campaign assumptions")

customers = st.sidebar.number_input(
    "Customers targeted", min_value=1, value=500, step=50
)
monthly_charge = st.sidebar.number_input(
    "Average monthly charge", min_value=0.0, value=70.0
)
profit_margin = st.sidebar.slider(
    "Profit margin (%)", 1, 100, 30
)
baseline_churn = st.sidebar.slider(
    "Baseline churn rate (%)", 0, 100, 27
)
assumed_reduction = st.sidebar.slider(
    "Assumed relative churn reduction (%)", 0, 100, 10
)
offer_cost = st.sidebar.number_input(
    "Offer cost per customer", min_value=0.0, value=10.0
)
months_saved = st.sidebar.slider(
    "Months of retained value", 1, 24, 6
)

expected_churners = customers * baseline_churn / 100
saved_customers = expected_churners * assumed_reduction / 100
value_per_customer = monthly_charge * profit_margin / 100 * months_saved
estimated_benefit = saved_customers * value_per_customer
campaign_cost = customers * offer_cost
net_benefit = estimated_benefit - campaign_cost

roi = (
    (net_benefit / campaign_cost) * 100
    if campaign_cost > 0 else None
)

st.subheader("Scenario results")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Customers targeted", f"{customers:,}")
col2.metric("Estimated customers retained", f"{saved_customers:,.1f}")
col3.metric("Campaign cost", f"{campaign_cost:,.2f}")
col4.metric("Estimated net benefit", f"{net_benefit:,.2f}")

if roi is not None:
    st.metric("Illustrative ROI", f"{roi:,.1f}%")
else:
    st.info("ROI is undefined when campaign cost is zero.")

st.subheader("Calculation details")
st.write(f"Expected churners before campaign: {expected_churners:,.1f}")
st.write(f"Estimated value per retained customer: {value_per_customer:,.2f}")
st.write(f"Estimated benefit: {estimated_benefit:,.2f}")

st.warning(
    "Illustrative scenario only. Churn reduction, profit margin, "
    "offer cost, and retained months are assumptions, not validated "
    "predictions of actual campaign performance."
)
