# ============================================================
# DATA: Union Budget — India (1947–2025)
# ============================================================
# Sources:
#   1994–2025 (verified):
#     CivicDataLab / Open Budgets India — Budget at a Glance Timeseries
#     https://openbudgetsindia.org/dataset/union-budget-at-a-glance-timeseries
#     Original source: Ministry of Finance, Government of India
#     https://www.indiabudget.gov.in
#     CAG Audit Reports (for Actuals): https://cag.gov.in/en/audit-report
#
#   Pre-1994 (estimates only):
#     dataful.in — "Total Expenditure since 1947-48"
#     https://dataful.in/datasets/20200/
#     Source: Ministry of Finance (Budget Estimates only — no Actuals available)
#
# IMPORTANT NOTES:
#   - All values in ₹ Crore
#   - "allocated" = Budget Estimate (BE) as presented to Parliament
#   - "spent"     = Actuals from CAG audit reports
#   - FY format: 1994-1995 means April 1994 – March 1995
#   - Pre-1994: "spent" = None (actuals not in any verified digital source)
#   - Pre-1994: "allocated" = Budget Estimate only, sourced from dataful.in
#   - SAME data is used for both PM and FM under the same FY year
#     (Budget is a single national document — not separate for PM/FM)
# ============================================================

# ── FY Year → Leader mapping ──────────────────────────────────
# Used to filter budget rows for each leader's tenure
# Key = start year of FY (e.g. 1994 for FY 1994-1995)
# PM/FM in office in April of that year gets credited
FY_TO_PM = {
    1947:"Jawaharlal Nehru (1947–1964)",
    1948:"Jawaharlal Nehru (1947–1964)",
    1949:"Jawaharlal Nehru (1947–1964)",
    1950:"Jawaharlal Nehru (1947–1964)",
    1951:"Jawaharlal Nehru (1947–1964)",
    1952:"Jawaharlal Nehru (1947–1964)",
    1953:"Jawaharlal Nehru (1947–1964)",
    1954:"Jawaharlal Nehru (1947–1964)",
    1955:"Jawaharlal Nehru (1947–1964)",
    1956:"Jawaharlal Nehru (1947–1964)",
    1957:"Jawaharlal Nehru (1947–1964)",
    1958:"Jawaharlal Nehru (1947–1964)",
    1959:"Jawaharlal Nehru (1947–1964)",
    1960:"Jawaharlal Nehru (1947–1964)",
    1961:"Jawaharlal Nehru (1947–1964)",
    1962:"Jawaharlal Nehru (1947–1964)",
    1963:"Jawaharlal Nehru (1947–1964)",
    1964:"Lal Bahadur Shastri (1964–1966)",
    1965:"Lal Bahadur Shastri (1964–1966)",
    1966:"Indira Gandhi (1966–1977)",
    1967:"Indira Gandhi (1966–1977)",
    1968:"Indira Gandhi (1966–1977)",
    1969:"Indira Gandhi (1966–1977)",
    1970:"Indira Gandhi (1966–1977)",
    1971:"Indira Gandhi (1966–1977)",
    1972:"Indira Gandhi (1966–1977)",
    1973:"Indira Gandhi (1966–1977)",
    1974:"Indira Gandhi (1966–1977)",
    1975:"Indira Gandhi (1966–1977)",
    1976:"Indira Gandhi (1966–1977)",
    1977:"Morarji Desai (1977–1979)",
    1978:"Morarji Desai (1977–1979)",
    1979:"Charan Singh (1979–1980)",
    1980:"Indira Gandhi (1980–1984)",
    1981:"Indira Gandhi (1980–1984)",
    1982:"Indira Gandhi (1980–1984)",
    1983:"Indira Gandhi (1980–1984)",
    1984:"Rajiv Gandhi (1984–1989)",
    1985:"Rajiv Gandhi (1984–1989)",
    1986:"Rajiv Gandhi (1984–1989)",
    1987:"Rajiv Gandhi (1984–1989)",
    1988:"Rajiv Gandhi (1984–1989)",
    1989:"V.P. Singh (1989–1990)",
    1990:"Chandra Shekhar (1990–1991)",
    1991:"P.V. Narasimha Rao (1991–1996)",
    1992:"P.V. Narasimha Rao (1991–1996)",
    1993:"P.V. Narasimha Rao (1991–1996)",
    1994:"P.V. Narasimha Rao (1991–1996)",
    1995:"P.V. Narasimha Rao (1991–1996)",
    1996:"H.D. Deve Gowda (1996–1997)",
    1997:"I.K. Gujral (1997–1998)",
    1998:"Atal Bihari Vajpayee (1998–1999)",
    1999:"Atal Bihari Vajpayee (1999–2004)",
    2000:"Atal Bihari Vajpayee (1999–2004)",
    2001:"Atal Bihari Vajpayee (1999–2004)",
    2002:"Atal Bihari Vajpayee (1999–2004)",
    2003:"Atal Bihari Vajpayee (1999–2004)",
    2004:"Manmohan Singh (2004–2014)",
    2005:"Manmohan Singh (2004–2014)",
    2006:"Manmohan Singh (2004–2014)",
    2007:"Manmohan Singh (2004–2014)",
    2008:"Manmohan Singh (2004–2014)",
    2009:"Manmohan Singh (2004–2014)",
    2010:"Manmohan Singh (2004–2014)",
    2011:"Manmohan Singh (2004–2014)",
    2012:"Manmohan Singh (2004–2014)",
    2013:"Manmohan Singh (2004–2014)",
    2014:"Narendra Modi (2014–present)",
    2015:"Narendra Modi (2014–present)",
    2016:"Narendra Modi (2014–present)",
    2017:"Narendra Modi (2014–present)",
    2018:"Narendra Modi (2014–present)",
    2019:"Narendra Modi (2014–present)",
    2020:"Narendra Modi (2014–present)",
    2021:"Narendra Modi (2014–present)",
    2022:"Narendra Modi (2014–present)",
    2023:"Narendra Modi (2014–present)",
    2024:"Narendra Modi (2014–present)",
}

FY_TO_FM = {
    1947:"R.K. Shanmukham Chetty (1947–1948)",
    1948:"John Mathai (1948–1950)",
    1949:"John Mathai (1948–1950)",
    1950:"C.D. Deshmukh (1950–1956)",
    1951:"C.D. Deshmukh (1950–1956)",
    1952:"C.D. Deshmukh (1950–1956)",
    1953:"C.D. Deshmukh (1950–1956)",
    1954:"C.D. Deshmukh (1950–1956)",
    1955:"C.D. Deshmukh (1950–1956)",
    1956:"T.T. Krishnamachari (1956–1958)",
    1957:"T.T. Krishnamachari (1956–1958)",
    1958:"Morarji Desai (1958–1963)",
    1959:"Morarji Desai (1958–1963)",
    1960:"Morarji Desai (1958–1963)",
    1961:"Morarji Desai (1958–1963)",
    1962:"Morarji Desai (1958–1963)",
    1963:"T.T. Krishnamachari (1964–1966)",
    1964:"T.T. Krishnamachari (1964–1966)",
    1965:"T.T. Krishnamachari (1964–1966)",
    1966:"Sachin Chaudhuri (1966–1967)",
    1967:"Morarji Desai (1967–1969)",
    1968:"Morarji Desai (1967–1969)",
    1969:"Indira Gandhi (FM Charge, 1969–1970)",
    1970:"Y.B. Chavan (1971–1975)",
    1971:"Y.B. Chavan (1971–1975)",
    1972:"Y.B. Chavan (1971–1975)",
    1973:"Y.B. Chavan (1971–1975)",
    1974:"Y.B. Chavan (1971–1975)",
    1975:"C. Subramaniam (1975–1977)",
    1976:"C. Subramaniam (1975–1977)",
    1977:"H.M. Patel (1977–1978)",
    1978:"Charan Singh (1978–1979)",
    1979:"R. Venkataraman (1980–1982)",
    1980:"R. Venkataraman (1980–1982)",
    1981:"R. Venkataraman (1980–1982)",
    1982:"Pranab Mukherjee (1982–1984)",
    1983:"Pranab Mukherjee (1982–1984)",
    1984:"V.P. Singh (1984–1986)",
    1985:"V.P. Singh (1984–1986)",
    1986:"N.D. Tiwari (1987–1988)",
    1987:"N.D. Tiwari (1987–1988)",
    1988:"S.B. Chavan (1988–1989)",
    1989:"Madhu Dandavate (1989–1990)",
    1990:"Yashwant Sinha (1990–1991)",
    1991:"Manmohan Singh (1991–1996)",
    1992:"Manmohan Singh (1991–1996)",
    1993:"Manmohan Singh (1991–1996)",
    1994:"Manmohan Singh (1991–1996)",
    1995:"Manmohan Singh (1991–1996)",
    1996:"P. Chidambaram (1996–1998)",
    1997:"P. Chidambaram (1996–1998)",
    1998:"Yashwant Sinha (1998–2002)",
    1999:"Yashwant Sinha (1998–2002)",
    2000:"Yashwant Sinha (1998–2002)",
    2001:"Yashwant Sinha (1998–2002)",
    2002:"Jaswant Singh (2002–2004)",
    2003:"Jaswant Singh (2002–2004)",
    2004:"P. Chidambaram (2004–2008)",
    2005:"P. Chidambaram (2004–2008)",
    2006:"P. Chidambaram (2004–2008)",
    2007:"P. Chidambaram (2004–2008)",
    2008:"Pranab Mukherjee (2009–2012)",
    2009:"Pranab Mukherjee (2009–2012)",
    2010:"Pranab Mukherjee (2009–2012)",
    2011:"Pranab Mukherjee (2009–2012)",
    2012:"P. Chidambaram (2012–2014)",
    2013:"P. Chidambaram (2012–2014)",
    2014:"Arun Jaitley (2014–2019)",
    2015:"Arun Jaitley (2014–2019)",
    2016:"Arun Jaitley (2014–2019)",
    2017:"Arun Jaitley (2014–2019)",
    2018:"Arun Jaitley (2014–2019)",
    2019:"Nirmala Sitharaman (2019–present)",
    2020:"Nirmala Sitharaman (2019–present)",
    2021:"Nirmala Sitharaman (2019–present)",
    2022:"Nirmala Sitharaman (2019–present)",
    2023:"Nirmala Sitharaman (2019–present)",
    2024:"Nirmala Sitharaman (2019–present)",
}

# ── Main Budget Data ──────────────────────────────────────────
# Key = FY start year (e.g. 1994 = FY 1994-1995)
# All values in ₹ Crore
# "allocated" = Budget Estimate (BE) as tabled in Parliament
# "spent"     = Actual Expenditure from CAG Audit Reports
# "source"    = data origin
# "data_type" = "verified" | "estimate_only"

_SRC_OBI    = "https://openbudgetsindia.org/dataset/union-budget-at-a-glance-timeseries"
_SRC_MOF    = "https://www.indiabudget.gov.in"
_SRC_CAG    = "https://cag.gov.in/en/audit-report"
_SRC_DATAFUL= "https://dataful.in/datasets/20200/"

UNION_BUDGET_DATA = {

    # ── PRE-1994: Budget Estimates only ──────────────────────
    # Source: dataful.in (Ministry of Finance data)
    # "spent" = None (actuals not available in verified digital form)
    # These are ESTIMATE figures only — labeled as such in app

    1947: {"allocated": 197,    "spent": None, "fiscal_deficit_gdp": None,
           "source": _SRC_DATAFUL, "data_type": "estimate_only"},
    1948: {"allocated": 338,    "spent": None, "fiscal_deficit_gdp": None,
           "source": _SRC_DATAFUL, "data_type": "estimate_only"},
    1949: {"allocated": 370,    "spent": None, "fiscal_deficit_gdp": None,
           "source": _SRC_DATAFUL, "data_type": "estimate_only"},
    1950: {"allocated": 379,    "spent": None, "fiscal_deficit_gdp": None,
           "source": _SRC_DATAFUL, "data_type": "estimate_only"},
    1951: {"allocated": 430,    "spent": None, "fiscal_deficit_gdp": None,
           "source": _SRC_DATAFUL, "data_type": "estimate_only"},
    1952: {"allocated": 515,    "spent": None, "fiscal_deficit_gdp": None,
           "source": _SRC_DATAFUL, "data_type": "estimate_only"},
    1953: {"allocated": 530,    "spent": None, "fiscal_deficit_gdp": None,
           "source": _SRC_DATAFUL, "data_type": "estimate_only"},
    1954: {"allocated": 560,    "spent": None, "fiscal_deficit_gdp": None,
           "source": _SRC_DATAFUL, "data_type": "estimate_only"},
    1955: {"allocated": 610,    "spent": None, "fiscal_deficit_gdp": None,
           "source": _SRC_DATAFUL, "data_type": "estimate_only"},
    1956: {"allocated": 720,    "spent": None, "fiscal_deficit_gdp": None,
           "source": _SRC_DATAFUL, "data_type": "estimate_only"},
    1957: {"allocated": 830,    "spent": None, "fiscal_deficit_gdp": None,
           "source": _SRC_DATAFUL, "data_type": "estimate_only"},
    1958: {"allocated": 890,    "spent": None, "fiscal_deficit_gdp": None,
           "source": _SRC_DATAFUL, "data_type": "estimate_only"},
    1959: {"allocated": 980,    "spent": None, "fiscal_deficit_gdp": None,
           "source": _SRC_DATAFUL, "data_type": "estimate_only"},
    1960: {"allocated": 1085,   "spent": None, "fiscal_deficit_gdp": None,
           "source": _SRC_DATAFUL, "data_type": "estimate_only"},
    1961: {"allocated": 1210,   "spent": None, "fiscal_deficit_gdp": None,
           "source": _SRC_DATAFUL, "data_type": "estimate_only"},
    1962: {"allocated": 1480,   "spent": None, "fiscal_deficit_gdp": None,
           "source": _SRC_DATAFUL, "data_type": "estimate_only"},
    1963: {"allocated": 1730,   "spent": None, "fiscal_deficit_gdp": None,
           "source": _SRC_DATAFUL, "data_type": "estimate_only"},
    1964: {"allocated": 1980,   "spent": None, "fiscal_deficit_gdp": None,
           "source": _SRC_DATAFUL, "data_type": "estimate_only"},
    1965: {"allocated": 2290,   "spent": None, "fiscal_deficit_gdp": None,
           "source": _SRC_DATAFUL, "data_type": "estimate_only"},
    1966: {"allocated": 2640,   "spent": None, "fiscal_deficit_gdp": None,
           "source": _SRC_DATAFUL, "data_type": "estimate_only"},
    1967: {"allocated": 2950,   "spent": None, "fiscal_deficit_gdp": None,
           "source": _SRC_DATAFUL, "data_type": "estimate_only"},
    1968: {"allocated": 3110,   "spent": None, "fiscal_deficit_gdp": None,
           "source": _SRC_DATAFUL, "data_type": "estimate_only"},
    1969: {"allocated": 3380,   "spent": None, "fiscal_deficit_gdp": None,
           "source": _SRC_DATAFUL, "data_type": "estimate_only"},
    1970: {"allocated": 3820,   "spent": None, "fiscal_deficit_gdp": None,
           "source": _SRC_DATAFUL, "data_type": "estimate_only"},
    1971: {"allocated": 4510,   "spent": None, "fiscal_deficit_gdp": None,
           "source": _SRC_DATAFUL, "data_type": "estimate_only"},
    1972: {"allocated": 5200,   "spent": None, "fiscal_deficit_gdp": None,
           "source": _SRC_DATAFUL, "data_type": "estimate_only"},
    1973: {"allocated": 5890,   "spent": None, "fiscal_deficit_gdp": None,
           "source": _SRC_DATAFUL, "data_type": "estimate_only"},
    1974: {"allocated": 7310,   "spent": None, "fiscal_deficit_gdp": None,
           "source": _SRC_DATAFUL, "data_type": "estimate_only"},
    1975: {"allocated": 8780,   "spent": None, "fiscal_deficit_gdp": None,
           "source": _SRC_DATAFUL, "data_type": "estimate_only"},
    1976: {"allocated": 9940,   "spent": None, "fiscal_deficit_gdp": None,
           "source": _SRC_DATAFUL, "data_type": "estimate_only"},
    1977: {"allocated": 11200,  "spent": None, "fiscal_deficit_gdp": None,
           "source": _SRC_DATAFUL, "data_type": "estimate_only"},
    1978: {"allocated": 12800,  "spent": None, "fiscal_deficit_gdp": None,
           "source": _SRC_DATAFUL, "data_type": "estimate_only"},
    1979: {"allocated": 14600,  "spent": None, "fiscal_deficit_gdp": None,
           "source": _SRC_DATAFUL, "data_type": "estimate_only"},
    1980: {"allocated": 17500,  "spent": None, "fiscal_deficit_gdp": None,
           "source": _SRC_DATAFUL, "data_type": "estimate_only"},
    1981: {"allocated": 20800,  "spent": None, "fiscal_deficit_gdp": None,
           "source": _SRC_DATAFUL, "data_type": "estimate_only"},
    1982: {"allocated": 24100,  "spent": None, "fiscal_deficit_gdp": None,
           "source": _SRC_DATAFUL, "data_type": "estimate_only"},
    1983: {"allocated": 28300,  "spent": None, "fiscal_deficit_gdp": None,
           "source": _SRC_DATAFUL, "data_type": "estimate_only"},
    1984: {"allocated": 33200,  "spent": None, "fiscal_deficit_gdp": None,
           "source": _SRC_DATAFUL, "data_type": "estimate_only"},
    1985: {"allocated": 39800,  "spent": None, "fiscal_deficit_gdp": None,
           "source": _SRC_DATAFUL, "data_type": "estimate_only"},
    1986: {"allocated": 46500,  "spent": None, "fiscal_deficit_gdp": None,
           "source": _SRC_DATAFUL, "data_type": "estimate_only"},
    1987: {"allocated": 54200,  "spent": None, "fiscal_deficit_gdp": None,
           "source": _SRC_DATAFUL, "data_type": "estimate_only"},
    1988: {"allocated": 63800,  "spent": None, "fiscal_deficit_gdp": None,
           "source": _SRC_DATAFUL, "data_type": "estimate_only"},
    1989: {"allocated": 75400,  "spent": None, "fiscal_deficit_gdp": None,
           "source": _SRC_DATAFUL, "data_type": "estimate_only"},
    1990: {"allocated": 89800,  "spent": None, "fiscal_deficit_gdp": None,
           "source": _SRC_DATAFUL, "data_type": "estimate_only"},
    1991: {"allocated": 107590, "spent": None, "fiscal_deficit_gdp": None,
           "source": _SRC_DATAFUL, "data_type": "estimate_only"},
    1992: {"allocated": 119954, "spent": None, "fiscal_deficit_gdp": None,
           "source": _SRC_DATAFUL, "data_type": "estimate_only"},
    1993: {"allocated": 142441, "spent": None, "fiscal_deficit_gdp": None,
           "source": _SRC_DATAFUL, "data_type": "estimate_only"},

    # ── 1994 ONWARDS: Verified data from CivicDataLab/OBI ─────
    # Source: Open Budgets India + Ministry of Finance + CAG
    # All values in ₹ Crore — exact figures from official documents

    1994: {"allocated": None,    "spent": 160739, "fiscal_deficit_gdp": None,
           "source": _SRC_OBI, "data_type": "verified",
           "note": "1994-95: Only Actuals available from OBI dataset. BE not in dataset."},

    1995: {"allocated": 172151,  "spent": 178275, "fiscal_deficit_gdp": None,
           "source": _SRC_OBI, "data_type": "verified"},

    1996: {"allocated": 204660,  "spent": 201007, "fiscal_deficit_gdp": None,
           "source": _SRC_OBI, "data_type": "verified"},

    1997: {"allocated": 232176,  "spent": 232068, "fiscal_deficit_gdp": None,
           "source": _SRC_OBI, "data_type": "verified"},

    1998: {"allocated": 267927,  "spent": 279366, "fiscal_deficit_gdp": None,
           "source": _SRC_OBI, "data_type": "verified"},

    1999: {"allocated": 283882,  "spent": 298084, "fiscal_deficit_gdp": 5.4,
           "source": _SRC_OBI, "data_type": "verified"},

    2000: {"allocated": 338487,  "spent": 325611, "fiscal_deficit_gdp": 5.7,
           "source": _SRC_OBI, "data_type": "verified"},

    2001: {"allocated": 375223,  "spent": 362453, "fiscal_deficit_gdp": 6.1,
           "source": _SRC_OBI, "data_type": "verified"},

    2002: {"allocated": 410309,  "spent": 414162, "fiscal_deficit_gdp": 5.9,
           "source": _SRC_OBI, "data_type": "verified"},

    2003: {"allocated": 438795,  "spent": 471368, "fiscal_deficit_gdp": 4.5,
           "source": _SRC_OBI, "data_type": "verified"},

    2004: {"allocated": 477829,  "spent": 497682, "fiscal_deficit_gdp": 4.0,
           "source": _SRC_OBI, "data_type": "verified"},

    2005: {"allocated": 514344,  "spent": 506123, "fiscal_deficit_gdp": 4.1,
           "source": _SRC_OBI, "data_type": "verified"},

    2006: {"allocated": 563991,  "spent": 583387, "fiscal_deficit_gdp": 3.5,
           "source": _SRC_OBI, "data_type": "verified"},

    2007: {"allocated": 680521,  "spent": 712671, "fiscal_deficit_gdp": 2.7,
           "source": _SRC_OBI, "data_type": "verified"},

    2008: {"allocated": 750884,  "spent": 883956, "fiscal_deficit_gdp": 6.0,
           "source": _SRC_OBI, "data_type": "verified"},

    2009: {"allocated": 1020838, "spent": 1024487, "fiscal_deficit_gdp": 6.4,
           "source": _SRC_OBI, "data_type": "verified"},

    2010: {"allocated": 1108749, "spent": 1197328, "fiscal_deficit_gdp": 4.9,
           "source": _SRC_OBI, "data_type": "verified"},

    2011: {"allocated": 1257729, "spent": 1304365, "fiscal_deficit_gdp": 5.7,
           "source": _SRC_OBI, "data_type": "verified"},

    2012: {"allocated": 1490925, "spent": 1410372, "fiscal_deficit_gdp": 4.8,
           "source": _SRC_OBI, "data_type": "verified"},

    2013: {"allocated": 1665297, "spent": 1559447, "fiscal_deficit_gdp": 4.4,
           "source": _SRC_OBI, "data_type": "verified"},

    2014: {"allocated": 1794892, "spent": 1663673, "fiscal_deficit_gdp": 4.1,
           "source": _SRC_OBI, "data_type": "verified"},

    2015: {"allocated": 1777477, "spent": 1790783, "fiscal_deficit_gdp": 3.9,
           "source": _SRC_OBI, "data_type": "verified"},

    2016: {"allocated": 1978060, "spent": 1975194, "fiscal_deficit_gdp": 3.5,
           "source": _SRC_OBI, "data_type": "verified"},

    2017: {"allocated": 2146735, "spent": 2141975, "fiscal_deficit_gdp": 3.5,
           "source": _SRC_OBI, "data_type": "verified"},

    2018: {"allocated": 2442213, "spent": 2315113, "fiscal_deficit_gdp": 3.4,
           "source": _SRC_OBI, "data_type": "verified"},

    2019: {"allocated": 2786349, "spent": 2686330, "fiscal_deficit_gdp": 4.6,
           "source": _SRC_OBI, "data_type": "verified"},

    2020: {"allocated": 3042230, "spent": 3509836, "fiscal_deficit_gdp": 9.2,
           "source": _SRC_OBI, "data_type": "verified"},

    2021: {"allocated": 3483236, "spent": 3793801, "fiscal_deficit_gdp": 6.7,
           "source": _SRC_OBI, "data_type": "verified"},

    2022: {"allocated": 3944909, "spent": 4193157, "fiscal_deficit_gdp": 6.4,
           "source": _SRC_OBI, "data_type": "verified"},

    2023: {"allocated": 4503097, "spent": None,    "fiscal_deficit_gdp": 5.9,
           "source": _SRC_OBI, "data_type": "verified",
           "note": "Actuals for 2023-24 not yet published in CAG audit at time of data compilation."},

    2024: {"allocated": 4820512, "spent": None,    "fiscal_deficit_gdp": 4.9,
           "source": _SRC_MOF, "data_type": "verified",
           "note": "2024-25 Budget Estimate only. Actuals will be available after CAG audit."},
}

# ── Sector budget data (₹ Lakh Crore) ─────────────────────────
# Source: Expenditure Budget Vol I, indiabudget.gov.in
SECTOR_BUDGET = {
    "Narendra Modi (2014–present)": {
        "Defence":           {"2014-15": 2.29, "2019-20": 3.37, "2024-25": 6.21},
        "Infrastructure":    {"2014-15": 1.70, "2019-20": 3.83, "2024-25": 11.11},
        "Education":         {"2014-15": 0.69, "2019-20": 0.94, "2024-25": 1.48},
        "Health":            {"2014-15": 0.35, "2019-20": 0.62, "2024-25": 0.90},
        "Rural Development": {"2014-15": 0.95, "2019-20": 1.14, "2024-25": 1.77},
        "source": "https://www.indiabudget.gov.in",
    },
    "Manmohan Singh (2004–2014)": {
        "Defence":           {"2004-05": 0.77, "2009-10": 1.42, "2013-14": 2.03},
        "Infrastructure":    {"2004-05": 0.45, "2009-10": 1.22, "2013-14": 1.87},
        "Education":         {"2004-05": 0.10, "2009-10": 0.26, "2013-14": 0.65},
        "Health":            {"2004-05": 0.09, "2009-10": 0.20, "2013-14": 0.37},
        "Rural Development": {"2004-05": 0.14, "2009-10": 0.61, "2013-14": 0.80},
        "source": "https://www.indiabudget.gov.in",
    },
    "Atal Bihari Vajpayee (1999–2004)": {
        "Defence":        {"1999-00": 0.46, "2002-03": 0.58, "2003-04": 0.65},
        "Infrastructure": {"1999-00": 0.28, "2002-03": 0.38, "2003-04": 0.44},
        "Education":      {"1999-00": 0.05, "2002-03": 0.07, "2003-04": 0.09},
        "Health":         {"1999-00": 0.04, "2002-03": 0.06, "2003-04": 0.08},
        "source": "https://www.indiabudget.gov.in",
    },
}

DISPLAY_AS_CRORE_BEFORE = 2024  # all values already in ₹ Crore

def get_budget_for_tenure(start_year, end_year):
    """
    Return budget rows for a leader's tenure.
    start_year / end_year = calendar year of tenure start/end.
    FY 2004 = FY 2004-2005 (April 2004 to March 2005).
    """
    return {
        fy: data
        for fy, data in UNION_BUDGET_DATA.items()
        if start_year <= fy <= end_year
    }

def get_tenure_summary(start_year, end_year):
    """
    Return total allocated and total spent for a tenure.
    Only sums verified rows where both values exist.
    Separates verified vs estimate-only data.
    """
    rows = get_budget_for_tenure(start_year, end_year)
    verified_alloc  = sum(v["allocated"] for v in rows.values()
                         if v.get("data_type") == "verified" and v.get("allocated"))
    verified_spent  = sum(v["spent"] for v in rows.values()
                         if v.get("data_type") == "verified" and v.get("spent"))
    estimate_alloc  = sum(v["allocated"] for v in rows.values()
                         if v.get("data_type") == "estimate_only" and v.get("allocated"))
    return {
        "verified_allocated": verified_alloc,
        "verified_spent":     verified_spent,
        "estimate_allocated": estimate_alloc,
        "has_estimates":      estimate_alloc > 0,
        "has_verified":       verified_alloc > 0,
    }
