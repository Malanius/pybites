from typing import List


NAMES = [
    "arnold schwarzenegger",
    "alec baldwin",
    "bob belderbos",
    "julian sequeira",
    "sandra bullock",
    "keanu reeves",
    "julbob pybites",
    "bob belderbos",
    "julian sequeira",
    "al pacino",
    "brad pitt",
    "matt damon",
    "brad pitt",
]


def dedup_and_title_case_names(names: List[str]) -> List[str]:
    """Should return a list of title cased names,
    each name appears only once"""
    deduped = list(set(names))
    return [name.title() for name in deduped]


def sort_by_surname_desc(names: List[str]) -> List[str]:
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    return sorted(names, key=lambda name: name.split(" ")[1], reverse=True)


def shortest_first_name(names: List[str]) -> str:
    """Returns the shortest first name (str).
    You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    shortest = "a" * 200
    for name in names:
        first_name = name.split(" ")[0]
        if len(first_name) < len(shortest):
            shortest = first_name
    return shortest
