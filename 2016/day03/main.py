from typing import List, Tuple

def read_input(filename: str) -> List[Tuple[int, int, int]]:
    candidates: List[Tuple[int, int, int]] = []
    with open(filename, 'r') as f:
        numbers = [line.split() for line in f.readlines()]
        for number in numbers:
            candidates.append((int(number[0]), int(number[1]), int(number[2])))
    return candidates

def read_input_vertically(filename: str) -> List[Tuple[int, int, int]]:
    candidates: List[Tuple[int, int, int]] = []
    with open(filename, 'r') as f:
        numbers = [line.split() for line in f.readlines()]
        for y in range(0, len(numbers), 3):
            for x in range(3):
                candidates.append((int(numbers[y][x]), int(numbers[y + 1][x]), int(numbers[y + 2][x])))
    return candidates

def is_valid_triangle(candidate: Tuple[int, int, int]) -> bool:
    a, b, c = candidate
    return a + b > c and a + c > b and b + c > a

if __name__ == '__main__':
    candidates_horizontally = read_input('input.txt')
    candidates_vertically = read_input_vertically('input.txt')

    print(f'Part 1: {sum(1 for c in candidates_horizontally if is_valid_triangle(c))}')
    print(f'Part 2: {sum(1 for c in candidates_vertically if is_valid_triangle(c))}')
