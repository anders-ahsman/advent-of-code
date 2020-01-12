import sys

def read_input():
    strings = []
    for s in sys.stdin:
        strings.append(s.rstrip())
    return strings

def part1(strings):
    total_code = 0
    total_value = 0
    for str_code in strings:
        total_code += len(str_code)
        str_value = eval(str_code)
        total_value += len(str_value)
    return total_code - total_value

strings = read_input()
print('Part 1:', part1(strings))
