import re
import sys


def read_expressions():
    return [line.rstrip() for line in sys.stdin]


def part1(expressions):
    return sum(solve(expr) for expr in expressions)


def part2(expressions):
    return sum(solve(expr, True) for expr in expressions)


def solve(expr, is_part2=False):
    expr = expr.replace(' ', '')

    while '(' in expr:
        start = expr.rindex('(') + 1
        end = start + expr[start:].index(')')
        res = solve(expr[start:end], is_part2)  # sub-expression contains no parenthesis
        expr = f'{expr[:start - 1]}{res}{expr[end + 1:]}'  # replace sub-expression with result

    if is_part2:
        while '+' in expr:
            expr = re.sub(r'(\d+)\+(\d+)', lambda m: str(int(m[1]) + int(m[2])), expr)
        while '*' in expr:
            expr = re.sub(r'(\d+)\*(\d+)', lambda m: str(int(m[1]) * int(m[2])), expr)
    else:
        while '+' in expr or '*' in expr:
            # since start of string is matched order will be left to right
            expr = re.sub(r'^(\d+)\+(\d+)', lambda m: str(int(m[1]) + int(m[2])), expr)
            expr = re.sub(r'^(\d+)\*(\d+)', lambda m: str(int(m[1]) * int(m[2])), expr)

    return int(expr)


if __name__ == '__main__':
    expressions = read_expressions()
    print(f'Part 1: {part1(expressions)}')
    print(f'Part 2: {part2(expressions)}')
