import csv
import os
import re
from pathlib import Path
from urllib.request import urlretrieve

data = "https://bites-data.s3.us-east-2.amazonaws.com/bite_levels.csv"
TMP = Path(os.getenv("TMP", "/tmp"))
stats = TMP / "bites.csv"

if not stats.exists():
    urlretrieve(data, stats)


def get_most_complex_bites(N=10, stats=stats):
    """Parse the bites.csv file (= stats variable passed in), see example
    output in the Bite description.
    Return a list of Bite IDs (int or str values are fine) of the N
    most complex Bites.
    """
    with open(stats, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f, delimiter=";")
        bites = [row for row in reader]
    bites = [bite for bite in bites if bite["Difficulty"] != "None"]
    bites.sort(key=lambda x: float(x["Difficulty"]), reverse=True)
    return [re.search(r"Bite (\d+).", bite["Bite"]).group(1) for bite in bites[:N]]


if __name__ == "__main__":
    res = get_most_complex_bites()
    print(res)
