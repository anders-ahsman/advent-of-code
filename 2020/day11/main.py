import sys


def read_floor():
    return [list(line.rstrip()) for line in sys.stdin]


def part1(floor):
    next_iter = [row[:] for row in floor]
    while True:
        for y in range(len(floor)):
            for x in range(len(floor[y])):
                count = occupied_count(floor, x, y)
                if floor[y][x] == 'L' and count == 0:
                    next_iter[y][x] = '#'
                elif floor[y][x] == '#' and count > 3:
                    next_iter[y][x] = 'L'
        if ''.join([''.join(row) for row in floor]) == ''.join([''.join(row) for row in next_iter]):
            return sum(row.count('#') for row in floor)
        floor = [row[:] for row in next_iter]


def occupied_count(floor, x, y):
    count = 0
    if x > 0:
        if floor[y][x - 1] == '#':
            count += 1
        if y > 0 and floor[y - 1][x - 1] == '#':
            count += 1
        if y + 1 < len(floor) and floor[y + 1][x - 1] == '#':
            count += 1
    if y > 0 and floor[y - 1][x] == '#':
        count += 1
    if y + 1 < len(floor) and floor[y + 1][x] == '#':
        count += 1
    if x + 1 < len(floor):
        if floor[y][x + 1] == '#':
            count += 1
        if y > 0 and floor[y - 1][x + 1] == '#':
            count += 1
        if y + 1 < len(floor) and floor[y + 1][x + 1] == '#':
            count += 1
    return count


if __name__ == '__main__':
    floor = read_floor()

    print(f'Part 1: {part1(floor)}')
