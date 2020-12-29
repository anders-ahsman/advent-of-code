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


if __name__ == '__main__':
    cups = '326519478'
    print(f'Part 1: {part1(cups)}')
