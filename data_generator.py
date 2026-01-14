# data_generator.py
import pandas as pd
import numpy as np


def generate_stock_universe():
    """Generate realistic sample data with REAL stock symbols"""

    # REAL stock symbols by sector (all actual NYSE/NASDAQ tickers)
    sectors_stocks = {
        "Technology": [
            "AAPL",
            "MSFT",
            "GOOGL",
            "AMZN",
            "META",
            "NVDA",
            "TSLA",
            "ADBE",
            "CRM",
            "INTC",
            "CSCO",
            "ORCL",
            "IBM",
            "QCOM",
            "AMD",
            "NOW",
            "SNOW",
            "NET",
            "CRWD",
            "PANW",
            "ZS",
            "DDOG",
            "MDB",
            "PLTR",
            "UBER",
            "SHOP",
            "SQ",
            "ROKU",
            "ZM",
            "DOCU",
            "FTNT",
            "OKTA",
            "TEAM",
            "SPLK",
            "HUBS",
            "TWLO",
            "TTD",
            "PYPL",
            "NFLX",
            "DIS",
        ],
        "Healthcare": [
            "JNJ",
            "UNH",
            "PFE",
            "ABT",
            "TMO",
            "LLY",
            "ABBV",
            "DHR",
            "MDT",
            "BMY",
            "AMGN",
            "GILD",
            "VRTX",
            "REGN",
            "ISRG",
            "DXCM",
            "IDXX",
            "BSX",
            "ZTS",
            "SYK",
            "CVS",
            "WBA",
            "CI",
            "HUM",
            "ELV",
            "MCK",
            "ABC",
            "CAH",
            "EW",
            "BIIB",
            "ALGN",
            "ILMN",
            "MTD",
            "WST",
            "RMD",
            "STE",
            "WAT",
            "PKI",
            "DGX",
            "LH",
        ],
        "Financials": [
            "JPM",
            "BAC",
            "WFC",
            "C",
            "GS",
            "MS",
            "SCHW",
            "BLK",
            "AXP",
            "V",
            "MA",
            "PYPL",
            "COF",
            "USB",
            "PNC",
            "TFC",
            "BK",
            "STT",
            "MMC",
            "SPGI",
            "ICE",
            "CME",
            "NDAQ",
            "MCO",
            "FIS",
            "FISV",
            "GPN",
            "JKHY",
            "SYF",
            "ALLY",
            "RF",
            "KEY",
            "HBAN",
            "CFG",
            "MTB",
            "ZION",
            "FHN",
            "BKU",
            "WBS",
            "SNV",
        ],
        "Consumer": [
            "PG",
            "KO",
            "PEP",
            "WMT",
            "COST",
            "TGT",
            "HD",
            "LOW",
            "NKE",
            "MCD",
            "SBUX",
            "DIS",
            "CMCSA",
            "T",
            "VZ",
            "TMUS",
            "CHTR",
            "ATVI",
            "EA",
            "TTWO",
            "LULU",
            "ULTA",
            "ROST",
            "TJX",
            "DG",
            "DLTR",
            "FIVE",
            "BURL",
            "CASY",
            "KR",
            "SYY",
            "HSY",
            "K",
            "GIS",
            "CPB",
            "KHC",
            "MDLZ",
            "STZ",
            "BF.B",
            "MO",
        ],
        "Industrial": [
            "BA",
            "CAT",
            "GE",
            "HON",
            "UPS",
            "FDX",
            "RTX",
            "LMT",
            "GD",
            "NOC",
            "DE",
            "EMR",
            "ITW",
            "ETN",
            "ROK",
            "TT",
            "CPRT",
            "CSX",
            "UNP",
            "NSC",
            "PCAR",
            "WM",
            "RSG",
            "WCN",
            "AWK",
            "AEP",
            "DUK",
            "SO",
            "NEE",
            "D",
            "EXC",
            "SRE",
            "XEL",
            "WEC",
            "ES",
            "EIX",
            "PEG",
            "AEE",
            "LNT",
            "ED",
        ],
        "Energy": [
            "XOM",
            "CVX",
            "COP",
            "SLB",
            "EOG",
            "PSX",
            "MPC",
            "VLO",
            "KMI",
            "WMB",
            "OXY",
            "HAL",
            "BKR",
            "FANG",
            "PXD",
            "EQT",
            "DVN",
            "MTDR",
            "MRO",
            "APA",
            "OKE",
            "TRP",
            "ENB",
            "EPD",
            "ET",
            "MPLX",
            "PAA",
            "LNG",
            "NOV",
            "FTI",
            "NBR",
            "HP",
            "PTEN",
            "PUMP",
            "WFRD",
            "TDW",
            "RIG",
            "VAL",
            "FTI",
            "HP",
        ],
    }

    # Helper function to generate company names
    def get_company_name(ticker, sector):
        """Get or generate a company name for a ticker"""

        # Major companies with known names
        known_names = {
            "AAPL": "Apple Inc.",
            "MSFT": "Microsoft Corp.",
            "GOOGL": "Alphabet Inc.",
            "AMZN": "Amazon.com Inc.",
            "META": "Meta Platforms Inc.",
            "NVDA": "NVIDIA Corp.",
            "TSLA": "Tesla Inc.",
            "JNJ": "Johnson & Johnson",
            "JPM": "JPMorgan Chase & Co.",
            "V": "Visa Inc.",
            "PG": "Procter & Gamble Co.",
            "UNH": "UnitedHealth Group Inc.",
            "HD": "Home Depot Inc.",
            "DIS": "Walt Disney Co.",
            "BAC": "Bank of America Corp.",
            "MA": "Mastercard Inc.",
            "XOM": "Exxon Mobil Corp.",
            "CVX": "Chevron Corp.",
            "PFE": "Pfizer Inc.",
            "ABT": "Abbott Laboratories",
            "WMT": "Walmart Inc.",
            "KO": "Coca-Cola Co.",
            "PEP": "PepsiCo Inc.",
            "CSCO": "Cisco Systems Inc.",
            "INTC": "Intel Corp.",
            "IBM": "International Business Machines Corp.",
            "ORCL": "Oracle Corp.",
            "QCOM": "Qualcomm Inc.",
            "AMD": "Advanced Micro Devices Inc.",
            "ADBE": "Adobe Inc.",
            "CRM": "Salesforce Inc.",
            "NFLX": "Netflix Inc.",
            "PYPL": "PayPal Holdings Inc.",
            "COST": "Costco Wholesale Corp.",
            "TMO": "Thermo Fisher Scientific Inc.",
            "ABBV": "AbbVie Inc.",
            "LLY": "Eli Lilly & Co.",
            "DHR": "Danaher Corp.",
            "MDT": "Medtronic plc",
            "BMY": "Bristol-Myers Squibb Co.",
            "AMGN": "Amgen Inc.",
            "T": "AT&T Inc.",
            "VZ": "Verizon Communications Inc.",
            "CMCSA": "Comcast Corp.",
            "NKE": "Nike Inc.",
            "MCD": "McDonald's Corp.",
            "SBUX": "Starbucks Corp.",
            "BA": "Boeing Co.",
            "CAT": "Caterpillar Inc.",
            "GE": "General Electric Co.",
            "HON": "Honeywell International Inc.",
            "UPS": "United Parcel Service Inc.",
            "FDX": "FedEx Corp.",
            "RTX": "Raytheon Technologies Corp.",
            "LMT": "Lockheed Martin Corp.",
            "GD": "General Dynamics Corp.",
            "NOC": "Northrop Grumman Corp.",
            "DE": "Deere & Co.",
            "CSX": "CSX Corp.",
            "UNP": "Union Pacific Corp.",
            "NSC": "Norfolk Southern Corp.",
            "LOW": "Lowe's Companies Inc.",
            "TGT": "Target Corp.",
            "WBA": "Walgreens Boots Alliance Inc.",
            "CVS": "CVS Health Corp.",
            "CI": "Cigna Corp.",
            "HUM": "Humana Inc.",
            "ELV": "Elevance Health Inc.",
            "MCK": "McKesson Corp.",
            "ABC": "AmerisourceBergen Corp.",
            "CAH": "Cardinal Health Inc.",
            "GS": "Goldman Sachs Group Inc.",
            "MS": "Morgan Stanley",
            "BLK": "BlackRock Inc.",
            "AXP": "American Express Co.",
            "SPGI": "S&P Global Inc.",
            "ICE": "Intercontinental Exchange Inc.",
            "CME": "CME Group Inc.",
            "NDAQ": "Nasdaq Inc.",
            "MCO": "Moody's Corp.",
            "FIS": "Fidelity National Information Services Inc.",
            "FISV": "Fiserv Inc.",
            "GPN": "Global Payments Inc.",
            "NOW": "ServiceNow Inc.",
            "SNOW": "Snowflake Inc.",
            "NET": "Cloudflare Inc.",
            "CRWD": "CrowdStrike Holdings Inc.",
            "PANW": "Palo Alto Networks Inc.",
            "ZS": "Zscaler Inc.",
            "DDOG": "Datadog Inc.",
            "MDB": "MongoDB Inc.",
            "PLTR": "Palantir Technologies Inc.",
            "UBER": "Uber Technologies Inc.",
            "SHOP": "Shopify Inc.",
            "SQ": "Block Inc.",
            "ROKU": "Roku Inc.",
            "ZM": "Zoom Video Communications Inc.",
            "DOCU": "DocuSign Inc.",
            "FTNT": "Fortinet Inc.",
            "OKTA": "Okta Inc.",
            "TEAM": "Atlassian Corp.",
            "SPLK": "Splunk Inc.",
            "HUBS": "HubSpot Inc.",
            "TWLO": "Twilio Inc.",
            "TTD": "The Trade Desk Inc.",
            "ISRG": "Intuitive Surgical Inc.",
            "VRTX": "Vertex Pharmaceuticals Inc.",
            "REGN": "Regeneron Pharmaceuticals Inc.",
            "DXCM": "Dexcom Inc.",
            "IDXX": "IDEXX Laboratories Inc.",
            "ALGN": "Align Technology Inc.",
            "ILMN": "Illumina Inc.",
            "MTD": "Mettler-Toledo International Inc.",
            "WST": "West Pharmaceutical Services Inc.",
            "RMD": "ResMed Inc.",
            "STE": "Steris plc",
            "WAT": "Waters Corp.",
            "PKI": "PerkinElmer Inc.",
            "DGX": "Quest Diagnostics Inc.",
            "LH": "Laboratory Corp. of America Holdings",
            "EW": "Edwards Lifesciences Corp.",
            "BIIB": "Biogen Inc.",
            "SYK": "Stryker Corp.",
            "ZTS": "Zoetis Inc.",
            "BSX": "Boston Scientific Corp.",
            "LULU": "Lululemon Athletica Inc.",
            "ULTA": "Ulta Beauty Inc.",
            "ROST": "Ross Stores Inc.",
            "TJX": "TJX Companies Inc.",
            "DG": "Dollar General Corp.",
            "DLTR": "Dollar Tree Inc.",
            "FIVE": "Five Below Inc.",
            "BURL": "Burlington Stores Inc.",
            "CASY": "Casey's General Stores Inc.",
            "KR": "Kroger Co.",
            "SYY": "Sysco Corp.",
            "HSY": "Hershey Co.",
            "K": "Kellogg Co.",
            "GIS": "General Mills Inc.",
            "CPB": "Campbell Soup Co.",
            "KHC": "Kraft Heinz Co.",
            "MDLZ": "Mondelez International Inc.",
            "STZ": "Constellation Brands Inc.",
            "BF.B": "Brown-Forman Corp.",
            "MO": "Altria Group Inc.",
            "PCAR": "PACCAR Inc.",
            "WM": "Waste Management Inc.",
            "RSG": "Republic Services Inc.",
            "WCN": "Waste Connections Inc.",
            "AWK": "American Water Works Co. Inc.",
            "AEP": "American Electric Power Co. Inc.",
            "DUK": "Duke Energy Corp.",
            "SO": "Southern Co.",
            "NEE": "NextEra Energy Inc.",
            "D": "Dominion Energy Inc.",
            "EXC": "Exelon Corp.",
            "SRE": "Sempra Energy",
            "XEL": "Xcel Energy Inc.",
            "WEC": "WEC Energy Group Inc.",
            "ES": "Eversource Energy",
            "EIX": "Edison International",
            "PEG": "Public Service Enterprise Group Inc.",
            "AEE": "Ameren Corp.",
            "LNT": "Alliant Energy Corp.",
            "ED": "Consolidated Edison Inc.",
            "OKE": "ONEOK Inc.",
            "TRP": "TC Energy Corp.",
            "ENB": "Enbridge Inc.",
            "EPD": "Enterprise Products Partners L.P.",
            "ET": "Energy Transfer L.P.",
            "MPLX": "MPLX L.P.",
            "PAA": "Plains All American Pipeline L.P.",
            "LNG": "Cheniere Energy Inc.",
            "NOV": "NOV Inc.",
            "FTI": "TechnipFMC plc",
            "NBR": "Nabors Industries Ltd.",
            "HP": "Helmerich & Payne Inc.",
            "PTEN": "Patterson-UTI Energy Inc.",
            "PUMP": "ProPetro Holding Corp.",
            "WFRD": "Weatherford International plc",
            "TDW": "Tidewater Inc.",
            "RIG": "Transocean Ltd.",
            "VAL": "Valaris Ltd.",
            "FANG": "Diamondback Energy Inc.",
            "PXD": "Pioneer Natural Resources Co.",
            "EQT": "EQT Corp.",
            "DVN": "Devon Energy Corp.",
            "MTDR": "Matador Resources Co.",
            "MRO": "Marathon Oil Corp.",
            "APA": "APA Corp.",
            "OXY": "Occidental Petroleum Corp.",
            "HAL": "Halliburton Co.",
            "BKR": "Baker Hughes Co.",
            "SLB": "Schlumberger Ltd.",
            "EOG": "EOG Resources Inc.",
            "PSX": "Phillips 66",
            "MPC": "Marathon Petroleum Corp.",
            "VLO": "Valero Energy Corp.",
            "KMI": "Kinder Morgan Inc.",
            "WMB": "Williams Companies Inc.",
            "COP": "ConocoPhillips",
            "ATVI": "Activision Blizzard Inc.",
            "EA": "Electronic Arts Inc.",
            "TTWO": "Take-Two Interactive Software Inc.",
            "CHTR": "Charter Communications Inc.",
            "TMUS": "T-Mobile US Inc.",
            "F": "Ford Motor Co.",
            "GM": "General Motors Co.",
        }

        if ticker in known_names:
            return known_names[ticker]

        # Generate a realistic name based on ticker and sector
        sector_keywords = {
            "Technology": [
                "Tech",
                "Technologies",
                "Software",
                "Systems",
                "Digital",
                "Cloud",
                "Data",
            ],
            "Healthcare": [
                "Health",
                "Medical",
                "Pharmaceuticals",
                "Bio",
                "Care",
                "Therapeutics",
            ],
            "Financials": [
                "Financial",
                "Capital",
                "Group",
                "Holdings",
                "Bank",
                "Trust",
                "Services",
            ],
            "Consumer": ["Brands", "Consumer", "Goods", "Retail", "Stores", "Products"],
            "Industrial": [
                "Industries",
                "Industrial",
                "Manufacturing",
                "Engineering",
                "Solutions",
            ],
            "Energy": ["Energy", "Resources", "Petroleum", "Oil", "Gas", "Power"],
        }

        keywords = sector_keywords.get(sector, ["Corp.", "Inc."])
        keyword = np.random.choice(keywords)

        # Try to make it sound like a real company
        if ticker.isalpha() and len(ticker) <= 4:
            return f"{ticker} {keyword}"
        else:
            return f"{ticker} Corporation"

    all_stocks = []
    stock_id = 0

    np.random.seed(42)  # For reproducibility

    for sector, tickers in sectors_stocks.items():
        for ticker in tickers:
            # Get company name
            company_name = get_company_name(ticker, sector)

            # Base price based on actual market caps (simplified)
            if ticker in ["AAPL", "MSFT", "GOOGL", "AMZN", "NVDA", "TSLA", "META"]:
                base_price = np.random.uniform(100, 500)
            elif ticker in ["JNJ", "JPM", "V", "PG", "UNH", "HD", "MA", "XOM", "CVX"]:
                base_price = np.random.uniform(80, 300)
            elif ticker in ["PFE", "WMT", "KO", "PEP", "CSCO", "INTC", "IBM", "ORCL"]:
                base_price = np.random.uniform(40, 200)
            else:
                base_price = np.random.uniform(20, 150)

            # Create realistic 52-week ranges
            current_price = base_price * np.random.uniform(0.8, 1.2)
            week_52_low = base_price * np.random.uniform(0.7, 0.95)
            week_52_high = base_price * np.random.uniform(1.05, 1.4)

            # Ensure current price is within range
            current_price = max(week_52_low, min(week_52_high, current_price))

            # Calculate metrics
            from_low_pct = ((current_price - week_52_low) / week_52_low) * 100
            from_high_pct = ((current_price - week_52_high) / week_52_high) * 100

            # Create realistic market cap based on price
            if ticker in ["AAPL", "MSFT", "GOOGL", "AMZN"]:
                market_cap = current_price * np.random.uniform(
                    1000, 5000
                )  # Trillion+ companies
            elif ticker in ["NVDA", "META", "TSLA", "JPM", "JNJ", "V", "PG"]:
                market_cap = current_price * np.random.uniform(500, 2000)  # Large caps
            else:
                market_cap = current_price * np.random.uniform(
                    50, 500
                )  # Mid/small caps

            all_stocks.append(
                {
                    "ID": stock_id,
                    "Symbol": ticker,
                    "Name": company_name,
                    "Sector": sector,
                    "Current Price": round(current_price, 2),
                    "52W Low": round(week_52_low, 2),
                    "52W High": round(week_52_high, 2),
                    "% From Low": round(from_low_pct, 1),
                    "% From High": round(from_high_pct, 1),
                    "Market Cap (B)": round(
                        market_cap / 1000, 2
                    ),  # Convert to billions
                    "Volume (M)": round(np.random.uniform(1, 200), 1),
                }
            )
            stock_id += 1

    # Add some additional real stocks to reach ~500
    additional_tickers = [
        "F",
        "GM",
        "GE",
        "F",
        "GM",
        "GE",
        "F",  # Auto/Industrial
        "TGT",
        "LOW",
        "HD",
        "WMT",
        "COST",  # Retail
        "BA",
        "LMT",
        "RTX",
        "NOC",
        "GD",  # Defense
        "XOM",
        "CVX",
        "COP",
        "SLB",
        "EOG",  # Energy
        "JPM",
        "BAC",
        "WFC",
        "C",
        "GS",  # Banks
        "PFE",
        "JNJ",
        "MRK",
        "ABT",
        "BMY",  # Pharma
        "AAPL",
        "MSFT",
        "GOOGL",
        "AMZN",
        "META",  # Tech
    ]

    for ticker in additional_tickers:
        if stock_id >= 500:  # Stop at 500
            break

        # Check if ticker already exists
        existing_symbols = [s["Symbol"] for s in all_stocks]
        if ticker not in existing_symbols:
            company_name = get_company_name(
                ticker, np.random.choice(list(sectors_stocks.keys()))
            )
            base_price = np.random.uniform(20, 300)

            current_price = base_price * np.random.uniform(0.8, 1.2)
            week_52_low = base_price * np.random.uniform(0.7, 0.95)
            week_52_high = base_price * np.random.uniform(1.05, 1.4)
            current_price = max(week_52_low, min(week_52_high, current_price))

            from_low_pct = ((current_price - week_52_low) / week_52_low) * 100
            from_high_pct = ((current_price - week_52_high) / week_52_high) * 100

            market_cap = current_price * np.random.uniform(50, 500)

            all_stocks.append(
                {
                    "ID": stock_id,
                    "Symbol": ticker,
                    "Name": company_name,
                    "Sector": np.random.choice(list(sectors_stocks.keys())),
                    "Current Price": round(current_price, 2),
                    "52W Low": round(week_52_low, 2),
                    "52W High": round(week_52_high, 2),
                    "% From Low": round(from_low_pct, 1),
                    "% From High": round(from_high_pct, 1),
                    "Market Cap (B)": round(market_cap / 1000, 2),
                    "Volume (M)": round(np.random.uniform(1, 200), 1),
                }
            )
            stock_id += 1

    return pd.DataFrame(all_stocks)


# Quick test if run directly
if __name__ == "__main__":
    df = generate_stock_universe()
    print(f"Generated {len(df)} stocks")
    print("\nSample with names:")
    sample = df[["Symbol", "Name", "Sector", "Current Price"]].head(10)
    for _, row in sample.iterrows():
        print(
            f"{row['Symbol']}: {row['Name']} ({row['Sector']}) - ${row['Current Price']}"
        )
