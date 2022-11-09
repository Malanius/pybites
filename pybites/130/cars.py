from collections import Counter

import requests

CAR_DATA = "https://bites-data.s3.us-east-2.amazonaws.com/cars.json"

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(CAR_DATA).json()


# your turn:
def most_prolific_automaker(year: int) -> str:
    """Given year 'year' return the automaker that released
    the highest number of new car models"""
    models_per_automaker = Counter()
    for car in data:
        if car["year"] == year:
            models_per_automaker[car["automaker"]] += 1
    return models_per_automaker.most_common(1)[0][0]


def get_models(automaker: str, year: int) -> set:
    """Filter cars 'data' by 'automaker' and 'year',
    return a set of models (a 'set' to avoid duplicate models)"""
    return {
        car["model"]
        for car in data
        if car["automaker"] == automaker and car["year"] == year
    }
