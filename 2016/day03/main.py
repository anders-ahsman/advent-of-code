from typing import List, Tuple

def read_input(filename: str) -> List[Tuple[int, int, int]]:
    candidates: List[Tuple[int, int, int]] = []
    with open(filename, 'r') as f:
        numbers = [line.split() for line in f.readlines()]
        for number in numbers:
            candidates.append((int(number[0]), int(number[1]), int(number[2])))
    return candidates

def is_valid_triangle(candidate: Tuple[int, int, int]) -> bool:
    a, b, c = candidate
    return a + b > c and a + c > b and b + c > a

if __name__ == '__main__':
    candidates = read_input('input.txt')
    print(sum(1 for c in candidates if is_valid_triangle(c)))