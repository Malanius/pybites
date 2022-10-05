from collections import namedtuple
from enum import Enum
from typing import Sequence

Suit = Enum("Suit", list("SHDC"))
Rank = Enum("Rank", list("AKQJT98765432"))
Card = namedtuple("Card", ["suit", "rank"])

HCP = {Rank.A: 4, Rank.K: 3, Rank.Q: 2, Rank.J: 1}
SSP = {2: 1, 1: 2, 0: 3}  # cards in a suit -> short suit points


class BridgeHand:
    def __init__(self, cards: Sequence[Card]):
        """
        Process and store the sequence of Card objects passed in input.
        Raise TypeError if not a sequence
        Raise ValueError if any element of the sequence is not an instance
        of Card, or if the number of elements is not 13
        """
        if not isinstance(cards, Sequence):
            raise TypeError("cards must be a sequence")

        if len(cards) != 13:
            raise ValueError("cards must have 13 elements")

        if not all(isinstance(card, Card) for card in cards):
            raise ValueError("cards must contain only Card objects")

        self.cards = cards

    def __str__(self) -> str:
        """
        Return a string representing this hand, in the following format:
        "S:AK3 H:T987 D:KJ98 C:QJ"
        List the suits in SHDC order, and the cards within each suit in
        AKQJT..2 order.
        Separate the suit symbol from its cards with a colon, and
        the suits with a single space.
        Note that a "10" should be represented with a capital 'T'
        """
        return " ".join(
            f"{suit.name}:{''.join(card.rank.name for card in cards)}"
            for suit, cards in self._get_suit_cards().items()
            if cards
        )

    def _get_suit_cards(self):
        return {
            suit: sorted(
                (card for card in self.cards if card.suit == suit),
                key=lambda card: card.rank.value,
            )
            for suit in Suit
        }

    @property
    def hcp(self) -> int:
        """Return the number of high card points contained in this hand"""
        return sum(HCP.get(card.rank, 0) for card in self.cards)

    def _get_suit_multiples(self, n):
        return sum(len(cards) == n for cards in self._get_suit_cards().values())

    @property
    def doubletons(self) -> int:
        """Return the number of doubletons contained in this hand"""
        return self._get_suit_multiples(2)

    @property
    def singletons(self) -> int:
        """Return the number of singletons contained in this hand"""
        return self._get_suit_multiples(1)

    @property
    def voids(self) -> int:
        """Return the number of voids (missing suits) contained in
        this hand
        """
        return self._get_suit_multiples(0)

    @property
    def ssp(self) -> int:
        """Return the number of short suit points in this hand.
        Doubletons are worth one point, singletons two points,
        voids 3 points
        """
        return SSP[2] * self.doubletons + SSP[1] * self.singletons + SSP[0] * self.voids

    @property
    def total_points(self) -> int:
        """Return the total points (hcp and ssp) contained in this hand"""
        return self.hcp + self.ssp

    def _calculate_single_card_ltc(self, cards):
        if cards[0].rank == Rank.A:
            return 0
        return 1

    def _calculate_two_card_ltc(self, cards):
        if cards[0].rank == Rank.A and cards[1].rank == Rank.K:
            return 0
        if cards[0].rank == Rank.A or cards[0].rank == Rank.K:
            return 1
        return 2

    def _calculate_three_card_ltc(self, cards):
        ranks = [card.rank for card in cards]
        if ranks == [Rank.A, Rank.K, Rank.Q]:
            return 0

        if (
            ranks[:2] == [Rank.A, Rank.K]
            or ranks[:2] == [Rank.A, Rank.Q]
            or ranks[:2] == [Rank.K, Rank.Q]
        ):
            print(ranks[:2])
            return 1

        if ranks[0] == Rank.A or ranks[0] == Rank.K or ranks[0] == Rank.Q:
            return 2

        # all cards are losers
        return 3

    def _calculate_suit_ltc(self, suit):
        """Return theloosing trick count for a given suit

        - a void = 0 losing tricks.
        - a singleton other than an A = 1 losing trick.
        - a doubleton AK = 0; Ax or Kx = 1; Qx or xx = 2 losing tricks.
        - a three card suit AKQ = 0; AKx, AQx or KQx = 1 losing trick.
        - a three card suit Axx, Kxx or Qxx = 2; xxx = 3 losing tricks.
        """
        top_three_cards = self._get_suit_cards()[suit][:3]

        if len(top_three_cards) == 0:
            return 0

        if len(top_three_cards) == 1:
            return self._calculate_single_card_ltc(top_three_cards)

        if len(top_three_cards) == 2:
            return self._calculate_two_card_ltc(top_three_cards)

        return self._calculate_three_card_ltc(top_three_cards)

    @property
    def ltc(self) -> int:
        """Return the losing trick count for this hand - see bite description
        for the procedure
        """
        return sum([self._calculate_suit_ltc(suit) for suit in Suit])
