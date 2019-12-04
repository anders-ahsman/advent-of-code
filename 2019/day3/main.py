import math
import sys

def read_input():
    wires = []
    for line in sys.stdin:
        wire = [x.replace('\n', '').replace('\r', '') for x in line.split(',')]
        wires.append(wire)
    return wires

def main(wires):
    size = 20000
    board = []
    for _ in range(size):
        board.append([0] * size)

    pos_start = int(math.floor(size / 2))
    for wire in wires:
        pos_x = pos_start
        pos_y = pos_start
        board[pos_y][pos_x] = 1
        visted = set()
        for op in wire:
            distance = int(op[1:])
            if op[0] == 'L':
                for x in range(pos_x - 1, pos_x - distance - 1, -1):
                    point = (x, pos_y)
                    if not point in visted:
                        board[pos_y][x] += 1
                        visted.add(point)
                pos_x -= distance
            elif op[0] == 'R':
                for x in range(pos_x + 1, pos_x + distance + 1):
                    point = (x, pos_y)
                    if not point in visted:
                        board[pos_y][x] += 1
                        visted.add(point)
                pos_x += distance
            elif op[0] == 'D':
                for y in range(pos_y + 1, pos_y + distance + 1):
                    point = (pos_x, y)
                    if not point in visted:
                        board[y][pos_x] += 1
                        visted.add(point)
                pos_y += distance
            elif op[0] == 'U':
                for y in range(pos_y - 1, pos_y - distance - 1, -1):
                    point = (pos_x, y)
                    if not point in visted:
                        board[y][pos_x] += 1
                        visted.add(point)
                pos_y -= distance

    distances = []
    for y, row in enumerate(board):
        for x, num in enumerate(row):
            if num > 1 and (x != pos_start and y != pos_start):
                distances.append(abs(x - pos_start) + abs(y - pos_start))

    return min(distances)

if __name__ == '__main__':
    wires = read_input()
    min_distance = main(wires)
    print('min_distance', min_distance)