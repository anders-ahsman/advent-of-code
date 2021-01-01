from collections import defaultdict


def solve(numbers, turns):
    num_to_turns_spoken = defaultdict(list)

    last_num = None
    for i, num in enumerate(numbers):
        num_to_turns_spoken[num].append(i)
        last_num = num

    for turn in range(len(numbers), turns):
        if len(num_to_turns_spoken[last_num]) > 1:
            last_num = num_to_turns_spoken[last_num][-1] - num_to_turns_spoken[last_num][-2]
        else:
            last_num = 0
        num_to_turns_spoken[last_num].append(turn)
    return last_num


if __name__ == '__main__':
    numbers = [1, 0, 16, 5, 17, 4]
    print(f'Part 1: {solve(numbers, 2020)}')
    print(f'Part 2: {solve(numbers, 30_000_000)}')
