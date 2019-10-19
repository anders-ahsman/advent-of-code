import re
from collections import defaultdict, deque

def part1():
    players, last_marble = read_input()
    high_score = play_marble(players, last_marble)
    print('%d players; last marble is worth %d points: high score is %d'
        % (players, last_marble, high_score))
    return high_score

def part2():
    players, last_marble = read_input()
    last_marble *= 100
    high_score = play_marble(players, last_marble)
    print('%d players; last marble is worth %d points: high score is %d'
        % (players, last_marble, high_score))
    return high_score

def read_input():
    with open('input.txt', 'r') as f:
        row = f.readline()
        m = re.match(r'(\d+) players; last marble is worth (\d+) points', row)
        return int(m.group(1)), int(m.group(2))

def play_marble(player_count, last_marble):
    score = defaultdict(int)
    circle = deque([0])

    # Current position at right end of deque
    for marble in range(1, last_marble + 1):
        if marble % 23 == 0:
            circle.rotate(7)
            player = marble % player_count
            score[player] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)

    high_score = max(score.values())
    return high_score

if __name__ == '__main__':
    part1()
    part2()