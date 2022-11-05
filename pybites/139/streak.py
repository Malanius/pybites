from datetime import datetime, timedelta, date
import re

TODAY = date(2018, 11, 12)


def extract_dates(data):
    """Extract unique dates from DB table representation as shown in Bite"""
    dates = set()
    for line in data.splitlines():
        match = re.search(r"\d{4}-\d{2}-\d{2}", line)
        if match:
            dates.add(datetime.strptime(match.group(), "%Y-%m-%d").date())
    return sorted(dates, reverse=True)


def calculate_streak(dates):
    """Receives sequence (set) of dates and returns number of days
    on coding streak.

    Note that a coding streak is defined as consecutive days coded
    since yesterday, because today is not over yet, however if today
    was coded, it counts too of course.

    So as today is 12th of Nov, having dates 11th/10th/9th of Nov in
    the table makes for a 3 days coding streak.

    See the tests for more examples that will be used to pass your code.
    """
    yesterday = TODAY - timedelta(days=1)
    streak = 0
    for date in dates:
        if date == TODAY or date == yesterday:
            streak += 1
            yesterday = date - timedelta(days=1)
        else:
            break
    return streak
