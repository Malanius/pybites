from dataclasses import dataclass, field
from functools import total_ordering
from typing import List, Tuple

bites: List[int] = [283, 282, 281, 263, 255, 230, 216, 204, 197, 196, 195]
names: List[str] = [
    "snow",
    "natalia",
    "alex",
    "maquina",
    "maria",
    "tim",
    "kenneth",
    "fred",
    "james",
    "sara",
    "sam",
]


@dataclass
@total_ordering
class Ninja:
    """
    The Ninja class will have the following features:

    string: name
    integer: bites
    support <, >, and ==, based on bites
    print out in the following format: [469] bob
    """

    name: str
    bites: int

    def __lt__(self, other):
        return self.bites < other.bites

    def __eq__(self, __o: object) -> bool:
        return self.bites == __o.bites

    def __str__(self):
        return f"[{self.bites}] {self.name}"


@dataclass
class Rankings:
    """
    The Rankings class will have the following features:

    method: add() that adds a Ninja object to the rankings
    method: dump() that removes/dumps the lowest ranking Ninja from Rankings
    method: highest() returns the highest ranking Ninja, but it takes an optional
            count parameter indicating how many of the highest ranking Ninjas to return
    method: lowest(), the same as highest but returns the lowest ranking Ninjas, also
            supports an optional count parameter
    returns how many Ninjas are in Rankings when len() is called on it
    method: pair_up(), pairs up study partners, takes an optional count
            parameter indicating how many Ninjas to pair up
    returns List containing tuples of the paired up Ninja objects
    """

    ninjas: List[Ninja] = field(default_factory=lambda: [])

    def __len__(self):
        return len(self.ninjas)

    def add(self, ninja: Ninja):
        self.ninjas.append(ninja)
        self.ninjas = sorted(self.ninjas, reverse=True, key=lambda x: x.bites)

    def dump(self) -> Ninja:
        return self.ninjas.pop()

    def highest(self, count: int = 1) -> List[Ninja]:
        return self.ninjas[:count]

    def lowest(self, count: int = 1) -> List[Ninja]:
        return self.ninjas[-count:][::-1]

    def pair_up(self, count: int = 3) -> List[Tuple[Ninja, Ninja]]:
        print(self.ninjas)
        high = self.highest(count)
        low = self.lowest(count)
        return list(zip(high, low))