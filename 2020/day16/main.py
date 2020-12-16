import re
import sys


def read_lines():
    return [line.rstrip() for line in sys.stdin]


def parse_restrictions(lines):
    restrictions = []
    for line in lines:
        if line == '':
            return restrictions
        m = re.match(r'.*: (\d+)-(\d+) or (\d+)-(\d+)', line)
        a, b, c, d = int(m[1]), int(m[2]), int(m[3]), int(m[4])
        restrictions.append(range(a, b + 1))
        restrictions.append(range(c, d + 1))


def read_nearby_tickets(lines):
    nearby_tickets = []
    found = False
    for line in lines:
        if line == 'nearby tickets:':
            found = True
            continue
        if not found:
            continue
        nearby_tickets.append([int(x) for x in line.split(',')])
    return nearby_tickets


def part1(nearby_tickets, restrictions):
    invalid = 0
    for ticket in nearby_tickets:
        for value in ticket:
            if not any(value in r for r in restrictions):
                invalid += value
    return invalid


if __name__ == '__main__':
    lines = read_lines()
    restrictions = parse_restrictions(lines)
    nearby_tickets = read_nearby_tickets(lines)
    print(f'Part 1: {part1(nearby_tickets, restrictions)}')
