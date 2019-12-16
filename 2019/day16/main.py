import sys

def read_input():
    digits = [int(char) for char in next(sys.stdin) if char != '\n']
    return digits

def main(digits):
    digits = calc_digits(digits, 100)
    print(f'Part 1: {digits}')

def calc_digits(digits, count):
    for _ in range(count):
        digits_copy = digits[:]
        for i in range(len(digits)):
            it = get_pattern_iter(i + 1)
            digit_sum = 0
            for j in range(len(digits)):
                digit_sum += digits_copy[j] * next(it)
            digits[i] = int(str(digit_sum)[-1])
    return ''.join([str(d) for d in digits[0:8]])

def get_pattern_iter(repeat_target):
    digits = (0, 1, 0, -1)
    pos = 0
    repeat_count = 0
    digit = digits[pos]
    is_first = True
    while True:
        if is_first:
            is_first = False
        else:
            yield digit

        repeat_count += 1
        if repeat_count >= repeat_target:
            repeat_count = 0
            pos = (pos + 1) % len(digits)
            digit = digits[pos]


if __name__ == '__main__':
    digits = read_input()
    main(digits)
