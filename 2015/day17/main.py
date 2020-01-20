import itertools
import sys

containers = [int(line.strip()) for line in sys.stdin]
match_cnt = 0
for bitmask in itertools.product(range(2), repeat=len(containers)):
    comb = [a * b for a, b in zip(containers, bitmask)]
    if sum(comb) == 150:
        match_cnt += 1
print('Part 1:', match_cnt)
