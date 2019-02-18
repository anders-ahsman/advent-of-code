import re
from collections import defaultdict

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

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, node):
        node.next = node
        node.prev = node
        self.cur_node = node

    def add_node(self, new_node):
        # Insert two positions right of current and move current to inserted
        new_node.next = self.cur_node.next.next
        new_node.prev = self.cur_node.next
        self.cur_node.next.next.prev = new_node
        self.cur_node.next.next = new_node
        self.cur_node = new_node

    def remove_at_pos(self, n):
        clockwise = n > 0
        for _ in range(abs(n)):
            self.cur_node = self.cur_node.next if clockwise else self.cur_node.prev

        removed_value = self.cur_node.value

        self.cur_node.prev.next = self.cur_node.next
        self.cur_node.next.prev = self.cur_node.prev
        self.cur_node = self.cur_node.next

        return removed_value

def play_marble(player_count, last_marble):
    score = defaultdict(int)
    circle = DoublyLinkedList(Node(0))
    player = 0
    for marble in range(1, last_marble + 1):
        player += 1
        if player > player_count:
            player = 1
        if marble % 23 == 0:
            score[player] += marble + circle.remove_at_pos(-7)
        else:
            circle.add_node(Node(marble))

    high_score = max(score.values())
    return high_score

if __name__ == '__main__':
    part1()
    part2()