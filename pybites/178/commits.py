import os
from collections import Counter
from datetime import datetime
from typing import Tuple, Union
from urllib.request import urlretrieve

from dateutil.parser import parse

commits = os.path.join(os.getenv("TMP", "/tmp"), "commits")
urlretrieve("https://bites-data.s3.us-east-2.amazonaws.com/git_log_stat.out", commits)

# you can use this constant as key to the yyyymm:count dict
YEAR_MONTH = "{y}-{m:02d}"


def parse_date(date: str) -> datetime:
    date = date[date.find(":") + 1 :].strip()
    return parse(date)


def parse_changes(changes: str) -> int:
    changed = changes.split(",")
    insertions = int(changed[1].strip().split(" ")[0])
    deletions = 0
    if len(changed) > 2:
        deletions = int(changed[2].strip().split(" ")[0])
    return insertions + deletions


def get_min_max_amount_of_commits(
    commit_log: str = commits, year: Union[int, None] = None
) -> Tuple[str, str]:
    """
    Calculate the amount of inserts / deletes per month from the
    provided commit log.

    Takes optional year arg, if provided only look at lines for
    that year, if not, use the entire file.

    Returns a tuple of (least_active_month, most_active_month)
    """
    with open(commit_log) as f:
        lines = f.readlines()

    counter = Counter()

    for line in lines:
        date, changes = line.split("|")
        date = parse_date(date)

        if year is not None and date.year != year:
            continue

        month = YEAR_MONTH.format(y=date.year, m=date.month)
        changes = parse_changes(changes)
        counter[month] += changes

    return counter.most_common()[-1][0], counter.most_common()[0][0]


get_min_max_amount_of_commits()
