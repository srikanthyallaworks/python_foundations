from dataclasses import dataclass
from enum import Enum
from typing import Tuple
import random
from itertools import tee
from collections import defaultdict
import time
import os
from cards import Suites,Suite,Color,Cards,Hands,HandRank


this_directory = os.path.dirname(__file__)
parent_directory = os.path.dirname(this_directory)
data_file = os.path.join(parent_directory, '_data/p054_poker.txt')

print('\n\n\n')

p1_victory_count=0
for line in open(data_file):
    chars = line.strip().split(' ')

    hand_1 =  {Cards.from_chars(s) for s in chars[:5]}
    hand_2 =  {Cards.from_chars(s) for s in chars[5:]}

    winner='Player 2'
    if Hands.get_hand_value(hand_1) >Hands.get_hand_value(hand_2):
        p1_victory_count+=1
        winner = 'Player 1'

    print(f'{hand_1} x {hand_2} Winner: {winner} !')

print(f'\n{p1_victory_count} wins for P1')

