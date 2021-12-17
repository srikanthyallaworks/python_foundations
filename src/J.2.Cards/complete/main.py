import os
try:
    from .deck import Deck
    from .hand import Hands
except:
    from deck import Deck
    from hand import Hands


def get_data_file():
    """Gets the path to the file containing poker hands

    Returns:
        str: Absolute path of the data file
    """
    this_directory = os.path.dirname(__file__)
    parent_directory = os.path.dirname(this_directory)
    return os.path.join(parent_directory, '_data/p054_poker.txt')


def get_euler59_solution(data_file):

    victories={
        'p1':0,
        'p2':0
    }

    for line in open(data_file):
        chars = line.strip().split(' ')

        hand_1 =  tuple((Deck.from_chars(s) for s in chars[:5]))
        hand_2 =  {Deck.from_chars(s) for s in chars[5:]}

        if Hands.get_hand_value(hand_1) >Hands.get_hand_value(hand_2):
            victories['p1']+=1
        else:
            victories['p2']+=1

    return victories


if __name__=='__main__':
    data_file = get_data_file()
    victories = get_euler59_solution(data_file)
    print(f'Player 1: {victories["p1"]} wins')
    print(f'Player 2: {victories["p2"]} wins')
