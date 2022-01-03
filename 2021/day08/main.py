#!/usr/bin/env python3

import sys
from typing import Dict, List, Set


def read_input() -> List[str]:
    return [line.strip() for line in sys.stdin]


def part1(segments: List[str]) -> int:
    count = 0
    for entry in segments:
        signal_patterns, output = entry.split(' | ')
        for digit in output.split(' '):
            if len(digit) in (2, 3, 4, 7):
                count += 1
    return count


def part2(entries: List[str]) -> int:
    output_sum = 0
    segment_lengths_to_possible_digits: Dict[int, List[int]] = {
        2: [1],
        3: [7],
        5: [2, 3, 5],
        4: [4],
        6: [0, 6, 9],
        7: [8]
    }
    for entry in entries:
        segments_to_possible_digits: Dict[str, List[int]] = {}
        signal_patterns, output = entry.split(' | ')

        for segment in signal_patterns.split(' '):
            sorted_segment = ''.join(sorted(segment))
            segments_to_possible_digits[sorted_segment] = segment_lengths_to_possible_digits[len(segment)]

        digits_to_segment_chars: Dict[int, Set[str]] = {}
        for segment, possible_digits in segments_to_possible_digits.items():
            if possible_digits == [1]:
                digits_to_segment_chars[1] = set(segment)
            elif possible_digits == [4]:
                digits_to_segment_chars[4] = set(segment)
            elif possible_digits == [7]:
                digits_to_segment_chars[7] = set(segment)
            elif possible_digits == [8]:
                digits_to_segment_chars[8] = set(segment)

        for segment in segments_to_possible_digits:
            sorted_segment = ''.join(sorted(segment))
            segment_chars = set(segment)
            shared_chars_with_1_count = len(segment_chars.intersection(digits_to_segment_chars[1]))
            shared_chars_with_4_count = len(segment_chars.intersection(digits_to_segment_chars[4]))
            shared_chars_with_7_count = len(segment_chars.intersection(digits_to_segment_chars[7]))
            shared_chars_with_8_count = len(segment_chars.intersection(digits_to_segment_chars[8]))

            if shared_chars_with_1_count == 2 and \
                    shared_chars_with_4_count == 3 and \
                    shared_chars_with_7_count == 3 and \
                    shared_chars_with_8_count == 6:
                segments_to_possible_digits[sorted_segment] = [0]
            elif shared_chars_with_1_count == 1 and \
                    shared_chars_with_4_count == 2 and \
                    shared_chars_with_7_count == 2 and \
                    shared_chars_with_8_count == 5:
                segments_to_possible_digits[sorted_segment] = [2]
            elif shared_chars_with_1_count == 2 and \
                    shared_chars_with_4_count == 3 and \
                    shared_chars_with_7_count == 3 and \
                    shared_chars_with_8_count == 5:
                segments_to_possible_digits[sorted_segment] = [3]
            elif shared_chars_with_1_count == 1 and \
                    shared_chars_with_4_count == 3 and \
                    shared_chars_with_7_count == 2 and \
                    shared_chars_with_8_count == 5:
                segments_to_possible_digits[sorted_segment] = [5]
            elif shared_chars_with_1_count == 1 and \
                    shared_chars_with_4_count == 3 and \
                    shared_chars_with_7_count == 2 and \
                    shared_chars_with_8_count == 6:
                segments_to_possible_digits[sorted_segment] = [6]
            elif shared_chars_with_1_count == 2 and \
                    shared_chars_with_4_count == 4 and \
                    shared_chars_with_7_count == 3 and \
                    shared_chars_with_8_count == 6:
                segments_to_possible_digits[sorted_segment] = [9]

        output_value = ''
        for segment in output.split(' '):
            sorted_segment = ''.join(sorted(segment))
            output_value += str(segments_to_possible_digits[sorted_segment][0])

        output_sum += int(output_value)

    return output_sum


if __name__ == '__main__':
    input = read_input()
    print(f'Part 1: {part1(input)}')
    print(f'Part 2: {part2(input)}')
