import itertools
import sys

containers = [int(line.strip()) for line in sys.stdin]
matches = []
for bitmask in itertools.product(range(2), repeat=len(containers)):
    comb = [a * b for a, b in zip(containers, bitmask)]
    if sum(comb) == 150:
        matches.append(comb)
print('Part 1:', len(matches))

non_zeros = []
for m in matches:
    non_zeros.append(len([x for x in m if x != 0]))
print('Part 2:', sum(1 for x in non_zeros if x == min(non_zeros)))
