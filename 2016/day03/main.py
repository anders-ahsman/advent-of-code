from typing import List, Tuple

def read_input(filename: str) -> List[List[int]]:
    with open(filename, 'r') as f:
        lines = [line.split() for line in f.readlines()]
        lines_int = [[int(num) for num in line] for line in lines]
    return lines_int

def parse_horizontally(lines: List[List[int]]) -> List[Tuple[int, int, int]]:
    candidates: List[Tuple[int, int, int]] = []
    for line in lines:
        candidates.append((line[0], line[1], line[2]))
    return candidates

def parse_vertically(lines: List[List[int]]) -> List[Tuple[int, int, int]]:
    candidates: List[Tuple[int, int, int]] = []
    for y in range(0, len(lines), 3):
        for x in range(3):
            candidates.append((lines[y][x], lines[y + 1][x], lines[y + 2][x]))
    return candidates

def is_valid_triangle(candidate: Tuple[int, int, int]) -> bool:
    a, b, c = candidate
    return a + b > c and a + c > b and b + c > a

if __name__ == '__main__':
    lines = read_input('input.txt')
    candidates_horizontally = parse_horizontally(lines)
    candidates_vertically = parse_vertically(lines)

    print(f'Part 1: {sum(1 for c in candidates_horizontally if is_valid_triangle(c))}')
    print(f'Part 2: {sum(1 for c in candidates_vertically if is_valid_triangle(c))}')
