import json
import re
from typing import Generator


def get_movie_data(files: list) -> list:
    """Parse movie json files into a list of dicts"""
    movies = []
    for file in files:
        with open(file) as f:
            movies.append(json.load(f))
    return movies


def get_single_comedy(movies: list) -> str:
    """return the movie with Comedy in Genres"""
    for movie in movies:
        if "Comedy" in movie["Genre"]:
            return movie["Title"]


def get_movie_nominations(movie: dict) -> int:
    """Helper to get a movies number of nominations"""
    nominations = re.findall(r"(\d+) nominations", movie["Awards"])
    print(nominations)
    return int(nominations[0]) if nominations else 0


def get_movie_most_nominations(movies: list) -> str:
    """Return the movie that had the most nominations"""
    return max(movies, key=get_movie_nominations)["Title"]


def get_movie_runtime(movie: dict) -> int:
    """Helper to get a movies runtime"""
    runtime = re.findall(r"(\d+) min", movie["Runtime"])
    return int(runtime[0]) if runtime else 0


def get_movie_longest_runtime(movies: list) -> str:
    """Return the movie that has the longest runtime"""
    return max(movies, key=get_movie_runtime)["Title"]
