from collections import namedtuple
from datetime import datetime

Transaction = namedtuple(
    "Transaction", "giver points date", defaults=(None, None, datetime.now())
)


class User:
    def __init__(self, name: str) -> None:
        self.name = name
        self._karma = 0
        self._transactions = []
        self._points = []
        self._fans = set()

    def __add__(self, transaction: Transaction) -> None:
        self._transactions.append(transaction)
        self._karma += transaction.points
        self._points.append(transaction.points)
        self._fans.add(transaction.giver.name)

    def __str__(self) -> str:
        fans_text = "fan" if len(self._fans) == 1 else "fans"
        return f"{self.name} has a karma of {self.karma} and {self.fans} {fans_text}"

    @property
    def karma(self) -> int:
        return self._karma

    @property
    def points(self) -> list:
        return [point for point in self._points]

    @property
    def fans(self) -> int:
        return len(self._fans)
