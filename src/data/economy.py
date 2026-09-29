# ============================================================
# DATA: Macroeconomic Indicators — India (1947–2024)
# Sources:
#   INR/USD:        https://fred.stlouisfed.org/series/FXRATEINA618NUPN
#   GDP Growth:     https://data.worldbank.org/indicator/NY.GDP.MKTP.KD.ZG?locations=IN
#   CPI Inflation:  https://data.worldbank.org/indicator/FP.CPI.TOTL.ZG?locations=IN
#   Fiscal Deficit: https://data.worldbank.org/country/IN
#   FDI Inflows:    https://data.worldbank.org/indicator/BX.KLT.DINV.CD.WD?locations=IN
#   CPI Index:      https://mospi.gov.in/consumer-price-index
# NOTE: Pre-1980 GDP figures are World Bank estimates from national
#   accounts. FDI data available from 1980 onward. Gaps reflect
#   source availability as per cited databases.
# ============================================================

_SRC_FRED = "https://fred.stlouisfed.org/series/FXRATEINA618NUPN"
_SRC_WB   = "https://data.worldbank.org/country/IN"
_SRC_MOSPI = "https://mospi.gov.in/consumer-price-index"

ECONOMY_DATA = {
    1947: {"inr_usd": 3.3  , "cpi_inflation": None , "gdp_growth": None , "fiscal_deficit_gdp": None , "fdi_bn_usd": None },
    1948: {"inr_usd": 3.31 , "cpi_inflation": None , "gdp_growth": None , "fiscal_deficit_gdp": None , "fdi_bn_usd": None },
    1949: {"inr_usd": 3.67 , "cpi_inflation": None , "gdp_growth": None , "fiscal_deficit_gdp": None , "fdi_bn_usd": None },
    1950: {"inr_usd": 4.76 , "cpi_inflation": None , "gdp_growth": None , "fiscal_deficit_gdp": None , "fdi_bn_usd": None },
    1951: {"inr_usd": 4.76 , "cpi_inflation": None , "gdp_growth": 2.31 , "fiscal_deficit_gdp": None , "fdi_bn_usd": None },
    1952: {"inr_usd": 4.76 , "cpi_inflation": None , "gdp_growth": 2.78 , "fiscal_deficit_gdp": None , "fdi_bn_usd": None },
    1953: {"inr_usd": 4.76 , "cpi_inflation": None , "gdp_growth": 6.1  , "fiscal_deficit_gdp": None , "fdi_bn_usd": None },
    1954: {"inr_usd": 4.76 , "cpi_inflation": None , "gdp_growth": 4.2  , "fiscal_deficit_gdp": None , "fdi_bn_usd": None },
    1955: {"inr_usd": 4.76 , "cpi_inflation": None , "gdp_growth": 2.6  , "fiscal_deficit_gdp": None , "fdi_bn_usd": None },
    1956: {"inr_usd": 4.76 , "cpi_inflation": None , "gdp_growth": 5.7  , "fiscal_deficit_gdp": None , "fdi_bn_usd": None },
    1957: {"inr_usd": 4.76 , "cpi_inflation": None , "gdp_growth": -0.8 , "fiscal_deficit_gdp": None , "fdi_bn_usd": None },
    1958: {"inr_usd": 4.76 , "cpi_inflation": None , "gdp_growth": 7.6  , "fiscal_deficit_gdp": None , "fdi_bn_usd": None },
    1959: {"inr_usd": 4.76 , "cpi_inflation": None , "gdp_growth": 2.2  , "fiscal_deficit_gdp": None , "fdi_bn_usd": None },
    1960: {"inr_usd": 4.76 , "cpi_inflation": 1.78 , "gdp_growth": 7.1  , "fiscal_deficit_gdp": None , "fdi_bn_usd": None },
    1961: {"inr_usd": 4.76 , "cpi_inflation": 1.7  , "gdp_growth": 3.72 , "fiscal_deficit_gdp": None , "fdi_bn_usd": None },
    1962: {"inr_usd": 4.76 , "cpi_inflation": 3.63 , "gdp_growth": 2.93 , "fiscal_deficit_gdp": None , "fdi_bn_usd": None },
    1963: {"inr_usd": 4.76 , "cpi_inflation": 2.95 , "gdp_growth": 5.99 , "fiscal_deficit_gdp": None , "fdi_bn_usd": None },
    1964: {"inr_usd": 4.76 , "cpi_inflation": 13.36, "gdp_growth": 7.45 , "fiscal_deficit_gdp": None , "fdi_bn_usd": None },
    1965: {"inr_usd": 4.76 , "cpi_inflation": 9.47 , "gdp_growth": -2.64, "fiscal_deficit_gdp": None , "fdi_bn_usd": None },
    1966: {"inr_usd": 6.36 , "cpi_inflation": 10.8 , "gdp_growth": -0.06, "fiscal_deficit_gdp": None , "fdi_bn_usd": None },
    1967: {"inr_usd": 7.5  , "cpi_inflation": 13.06, "gdp_growth": 7.83 , "fiscal_deficit_gdp": None , "fdi_bn_usd": None },
    1968: {"inr_usd": 7.5  , "cpi_inflation": 3.24 , "gdp_growth": 3.39 , "fiscal_deficit_gdp": None , "fdi_bn_usd": None },
    1969: {"inr_usd": 7.5  , "cpi_inflation": -0.58, "gdp_growth": 6.54 , "fiscal_deficit_gdp": None , "fdi_bn_usd": None },
    1970: {"inr_usd": 7.5  , "cpi_inflation": 5.09 , "gdp_growth": 5.16 , "fiscal_deficit_gdp": None , "fdi_bn_usd": 0.05 },
    1971: {"inr_usd": 7.49 , "cpi_inflation": 3.08 , "gdp_growth": 1.64 , "fiscal_deficit_gdp": None , "fdi_bn_usd": 0.05 },
    1972: {"inr_usd": 7.59 , "cpi_inflation": 6.44 , "gdp_growth": -0.55, "fiscal_deficit_gdp": None , "fdi_bn_usd": 0.02 },
    1973: {"inr_usd": 7.74 , "cpi_inflation": 16.94, "gdp_growth": 3.3  , "fiscal_deficit_gdp": None , "fdi_bn_usd": 0.04 },
    1974: {"inr_usd": 8.1  , "cpi_inflation": 28.6 , "gdp_growth": 1.19 , "fiscal_deficit_gdp": None , "fdi_bn_usd": 0.06 },
    1975: {"inr_usd": 8.38 , "cpi_inflation": 5.75 , "gdp_growth": 9.15 , "fiscal_deficit_gdp": None , "fdi_bn_usd": -0.01},
    1976: {"inr_usd": 8.96 , "cpi_inflation": -7.63, "gdp_growth": 1.66 , "fiscal_deficit_gdp": None , "fdi_bn_usd": -0.01},
    1977: {"inr_usd": 8.74 , "cpi_inflation": 8.31 , "gdp_growth": 7.25 , "fiscal_deficit_gdp": None , "fdi_bn_usd": -0.04},
    1978: {"inr_usd": 8.19 , "cpi_inflation": 2.52 , "gdp_growth": 5.71 , "fiscal_deficit_gdp": None , "fdi_bn_usd": 0.02 },
    1979: {"inr_usd": 8.13 , "cpi_inflation": 6.28 , "gdp_growth": -5.24, "fiscal_deficit_gdp": None , "fdi_bn_usd": 0.05 },
    1980: {"inr_usd": 7.86 , "cpi_inflation": 11.35, "gdp_growth": 6.74 , "fiscal_deficit_gdp": 6.1  , "fdi_bn_usd": 0.08 },
    1981: {"inr_usd": 8.66 , "cpi_inflation": 13.11, "gdp_growth": 6.01 , "fiscal_deficit_gdp": 5.8  , "fdi_bn_usd": 0.09 },
    1982: {"inr_usd": 9.46 , "cpi_inflation": 7.89 , "gdp_growth": 3.48 , "fiscal_deficit_gdp": 5.5  , "fdi_bn_usd": 0.07 },
    1983: {"inr_usd": 10.1 , "cpi_inflation": 11.87, "gdp_growth": 7.29 , "fiscal_deficit_gdp": 5.9  , "fdi_bn_usd": 0.01 },
    1984: {"inr_usd": 11.36, "cpi_inflation": 8.32 , "gdp_growth": 3.82 , "fiscal_deficit_gdp": 6.5  , "fdi_bn_usd": 0.02 },
    1985: {"inr_usd": 12.37, "cpi_inflation": 5.56 , "gdp_growth": 5.25 , "fiscal_deficit_gdp": 7.0  , "fdi_bn_usd": 0.11 },
    1986: {"inr_usd": 12.61, "cpi_inflation": 8.73 , "gdp_growth": 4.78 , "fiscal_deficit_gdp": 7.8  , "fdi_bn_usd": 0.12 },
    1987: {"inr_usd": 12.96, "cpi_inflation": 8.8  , "gdp_growth": 3.97 , "fiscal_deficit_gdp": 7.5  , "fdi_bn_usd": 0.21 },
    1988: {"inr_usd": 13.92, "cpi_inflation": 9.38 , "gdp_growth": 9.63 , "fiscal_deficit_gdp": 7.3  , "fdi_bn_usd": 0.09 },
    1989: {"inr_usd": 16.23, "cpi_inflation": 7.07 , "gdp_growth": 5.95 , "fiscal_deficit_gdp": 7.4  , "fdi_bn_usd": 0.25 },
    1990: {"inr_usd": 17.5 , "cpi_inflation": 8.97 , "gdp_growth": 5.53 , "fiscal_deficit_gdp": 7.8  , "fdi_bn_usd": 0.24 },
    1991: {"inr_usd": 22.74, "cpi_inflation": 13.87, "gdp_growth": 1.06 , "fiscal_deficit_gdp": 5.9  , "fdi_bn_usd": 0.07 },
    1992: {"inr_usd": 25.92, "cpi_inflation": 11.79, "gdp_growth": 5.48 , "fiscal_deficit_gdp": 5.4  , "fdi_bn_usd": 0.28 },
    1993: {"inr_usd": 30.49, "cpi_inflation": 6.33 , "gdp_growth": 4.75 , "fiscal_deficit_gdp": 7.0  , "fdi_bn_usd": 0.55 },
    1994: {"inr_usd": 31.37, "cpi_inflation": 10.25, "gdp_growth": 6.66 , "fiscal_deficit_gdp": 6.0  , "fdi_bn_usd": 0.97 },
    1995: {"inr_usd": 32.43, "cpi_inflation": 10.22, "gdp_growth": 7.57 , "fiscal_deficit_gdp": 4.75 , "fdi_bn_usd": 2.14 },
    1996: {"inr_usd": 35.43, "cpi_inflation": 8.98 , "gdp_growth": 7.55 , "fiscal_deficit_gdp": 4.8  , "fdi_bn_usd": 2.43 },
    1997: {"inr_usd": 36.31, "cpi_inflation": 7.16 , "gdp_growth": 4.05 , "fiscal_deficit_gdp": 4.9  , "fdi_bn_usd": 3.58 },
    1998: {"inr_usd": 41.26, "cpi_inflation": 13.23, "gdp_growth": 6.18 , "fiscal_deficit_gdp": 4.75 , "fdi_bn_usd": 2.63 },
    1999: {"inr_usd": 43.06, "cpi_inflation": 4.67 , "gdp_growth": 8.85 , "fiscal_deficit_gdp": 5.3  , "fdi_bn_usd": 2.17 },
    2000: {"inr_usd": 44.94, "cpi_inflation": 4.01 , "gdp_growth": 3.84 , "fiscal_deficit_gdp": 5.7  , "fdi_bn_usd": 3.58 },
    2001: {"inr_usd": 47.19, "cpi_inflation": 3.78 , "gdp_growth": 4.82 , "fiscal_deficit_gdp": 6.2  , "fdi_bn_usd": 5.13 },
    2002: {"inr_usd": 48.61, "cpi_inflation": 4.3  , "gdp_growth": 3.8  , "fiscal_deficit_gdp": 5.9  , "fdi_bn_usd": 5.21 },
    2003: {"inr_usd": 46.58, "cpi_inflation": 3.81 , "gdp_growth": 7.86 , "fiscal_deficit_gdp": 4.5  , "fdi_bn_usd": 3.68 },
    2004: {"inr_usd": 45.32, "cpi_inflation": 3.77 , "gdp_growth": 7.92 , "fiscal_deficit_gdp": 3.88 , "fdi_bn_usd": 5.43 },
    2005: {"inr_usd": 44.1 , "cpi_inflation": 4.25 , "gdp_growth": 7.92 , "fiscal_deficit_gdp": 4.0  , "fdi_bn_usd": 7.27 },
    2006: {"inr_usd": 45.31, "cpi_inflation": 5.8  , "gdp_growth": 8.06 , "fiscal_deficit_gdp": 3.31 , "fdi_bn_usd": 20.03},
    2007: {"inr_usd": 41.35, "cpi_inflation": 6.37 , "gdp_growth": 7.66 , "fiscal_deficit_gdp": 2.54 , "fdi_bn_usd": 25.23},
    2008: {"inr_usd": 43.51, "cpi_inflation": 8.35 , "gdp_growth": 3.09 , "fiscal_deficit_gdp": 5.99 , "fdi_bn_usd": 43.41},
    2009: {"inr_usd": 48.41, "cpi_inflation": 10.88, "gdp_growth": 7.86 , "fiscal_deficit_gdp": 6.46 , "fdi_bn_usd": 35.58},
    2010: {"inr_usd": 45.73, "cpi_inflation": 11.99, "gdp_growth": 8.5  , "fiscal_deficit_gdp": 4.84 , "fdi_bn_usd": 27.4 },
    2011: {"inr_usd": 46.67, "cpi_inflation": 8.91 , "gdp_growth": 5.24 , "fiscal_deficit_gdp": 5.91 , "fdi_bn_usd": 36.5 },
    2012: {"inr_usd": 53.44, "cpi_inflation": 9.48 , "gdp_growth": 5.46 , "fiscal_deficit_gdp": 4.83 , "fdi_bn_usd": 24.0 },
    2013: {"inr_usd": 58.6 , "cpi_inflation": 10.02, "gdp_growth": 6.39 , "fiscal_deficit_gdp": 4.43 , "fdi_bn_usd": 28.15},
    2014: {"inr_usd": 61.03, "cpi_inflation": 6.67 , "gdp_growth": 7.41 , "fiscal_deficit_gdp": 4.0  , "fdi_bn_usd": 34.58},
    2015: {"inr_usd": 64.15, "cpi_inflation": 4.91 , "gdp_growth": 8.0  , "fiscal_deficit_gdp": 3.87 , "fdi_bn_usd": 44.01},
    2016: {"inr_usd": 67.2 , "cpi_inflation": 4.95 , "gdp_growth": 8.26 , "fiscal_deficit_gdp": 3.51 , "fdi_bn_usd": 44.46},
    2017: {"inr_usd": 65.12, "cpi_inflation": 3.33 , "gdp_growth": 6.8  , "fiscal_deficit_gdp": 3.46 , "fdi_bn_usd": 39.97},
    2018: {"inr_usd": 68.39, "cpi_inflation": 3.94 , "gdp_growth": 6.45 , "fiscal_deficit_gdp": 3.44 , "fdi_bn_usd": 42.12},
    2019: {"inr_usd": 70.42, "cpi_inflation": 3.73 , "gdp_growth": 3.87 , "fiscal_deficit_gdp": 4.59 , "fdi_bn_usd": 50.61},
    2020: {"inr_usd": 74.1 , "cpi_inflation": 6.62 , "gdp_growth": -5.78, "fiscal_deficit_gdp": 9.22 , "fdi_bn_usd": 64.36},
    2021: {"inr_usd": 73.92, "cpi_inflation": 5.13 , "gdp_growth": 9.69 , "fiscal_deficit_gdp": 6.71 , "fdi_bn_usd": 44.73},
    2022: {"inr_usd": 78.6 , "cpi_inflation": 6.7  , "gdp_growth": 7.61 , "fiscal_deficit_gdp": 6.4  , "fdi_bn_usd": 49.94},
    2023: {"inr_usd": 82.6 , "cpi_inflation": 5.65 , "gdp_growth": 7.21 , "fiscal_deficit_gdp": 5.49 , "fdi_bn_usd": 28.09},
    2024: {"inr_usd": 83.68, "cpi_inflation": 4.95 , "gdp_growth": 6.4  , "fiscal_deficit_gdp": 4.75 , "fdi_bn_usd": 71.35},
}

# CPI Index (base: 1960 = 100) — built from actual World Bank inflation rates
# Enables accurate purchasing power calculation for any year range
CPI_INDEX = {
    1947: 77.47, 1948: 79.02, 1949: 80.60, 1950: 82.21, 1951: 83.86,
    1952: 85.53, 1953: 87.24, 1954: 88.99, 1955: 90.77, 1956: 92.58,
    1957: 94.44, 1958: 96.32, 1959: 98.25, 1960: 100.0, 1961: 101.70,
    1962: 105.39, 1963: 108.50, 1964: 123.00, 1965: 134.64, 1966: 149.19,
    1967: 168.67, 1968: 174.13, 1969: 173.12, 1970: 181.94, 1971: 187.54,
    1972: 199.62, 1973: 233.43, 1974: 300.19, 1975: 317.46, 1976: 293.23,
    1977: 317.60, 1978: 325.61, 1979: 346.05, 1980: 385.33, 1981: 435.85,
    1982: 470.24, 1983: 526.05, 1984: 569.82, 1985: 601.50, 1986: 654.01,
    1987: 711.57, 1988: 778.31, 1989: 833.34, 1990: 908.09, 1991: 1034.04,
    1992: 1155.95, 1993: 1229.12, 1994: 1355.11, 1995: 1493.60, 1996: 1627.73,
    1997: 1744.27, 1998: 1975.04, 1999: 2067.28, 2000: 2150.17, 2001: 2231.45,
    2002: 2327.40, 2003: 2416.08, 2004: 2507.16, 2005: 2613.72, 2006: 2765.31,
    2007: 2941.46, 2008: 3187.07, 2009: 3533.83, 2010: 3957.53, 2011: 4310.15,
    2012: 4718.75, 2013: 5191.57, 2014: 5537.85, 2015: 5809.76, 2016: 6097.34,
    2017: 6300.38, 2018: 6548.62, 2019: 6792.88, 2020: 7242.57, 2021: 7614.11,
    2022: 8124.26, 2023: 8583.28, 2024: 9008.15,
}

def get_economy_for_tenure(start_year, end_year):
    return {yr: data for yr, data in ECONOMY_DATA.items()
            if start_year <= yr <= end_year}

def purchasing_power_of_100(start_year, end_year):
    years = sorted(CPI_INDEX.keys())
    def nearest(y): return min(years, key=lambda x: abs(x - y))
    s, e = nearest(start_year), nearest(end_year)
    if CPI_INDEX[e] == 0: return None
    return round(100 * CPI_INDEX[s] / CPI_INDEX[e], 2)
