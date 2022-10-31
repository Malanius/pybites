import itertools as it
from typing import List, Tuple


def friends_teams(
    friends: List[str], team_size: int = 2, order_does_matter: bool = False
) -> List[Tuple[str]]:
    if order_does_matter:
        return list(it.permutations(friends, team_size))
    return list(it.combinations(friends, team_size))
