def part1():
    data = read_input()
    freq_sum = sum(data)
    return freq_sum

def read_input():
    with open('input.txt', 'r') as f:
        data = [int(x) for x in f.readlines()]
    return data

def part2():
    data = read_input()
    seen = {0}
    freq = 0
    from itertools import cycle
    for num in cycle(data):
        freq += num
        if freq in seen:
            return freq
        seen.add(freq)

if __name__ == '__main__':
    freq_sum = part1()
    print('Frequence sum:', freq_sum)

    first_repeating_freq = part2()
    print('First repeating frequency:', first_repeating_freq)