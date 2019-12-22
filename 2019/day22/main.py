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
    shuffled = deck[count:] + deck[:count]
    return shuffled

def deal_into_new_stack(deck):
    deck.reverse()
    return deck

def deal_with_increment(deck, increment):
    deck_size = len(deck)
    shuffled = [None] * deck_size
    pos = 0
    while deck:
        shuffled[pos] = deck[0]
        deck = deck[1:]
        pos += increment
        pos = pos % deck_size
    return shuffled

if __name__ == '__main__':
    shuffles = read_input()
    part1(shuffles)