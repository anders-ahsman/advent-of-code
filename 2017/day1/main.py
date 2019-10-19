def part2():
    digits = [int(c) for c in read_input()]
    match_sum = 0

    for i, digit in enumerate(digits):
        pos = i + int(len(digits) / 2 - len(digits))
        match = digit == digits[pos]
        if match:
            match_sum += digit

    print(match_sum)

def read_input():
    with open('input.txt', 'r') as f:
        s = f.readline()
        return s

if __name__ == '__main__':
    part2()