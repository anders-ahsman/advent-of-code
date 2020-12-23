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
    p1, p2, p1_won = combat(player1, player2)
    return get_total(p1) if p1_won else get_total(p2)


def part2(player1, player2):
    p1, p2, p1_won = combat(player1, player2, recursive=True)
    return get_total(p1) if p1_won else get_total(p2)


def get_total(player):
    return sum(player.pop() * i for i in range(1, len(player) + 1))


def combat(player1, player2, recursive=False):
    seen = set()
    p1, p2 = player1.copy(), player2.copy()
    while len(p1) > 0 and len(p2) > 0:
        card_combo = str(p1) + str(p2)
        if card_combo in seen:
            p1_won = True
            return p1, p2, p1_won
        seen.add(card_combo)

        card1, card2 = p1.popleft(), p2.popleft()
        if recursive:
            if len(p1) >= card1 and len(p2) >= card2:
                p1_sub = deque(list(p1)[:card1])
                p2_sub = deque(list(p2)[:card2])
                _, _, p1_won = combat(p1_sub, p2_sub, recursive=True)
                if p1_won:
                    p1.extend([card1, card2])
                else:
                    p2.extend([card2, card1])
            else:
                if card1 > card2:
                    p1.extend([card1, card2])
                else:
                    p2.extend([card2, card1])
        else:
            if card1 > card2:
                p1.extend([card1, card2])
            else:
                p2.extend([card2, card1])
    p1_won = len(p1) > 0
    return p1, p2, p1_won


if __name__ == '__main__':
    player1, player2 = read_input()
    print(f'Part 1: {part1(player1, player2)}')
    print(f'Part 2: {part2(player1, player2)}')
