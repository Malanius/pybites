ASIN_DP = "/dp/"


def generate_affiliation_link(url: str) -> str:
    print(url)
    asin_start = url.find(ASIN_DP)
    asin_end = url.find("/", asin_start + len(ASIN_DP))
    if asin_end == -1:
        asin_end = len(url)
    asin = url[asin_start:asin_end]
    print(asin)
    return f"http://www.amazon.com{asin}/?tag=pyb0f-20"
