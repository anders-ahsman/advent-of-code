import numpy as np
import re

def part1():
    claims = load_claims()
    overlap_count = calc_overlap_count(claims)
    print('Claimed more than once:', overlap_count)
    return overlap_count

class Claim(object):
    pass

def load_claims():
    claims = []
    data = read_input()
    for row in data:
        m = re.match(r'^#(\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+)$', row)
        c = Claim()
        c.id = int(m.group(1))
        c.x = int(m.group(2))
        c.y = int(m.group(3))
        c.width = int(m.group(4))
        c.height = int(m.group(5))
        claims.append(c)
    return claims

def read_input():
    with open('input.txt', 'r') as f:
        data = [x.strip() for x in f.readlines()]
    return data

def calc_overlap_count(claims):
    size = 1000
    fabric = np.zeros((size, size))

    for c in claims:
        fabric[c.x:c.x + c.width, c.y:c.y + c.height] += 1

    overlap_count = 0
    for cell in np.nditer(fabric):
        if cell > 1:
            overlap_count += 1
    return overlap_count

def part2():
    claims = load_claims()
    claim_id_intact = calc_claim_id_intact(claims)
    print('Claims intact for ID:', claim_id_intact)
    return claim_id_intact

def calc_claim_id_intact(claims):
    size = 1000
    fabric = np.zeros((size, size))

    for c in claims:
        fabric[c.x:c.x + c.width, c.y:c.y + c.height] += 1

    for c in claims:
        if all(cell == 1 for cell in np.nditer(fabric[c.x:c.x + c.width, c.y:c.y + c.height])):
            return c.id

if __name__ == '__main__':
    part1()
    part2()