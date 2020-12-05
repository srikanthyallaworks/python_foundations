import os
try:
    from .deck import Deck
    from .hand import Hands
except:
    from deck import Deck
    from hand import Hands


def get_data_file():
    this_directory = os.path.dirname(__file__)
    parent_directory = os.path.dirname(this_directory)
    return os.path.join(parent_directory, '_data/p054_poker.txt')

def play(data_file):
    print('\n\n\n')

    p1_victory_count=0
    for line in open(data_file):
        chars = line.strip().split(' ')

        hand_1 =  {Deck.from_chars(s) for s in chars[:5]}
        hand_2 =  {Deck.from_chars(s) for s in chars[5:]}

        winner='Player 2'
        if Hands.get_hand_value(hand_1) >Hands.get_hand_value(hand_2):
            p1_victory_count+=1
            winner = 'Player 1'

        print(f'{hand_1} x {hand_2} Winner: {winner} !')

    print(f'\n{p1_victory_count} wins for P1')


def main():
    data_file = get_data_file()
    play(data_file)


if __name__=='__main__':
    main()
