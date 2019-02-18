import re

def part1():
    players, last_marble = read_input()
    play_marble(players, last_marble)

def read_input():
    with open('input_test.txt', 'r') as f:
        row = f.readline()
        m = re.match(r'(\d+) players; last marble is worth (\d+) points', row)
        return int(m.group(1)), int(m.group(2))

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class DoublyLinkedList:
    def __init__(self, initial_node):
        initial_node.next = initial_node
        self.cur_node = initial_node

    def __repr__(self):
        # Go to node 0
        node = self.cur_node
        while node.value != 0:
            node = node.next
        values = [node.value]

        # Iterate until at node 0 again
        node = node.next
        while node.value != 0:
            values.append(node.value)
            # representation += str(node.value) + ' '
            node = node.next

        representation = ''
        for v in values:
            if v == self.cur_node.value:
                representation += '(%2d) ' % v
            else:
                representation += ' %2d  ' % v
        return representation

    def add_node(self, new_node):
        new_node.next = self.cur_node.next.next
        self.cur_node.next.next = new_node
        self.cur_node = new_node

def play_marble(players, last_marble):
    n = Node(0)
    dll = DoublyLinkedList(n)
    for i in range(1, 22):
        dll.add_node(Node(i))
        print(dll)

if __name__ == '__main__':
    part1()