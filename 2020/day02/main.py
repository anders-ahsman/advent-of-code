import re
import sys


pattern = r'^(\d+)-(\d+) (\w): (\w+)$'

def read_lines():
    return [line.strip() for line in sys.stdin]


def password1(lines):
    valid_count = 0
    for line in lines:
        m = re.match(pattern, line)
        min_len = int(m.group(1))
        max_len = int(m.group(2))
        letter = m.group(3)
        password = m.group(4)
        if min_len <= password.count(letter) <= max_len:
            valid_count += 1
    return valid_count


def password2(lines):
    valid_count = 0
    for line in lines:
        m = re.match(pattern, line)
        min_pos = int(m.group(1)) - 1
        max_pos = int(m.group(2)) - 1
        letter = m.group(3)
        password = m.group(4)
        if (password[min_pos] == letter and password[max_pos] != letter) or \
                (password[min_pos] != letter and password[max_pos] == letter):
            valid_count += 1
    return valid_count


if __name__ == '__main__':
    lines = read_lines()
    print(f'Part 1: {password1(lines)}')
    print(f'Part 2: {password2(lines)}')
