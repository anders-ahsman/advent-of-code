from math import floor, sqrt


# sum of divisors
def sigma(n: int, only_first_50: bool) -> int:
    s: int = n + 1
    root: int = floor(sqrt(n))
    for i in range(2, root + 1):
        if n % i == 0 and (not only_first_50 or only_first_50 and i <= 50):
            s += i + n // i
    if sqrt(n) % 1 == 0:
        s -= root
    return s

def part1(target: int) -> int:
    house: int = 0 # todo: could start further ahead
    while True:
        house += 1
        if sigma(house, False) * 10 >= target:
            return house

def part2(target: int) -> int:
    house: int = 0
    while True:
        house += 1
        if sigma(house, True) * 11 >= target:
            return house

target: int = 29000000
print('Part 1:', part1(target))
print('Part 2:', part2(target))
