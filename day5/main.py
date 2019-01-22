import re
import string

def read_polymer():
    with open('input.txt', 'r') as f:
        polymer = f.read()
        return polymer

def opposite_polarity(a, b):
    return abs(ord(a) - ord(b)) == 32

def calc_final_length(polymer):
    stack = []
    for c in polymer:
        if len(stack) > 0 and opposite_polarity(c, stack[-1]):
            stack.pop()
        else:
            stack.append(c)
    return len(stack)

def part1():
    polymer = read_polymer()
    final_length = calc_final_length(polymer)
    print('Final length (part 1):', final_length)

def part2():
    polymer = read_polymer()
    min_length = None

    for c in string.ascii_lowercase:
        after_remove = re.sub(c, '', polymer, flags=re.IGNORECASE)
        length = calc_final_length(after_remove)
        if not min_length or length < min_length:
            min_length = length

    print('Shortest final length (part 2):', min_length)

if __name__ == '__main__':
    part1()
    part2()