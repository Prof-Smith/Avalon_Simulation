
import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Avalon Tech Ventures - Financial Simulation", layout="wide")

st.title("🏢 Avalon Tech Ventures - Financial Analysis Simulator")
st.markdown("Apply key financial concepts interactively using real-world scenarios.")

# Module 1: NPV and IRR Calculation
st.header("📊 Investment Evaluation")
st.subheader("Net Present Value (NPV) and Internal Rate of Return (IRR)")

cash_flows = st.text_input("Enter cash flows separated by commas (e.g., -250,100,100,100,100,100)", "-250,100,100,100,100,100")
r = st.number_input("Discount Rate (%)", min_value=0.0, max_value=100.0, value=4.0)

if st.button("Calculate NPV and IRR"):
    cash_flows_list = [float(x) for x in cash_flows.split(",")]
    npv = sum(cf / (1 + r/100)**i for i, cf in enumerate(cash_flows_list))
    try:
        irr = np.irr(cash_flows_list) * 100
    except:
        irr = "Calculation Error"
    st.write(f"**NPV:** ${npv:.2f}")
    st.write(f"**IRR:** {irr if isinstance(irr, str) else f'{irr:.2f}%'}")

# Module 2: Loan Amortization
st.header("💰 Loan Structuring")
st.subheader("Flat Payment Schedule using PMT")

loan_amount = st.number_input("Loan Amount", value=10000.0)
interest_rate = st.number_input("Annual Interest Rate (%)", value=7.0)
loan_years = st.number_input("Loan Term (Years)", value=10)

if st.button("Calculate Loan Payments"):
    rate = interest_rate / 100
    payments = loan_years
    pmt = np.pmt(rate, payments, -loan_amount)
    st.write(f"**Annual Payment:** ${pmt:.2f}")

# Module 3: Retirement Planning
st.header("🏖️ Retirement Planning")
st.subheader("Future Value and Present Value Calculations")

deposit_years = st.number_input("Years of Deposit", value=5)
withdraw_years = st.number_input("Years of Withdrawal", value=8)
annual_withdrawal = st.number_input("Annual Withdrawal Amount", value=30000.0)
retirement_rate = st.number_input("Annual Interest Rate (%)", value=7.0)

if st.button("Calculate Required Annual Deposit"):
    r = retirement_rate / 100
    pv_withdrawals = annual_withdrawal * (1 - (1 + r)**-withdraw_years) / r
    annual_deposit = pv_withdrawals / ((1 + r) * ((1 - (1 + r)**-deposit_years) / r))
    st.write(f"**Required Annual Deposit:** ${annual_deposit:.2f}")

# Module 4: Continuous Compounding
st.header("🔁 Continuous Compounding")
st.subheader("Compare Compounding Methods")

principal = st.number_input("Initial Deposit", value=1000.0)
rate_cc = st.number_input("Annual Interest Rate (%)", value=5.0)
time_cc = st.number_input("Time (Years)", value=1.0)

if st.button("Calculate Future Value with Continuous Compounding"):
    fv_continuous = principal * np.exp(rate_cc / 100 * time_cc)
    st.write(f"**Future Value (Continuous Compounding):** ${fv_continuous:.2f}")

# Module 5: Irregular Cash Flows
st.header("📅 Irregular Cash Flows")
st.subheader("XNPV and XIRR Simulation")

dates_input = st.text_input("Enter dates (YYYY-MM-DD) separated by commas", "2025-01-01,2026-01-01,2027-01-01")
cash_input = st.text_input("Enter corresponding cash flows separated by commas", "-1000,500,700")
discount_rate_xnpv = st.number_input("Discount Rate for XNPV (%)", value=10.0)

if st.button("Calculate XNPV and XIRR"):
    dates = [datetime.strptime(d.strip(), "%Y-%m-%d") for d in dates_input.split(",")]
    cash_flows = [float(c.strip()) for c in cash_input.split(",")]
    df = pd.DataFrame({"Date": dates, "Cash Flow": cash_flows})
    df["Days"] = (df["Date"] - df["Date"].iloc[0]).dt.days
    xnpv = sum(cf / (1 + discount_rate_xnpv/100)**(days/365) for cf, days in zip(df["Cash Flow"], df["Days"]))
    try:
        xirr = np.irr(cash_flows) * 100
    except:
        xirr = "Calculation Error"
    st.write(f"**XNPV:** ${xnpv:.2f}")
    st.write(f"**XIRR:** {xirr if isinstance(xirr, str) else f'{xirr:.2f}%'}")
