def part1(cups):
    cups = [int(x) for x in cups]
    moves = 100
    successors = solve(cups, moves)

    res = ''
    cup = successors[1]
    while cup != 1:
        res += str(cup)
        cup = successors[cup]
    return res


def part2(cups):
    cups = [int(x) for x in cups] + list(range(10, 1_000_001))
    moves = 10_000_000
    successors = solve(cups, moves)
    return successors[1] * successors[successors[1]]


def solve(cups, moves):
    successors = {}
    for c1, c2 in zip(cups, cups[1:] + cups[:1]):
        successors[c1] = c2

    curr = cups[0]
    for _ in range(moves):
        a = successors[curr]
        b = successors[a]
        c = successors[b]

        dest = curr
        while True:
            dest -= 1
            if dest == 0:
                dest = max(cups)
            if dest not in (a, b, c):
                break

        successors[curr], successors[dest], successors[c] = successors[c], a, successors[dest]
        curr = successors[curr]
    return successors

if __name__ == '__main__':
    cups = '326519478'
    print(f'Part 1: {part1(cups)}')
    print(f'Part 2: {part2(cups)}')
