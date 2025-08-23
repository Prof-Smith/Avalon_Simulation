
# Avalon Tech Ventures - Financial Analysis Simulator

This Streamlit app allows users to explore key financial modeling concepts interactively.

## Modules Included
1. **Investment Evaluation** – NPV and IRR calculator
2. **Loan Structuring** – Flat payment schedule using PMT
3. **Retirement Planning** – Required deposits using FV and PV
4. **Continuous Compounding** – Compare compounding methods
5. **Irregular Cash Flows** – XNPV and XIRR with date-based inputs

## Installation
To install the required dependencies, run:
```bash
pip install -r requirements.txt
```

## Running the App
To launch the Streamlit app, run:
```bash
streamlit run avalon_simulation.py
```

## Requirements
- Python 3.7+
- Streamlit
- NumPy
- Pandas
- numpy-financial

## Troubleshooting
If you encounter an error related to `numpy_financial`, please install it using:
```bash
pip install numpy-financial
```
Then restart the Streamlit app.

## Author
Created for educational use based on *Financial Modeling, 5th Edition* by Benninga & Mofkadi.
