import os
import urllib.request
from collections import defaultdict

TMP = os.getenv("TMP", "/tmp")
DATA = "safari.logs"
SAFARI_LOGS = os.path.join(TMP, DATA)
PY_BOOK, OTHER_BOOK = "🐍", "."

urllib.request.urlretrieve(
    f"https://bites-data.s3.us-east-2.amazonaws.com/{DATA}", SAFARI_LOGS
)

chart = defaultdict(str)


def create_chart():

    lines = (line.strip() for line in open(SAFARI_LOGS))

    while True:
        try:
            book_line = next(lines)
            action_line = next(lines)
        except StopIteration:
            break

        if "skipping" in action_line:
            continue

        date = book_line.split()[0]
        book = PY_BOOK if "python" in book_line.lower() else OTHER_BOOK
        chart[date] += book

    for date, books in sorted(chart.items()):
        print(f"{date} {books}")
