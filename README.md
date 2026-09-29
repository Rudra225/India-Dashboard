<div align="center">
  <h1>🇮🇳 India Political & Economic Dashboard</h1>
  <p>A fully automated data engine tracking India's macroeconomy, Union Budgets, and the financial backgrounds of 4,500+ sitting MLAs and MPs.</p>

  <img src="https://img.shields.io/badge/Python-3.11+-blue.svg?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B.svg?logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/Pandas-150458.svg?logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/Status-Active-success.svg" alt="Status">
</div>

<br>

## 📌 Overview
This project solves the problem of scattered public data in India. Instead of manually searching through dozens of disconnected government portals, this dashboard aggregates, cleans, and visualizes decades of historical and real-time government data into a single interactive interface.

### ✨ Key Features
- **Macro Economy Tracker:** Correlates GDP growth, inflation, and INR/USD exchange rates with every Prime Minister's tenure (1947–2024).
- **Union Budget Analytics:** Visualizes sector-wise allocations vs. actual expenditures.
- **State Metrics:** Interactive tracking of State GDP, Debt, and Crime Statistics across all 30 regions.
- **Local Leaders (Live):** Parses unstructured election affidavits to display the live financial backgrounds (Assets, Liabilities, Dues) of 4,500+ sitting Lok Sabha MPs and State MLAs.

## ⚙️ The Engineering Stack
- **Frontend / UI:** `Streamlit`, `Plotly`, `HTML/CSS injected tables`
- **Data Processing:** `Pandas`, `NumPy`, `Regex` (for cleaning corrupted affidavit HTML)
- **Data Ingestion Pipeline (Backend):** Asynchronous Python scrapers using `curl_cffi` to responsibly bypass rate-limits and fetch thousands of records concurrently.

## 🚀 Quick Start
### 1. Clone the repository
```bash
git clone https://github.com/Rudra225/India-Dashboard.git
cd India-Dashboard
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the application
```bash
streamlit run src/app.py
```
*The app will automatically open in your browser at `http://localhost:8501`.*

## 📂 Repository Architecture
```text
India-Dashboard/
├── src/                  # Frontend Streamlit App & Logic
│   ├── app.py            # Main entry point
│   ├── helpers.py        # UI rendering utilities and CSS
│   ├── pages/            # Multi-page dashboard views
│   └── data/             # Static JSON stores (ECI / MyNeta / RBI)
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```
*(Note: Backend scraping scripts and infrastructure pipelines are intentionally excluded from this public repository for security and rate-limiting compliance).*

## ⚠️ Legal Disclaimer
**Educational Project Only.** The data presented in this dashboard (especially asset and liability declarations of public officials) is programmatically scraped from public sources (Election Commission of India / ADR MyNeta). Due to the nature of unstructured HTML parsing and data extraction, **accuracy is not guaranteed**. 
- This repository is provided "as is" for research and educational purposes only.
- The creator assumes no legal liability for any discrepancies, errors, or misrepresentations in the parsed data.
- For verified, official figures, please consult the original affidavits filed with the Election Commission of India at [affidavit.eci.gov.in](https://affidavit.eci.gov.in).
