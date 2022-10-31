from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    """Generate a special PyBites date every 100 days.
       See the Bite description for more info"""
    days = 100
    while True:
        yield PYBITES_BORN + timedelta(days=days)
        days += 100
