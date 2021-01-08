from functools import reduce
from itertools import combinations
from operator import mul
import sys


weights = [int(line.rstrip()) for line in sys.stdin]

def solve(num_groups):
    target_weight = sum(weights) // num_groups
    for i in range(len(weights)):
        candidates = [reduce(mul, c) for c in combinations(weights, i) if sum(c) == target_weight]
        if candidates:
            return min(candidates)

print(f'Part 1: {solve(3)}')
print(f'Part 2: {solve(4)}')
