import re
from itertools import zip_longest


def get_weekdays(calendar_output: str) -> dict:
    """Receives a multiline Unix cal output and returns a mapping (dict) where
    keys are int days and values are the 2 letter weekdays (Su Mo Tu ...)"""
    lines = calendar_output.splitlines()[1:]  # skip first line with month and year
    weekdays = lines[0].split()
    print(weekdays)
    day_tuples = []
    for line in lines[1:]:
        days = re.findall(r"(.{2}\s?)", line)
        print(days)
        day_tuples.extend(list(zip_longest(days, weekdays, fillvalue="")))

    print(day_tuples)
    return {int(day): weekday for day, weekday in day_tuples if day.strip()}
