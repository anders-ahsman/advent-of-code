import operator
import re
import sys

req_attributes = {}
for attr_and_count in [
    'children: 3', 'cats: 7', 'samoyeds: 2', 'pomeranians: 3', 'akitas: 0',
    'vizslas: 0', 'goldfish: 5', 'trees: 3', 'cars: 2', 'perfumes: 1'
]:
    attr, count = attr_and_count.split(': ')
    req_attributes[attr] = int(count)

sue_attributes = []
pattern = r'Sue \d+: (.*)'
for line in sys.stdin:
    sue_attr = {}
    for attr_and_count in re.findall(pattern, line)[0].split(', '):
        attr, count = attr_and_count.split(': ')
        sue_attr[attr] = int(count)
    sue_attributes.append(sue_attr)

for i, sue_attr in enumerate(sue_attributes):
    mismatch = False
    for req_attr, req_count in req_attributes.items():
        if req_attr in sue_attr and req_count != sue_attr[req_attr]:
            mismatch = True
            break
    if not mismatch:
        print('Part 1:', i + 1)

for i, sue_attr in enumerate(sue_attributes):
    mismatch = False
    for req_attr, req_count in req_attributes.items():
        if req_attr in sue_attr:
            if req_attr in ['cats', 'trees']:
                op = operator.lt
            elif req_attr in ['goldfish', 'pomeranians']:
                op = operator.gt
            else:
                op = operator.eq
            if not op(req_count, sue_attr[req_attr]):
                mismatch = True
                break
    if not mismatch:
        print('Part 2:', i + 1)
