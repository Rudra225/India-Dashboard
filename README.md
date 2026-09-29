# 🇮🇳 India Political-Economic Dashboard

A transparency tool covering ALL Indian Prime Ministers and Finance Ministers since 1947.

## 📦 Setup (Do this once)

### Step 1 — Install Python
Download Python 3.11+ from https://www.python.org/downloads/

### Step 2 — Install required libraries
Open Terminal (Mac/Linux) or Command Prompt (Windows), then run:
```
pip install streamlit pandas plotly
```

### Step 3 — Run the app
Navigate to this folder in Terminal/Command Prompt:
```
cd path/to/india-leader-dashboard
streamlit run app.py
```
The app will open automatically at http://localhost:8501

## 📊 What's inside
- **15 Prime Ministers** — Nehru to Modi (1947–2024)
- **30+ Finance Ministers** — RK Shanmukham Chetty to Nirmala Sitharaman
- **Union Budget data** — 1947–2024 (allocation vs actual spend)
- **Economic indicators** — INR/USD, GDP growth, CPI, fiscal deficit, FDI
- **EC asset declarations** — post-1999 leaders
- **Party asset data** — INC vs BJP

## 🗂️ Data Sources
All data sourced from:
- https://www.indiabudget.gov.in — Budget documents
- https://cag.gov.in — Audit/actual expenditure
- https://rbi.org.in — Macroeconomic data
- https://affidavit.eci.gov.in — EC declarations
- https://myneta.info — ADR asset analysis
- https://mospi.gov.in — CPI/GDP data
- https://data.worldbank.org/country/india — GDP growth
- https://fred.stlouisfed.org — Historical FX rates
- https://dpiit.gov.in — FDI statistics
