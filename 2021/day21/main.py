#!/usr/bin/env python3


from typing import Generator


def part1() -> int:
    def deterministic_die_100() -> Generator[int, None, None]:
        i = 1
        while True:
            yield i

            i += 1
            if i > 100:
                i = 1

    die = deterministic_die_100()

    roll_count = 0
    score_p1 = 0
    score_p2 = 0
    is_p1 = True

    # starting positions copied from puzzle input
    pos_p1 = 10
    pos_p2 = 1

    while score_p1 < 1000 and score_p2 < 1000:
        roll_sum = sum([next(die) for _ in range(3)])
        if is_p1:
            pos_p1 = (pos_p1 + roll_sum) % 10
            if pos_p1 == 0:
                pos_p1 = 10
            score_p1 += pos_p1
        else:
            pos_p2 = (pos_p2 + roll_sum) % 10
            if pos_p2 == 0:
                pos_p2 = 10
            score_p2 += pos_p2

        roll_count += 3
        is_p1 = not is_p1

    score_looser = min(score_p1, score_p2)
    return score_looser * roll_count


if __name__ == '__main__':
    print(f'Part 1: {part1()}')
