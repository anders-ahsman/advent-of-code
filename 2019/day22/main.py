import sys

def read_input():
    shuffles = [line.rstrip() for line in sys.stdin]
    return shuffles

def part1(shuffles):
    deck = list(range(10007))
    for shuffle in shuffles:
        if 'deal with increment' in shuffle:
            increment = int(shuffle.split(' ')[-1])
            deck = deal_with_increment(deck, increment)
        elif 'cut' in shuffle:
            count = int(shuffle.split(' ')[-1])
            deck = cut(deck, count)
        elif 'deal into new stack' == shuffle:
            deck = deal_into_new_stack(deck)
        else:
            raise Exception(f'Unknown shuffle {shuffle}')

    print('Part 1:', deck.index(2019))

def cut(deck, count):
    return deck[count:] + deck[:count]

def deal_into_new_stack(deck):
    deck.reverse()
    return deck

def deal_with_increment(deck, increment):
    deck_size = len(deck)
    pos_table = 0
    temp = {}
    for pos_deck in range(deck_size):
        if pos_deck in temp:
            card_to_place = temp[pos_deck]
            del(temp[pos_deck])
        else:
            card_to_place = deck[pos_deck]

        if card_to_place != deck[pos_table]:
            temp[pos_table] = deck[pos_table]
            deck[pos_table] = card_to_place

        pos_table = (pos_table + increment) % deck_size
    return deck

if __name__ == '__main__':
    shuffles = read_input()
    part1(shuffles)