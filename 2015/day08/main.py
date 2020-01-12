import sys

def read_input():
    strings = []
    for s in sys.stdin:
        strings.append(s.rstrip())
    return strings

def part1(strings):
    literal_count = 0
    actual_count = 0
    for literal_str in strings:
        literal_count += len(literal_str)
        actual_count += len(eval(literal_str))
    return literal_count - actual_count

def part2(strings):
    literal_count = 0
    encoded_count = 0
    for literal_str in strings:
        literal_count += len(literal_str)
        encoded_count += len(escape(literal_str))
    return encoded_count - literal_count

def escape(string):
    return ('"' + string
        .replace('\\', '\\\\')
        .replace('"', '\\"')
        + '"')

strings = read_input()
print('Part 1:', part1(strings))
print('Part 2:', part2(strings))
