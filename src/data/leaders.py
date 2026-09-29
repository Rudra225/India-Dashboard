# ============================================================
# DATA: All Indian Prime Ministers & Finance Ministers (1947–2024)
# Sources:
#   PM list:  https://www.pmindia.gov.in/en/former-prime-ministers/
#   FM list:  https://finmin.nic.in
#   Cross-verified via Wikipedia state pages and ECI records
# ============================================================

# Stable verified source URLs only — no deep PDF links
_SRC_PMO    = "https://www.pmindia.gov.in/en/former-prime-ministers/"
_SRC_FINMIN = "https://finmin.nic.in"
_SRC_ECI    = "https://affidavit.eci.gov.in"
_SRC_WB     = "https://data.worldbank.org/country/IN"

PRIME_MINISTERS = {
    "Jawaharlal Nehru (1947–1964)": {
        "name": "Jawaharlal Nehru", "role": "Prime Minister",
        "party": "Indian National Congress", "start_year": 1947, "end_year": 1964,
        "source": _SRC_PMO,
        "summary": "First PM of India. Architect of modern India — established IITs, PSUs, mixed economy, non-alignment. Longest-serving PM (16 yrs 286 days). Presided over 1962 Sino-Indian War.",
    },
    "Gulzarilal Nanda (Acting, 1964)": {
        "name": "Gulzarilal Nanda", "role": "Acting Prime Minister",
        "party": "Indian National Congress", "start_year": 1964, "end_year": 1964,
        "source": _SRC_PMO,
        "summary": "Served as Acting PM for 13 days after Nehru's death in 1964. Also served again briefly in 1966. India's longest-lived PM (99 years).",
    },
    "Lal Bahadur Shastri (1964–1966)": {
        "name": "Lal Bahadur Shastri", "role": "Prime Minister",
        "party": "Indian National Congress", "start_year": 1964, "end_year": 1966,
        "source": _SRC_PMO,
        "summary": "Led India during the 1965 Indo-Pak War. Coined 'Jai Jawan Jai Kisan'. Died in Tashkent in 1966 — only PM to die abroad in office.",
    },
    "Gulzarilal Nanda (Acting, 1966)": {
        "name": "Gulzarilal Nanda", "role": "Acting Prime Minister",
        "party": "Indian National Congress", "start_year": 1966, "end_year": 1966,
        "source": _SRC_PMO,
        "summary": "Second stint as Acting PM for 13 days after Shastri's death in Tashkent.",
    },
    "Indira Gandhi (1966–1977)": {
        "name": "Indira Gandhi", "role": "Prime Minister",
        "party": "Indian National Congress", "start_year": 1966, "end_year": 1977,
        "source": _SRC_PMO,
        "summary": "First and only female PM of India. Green Revolution, bank nationalisation, 1971 Bangladesh liberation war, Emergency (1975–77). Devalued rupee in 1966.",
    },
    "Morarji Desai (1977–1979)": {
        "name": "Morarji Desai", "role": "Prime Minister",
        "party": "Janata Party", "start_year": 1977, "end_year": 1979,
        "source": _SRC_PMO,
        "summary": "First non-Congress PM. Led Janata Party coalition post-Emergency. Restored civil liberties. Resigned after internal coalition conflicts.",
    },
    "Charan Singh (1979–1980)": {
        "name": "Charan Singh", "role": "Prime Minister",
        "party": "Janata Party (Secular)", "start_year": 1979, "end_year": 1980,
        "source": _SRC_PMO,
        "summary": "PM for only 170 days. Never addressed Parliament as PM. Resigned before trust vote. Known as champion of farmers' rights.",
    },
    "Indira Gandhi (1980–1984)": {
        "name": "Indira Gandhi", "role": "Prime Minister",
        "party": "Indian National Congress (I)", "start_year": 1980, "end_year": 1984,
        "source": _SRC_PMO,
        "summary": "Returned to power with massive mandate. Operation Blue Star (1984), Punjab crisis. Assassinated by bodyguards on 31 Oct 1984.",
    },
    "Rajiv Gandhi (1984–1989)": {
        "name": "Rajiv Gandhi", "role": "Prime Minister",
        "party": "Indian National Congress", "start_year": 1984, "end_year": 1989,
        "source": _SRC_PMO,
        "summary": "Youngest PM at 40. Began India's IT/telecom revolution, computerised railways. Bofors scandal cost him the 1989 election. Assassinated in 1991.",
    },
    "V.P. Singh (1989–1990)": {
        "name": "Vishwanath Pratap Singh", "role": "Prime Minister",
        "party": "Janata Dal (National Front)", "start_year": 1989, "end_year": 1990,
        "source": _SRC_PMO,
        "summary": "Implemented Mandal Commission OBC reservations. Fell after losing confidence vote. In office 343 days.",
    },
    "Chandra Shekhar (1990–1991)": {
        "name": "Chandra Shekhar", "role": "Prime Minister",
        "party": "Janata Dal (Socialist) / Samajwadi Janata Party", "start_year": 1990, "end_year": 1991,
        "source": _SRC_PMO,
        "summary": "Caretaker PM for 7 months. His FM Yashwant Sinha mortgaged 67 tonnes of gold to Bank of England to avert BoP crisis.",
    },
    "P.V. Narasimha Rao (1991–1996)": {
        "name": "P.V. Narasimha Rao", "role": "Prime Minister",
        "party": "Indian National Congress", "start_year": 1991, "end_year": 1996,
        "source": _SRC_PMO,
        "summary": "Father of Indian economic liberalisation. With FM Manmohan Singh, launched 1991 LPG reforms — opened India to FDI, dismantled License Raj. Babri Masjid demolition 1992.",
    },
    "H.D. Deve Gowda (1996–1997)": {
        "name": "H.D. Deve Gowda", "role": "Prime Minister",
        "party": "Janata Dal (United Front)", "start_year": 1996, "end_year": 1997,
        "source": _SRC_PMO,
        "summary": "PM for 11 months. Led 13-party coalition. Fell after Congress withdrew support.",
    },
    "I.K. Gujral (1997–1998)": {
        "name": "Inder Kumar Gujral", "role": "Prime Minister",
        "party": "Janata Dal (United Front)", "start_year": 1997, "end_year": 1998,
        "source": _SRC_PMO,
        "summary": "Known for 'Gujral Doctrine' — improved relations with neighbours. PM for 11 months.",
    },
    "Atal Bihari Vajpayee (1996)": {
        "name": "Atal Bihari Vajpayee", "role": "Prime Minister",
        "party": "Bharatiya Janata Party", "start_year": 1996, "end_year": 1996,
        "source": _SRC_PMO,
        "summary": "10th PM. Served a short 13-day term in May 1996 before resigning due to lack of majority.",
    },
    "Atal Bihari Vajpayee (1998–1999)": {
        "name": "Atal Bihari Vajpayee", "role": "Prime Minister",
        "party": "Bharatiya Janata Party (NDA)", "start_year": 1998, "end_year": 1999,
        "source": _SRC_PMO,
        "summary": "Served a 13-month term. Government fell by a single vote in April 1999. Conducted Pokhran-II nuclear tests in 1998.",
    },
    "Atal Bihari Vajpayee (1999–2004)": {
        "name": "Atal Bihari Vajpayee", "role": "Prime Minister",
        "party": "Bharatiya Janata Party (NDA)", "start_year": 1999, "end_year": 2004,
        "source": _SRC_PMO,
        "summary": "First full-term non-Congress PM. Kargil War 1999, Golden Quadrilateral highway project. India's GDP crossed $600Bn under his tenure.",
    },
    "Manmohan Singh (2004–2014)": {
        "name": "Manmohan Singh", "role": "Prime Minister",
        "party": "Indian National Congress (UPA)", "start_year": 2004, "end_year": 2014,
        "source": _SRC_PMO,
        "summary": "13th PM. Oversaw India's highest-growth decade (avg ~7.5% GDP). MGNREGA, RTI, nuclear deal with US. GDP grew from $700Bn to $2Tn.",
    },
    "Narendra Modi (2014–present)": {
        "name": "Narendra Modi", "role": "Prime Minister",
        "party": "Bharatiya Janata Party (NDA)", "start_year": 2014, "end_year": 2024,
        "source": "https://www.pmindia.gov.in/en/",
        "summary": "14th/15th PM. GST rollout, demonetisation, PLI schemes, PM-Kisan, Ayushman Bharat. India became 5th largest economy. Third term from June 2024.",
    },
}

FINANCE_MINISTERS = {
    "R.K. Shanmukham Chetty (1947–1948)": {
        "name": "R.K. Shanmukham Chetty", "role": "Finance Minister",
        "party": "Independent / Congress-backed", "start_year": 1947, "end_year": 1948,
        "source": _SRC_FINMIN,
        "summary": "First FM of independent India. Presented India's first-ever Union Budget on 26 Nov 1947. Focused on post-partition economic stabilisation.",
    },
    "John Mathai (1948–1950)": {
        "name": "John Mathai", "role": "Finance Minister",
        "party": "Indian National Congress", "start_year": 1948, "end_year": 1950,
        "source": _SRC_FINMIN,
        "summary": "Presented first Budget of the Republic of India (1950–51). Resigned over Planning Commission's powers.",
    },
    "C.D. Deshmukh (1950–1956)": {
        "name": "C.D. Deshmukh", "role": "Finance Minister",
        "party": "Indian National Congress", "start_year": 1950, "end_year": 1956,
        "source": _SRC_FINMIN,
        "summary": "Only person to serve as both RBI Governor and FM. Oversaw India's First Five-Year Plan. Resigned over States Reorganisation.",
    },
    "T.T. Krishnamachari (1956–1958)": {
        "name": "T.T. Krishnamachari", "role": "Finance Minister",
        "party": "Indian National Congress", "start_year": 1956, "end_year": 1958,
        "source": _SRC_FINMIN,
        "summary": "Introduced wealth tax and estate duty. Resigned over the Mundhra scandal — India's first financial scam involving LIC.",
    },
    "Jawaharlal Nehru (FM Charge, 1958)": {
        "name": "Jawaharlal Nehru", "role": "Finance Minister (Additional Charge)",
        "party": "Indian National Congress", "start_year": 1958, "end_year": 1958,
        "source": _SRC_FINMIN,
        "summary": "Held FM portfolio briefly as PM during interregnum after TTK's resignation.",
    },
    "Morarji Desai (1958–1963)": {
        "name": "Morarji Desai", "role": "Finance Minister (1st Stint)",
        "party": "Indian National Congress", "start_year": 1958, "end_year": 1963,
        "source": _SRC_FINMIN,
        "summary": "Presented 8 budgets in first stint. All-time record holder for most Union Budgets (10 total). Gold Control Act to curb gold consumption.",
    },
    "T.T. Krishnamachari (1964–1966)": {
        "name": "T.T. Krishnamachari", "role": "Finance Minister (2nd Stint)",
        "party": "Indian National Congress", "start_year": 1964, "end_year": 1966,
        "source": _SRC_FINMIN,
        "summary": "Returned as FM under Shastri and early Indira Gandhi. Presided over 1966 rupee devaluation discussions.",
    },
    "Sachin Chaudhuri (1966–1967)": {
        "name": "Sachin Chaudhuri", "role": "Finance Minister",
        "party": "Indian National Congress", "start_year": 1966, "end_year": 1967,
        "source": _SRC_FINMIN,
        "summary": "Oversaw the dramatic June 1966 rupee devaluation from ₹4.76 to ₹7.50 per USD — a 57% devaluation to boost exports.",
    },
    "Morarji Desai (1967–1969)": {
        "name": "Morarji Desai", "role": "Finance Minister (2nd Stint)",
        "party": "Indian National Congress", "start_year": 1967, "end_year": 1969,
        "source": _SRC_FINMIN,
        "summary": "Second stint, presented 2 more budgets raising total to 10 — still the all-time record. Also served as Deputy PM.",
    },
    "Indira Gandhi (FM Charge, 1969–1970)": {
        "name": "Indira Gandhi", "role": "Finance Minister (Additional Charge)",
        "party": "Indian National Congress (I)", "start_year": 1969, "end_year": 1970,
        "source": _SRC_FINMIN,
        "summary": "First woman to hold FM portfolio. Nationalised 14 major banks in 1969. Abolished privy purses of former royals.",
    },
    "Y.B. Chavan (1971–1975)": {
        "name": "Y.B. Chavan", "role": "Finance Minister",
        "party": "Indian National Congress", "start_year": 1971, "end_year": 1975,
        "source": _SRC_FINMIN,
        "summary": "Managed war finances during 1971 Bangladesh liberation war. Dealt with 1973 oil shock's impact on India.",
    },
    "C. Subramaniam (1975–1977)": {
        "name": "C. Subramaniam", "role": "Finance Minister",
        "party": "Indian National Congress", "start_year": 1975, "end_year": 1977,
        "source": _SRC_FINMIN,
        "summary": "FM during Emergency era. Credited with earlier Green Revolution in agriculture.",
    },
    "H.M. Patel (1977–1978)": {
        "name": "H.M. Patel", "role": "Finance Minister",
        "party": "Janata Party", "start_year": 1977, "end_year": 1978,
        "source": _SRC_FINMIN,
        "summary": "FM in Morarji Desai's Janata government. Rolled back Emergency-era economic measures.",
    },
    "Charan Singh (1978–1979)": {
        "name": "Charan Singh", "role": "Finance Minister",
        "party": "Janata Party", "start_year": 1978, "end_year": 1979,
        "source": _SRC_FINMIN,
        "summary": "Served as both Deputy PM and FM briefly. Farm-focused budgets reflecting agrarian politics.",
    },
    "R. Venkataraman (1980–1982)": {
        "name": "R. Venkataraman", "role": "Finance Minister",
        "party": "Indian National Congress (I)", "start_year": 1980, "end_year": 1982,
        "source": _SRC_FINMIN,
        "summary": "FM in Indira Gandhi's comeback government. Later became President of India. Managed post-Emergency recovery, IMF loan 1981.",
    },
    "Pranab Mukherjee (1982–1984)": {
        "name": "Pranab Mukherjee", "role": "Finance Minister (1st Stint)",
        "party": "Indian National Congress (I)", "start_year": 1982, "end_year": 1984,
        "source": _SRC_FINMIN,
        "summary": "First FM stint. Managed fiscal stress, oil price shocks. Later became President of India.",
    },
    "V.P. Singh (1984–1986)": {
        "name": "V.P. Singh", "role": "Finance Minister",
        "party": "Indian National Congress", "start_year": 1984, "end_year": 1986,
        "source": _SRC_FINMIN,
        "summary": "Rajiv Gandhi's FM. Crackdown on tax evasion. Resigned and later became PM (1989–90).",
    },
    "N.D. Tiwari (1987–1988)": {
        "name": "N.D. Tiwari", "role": "Finance Minister",
        "party": "Indian National Congress", "start_year": 1987, "end_year": 1988,
        "source": _SRC_FINMIN,
        "summary": "Managed Rajiv era budgets facing Bofors-era political turbulence.",
    },
    "S.B. Chavan (1988–1989)": {
        "name": "S.B. Chavan", "role": "Finance Minister",
        "party": "Indian National Congress", "start_year": 1988, "end_year": 1989,
        "source": _SRC_FINMIN,
        "summary": "FM in Rajiv Gandhi's final year. Presented budget amid political crisis.",
    },
    "Madhu Dandavate (1989–1990)": {
        "name": "Madhu Dandavate", "role": "Finance Minister",
        "party": "Janata Dal", "start_year": 1989, "end_year": 1990,
        "source": _SRC_FINMIN,
        "summary": "FM in V.P. Singh's National Front government. Presented one budget amid political instability.",
    },
    "Yashwant Sinha (1990–1991)": {
        "name": "Yashwant Sinha", "role": "Finance Minister (1st Stint)",
        "party": "Samajwadi Janata Party", "start_year": 1990, "end_year": 1991,
        "source": _SRC_FINMIN,
        "summary": "Mortgaged India's gold to avert BoP crisis. Shipped 67 tonnes of gold to Bank of England as collateral.",
    },
    "Manmohan Singh (1991–1996)": {
        "name": "Manmohan Singh", "role": "Finance Minister",
        "party": "Indian National Congress", "start_year": 1991, "end_year": 1996,
        "source": _SRC_FINMIN,
        "summary": "Architect of 1991 LPG reforms. Dismantled License Raj, opened FDI, devalued rupee. Most transformative budget in India's history.",
    },
    "P. Chidambaram (1996–1998)": {
        "name": "P. Chidambaram", "role": "Finance Minister (1st Stint)",
        "party": "Tamil Maanila Congress", "start_year": 1996, "end_year": 1998,
        "source": _SRC_FINMIN,
        "summary": "Presented 'Dream Budget' of 1997 — slashed income tax rates dramatically, boosted compliance.",
    },
    "Yashwant Sinha (1998–2002)": {
        "name": "Yashwant Sinha", "role": "Finance Minister (2nd Stint)",
        "party": "Bharatiya Janata Party", "start_year": 1998, "end_year": 2002,
        "source": _SRC_FINMIN,
        "summary": "FM in Vajpayee's NDA. Managed post-Pokhran sanctions, passed FRBM Act framework. India's forex reserves crossed $100Bn.",
    },
    "Jaswant Singh (2002–2004)": {
        "name": "Jaswant Singh", "role": "Finance Minister",
        "party": "Bharatiya Janata Party", "start_year": 2002, "end_year": 2004,
        "source": _SRC_FINMIN,
        "summary": "FRBM Act passed 2003. Managed fiscal consolidation. India achieved 8%+ growth late in tenure.",
    },
    "P. Chidambaram (2004–2008)": {
        "name": "P. Chidambaram", "role": "Finance Minister (2nd Stint)",
        "party": "Indian National Congress", "start_year": 2004, "end_year": 2008,
        "source": _SRC_FINMIN,
        "summary": "India's golden growth years — 9%+ GDP. FRBM compliance, financial inclusion, NREGA implementation.",
    },
    "Pranab Mukherjee (2009–2012)": {
        "name": "Pranab Mukherjee", "role": "Finance Minister (2nd Stint)",
        "party": "Indian National Congress", "start_year": 2009, "end_year": 2012,
        "source": _SRC_FINMIN,
        "summary": "UPA-II FM. Managed post-GFC stimulus, rising fiscal deficit. Proposed GAAR. Became President of India in 2012.",
    },
    "P. Chidambaram (2012–2014)": {
        "name": "P. Chidambaram", "role": "Finance Minister (3rd Stint)",
        "party": "Indian National Congress", "start_year": 2012, "end_year": 2014,
        "source": _SRC_FINMIN,
        "summary": "Third stint. Fiscal consolidation after deficit surge. Rupee hit record lows in 2013.",
    },
    "Arun Jaitley (2014–2019)": {
        "name": "Arun Jaitley", "role": "Finance Minister",
        "party": "Bharatiya Janata Party", "start_year": 2014, "end_year": 2019,
        "source": _SRC_FINMIN,
        "summary": "Shepherded GST through Parliament (2017). IBC/Insolvency Code, DBT reforms. Presented 5 budgets. Passed away Aug 2019.",
    },
    "Nirmala Sitharaman (2019–present)": {
        "name": "Nirmala Sitharaman", "role": "Finance Minister",
        "party": "Bharatiya Janata Party", "start_year": 2019, "end_year": 2024,
        "source": _SRC_FINMIN,
        "summary": "First full-time woman FM. Record 7 consecutive budgets. COVID economic response, PLI schemes, capex-led recovery.",
    },
}

ALL_LEADERS = {**PRIME_MINISTERS, **FINANCE_MINISTERS}
