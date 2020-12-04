from dataclasses import dataclass
from enum import Enum
from typing import Tuple
import random
from itertools import tee
from collections import defaultdict
import time


class Color(Enum):
    Unknown=0
    Red=1
    Black=2

value_symbols = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    
@dataclass(frozen=True)
class CardValue():
    symbol:str
    value:int



@dataclass(frozen=True)
class Suite():
  name:str
  symbol:str
  color:Color

suites=(
    Suite('Spades','♠',Color.Black),
    Suite('Hearts','♥',Color.Red),
    Suite('Diamonds','♦',Color.Red),
    Suite('Clubs','♣',Color.Black)
)

@dataclass(frozen=True)
class Card():
    suite:Suite
    value:CardValue

    def __str__(self):
        return self.suite.symbol + self.value.symbol

    def __repr__(self):
        return self.suite.symbol + self.value.symbol


@dataclass(frozen=True)
class Hand():
    cards:Tuple[Card]


card_values = [CardValue(s,i+2) for i,s in enumerate(value_symbols)]

def get_deck():
    return [Card(s,v) for s in suites for v in card_values]


players=['Jim','Hazel','Denny','Pierre','Kim','Ellen']


def has_flush(cards):
    return 1 == len({c.suite for c in cards})


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def has_straight(cards):
    values = sorted([c.value.value for c in cards])
    for a,b in pairwise(values):
        if (a+1)!=b:
            return False
    return True

def get_sets(cards):
    groups = [list(g) for k,g in groupby(cards,lambda c:c.value.value)]
    return [g for g in groups if len(g)>1]


class HandType(Enum):
    HighCard=0
    Pair=1
    TwoPair=2
    ThreeOfAKind=3
    Straight=4
    Flush=5
    FullHouse=6
    FourOfAKind=7
    StraightFlush=8





def groupby(items,get_key):
    groups = defaultdict(lambda:[])
    for item in items:
        groups[get_key(item)].append(item)
    return groups.items()
    


def get_hand_value(cards):

    sets = get_sets(cards)
    if sets:
        if len(sets)>1:
            biggest_set = max([len(s) for s in sets])
            if biggest_set==3:
                return HandType.FullHouse
            return HandType.TwoPair

        set_count = len(sets[0])
        if set_count==2:
            return HandType.Pair
        if set_count==3:
            return HandType.ThreeOfAKind            

        return HandType.FourOfAKind

    straight = has_straight(cards)
    flush = has_flush(cards)

    if straight and flush:
        return HandType.StraightFlush

    if straight:
        return HandType.Straight

    if flush:
        return HandType.Flush

    return HandType.HighCard


def get_hand_type(cards):

    sets = get_sets(cards)
    if sets:
        if len(sets)>1:
            biggest_set = max([len(s) for s in sets])
            if biggest_set==3:
                return HandType.FullHouse
            return HandType.TwoPair

        set_count = len(sets[0])
        if set_count==2:
            return HandType.Pair
        if set_count==3:
            return HandType.ThreeOfAKind            

        return HandType.FourOfAKind

    straight = has_straight(cards)
    flush = has_flush(cards)

    if straight and flush:
        return HandType.StraightFlush

    if straight:
        return HandType.Straight

    if flush:
        return HandType.Flush

    return HandType.HighCard


def calculate_odds():
    rounds = 1500000
    hand_counts = [0 for item in HandType]
    deck = get_deck()

    for r in range(rounds):
       hand = random.sample(deck,5)
       hand_type = get_hand_type(hand)
       hand_counts[hand_type.value]+=1

    for type in HandType:
        print(f'{type.name} {hand_counts[type.value]/rounds*100}')

def play_hand():
    deck = get_deck()
    random.shuffle(deck)
    for p in players:
        hand,deck=deck[0:5],deck[5:]
        print(f'{p} gets {hand} - {get_hand_type(hand)}')


#start = time.time()
#calculate_odds()              
#print(f"\nElapsed: {time.time() - start}")
