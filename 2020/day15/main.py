def part1(numbers):
    def rindex(l, val):
        return len(l) - l[::-1].index(val) - 1

    t = len(numbers)
    while t < 2020:
        last_number = numbers[-1]
        if numbers.count(last_number) > 1:
            idx_r = rindex(numbers, last_number)
            idx_l = rindex(numbers[:idx_r], last_number)
            next_number = idx_r - idx_l
        else:
            next_number = 0
        numbers.append(next_number)
        t += 1
    return numbers[-1]


if __name__ == '__main__':
    numbers = [1, 0, 16, 5, 17, 4]
    print(f'Part 1: {part1(numbers)}')
