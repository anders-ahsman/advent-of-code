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
    print('Final length:', final_length)

if __name__ == '__main__':
    part1()