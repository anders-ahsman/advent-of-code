import sys

def read_input():
    shuffles = [line.rstrip() for line in sys.stdin]
    return shuffles

def part1(shuffles):
    cards = list(range(10007))
    for shuffle in shuffles:
        if 'deal with increment' in shuffle:
            increment = int(shuffle.split(' ')[-1])
            cards = deal_with_increment(cards, increment)
        elif 'cut' in shuffle:
            count = int(shuffle.split(' ')[-1])
            cards = cut(cards, count)
        elif 'deal into new stack' == shuffle:
            cards = deal_into_new_stack(cards)
        else:
            raise Exception(f'Unknown shuffle {shuffle}')

    print('Part 1:', cards.index(2019))

def cut(cards, count):
    shuffled = cards[count:] + cards[:count]
    return shuffled

def deal_into_new_stack(cards):
    shuffled = cards[:]
    shuffled.reverse()
    return shuffled

def deal_with_increment(cards, increment):
    card_count = len(cards)
    shuffled = [None] * card_count
    pos = 0
    while cards:
        shuffled[pos] = cards[0]
        cards = cards[1:]
        pos += increment
        pos = pos % card_count
    return shuffled

if __name__ == '__main__':
    shuffles = read_input()
    part1(shuffles)