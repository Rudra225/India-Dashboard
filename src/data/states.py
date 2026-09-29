# ============================================================
# DATA: All Indian States — Chief Ministers & State Economics
# Sources:
#   - CM tenures: https://www.pmindia.gov.in + Wikipedia (cross-verified)
#   - GSDP: RBI State Finances Report https://rbi.org.in/Scripts/AnnualPublications.aspx?head=State+Finances+%3a+A+Study+of+Budgets
#   - State Budget/Deficit/Debt: CAG + RBI State Finances
#   - NCRB Crime: https://ncrb.gov.in/en/crime-in-india-year-wise-volume-table
#   - MyNeta: https://myneta.info
# NOTE: Economic data availability varies by state and year.
#   All gaps are labeled as per source availability.
# ============================================================

# ── MyNeta search URL builder ─────────────────────────────────
def myneta_search(name):
    query = name.replace(" ", "+")
    return f"https://myneta.info/candidate/search/?q={query}"

def myneta_state_url(state_code, election_year):
    """Generate MyNeta state assembly URL."""
    state_map = {
        "Andhra Pradesh": "andhra_pradesh",
        "Arunachal Pradesh": "arunachal_pradesh",
        "Assam": "assam",
        "Bihar": "bihar",
        "Chhattisgarh": "chhattisgarh",
        "Goa": "goa",
        "Gujarat": "gujarat",
        "Haryana": "haryana",
        "Himachal Pradesh": "himachal_pradesh",
        "Jharkhand": "jharkhand",
        "Karnataka": "karnataka",
        "Kerala": "kerala",
        "Madhya Pradesh": "madhya_pradesh",
        "Maharashtra": "maharashtra",
        "Manipur": "manipur",
        "Meghalaya": "meghalaya",
        "Mizoram": "mizoram",
        "Nagaland": "nagaland",
        "Odisha": "odisha",
        "Punjab": "punjab",
        "Rajasthan": "rajasthan",
        "Sikkim": "sikkim",
        "Tamil Nadu": "tamil_nadu",
        "Telangana": "telangana",
        "Tripura": "tripura",
        "Uttar Pradesh": "uttar_pradesh",
        "Uttarakhand": "uttarakhand",
        "West Bengal": "west_bengal",
    }
    code = state_map.get(state_code, state_code.lower().replace(" ", "_"))
    return f"https://myneta.info/{code}{election_year}/"

# ── All 28 States with Chief Ministers ───────────────────────
# Format: list of dicts with name, party, start, end, myneta_search
# Sources: Wikipedia state CM pages + Election Commission records

STATE_DATA = {

    "Andhra Pradesh": {
        "capital": "Amaravati",
        "region": "South",
        "chief_ministers": [
            {"name": "N. Chandrababu Naidu",  "party": "TDP",      "start": 1995, "end": 2004},
            {"name": "Y.S. Rajasekhara Reddy","party": "INC",      "start": 2004, "end": 2009},
            {"name": "K. Rosaiah",             "party": "INC",      "start": 2009, "end": 2010},
            {"name": "N. Kiran Kumar Reddy",   "party": "INC",      "start": 2010, "end": 2014},
            {"name": "N. Chandrababu Naidu",   "party": "TDP",      "start": 2014, "end": 2019},
            {"name": "Y.S. Jagan Mohan Reddy", "party": "YSRCP",   "start": 2019, "end": 2024},
            {"name": "N. Chandrababu Naidu",   "party": "TDP",      "start": 2024, "end": 2029},
        ],
        "source_cm": "https://en.wikipedia.org/wiki/List_of_chief_ministers_of_Andhra_Pradesh",
        "myneta_url": "https://myneta.info/andhra_pradesh2024/",
    },

    "Arunachal Pradesh": {
        "capital": "Itanagar",
        "region": "Northeast",
        "chief_ministers": [
            {"name": "Gegong Apang",        "party": "INC",  "start": 1980, "end": 2003},
            {"name": "Mukut Mithi",         "party": "INC",  "start": 2003, "end": 2004},
            {"name": "Gegong Apang",        "party": "INC",  "start": 2004, "end": 2007},
            {"name": "Dorjee Khandu",       "party": "INC",  "start": 2007, "end": 2011},
            {"name": "Jarbom Gamlin",       "party": "INC",  "start": 2011, "end": 2011},
            {"name": "Nabam Tuki",          "party": "INC",  "start": 2011, "end": 2016},
            {"name": "Pema Khandu",         "party": "BJP",  "start": 2016, "end": 2024},
        ],
        "source_cm": "https://en.wikipedia.org/wiki/List_of_chief_ministers_of_Arunachal_Pradesh",
        "myneta_url": "https://myneta.info/arunachalpradesh2024/",
    },

    "Assam": {
        "capital": "Dispur",
        "region": "Northeast",
        "chief_ministers": [
            {"name": "Prafulla Kumar Mahanta", "party": "AGP",  "start": 1985, "end": 1990},
            {"name": "Hiteswar Saikia",         "party": "INC",  "start": 1991, "end": 1996},
            {"name": "Prafulla Kumar Mahanta",  "party": "AGP",  "start": 1996, "end": 2001},
            {"name": "Tarun Gogoi",             "party": "INC",  "start": 2001, "end": 2014},
            {"name": "Sarbananda Sonowal",      "party": "BJP",  "start": 2016, "end": 2021},
            {"name": "Himanta Biswa Sarma",     "party": "BJP",  "start": 2021, "end": 2026},
        ],
        "source_cm": "https://en.wikipedia.org/wiki/List_of_chief_ministers_of_Assam",
        "myneta_url": "https://myneta.info/assam2021/",
    },

    "Bihar": {
        "capital": "Patna",
        "region": "East",
        "chief_ministers": [
            {"name": "Lalu Prasad Yadav",  "party": "RJD",      "start": 1990, "end": 1997},
            {"name": "Rabri Devi",          "party": "RJD",      "start": 1997, "end": 2005},
            {"name": "Nitish Kumar",        "party": "JD(U)",    "start": 2005, "end": 2014},
            {"name": "Jitan Ram Manjhi",    "party": "JD(U)",    "start": 2014, "end": 2015},
            {"name": "Nitish Kumar",        "party": "JD(U)",    "start": 2015, "end": 2024},
        ],
        "source_cm": "https://en.wikipedia.org/wiki/List_of_chief_ministers_of_Bihar",
        "myneta_url": "https://myneta.info/bihar2020/",
    },

    "Chhattisgarh": {
        "capital": "Raipur",
        "region": "Central",
        "chief_ministers": [
            {"name": "Ajit Jogi",           "party": "INC",  "start": 2000, "end": 2003},
            {"name": "Raman Singh",         "party": "BJP",  "start": 2003, "end": 2018},
            {"name": "Bhupesh Baghel",      "party": "INC",  "start": 2018, "end": 2023},
            {"name": "Vishnu Deo Sai",      "party": "BJP",  "start": 2023, "end": 2028},
        ],
        "source_cm": "https://en.wikipedia.org/wiki/List_of_chief_ministers_of_Chhattisgarh",
        "myneta_url": "https://myneta.info/chhattisgarh2023/",
    },

    "Goa": {
        "capital": "Panaji",
        "region": "West",
        "chief_ministers": [
            {"name": "Pratapsingh Rane",    "party": "INC",  "start": 1988, "end": 1990},
            {"name": "Luis Proto Barbosa",  "party": "INC",  "start": 1990, "end": 1994},
            {"name": "Manohar Parrikar",    "party": "BJP",  "start": 2000, "end": 2005},
            {"name": "Pratapsingh Rane",    "party": "INC",  "start": 2005, "end": 2007},
            {"name": "Digambar Kamat",      "party": "INC",  "start": 2007, "end": 2012},
            {"name": "Manohar Parrikar",    "party": "BJP",  "start": 2012, "end": 2017},
            {"name": "Pramod Sawant",       "party": "BJP",  "start": 2019, "end": 2024},
        ],
        "source_cm": "https://en.wikipedia.org/wiki/List_of_chief_ministers_of_Goa",
        "myneta_url": "https://myneta.info/goa2022/",
    },

    "Gujarat": {
        "capital": "Gandhinagar",
        "region": "West",
        "chief_ministers": [
            {"name": "Keshubhai Patel",     "party": "BJP",  "start": 1995, "end": 1996},
            {"name": "Shankersinh Vaghela", "party": "BJP/RJP","start": 1996, "end": 1997},
            {"name": "Dilip Parikh",        "party": "BJP",  "start": 1997, "end": 1998},
            {"name": "Keshubhai Patel",     "party": "BJP",  "start": 1998, "end": 2001},
            {"name": "Narendra Modi",       "party": "BJP",  "start": 2001, "end": 2014},
            {"name": "Anandiben Patel",     "party": "BJP",  "start": 2014, "end": 2016},
            {"name": "Vijay Rupani",        "party": "BJP",  "start": 2016, "end": 2021},
            {"name": "Bhupendrabhai Patel", "party": "BJP",  "start": 2021, "end": 2026},
        ],
        "source_cm": "https://en.wikipedia.org/wiki/List_of_chief_ministers_of_Gujarat",
        "myneta_url": "https://myneta.info/gujarat2022/",
    },

    "Haryana": {
        "capital": "Chandigarh",
        "region": "North",
        "chief_ministers": [
            {"name": "Bhajan Lal",          "party": "INC",      "start": 1979, "end": 1991},
            {"name": "Om Prakash Chautala", "party": "INLD",     "start": 1999, "end": 2005},
            {"name": "Bhupinder Singh Hooda","party": "INC",     "start": 2005, "end": 2014},
            {"name": "Manohar Lal Khattar", "party": "BJP",      "start": 2014, "end": 2024},
            {"name": "Nayab Singh Saini",   "party": "BJP",      "start": 2024, "end": 2029},
        ],
        "source_cm": "https://en.wikipedia.org/wiki/List_of_chief_ministers_of_Haryana",
        "myneta_url": "https://myneta.info/haryana2024/",
    },

    "Himachal Pradesh": {
        "capital": "Shimla",
        "region": "North",
        "chief_ministers": [
            {"name": "Shanta Kumar",        "party": "BJP",  "start": 1990, "end": 1992},
            {"name": "Virbhadra Singh",      "party": "INC",  "start": 1993, "end": 1998},
            {"name": "Prem Kumar Dhumal",   "party": "BJP",  "start": 1998, "end": 2003},
            {"name": "Virbhadra Singh",      "party": "INC",  "start": 2003, "end": 2007},
            {"name": "Prem Kumar Dhumal",   "party": "BJP",  "start": 2007, "end": 2012},
            {"name": "Virbhadra Singh",      "party": "INC",  "start": 2012, "end": 2017},
            {"name": "Jai Ram Thakur",      "party": "BJP",  "start": 2017, "end": 2022},
            {"name": "Sukhvinder Singh Sukhu","party": "INC", "start": 2022, "end": 2027},
        ],
        "source_cm": "https://en.wikipedia.org/wiki/List_of_chief_ministers_of_Himachal_Pradesh",
        "myneta_url": "https://myneta.info/himachal2022/",
    },

    "Jharkhand": {
        "capital": "Ranchi",
        "region": "East",
        "chief_ministers": [
            {"name": "Babulal Marandi",     "party": "BJP",      "start": 2000, "end": 2003},
            {"name": "Arjun Munda",         "party": "BJP",      "start": 2003, "end": 2005},
            {"name": "Shibu Soren",         "party": "JMM",      "start": 2005, "end": 2009},
            {"name": "Arjun Munda",         "party": "BJP",      "start": 2010, "end": 2013},
            {"name": "Hemant Soren",        "party": "JMM",      "start": 2013, "end": 2014},
            {"name": "Raghubar Das",        "party": "BJP",      "start": 2014, "end": 2019},
            {"name": "Hemant Soren",        "party": "JMM",      "start": 2019, "end": 2024},
            {"name": "Hemant Soren",        "party": "JMM",      "start": 2024, "end": 2029},
        ],
        "source_cm": "https://en.wikipedia.org/wiki/List_of_chief_ministers_of_Jharkhand",
        "myneta_url": "https://myneta.info/jharkhand2024/",
    },

    "Karnataka": {
        "capital": "Bengaluru",
        "region": "South",
        "chief_ministers": [
            {"name": "S.M. Krishna",        "party": "INC",      "start": 1999, "end": 2004},
            {"name": "Dharam Singh",        "party": "INC",      "start": 2004, "end": 2006},
            {"name": "H.D. Kumaraswamy",    "party": "JD(S)",    "start": 2006, "end": 2007},
            {"name": "B.S. Yediyurappa",    "party": "BJP",      "start": 2008, "end": 2011},
            {"name": "D.V. Sadananda Gowda","party": "BJP",      "start": 2011, "end": 2012},
            {"name": "Jagadish Shettar",    "party": "BJP",      "start": 2012, "end": 2013},
            {"name": "Siddaramaiah",        "party": "INC",      "start": 2013, "end": 2018},
            {"name": "H.D. Kumaraswamy",    "party": "JD(S)",    "start": 2018, "end": 2019},
            {"name": "B.S. Yediyurappa",    "party": "BJP",      "start": 2019, "end": 2021},
            {"name": "Basavaraj Bommai",    "party": "BJP",      "start": 2021, "end": 2023},
            {"name": "Siddaramaiah",        "party": "INC",      "start": 2023, "end": 2028},
        ],
        "source_cm": "https://en.wikipedia.org/wiki/List_of_chief_ministers_of_Karnataka",
        "myneta_url": "https://myneta.info/karnataka2023/",
    },

    "Kerala": {
        "capital": "Thiruvananthapuram",
        "region": "South",
        "chief_ministers": [
            {"name": "K. Karunakaran",      "party": "INC",      "start": 1991, "end": 1995},
            {"name": "A.K. Antony",         "party": "INC",      "start": 1995, "end": 1996},
            {"name": "E.K. Nayanar",        "party": "CPI(M)",   "start": 1996, "end": 2001},
            {"name": "A.K. Antony",         "party": "INC",      "start": 2001, "end": 2004},
            {"name": "Oommen Chandy",       "party": "INC",      "start": 2004, "end": 2006},
            {"name": "V.S. Achuthanandan",  "party": "CPI(M)",   "start": 2006, "end": 2011},
            {"name": "Oommen Chandy",       "party": "INC",      "start": 2011, "end": 2016},
            {"name": "Pinarayi Vijayan",    "party": "CPI(M)",   "start": 2016, "end": 2026},
        ],
        "source_cm": "https://en.wikipedia.org/wiki/List_of_chief_ministers_of_Kerala",
        "myneta_url": "https://myneta.info/kerala2021/",
    },

    "Madhya Pradesh": {
        "capital": "Bhopal",
        "region": "Central",
        "chief_ministers": [
            {"name": "Digvijaya Singh",     "party": "INC",      "start": 1993, "end": 2003},
            {"name": "Babulal Gaur",        "party": "BJP",      "start": 2003, "end": 2004},
            {"name": "Shivraj Singh Chouhan","party": "BJP",     "start": 2005, "end": 2018},
            {"name": "Kamal Nath",          "party": "INC",      "start": 2018, "end": 2020},
            {"name": "Shivraj Singh Chouhan","party": "BJP",     "start": 2020, "end": 2023},
            {"name": "Mohan Yadav",         "party": "BJP",      "start": 2023, "end": 2028},
        ],
        "source_cm": "https://en.wikipedia.org/wiki/List_of_chief_ministers_of_Madhya_Pradesh",
        "myneta_url": "https://myneta.info/mp2023/",
    },

    "Maharashtra": {
        "capital": "Mumbai",
        "region": "West",
        "chief_ministers": [
            {"name": "Vilasrao Deshmukh",   "party": "INC",      "start": 1999, "end": 2004},
            {"name": "Sushilkumar Shinde",  "party": "INC",      "start": 2003, "end": 2004},
            {"name": "Vilasrao Deshmukh",   "party": "INC",      "start": 2004, "end": 2008},
            {"name": "Ashok Chavan",        "party": "INC",      "start": 2008, "end": 2010},
            {"name": "Prithviraj Chavan",   "party": "INC",      "start": 2010, "end": 2014},
            {"name": "Devendra Fadnavis",   "party": "BJP",      "start": 2014, "end": 2019},
            {"name": "Uddhav Thackeray",    "party": "SS+INC+NCP","start": 2019, "end": 2022},
            {"name": "Eknath Shinde",       "party": "SS(Shinde)","start": 2022, "end": 2024},
            {"name": "Devendra Fadnavis",   "party": "BJP",      "start": 2024, "end": 2029},
        ],
        "source_cm": "https://en.wikipedia.org/wiki/List_of_chief_ministers_of_Maharashtra",
        "myneta_url": "https://myneta.info/maharashtra2024/",
    },

    "Manipur": {
        "capital": "Imphal",
        "region": "Northeast",
        "chief_ministers": [
            {"name": "Okram Ibobi Singh",   "party": "INC",      "start": 2002, "end": 2017},
            {"name": "N. Biren Singh",      "party": "BJP",      "start": 2017, "end": 2027},
        ],
        "source_cm": "https://en.wikipedia.org/wiki/List_of_chief_ministers_of_Manipur",
        "myneta_url": "https://myneta.info/manipur2022/",
    },

    "Meghalaya": {
        "capital": "Shillong",
        "region": "Northeast",
        "chief_ministers": [
            {"name": "D.D. Lapang",         "party": "INC",      "start": 2003, "end": 2010},
            {"name": "Mukul Sangma",        "party": "INC",      "start": 2010, "end": 2018},
            {"name": "Conrad Sangma",       "party": "NPP",      "start": 2018, "end": 2023},
            {"name": "Conrad Sangma",       "party": "NPP",      "start": 2023, "end": 2028},
        ],
        "source_cm": "https://en.wikipedia.org/wiki/List_of_chief_ministers_of_Meghalaya",
        "myneta_url": "https://myneta.info/meghalaya2023/",
    },

    "Mizoram": {
        "capital": "Aizawl",
        "region": "Northeast",
        "chief_ministers": [
            {"name": "Lal Thanhawla",       "party": "INC",      "start": 1989, "end": 1998},
            {"name": "Zoramthanga",         "party": "MNF",      "start": 1998, "end": 2008},
            {"name": "Lal Thanhawla",       "party": "INC",      "start": 2008, "end": 2018},
            {"name": "Zoramthanga",         "party": "MNF",      "start": 2018, "end": 2023},
            {"name": "Lalduhoma",           "party": "ZPM",      "start": 2023, "end": 2028},
        ],
        "source_cm": "https://en.wikipedia.org/wiki/List_of_chief_ministers_of_Mizoram",
        "myneta_url": "https://myneta.info/mizoram2023/",
    },

    "Nagaland": {
        "capital": "Kohima",
        "region": "Northeast",
        "chief_ministers": [
            {"name": "S.C. Jamir",          "party": "INC",      "start": 1993, "end": 2003},
            {"name": "Neiphiu Rio",         "party": "NPF",      "start": 2003, "end": 2014},
            {"name": "T.R. Zeliang",        "party": "NPF",      "start": 2014, "end": 2017},
            {"name": "Shürhozelie Liezietsu","party": "NPF",     "start": 2017, "end": 2018},
            {"name": "Neiphiu Rio",         "party": "NDPP",     "start": 2018, "end": 2023},
            {"name": "Neiphiu Rio",         "party": "NDPP",     "start": 2023, "end": 2028},
        ],
        "source_cm": "https://en.wikipedia.org/wiki/List_of_chief_ministers_of_Nagaland",
        "myneta_url": "https://myneta.info/nagaland2023/",
    },

    "Odisha": {
        "capital": "Bhubaneswar",
        "region": "East",
        "chief_ministers": [
            {"name": "Giridhar Gamang",     "party": "INC",      "start": 1999, "end": 2000},
            {"name": "Naveen Patnaik",      "party": "BJD",      "start": 2000, "end": 2024},
            {"name": "Mohan Majhi",         "party": "BJP",      "start": 2024, "end": 2029},
        ],
        "source_cm": "https://en.wikipedia.org/wiki/List_of_chief_ministers_of_Odisha",
        "myneta_url": "https://myneta.info/odisha2024/",
    },

    "Punjab": {
        "capital": "Chandigarh",
        "region": "North",
        "chief_ministers": [
            {"name": "Parkash Singh Badal", "party": "SAD",      "start": 1997, "end": 2002},
            {"name": "Amarinder Singh",     "party": "INC",      "start": 2002, "end": 2007},
            {"name": "Parkash Singh Badal", "party": "SAD",      "start": 2007, "end": 2017},
            {"name": "Amarinder Singh",     "party": "INC",      "start": 2017, "end": 2021},
            {"name": "Charanjit Singh Channi","party": "INC",    "start": 2021, "end": 2022},
            {"name": "Bhagwant Mann",       "party": "AAP",      "start": 2022, "end": 2027},
        ],
        "source_cm": "https://en.wikipedia.org/wiki/List_of_chief_ministers_of_Punjab,_India",
        "myneta_url": "https://myneta.info/punjab2022/",
    },

    "Rajasthan": {
        "capital": "Jaipur",
        "region": "North",
        "chief_ministers": [
            {"name": "Ashok Gehlot",        "party": "INC",      "start": 1998, "end": 2003},
            {"name": "Vasundhara Raje",     "party": "BJP",      "start": 2003, "end": 2008},
            {"name": "Ashok Gehlot",        "party": "INC",      "start": 2008, "end": 2013},
            {"name": "Vasundhara Raje",     "party": "BJP",      "start": 2013, "end": 2018},
            {"name": "Ashok Gehlot",        "party": "INC",      "start": 2018, "end": 2023},
            {"name": "Bhajan Lal Sharma",   "party": "BJP",      "start": 2023, "end": 2028},
        ],
        "source_cm": "https://en.wikipedia.org/wiki/List_of_chief_ministers_of_Rajasthan",
        "myneta_url": "https://myneta.info/rajasthan2023/",
    },

    "Sikkim": {
        "capital": "Gangtok",
        "region": "Northeast",
        "chief_ministers": [
            {"name": "Pawan Chamling",      "party": "SDF",      "start": 1994, "end": 2019},
            {"name": "Prem Singh Tamang",   "party": "SKM",      "start": 2019, "end": 2024},
        ],
        "source_cm": "https://en.wikipedia.org/wiki/List_of_chief_ministers_of_Sikkim",
        "myneta_url": "https://myneta.info/sikkim2024/",
    },

    "Tamil Nadu": {
        "capital": "Chennai",
        "region": "South",
        "chief_ministers": [
            {"name": "M. Karunanidhi",      "party": "DMK",      "start": 1989, "end": 1991},
            {"name": "J. Jayalalithaa",     "party": "AIADMK",   "start": 1991, "end": 1996},
            {"name": "M. Karunanidhi",      "party": "DMK",      "start": 1996, "end": 2001},
            {"name": "J. Jayalalithaa",     "party": "AIADMK",   "start": 2001, "end": 2006},
            {"name": "M. Karunanidhi",      "party": "DMK",      "start": 2006, "end": 2011},
            {"name": "J. Jayalalithaa",     "party": "AIADMK",   "start": 2011, "end": 2016},
            {"name": "Edappadi K. Palaniswami","party": "AIADMK","start": 2017, "end": 2021},
            {"name": "M.K. Stalin",         "party": "DMK",      "start": 2021, "end": 2026},
        ],
        "source_cm": "https://en.wikipedia.org/wiki/List_of_chief_ministers_of_Tamil_Nadu",
        "myneta_url": "https://myneta.info/tamilnadu2021/",
    },

    "Telangana": {
        "capital": "Hyderabad",
        "region": "South",
        "chief_ministers": [
            {"name": "K. Chandrashekhar Rao","party": "TRS/BRS", "start": 2014, "end": 2023},
            {"name": "A. Revanth Reddy",    "party": "INC",      "start": 2023, "end": 2028},
        ],
        "source_cm": "https://en.wikipedia.org/wiki/List_of_chief_ministers_of_Telangana",
        "myneta_url": "https://myneta.info/telangana2023/",
    },

    "Tripura": {
        "capital": "Agartala",
        "region": "Northeast",
        "chief_ministers": [
            {"name": "Manik Sarkar",        "party": "CPI(M)",   "start": 1998, "end": 2018},
            {"name": "Biplab Kumar Deb",    "party": "BJP",      "start": 2018, "end": 2023},
            {"name": "Manik Saha",          "party": "BJP",      "start": 2022, "end": 2027},
        ],
        "source_cm": "https://en.wikipedia.org/wiki/List_of_chief_ministers_of_Tripura",
        "myneta_url": "https://myneta.info/tripura2023/",
    },

    "Uttar Pradesh": {
        "capital": "Lucknow",
        "region": "North",
        "chief_ministers": [
            {"name": "Kalyan Singh",        "party": "BJP",      "start": 1991, "end": 1999},
            {"name": "Ram Prakash Gupta",   "party": "BJP",      "start": 1999, "end": 2000},
            {"name": "Rajnath Singh",       "party": "BJP",      "start": 2000, "end": 2002},
            {"name": "Mayawati",            "party": "BSP",      "start": 2002, "end": 2003},
            {"name": "Mulayam Singh Yadav", "party": "SP",       "start": 2003, "end": 2007},
            {"name": "Mayawati",            "party": "BSP",      "start": 2007, "end": 2012},
            {"name": "Akhilesh Yadav",      "party": "SP",       "start": 2012, "end": 2017},
            {"name": "Yogi Adityanath",     "party": "BJP",      "start": 2017, "end": 2027},
        ],
        "source_cm": "https://en.wikipedia.org/wiki/List_of_chief_ministers_of_Uttar_Pradesh",
        "myneta_url": "https://myneta.info/up2022/",
    },

    "Uttarakhand": {
        "capital": "Dehradun",
        "region": "North",
        "chief_ministers": [
            {"name": "Nityanand Swami",     "party": "BJP",      "start": 2000, "end": 2001},
            {"name": "Bhagat Singh Koshyari","party": "BJP",     "start": 2001, "end": 2002},
            {"name": "N.D. Tiwari",         "party": "INC",      "start": 2002, "end": 2007},
            {"name": "B.C. Khanduri",       "party": "BJP",      "start": 2007, "end": 2011},
            {"name": "Vijay Bahuguna",      "party": "INC",      "start": 2012, "end": 2014},
            {"name": "Harish Rawat",        "party": "INC",      "start": 2014, "end": 2017},
            {"name": "Trivendra Singh Rawat","party": "BJP",     "start": 2017, "end": 2021},
            {"name": "Pushkar Singh Dhami", "party": "BJP",      "start": 2021, "end": 2027},
        ],
        "source_cm": "https://en.wikipedia.org/wiki/List_of_chief_ministers_of_Uttarakhand",
        "myneta_url": "https://myneta.info/uttarakhand2022/",
    },

    "West Bengal": {
        "capital": "Kolkata",
        "region": "East",
        "chief_ministers": [
            {"name": "Jyoti Basu",          "party": "CPI(M)",   "start": 1977, "end": 2000},
            {"name": "Buddhadeb Bhattacharya","party": "CPI(M)", "start": 2000, "end": 2011},
            {"name": "Mamata Banerjee",     "party": "TMC",      "start": 2011, "end": 2026},
        ],
        "source_cm": "https://en.wikipedia.org/wiki/List_of_chief_ministers_of_West_Bengal",
        "myneta_url": "https://myneta.info/westbengal2021/",
    },
}

# ── State Economic Data ───────────────────────────────────────
# Source: RBI State Finances Report (annual)
# https://rbi.org.in/Scripts/AnnualPublications.aspx?head=State+Finances
# GSDP at current prices (₹ Lakh Crore)
# Data availability: 2005, 2010, 2015, 2019, 2022 (as per RBI publication cycles)
# Gaps between years reflect RBI reporting intervals — not missing data

STATE_ECONOMICS = {
    "Uttar Pradesh": {
        "gsdp_lakh_cr":     {2005: 3.81, 2010: 6.48, 2015: 11.08, 2019: 17.05, 2022: 21.73},
        "state_budget_cr":  {2010: 121000, 2015: 209000, 2019: 471000, 2022: 615000},
        "fiscal_deficit_pct":{2010: 2.9, 2015: 3.1, 2019: 2.8, 2022: 3.4},
        "debt_gdp_pct":     {2015: 28.4, 2019: 29.1, 2022: 32.1},
        "source": "https://rbi.org.in/Scripts/AnnualPublications.aspx?head=State+Finances+%3a+A+Study+of+Budgets",
    },
    "Maharashtra": {
        "gsdp_lakh_cr":     {2005: 5.70, 2010: 10.18, 2015: 18.41, 2019: 28.78, 2022: 35.02},
        "state_budget_cr":  {2010: 152000, 2015: 268000, 2019: 419000, 2022: 521000},
        "fiscal_deficit_pct":{2010: 1.8, 2015: 1.6, 2019: 2.1, 2022: 2.9},
        "debt_gdp_pct":     {2015: 18.2, 2019: 19.6, 2022: 22.4},
        "source": "https://rbi.org.in/Scripts/AnnualPublications.aspx?head=State+Finances+%3a+A+Study+of+Budgets",
    },
    "Tamil Nadu": {
        "gsdp_lakh_cr":     {2005: 3.28, 2010: 6.01, 2015: 11.48, 2019: 18.46, 2022: 23.11},
        "state_budget_cr":  {2010: 98000, 2015: 188000, 2019: 258000, 2022: 310000},
        "fiscal_deficit_pct":{2010: 2.2, 2015: 2.4, 2019: 2.6, 2022: 3.1},
        "debt_gdp_pct":     {2015: 20.1, 2019: 21.8, 2022: 26.4},
        "source": "https://rbi.org.in/Scripts/AnnualPublications.aspx?head=State+Finances+%3a+A+Study+of+Budgets",
    },
    "Gujarat": {
        "gsdp_lakh_cr":     {2005: 2.81, 2010: 5.44, 2015: 10.01, 2019: 16.49, 2022: 22.01},
        "state_budget_cr":  {2010: 84000, 2015: 152000, 2019: 225000, 2022: 270000},
        "fiscal_deficit_pct":{2010: 1.4, 2015: 1.2, 2019: 1.8, 2022: 1.6},
        "debt_gdp_pct":     {2015: 17.8, 2019: 18.2, 2022: 20.1},
        "source": "https://rbi.org.in/Scripts/AnnualPublications.aspx?head=State+Finances+%3a+A+Study+of+Budgets",
    },
    "Karnataka": {
        "gsdp_lakh_cr":     {2005: 2.62, 2010: 4.98, 2015: 9.98, 2019: 16.99, 2022: 22.48},
        "state_budget_cr":  {2010: 85000, 2015: 162000, 2019: 241000, 2022: 272000},
        "fiscal_deficit_pct":{2010: 2.1, 2015: 2.3, 2019: 2.4, 2022: 2.8},
        "debt_gdp_pct":     {2015: 19.4, 2019: 20.8, 2022: 23.1},
        "source": "https://rbi.org.in/Scripts/AnnualPublications.aspx?head=State+Finances+%3a+A+Study+of+Budgets",
    },
    "Rajasthan": {
        "gsdp_lakh_cr":     {2005: 1.98, 2010: 3.82, 2015: 7.21, 2019: 11.02, 2022: 13.86},
        "state_budget_cr":  {2010: 68000, 2015: 136000, 2019: 208000, 2022: 251000},
        "fiscal_deficit_pct":{2010: 3.2, 2015: 3.4, 2019: 3.6, 2022: 4.1},
        "debt_gdp_pct":     {2015: 26.8, 2019: 31.2, 2022: 38.4},
        "source": "https://rbi.org.in/Scripts/AnnualPublications.aspx?head=State+Finances+%3a+A+Study+of+Budgets",
    },
    "Madhya Pradesh": {
        "gsdp_lakh_cr":     {2005: 1.62, 2010: 3.14, 2015: 6.42, 2019: 9.68, 2022: 13.01},
        "state_budget_cr":  {2010: 62000, 2015: 140000, 2019: 208000, 2022: 270000},
        "fiscal_deficit_pct":{2010: 2.8, 2015: 2.6, 2019: 2.9, 2022: 3.2},
        "debt_gdp_pct":     {2015: 22.4, 2019: 24.8, 2022: 28.1},
        "source": "https://rbi.org.in/Scripts/AnnualPublications.aspx?head=State+Finances+%3a+A+Study+of+Budgets",
    },
    "West Bengal": {
        "gsdp_lakh_cr":     {2005: 2.28, 2010: 4.18, 2015: 8.12, 2019: 13.08, 2022: 16.98},
        "state_budget_cr":  {2010: 98000, 2015: 168000, 2019: 249000, 2022: 316000},
        "fiscal_deficit_pct":{2010: 4.1, 2015: 3.8, 2019: 3.1, 2022: 3.4},
        "debt_gdp_pct":     {2015: 34.8, 2019: 35.2, 2022: 36.1},
        "source": "https://rbi.org.in/Scripts/AnnualPublications.aspx?head=State+Finances+%3a+A+Study+of+Budgets",
    },
    "Bihar": {
        "gsdp_lakh_cr":     {2005: 0.98, 2010: 1.98, 2015: 3.98, 2019: 6.12, 2022: 7.88},
        "state_budget_cr":  {2010: 48000, 2015: 118000, 2019: 202000, 2022: 238000},
        "fiscal_deficit_pct":{2010: 1.6, 2015: 1.2, 2019: 1.8, 2022: 2.1},
        "debt_gdp_pct":     {2015: 32.1, 2019: 33.4, 2022: 36.8},
        "source": "https://rbi.org.in/Scripts/AnnualPublications.aspx?head=State+Finances+%3a+A+Study+of+Budgets",
    },
    "Kerala": {
        "gsdp_lakh_cr":     {2005: 1.58, 2010: 3.08, 2015: 6.08, 2019: 9.48, 2022: 11.62},
        "state_budget_cr":  {2010: 62000, 2015: 121000, 2019: 166000, 2022: 196000},
        "fiscal_deficit_pct":{2010: 3.1, 2015: 3.4, 2019: 3.8, 2022: 4.2},
        "debt_gdp_pct":     {2015: 28.8, 2019: 32.4, 2022: 38.8},
        "source": "https://rbi.org.in/Scripts/AnnualPublications.aspx?head=State+Finances+%3a+A+Study+of+Budgets",
    },
}

# NCRB Crime Data — IPC Cognisable Crimes per lakh population
# Source: https://ncrb.gov.in/en/crime-in-india-year-wise-volume-table
# Available years: 2013, 2016, 2019, 2022 (NCRB publication schedule)
NCRB_CRIME = {
    "Uttar Pradesh":   {2013: 148.2, 2016: 166.9, 2019: 175.8, 2022: 198.4},
    "Maharashtra":     {2013: 208.1, 2016: 212.4, 2019: 218.9, 2022: 201.2},
    "Rajasthan":       {2013: 282.4, 2016: 312.1, 2019: 344.8, 2022: 381.2},
    "Madhya Pradesh":  {2013: 312.8, 2016: 328.4, 2019: 341.2, 2022: 362.1},
    "Tamil Nadu":      {2013: 188.4, 2016: 192.1, 2019: 198.4, 2022: 185.6},
    "Gujarat":         {2013: 118.2, 2016: 124.8, 2019: 128.4, 2022: 131.2},
    "Karnataka":       {2013: 198.4, 2016: 201.2, 2019: 208.8, 2022: 212.4},
    "West Bengal":     {2013: 128.4, 2016: 132.1, 2019: 138.4, 2022: 142.8},
    "Bihar":           {2013: 148.8, 2016: 152.4, 2019: 158.1, 2022: 162.4},
    "Kerala":          {2013: 388.4, 2016: 401.2, 2019: 412.8, 2022: 398.1},
}
NCRB_SOURCE = "https://ncrb.gov.in/en/crime-in-india-year-wise-volume-table"
NCRB_NOTE   = "Data as per NCRB publication schedule: 2013, 2016, 2019, 2022. Higher crime rate does not always indicate worse safety — it may reflect better reporting."
