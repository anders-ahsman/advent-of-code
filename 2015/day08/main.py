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

def part2(strings):
    total_code = 0
    total_encoded = 0
    for str_code in strings:
        total_code += len(str_code)
        total_encoded += len(escape(str_code))
    return total_encoded - total_code

def escape(string):
    return ('"' + string
        .replace('\\', '\\\\')
        .replace('"', '\\"')
        + '"')

strings = read_input()
print('Part 1:', part1(strings))
print('Part 2:', part2(strings))
