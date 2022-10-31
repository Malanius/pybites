SCORES = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
RANKS = "white yellow orange green blue brown black paneled red".split()
BELTS = dict(zip(SCORES, RANKS))


class NinjaBelt:
    def __init__(self, score=0):
        self._score = score
        self._last_earned_belt = None

    def _get_belt(self, new_score):
        """Might be a useful helper"""
        for score in reversed(SCORES):
            if new_score >= score:
                return BELTS[score]

    def _get_score(self):
        return self._score

    def _set_score(self, new_score):
        """Update score and last earned belt"""
        if type(new_score) != int:
            raise ValueError("Score takes an int")

        if new_score < self._score:
            raise ValueError("Cannot lower score")

        self._score = new_score

        belt_for_score = self._get_belt(new_score)
        if belt_for_score != self._last_earned_belt:
            self._last_earned_belt = belt_for_score
            print(
                f"Congrats, you earned {self._score} points obtaining the PyBites Ninja {belt_for_score.title()} Belt"
            )
        else:
            print(f"Set new score to {self._score}")

    score = property(_get_score, _set_score)
