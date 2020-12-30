def part1(cups):
    cups = [int(x) for x in cups]
    idx = 0
    for _ in range(100):
        # use "double" list to simulate circle
        picked_up = (cups + cups)[idx + 1:idx + 4]

        value = cups[idx]
        dest_value = value - 1
        if dest_value == 0:
            dest_value = max(cups)
        while dest_value in picked_up:
            dest_value -= 1
            if dest_value == 0:
                dest_value = max(cups)
        dest_idx = cups.index(dest_value)

        cups = [c for c in cups[:dest_idx + 1] if c not in picked_up] + \
               picked_up + \
               [c for c in cups[dest_idx + 1:] if c not in picked_up]

        idx = (cups.index(value) + 1) % len(cups)

    return ''.join([str((cups + cups)[i])
                    for i in range(cups.index(1) + 1, cups.index(1) + 9)])


def part2(cups):
    cups = [int(x) for x in cups] + list(range(10, 1_000_001))
    successors = {}
    for c1, c2 in zip(cups, cups[1:] + cups[:1]):
        successors[c1] = c2

    curr = cups[0]
    for _ in range(10_000_000):
        a = successors[curr]
        b = successors[a]
        c = successors[b]

        dest = curr - 1
        if dest == 0:
            dest = max(cups)
        while dest in (a, b, c):
            dest -= 1
            if dest == 0:
                dest = max(cups)

        successors[curr], successors[dest], successors[c] = successors[c], a, successors[dest]
        curr = successors[curr]

    return successors[1] * successors[successors[1]]

if __name__ == '__main__':
    cups = '326519478'
    print(f'Part 1: {part1(cups)}')
    print(f'Part 2: {part2(cups)}')
