from enum import IntEnum
from typing import Tuple

from deck import Card, Deck
from custom_iter_tools import pairwise, groupby


Hand = Tuple[Card, Card, Card, Card]


class HandRank(IntEnum):
    HighCard = 0
    Pair = 1
    TwoPair = 2
    ThreeOfAKind = 3
    Straight = 4
    Flush = 5
    FullHouse = 6
    FourOfAKind = 7
    StraightFlush = 8


class Hands:
    @staticmethod
    def is_flush(cards: Hand) -> bool:
        return 1 == len({c.suite for c in cards})

    @staticmethod
    def is_straight(cards: Hand) -> bool:
        values = sorted([c.rank.value for c in cards])
        for a, b in pairwise(values):
            if (a + 1) != b:
                return False
        return True

    @staticmethod
    def get_sets(cards: Hand):
        groups = [list(g) for k, g in groupby(cards, lambda c: c.rank.value)]
        return [g for g in groups if len(g) > 1]

    @staticmethod
    def from_string(reprs: str) -> Hand:
        return {Deck.from_string(s) for s in reprs.split(" ")}

    @staticmethod
    def from_chars_string(reprs: str) -> Hand:
        return {Deck.from_chars(s) for s in reprs.split(" ")}

    # TODO: Consider using struct.pack
    @staticmethod
    def get_hand_value(cards: Hand):
        rank = Hands.get_hand_rank(cards)
        value = rank.value << 48
        tie_breaker_cards = []

        if rank in [HandRank.ThreeOfAKind, HandRank.Pair, HandRank.FourOfAKind]:
            tuple_value = Hands.get_sets(cards)[0][0].rank
            tie_breaker_cards = sorted(
                [c.rank.value for c in cards if c.rank != tuple_value]
            )
            tie_breaker_cards.append(tuple_value.value)

        elif rank == HandRank.FullHouse:
            sets = Hands.get_sets(cards)
            triple = sets[0] if len(sets[0]) == 3 else sets[1]
            tie_breaker_cards = [triple[0].rank.value]

        elif rank == HandRank.TwoPair:
            pairs = [s[0].rank.value for s in Hands.get_sets(cards)]
            tie_breaker_cards = [
                c.rank.value for c in cards if c.rank.value not in pairs
            ]
            tie_breaker_cards += sorted(pairs)

        else:
            tie_breaker_cards = sorted([c.rank.value for c in cards])

        for i, v in enumerate(tie_breaker_cards):
            value |= v << (6 * i)

        return value

    @staticmethod
    def get_hand_rank(cards: Hand):
        sets = Hands.get_sets(cards)
        if sets:
            if len(sets) > 1:
                biggest_set = max([len(s) for s in sets])
                if biggest_set == 3:
                    return HandRank.FullHouse
                return HandRank.TwoPair

            set_count = len(sets[0])
            if set_count == 2:
                return HandRank.Pair
            if set_count == 3:
                return HandRank.ThreeOfAKind

            return HandRank.FourOfAKind

        straight = Hands.is_straight(cards)
        flush = Hands.is_flush(cards)

        if straight and flush:
            return HandRank.StraightFlush

        if straight:
            return HandRank.Straight

        if flush:
            return HandRank.Flush

        return HandRank.HighCard
