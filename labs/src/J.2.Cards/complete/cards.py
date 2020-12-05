from abc import ABCMeta
from dataclasses import dataclass
from enum import IntEnum,Enum
from typing import Tuple, Literal
from custom_iter_tools import pairwise, groupby


class Color(Enum):
    Unknown=0
    Red=1
    Black=2

@dataclass(frozen=True)
class CardRank():
    symbol:str
    value:int
    @property
    def character(self):
        if self.symbol=='10':
            return 'T'
        return self.symbol

class CardRanks:
    _symbols=('2','3','4','5','6','7','8','9','10','J','Q','K','A')
    _lookup={s:CardRank(s,i+2) for i,s in enumerate(_symbols)}

    def from_string(value:str)->CardRank:
        return CardRanks._lookup[value]

    def get_all():
        return CardRanks._lookup.values()

SuiteIdentifier=Literal['♠','♥','♦','♣']

@dataclass(frozen=True)
class Suite():
  name:str
  symbol:SuiteIdentifier
  color:Color
  @property
  def character(self):
      return self.name[0]

@dataclass(frozen=True,init=False)
class Suites():
  spades=Suite('Spades','♠',Color.Black)
  hearts=Suite('Hearts','♥',Color.Red)
  diamonds=Suite('Diamonds','♦',Color.Red)
  clubs=Suite('Clubs','♣',Color.Black)
  all=(clubs,diamonds,hearts,spades)

  _symbol_lookup={s.symbol:s for s in all}

  def get_all():
      return list(Suites.all)

  def from_symbol(value:SuiteIdentifier)->Suite:
      return Suites._symbol_lookup[value]





@dataclass(frozen=True)
class Card():
    suite:Suite
    rank:CardRank

    @property
    def chars(self):
        return self.rank.character + self.suite.character

    def __str__(self):
        return self.suite.symbol + self.rank.character

    def __repr__(self):
        return self.suite.symbol + self.rank.character


@dataclass(frozen=True,init=False)
class Cards():
  _all = [Card(s,v) for s in Suites.get_all() for v in CardRanks.get_all()]
  _repr_lookup = {repr(c):c for c in _all}
  _chars_lookup = {c.chars:c for c in _all}  

  @staticmethod
  def build_deck():
      return Cards._all[:]  

  @staticmethod
  def from_string(chars):
      return Cards._repr_lookup[chars]

  @staticmethod
  def from_chars(chars):
      return Cards._chars_lookup[chars]

Hand = Tuple[Card,Card,Card,Card,Card]



class HandRank(IntEnum):
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
        values = sorted([c.rank.value for c in cards])
        for a,b in pairwise(values):
            if (a+1)!=b:
                return False
        return True

    def get_sets(cards:Hand):
        groups = [list(g) for k,g in groupby(cards,lambda c:c.rank.value)]
        return [g for g in groups if len(g)>1]


    def from_string(reprs:str)->Hand:
        return {Cards.from_string(s) for s in reprs.split(' ')}

    def from_chars_string(reprs:str)->Hand:
        return {Cards.from_chars(s) for s in reprs.split(' ')}

    # TODO: Consider using struct.pack
    def get_hand_value(cards:Hand):
        rank = Hands.get_hand_rank(cards)
        value = rank.value << 48
        tie_breaker_cards=[]

        if rank in [HandRank.ThreeOfAKind,HandRank.Pair,HandRank.FourOfAKind]:
            tuple_value = Hands.get_sets(cards)[0][0].rank
            tie_breaker_cards=sorted([c.rank.value for c in cards if c.rank!=tuple_value])
            tie_breaker_cards.append(tuple_value.value)

        elif rank == HandRank.FullHouse:
            sets = Hands.get_sets(cards)
            triple = sets[0] if len(sets[0])==3 else sets[1]
            tie_breaker_cards = [triple[0].rank.value]

        elif rank == HandRank.TwoPair:
            pairs = [s[0].rank.value for s in Hands.get_sets(cards)]
            tie_breaker_cards = [c.rank.value for c in cards if c.rank.value not in pairs]
            tie_breaker_cards += sorted(pairs)
        
        else:
            tie_breaker_cards=sorted([c.rank.value for c in cards])

        for i,v in enumerate(tie_breaker_cards):
            value |= v << (6*i)

        return value 


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


