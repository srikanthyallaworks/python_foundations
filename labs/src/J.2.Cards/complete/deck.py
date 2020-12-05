from dataclasses import dataclass
from enum import IntEnum,Enum
from typing import Tuple, Literal



class Color(Enum):
    Unknown=0
    Red=1
    Black=2



@dataclass(frozen=True)
class CardRank:
    symbol:str
    value:int
    @property
    def character(self):
        if self.symbol=='10':
            return 'T'
        return self.symbol


#@dataclass(frozen=True)
class CardRanks:
    _symbols=('2','3','4','5','6','7','8','9','10','J','Q','K','A')
    _lookup={s:CardRank(s,i+2) for i,s in enumerate(_symbols)}

    def from_string(value:str)->CardRank:
        return CardRanks._lookup[value]

    def get_all():
        return CardRanks._lookup.values()



SuiteIdentifier=Literal['♠','♥','♦','♣']



@dataclass(frozen=True)
class Suite:
  name:str
  symbol:SuiteIdentifier
  color:Color
  @property
  def character(self):
      return self.name[0]





@dataclass(frozen=True)
class Card:
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
class Suites:
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






@dataclass(frozen=True,init=False)
class Deck:
  _all = [Card(s,v) for s in Suites.get_all() for v in CardRanks.get_all()]
  _repr_lookup = {repr(c):c for c in _all}
  _chars_lookup = {c.chars:c for c in _all}  

  def build_deck():
      return Deck._all[:]  

  @staticmethod
  def from_string(chars):
      return Deck._repr_lookup[chars]

  @staticmethod
  def from_chars(chars):
      return Deck._chars_lookup[chars]


