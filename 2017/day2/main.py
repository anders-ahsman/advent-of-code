import re

def part1():
    checksum = 0
    rows = read_input()
    for row in rows:
        diff = max(row) - min(row)
        checksum += diff

    print(checksum)

def read_input():
    with open('input.txt', 'r') as f:
        rows = []
        for row in f.readlines():
            rows.append([int(x) for x in row.split('\t')])
        return rows

if __name__ == '__main__':
    part1()