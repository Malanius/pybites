from collections import Counter

import requests

STOCK_DATA = "https://bites-data.s3.us-east-2.amazonaws.com/stocks.json"

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(STOCK_DATA).json()


def _cap_str_to_mln_float(cap: str) -> float:
    """If cap = 'n/a' return 0, else:
    - strip off leading '$',
    - if 'M' in cap value, strip it off and return value as float,
    - if 'B', strip it off, multiply by 1,000 and return
      value as float"""
    if cap == "n/a":
        return 0

    cap = cap.strip("$")
    if "M" in cap:
        return float(cap.strip("M"))
    elif "B" in cap:
        return float(cap.strip("B")) * 1000

    raise ValueError("Invalid cap value")


def get_industry_cap(industry: str) -> float:
    """Return the sum of all cap values for given industry, use
    the _cap_str_to_mln_float to parse the cap values,
    return a float with 2 digit precision"""
    records_for_industry = [record for record in data if record["industry"] == industry]
    return round(
        sum(_cap_str_to_mln_float(record["cap"]) for record in records_for_industry), 2
    )


def get_stock_symbol_with_highest_cap() -> str:
    """Return the stock symbol (e.g. PACD) with the highest cap, use
    the _cap_str_to_mln_float to parse the cap values"""
    sorted_by_cap = sorted(
        data, key=lambda record: _cap_str_to_mln_float(record["cap"]), reverse=True
    )
    return sorted_by_cap[0]["symbol"]


def get_sectors_with_max_and_min_stocks():
    """Return a tuple of the sectors with most and least stocks,
    discard n/a"""
    sectors = [record["sector"] for record in data if record["sector"] != "n/a"]
    sector_counts = Counter(sectors)
    max_sector = sector_counts.most_common(1)[0][0]
    min_sector = sector_counts.most_common()[-1][0]
    return max_sector, min_sector
