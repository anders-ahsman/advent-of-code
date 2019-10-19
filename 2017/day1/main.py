def part1():
    digits = [int(c) for c in read_input()]
    digits.append(digits[0])

    match_sum = 0
    last_digit = None
    for digit in digits:
        if last_digit == None:
            last_digit = digit
            continue

        if digit == last_digit:
            match_sum += digit

        last_digit = digit

    print(match_sum)

def read_input():
    with open('input.txt', 'r') as f:
        s = f.readline()
        return s

if __name__ == '__main__':
    part1()