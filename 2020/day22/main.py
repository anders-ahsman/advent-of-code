from collections import deque
import sys


def read_input():
    player1, player2 = deque(), deque()
    player1_done = False
    for line in sys.stdin:
        line = line.rstrip()
        if 'Player' in line:
            continue
        if line == '':
            player1_done = True
            continue
        if player1_done:
            player2.append(int(line))
        else:
            player1.append(int(line))
    return player1, player2


def part1(player1, player2):
    while len(player1) > 0 and len(player2) > 0:
        card1, card2 = player1.popleft(), player2.popleft()
        if card1 > card2:
            player1.append(card1)
            player1.append(card2)
        else:
            player2.append(card2)
            player2.append(card1)
    return get_total(player1) if len(player1) > 0 else get_total(player2)


def get_total(player):
    return sum(player.pop() * i for i in range(1, len(player) + 1))


if __name__ == '__main__':
    player1, player2 = read_input()
    print(f'Part 1: {part1(player1, player2)}')
