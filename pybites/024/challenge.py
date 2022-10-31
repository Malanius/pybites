from abc import ABC, abstractmethod
from typing import List


class Challenge(ABC):
    def __init__(self, number: int, title: str) -> None:
        self.number = number
        self.title = title

    @abstractmethod
    def pretty_title(self) -> str:
        pass

    @abstractmethod
    def verify(self, result: str) -> bool:
        pass


class BlogChallenge(Challenge):
    def __init__(self, number: int, title: str, merged_prs: List[int]) -> None:
        super().__init__(number, title)
        self.merged_prs = merged_prs

    @property
    def pretty_title(self) -> str:
        return f"PCC{self.number} - {self.title}"

    def verify(self, pr: int) -> bool:
        return pr in self.merged_prs


class BiteChallenge(Challenge):
    def __init__(self, number: int, title: str, result: str) -> None:
        super().__init__(number, title)
        self.result = result

    @property
    def pretty_title(self) -> str:
        return f"Bite {self.number}. {self.title}"

    def verify(self, result: str) -> bool:
        return result == self.result
