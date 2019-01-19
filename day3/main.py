import numpy as np
import re

with open('input.txt', 'r') as f:
    data = [x.strip() for x in f.readlines()]

class Claim(object):
    pass

def load_claims():
    claims = []
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

def calc_overlaps(claims):
    fabric = np.array([[0] * 1000 for x in range(1000)])

    for c in claims:
        fabric[c.x:c.x + c.width, c.y:c.y + c.height] += 1

    claimed_more_than_once = 0
    for row in fabric:
        for cell in row:
            if cell > 1:
                claimed_more_than_once += 1
    print('Claimed more than once:', claimed_more_than_once)

claims = load_claims()
calc_overlaps(claims)