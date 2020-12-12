import sys


def read_floor():
    return [list(line.rstrip()) for line in sys.stdin]


def part1(floor):
    next_floor = [row[:] for row in floor]
    while True:
        for y in range(len(floor)):
            for x in range(len(floor[y])):
                count = occupied_count(floor, x, y)
                if floor[y][x] == 'L' and count == 0:
                    next_floor[y][x] = '#'
                elif floor[y][x] == '#' and count > 3:
                    next_floor[y][x] = 'L'
        no_change = ''.join([''.join(row) for row in floor]) == ''.join([''.join(row) for row in next_floor])
        if no_change:
            return sum(row.count('#') for row in floor)
        floor = [row[:] for row in next_floor]


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


def part2(floor):
    next_floor = [row[:] for row in floor]
    while True:
        for row in floor:
            print(''.join(row))
        print()
        for y in range(len(floor)):
            for x in range(len(floor[y])):
                count = occupied_visible_count(floor, x, y)
                if floor[y][x] == 'L' and count == 0:
                    next_floor[y][x] = '#'
                elif floor[y][x] == '#' and count > 4:
                    next_floor[y][x] = 'L'
        no_change = ''.join([''.join(row) for row in floor]) == ''.join([''.join(row) for row in next_floor])
        if no_change:
            return sum(row.count('#') for row in floor)
        floor = [row[:] for row in next_floor]


def occupied_visible_count(floor, x, y):
    count = 0

    # north
    y1 = y
    while y1 > 0:
        y1 -= 1
        if floor[y1][x] == 'L':
            break
        if floor[y1][x] == '#':
            count += 1
            break

    # south
    y1 = y
    while y1 + 1 < len(floor):
        y1 += 1
        if floor[y1][x] == 'L':
            break
        if floor[y1][x] == '#':
            count += 1
            break

    # west
    x1 = x
    while x1 > 0:
        x1 -= 1
        if floor[y][x1] == 'L':
            break
        if floor[y][x1] == '#':
            count += 1
            break

    # east
    x1 = x
    while x1 + 1 < len(floor[y]):
        x1 += 1
        if floor[y][x1] == 'L':
            break
        if floor[y][x1] == '#':
            count += 1
            break

    # northwest
    x1 = x
    y1 = y
    while x1 > 0 and y1 > 0:
        x1 -= 1
        y1 -= 1
        if floor[y1][x1] == 'L':
            break
        if floor[y1][x1] == '#':
            count += 1
            break

    # northeast
    x1 = x
    y1 = y
    while x1 + 1 < len(floor[y]) and y1 > 0:
        x1 += 1
        y1 -= 1
        if floor[y1][x1] == 'L':
            break
        if floor[y1][x1] == '#':
            count += 1
            break

    # southeast
    x1 = x
    y1 = y
    while x1 + 1 < len(floor[y]) and y1 + 1 < len(floor):
        x1 += 1
        y1 += 1
        if floor[y1][x1] == 'L':
            break
        if floor[y1][x1] == '#':
            count += 1
            break

    # southwest
    x1 = x
    y1 = y
    while x1 > 0 and y1 + 1 < len(floor):
        x1 -= 1
        y1 += 1
        if floor[y1][x1] == 'L':
            break
        if floor[y1][x1] == '#':
            count += 1
            break

    return count


if __name__ == '__main__':
    floor = read_floor()
    print(f'Part 1: {part1(floor)}')
    print(f'Part 2: {part2(floor)}')
