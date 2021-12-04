from collections import defaultdict
import sys


def read_boarding_passes():
    return [line.strip() for line in sys.stdin]


def part1(boarding_passes):
    max_seat_id = 0
    for boarding_pass in boarding_passes:
        lower = 0
        upper = 127
        for ch in boarding_pass[:7]:
            if ch == 'F':
                upper = (lower + upper) // 2
            else:
                lower = (lower + upper) // 2 + 1
        assert lower == upper
        row = lower

        lower = 0
        upper = 7
        for ch in boarding_pass[7:]:
            if ch == 'L':
                upper = (lower + upper) // 2
            else:
                lower = (lower + upper) // 2 + 1
        assert lower == upper
        seat = lower
        seat_id = row * 8 + seat

        if seat_id > max_seat_id:
            max_seat_id = seat_id
    return max_seat_id


def part2(boarding_passes):
    rows = defaultdict(list)
    for boarding_pass in boarding_passes:
        lower = 0
        upper = 127
        for ch in boarding_pass[:7]:
            if ch == 'F':
                upper = (lower + upper) // 2
            elif ch == 'B':
                lower = (lower + upper) // 2 + 1
            else:
                raise ValueError
        assert lower == upper
        row = lower

        lower = 0
        upper = 7
        for ch in boarding_pass[7:]:
            if ch == 'L':
                upper = (lower + upper) // 2
            elif ch == 'R':
                lower = (lower + upper) // 2 + 1
            else:
                raise ValueError
        assert lower == upper
        seat = lower

        rows[row].append(seat)

    candidates = {row: seats for row, seats in rows.items() if len(seats) != 8 and row - 1 in rows and row + 1 in rows}
    assert len(candidates) == 1
    row = list(candidates.keys())[0]
    seats = list(candidates.values())[0]
    seat = list(set(list(range(8))) - set(seats))[0]
    seat_id = row * 8 + seat
    return seat_id


if __name__ == '__main__':
    boarding_passes = read_boarding_passes()
    print(f'Part 1: {part1(boarding_passes)}')
    print(f'Part 2: {part2(boarding_passes)}')
