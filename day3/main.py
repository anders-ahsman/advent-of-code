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
    size = 1000
    fabric = np.zeros((size, size))

    for c in claims:
        fabric[c.x:c.x + c.width, c.y:c.y + c.height] += 1

    claimed_more_than_once = 0
    for cell in np.nditer(fabric):
        if cell > 1:
            claimed_more_than_once += 1
    print('Claimed more than once:', claimed_more_than_once)

    for c in claims:
        if all(cell == 1 for cell in np.nditer(fabric[c.x:c.x + c.width, c.y:c.y + c.height])):
            print('Claims intact for ID:', c.id)
            break

claims = load_claims()
calc_overlaps(claims)