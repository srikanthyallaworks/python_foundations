from abc import ABCMeta
from dataclasses import dataclass
from enum import Enum
from typing import Tuple, Literal
from custom_iter_tools import pairwise, groupby


class Color(Enum):
    Unknown=0
    Red=1
    Black=2
    
@dataclass(frozen=True)
class CardValue():
    symbol:str
    value:int


class CardValues:
    _symbols=('2','3','4','5','6','7','8','9','10','J','Q','K','A')
    _lookup={s:CardValue(s,i+2) for i,s in enumerate(_symbols)}

    @classmethod
    def from_string(cls,value:str)->CardValue:
        return CardValues._lookup[value]

    @classmethod
    def get_all(cls):
        return CardValues._lookup.values()

SuiteIdentifier=Literal['♠','♥','♦','♣']

@dataclass(frozen=True)
class Suite():
  name:str
  symbol:SuiteIdentifier
  color:Color

@dataclass(frozen=True,init=False)
class Suites():
  spades=Suite('Spades','♠',Color.Black)
  hearts=Suite('Hearts','♥',Color.Red)
  diamonds=Suite('Diamonds','♦',Color.Red)
  clubs=Suite('Clubs','♣',Color.Black)
  all=(clubs,diamonds,hearts,spades)
  _symbol_lookup={s.symbol:s for s in all}

  @staticmethod
  def get_all():
      return list(Suites.all)

  @staticmethod
  def from_string(value:SuiteIdentifier)->Suite:
      return Suites._symbol_lookup[value]



@dataclass(frozen=True)
class Card():
    suite:Suite
    value:CardValue

    def __str__(self):
        return self.suite.symbol + self.value.symbol

    def __repr__(self):
        return self.suite.symbol + self.value.symbol


@dataclass(frozen=True,init=False)
class Cards():
  _all = [Card(s,v) for s in Suites.get_all() for v in CardValues.get_all()]
  _repr_lookup = {repr(c):c for c in _all}

  @staticmethod
  def build_deck():
      return Cards._all[:]  

  @staticmethod
  def from_string(chars):
      return Cards._repr_lookup[chars]

Hand = Tuple[Card,Card,Card,Card,Card]



class HandRank(Enum):
    HighCard=0
    Pair=1
    TwoPair=2
    ThreeOfAKind=3
    Straight=4
    Flush=5
    FullHouse=6
    FourOfAKind=7
    StraightFlush=8


class Hands:

    def is_flush(cards:Hand)->bool:
        return 1 == len({c.suite for c in cards})

    def is_straight(cards:Hand)->bool:
        values = sorted([c.value.value for c in cards])
        for a,b in pairwise(values):
            if (a+1)!=b:
                return False
        return True

    def get_sets(cards:Hand):
        groups = [list(g) for k,g in groupby(cards,lambda c:c.value.value)]
        return [g for g in groups if len(g)>1]

    def get_hand_rank(cards:Hand):

        sets = Hands.get_sets(cards)
        if sets:
            if len(sets)>1:
                biggest_set = max([len(s) for s in sets])
                if biggest_set==3:
                    return HandRank.FullHouse
                return HandRank.TwoPair

            set_count = len(sets[0])
            if set_count==2:
                return HandRank.Pair
            if set_count==3:
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


