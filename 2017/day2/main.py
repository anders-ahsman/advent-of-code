import re

def part1(rows):
    checksum = 0
    for row in rows:
        diff = max(row) - min(row)
        checksum += diff
    return checksum

def part2(rows):
    checksum = 0
    for row in rows:
        for this in row:
            for other in row:
                if this != other and other % this == 0:
                    checksum += int(other / this)
    return checksum

def read_input():
    with open('input.txt', 'r') as f:
        rows = []
        for row in f.readlines():
            rows.append([int(x) for x in row.split('\t')])
        return rows

if __name__ == '__main__':
    rows = read_input()
    checksum1 = part1(rows)
    checksum2 = part2(rows)

    print(checksum1, checksum2)