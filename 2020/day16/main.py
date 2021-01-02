from collections import defaultdict
from math import prod
import re
import sys


def read_lines():
    return [line.rstrip() for line in sys.stdin]


def parse_restrictions(lines):
    restrictions = {}
    for line in lines:
        if line == '':
            return restrictions
        m = re.match(r'(.*): (\d+)-(\d+) or (\d+)-(\d+)', line)
        field, a, b, c, d = m[1], int(m[2]), int(m[3]), int(m[4]), int(m[5])
        total_range = list(range(a, b + 1)) + list(range(c, d + 1))
        restrictions[field] = total_range


def read_my_ticket(lines):
    found = False
    for line in lines:
        if line == 'your ticket:':
            found = True
            continue
        if found:
            return [int(x) for x in line.split(',')]


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
            if not any(value in r for r in restrictions.values()):
                invalid += value
    return invalid


def part2(my_ticket, nearby_tickets, restrictions):
    pos_to_possible_fields = defaultdict(set)
    pos_to_field = {}
    tickets = get_valid_tickets(nearby_tickets, restrictions)
    ticket_length = len(tickets[0])
    assert all(len(t) == ticket_length for t in tickets)
    while len(pos_to_field) < ticket_length:
        for pos in range(ticket_length):
            if pos in pos_to_field:
                continue
            for field in restrictions:
                if all(t[pos] in restrictions[field] for t in tickets):
                    pos_to_possible_fields[pos].add(field)
        for pos, fields in pos_to_possible_fields.items():
            if len(fields) == 1:
                field = list(fields)[0]
                pos_to_field[pos] = field
                del restrictions[field]
        pos_to_possible_fields.clear()
    return prod(my_ticket[pos] for pos in pos_to_field if 'departure' in pos_to_field[pos])


def get_valid_tickets(nearby_tickets, restrictions):
    valid_tickets = []
    for ticket in nearby_tickets:
        all_valid = True
        for value in ticket:
            if not any(value in r for r in restrictions.values()):
                all_valid = False
                break
        if all_valid:
            valid_tickets.append(ticket)
    return valid_tickets


if __name__ == '__main__':
    lines = read_lines()
    restrictions = parse_restrictions(lines)
    nearby_tickets = read_nearby_tickets(lines)
    print(f'Part 1: {part1(nearby_tickets, restrictions)}')
    my_ticket = read_my_ticket(lines)
    print(f'Part 2: {part2(my_ticket, nearby_tickets, restrictions)}')
