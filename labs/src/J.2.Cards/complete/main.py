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


def play():
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


def show_info():
    def get_hands():
        for line in open(data_file):
            yield  {Cards.from_chars(s) for s in line[:14]}
            yield  {Cards.from_chars(s) for s in line[14:]}


    def get_hand_infos():
        for hand in get_hands():
            yield hand,Hands.get_hand_value(hand),Hands.get_hand_rank(hand)

    for info in sorted(get_hand_infos(),key=lambda h:h[1]):
        print('\n\n')
        print(info[0])
        print(info[1])
        print(info[2])

def do_stuff():
    deck = Cards.build_deck()

    print('\n\n')
    while True:

        deal = random.sample(deck,10)
        hand_a=deal[:5]
        hand_b=deal[5:]

        rank_a=Hands.get_hand_rank(hand_a)
        value_a=Hands.get_hand_value(hand_a)
        
        value_b=Hands.get_hand_value(hand_b)
        rank_b=Hands.get_hand_rank(hand_b)

        # if value_b==value_a and rank_a != rank_b:
        #     print(f'\n\na:{hand_a} b:{hand_b}')    
            
        if rank_a > HandRank.Straight and rank_a == rank_b:
            print(f'a:{hand_a}        {value_a}')
            print(f'b:{hand_b}        {value_b}\n\n')
        

play()
