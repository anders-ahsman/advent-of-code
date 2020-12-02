import sys


def read_lines():
    return [line.strip() for line in sys.stdin]


def password1(lines):
    valid_count = 0
    for line in lines:
        lengths, letter, password = line.split(' ')
        min_len, max_len = lengths.split('-')
        min_len = int(min_len)
        max_len = int(max_len)
        letter = letter[:-1]
        if min_len <= password.count(letter) <= max_len:
            valid_count += 1
    return valid_count


def password2(lines):
    valid_count = 0
    for line in lines:
        lengths, letter, password = line.split(' ')
        min_pos, max_pos = lengths.split('-')
        min_pos = int(min_pos) - 1
        max_pos = int(max_pos) - 1
        letter = letter[:-1]
        if (password[min_pos] == letter or password[max_pos] == letter) and not \
                (password[min_pos] == letter and password[max_pos] == letter):
            valid_count += 1
    return valid_count


if __name__ == '__main__':
    lines = read_lines()
    print(f'Part 1: {password1(lines)}')
    print(f'Part 2: {password2(lines)}')
