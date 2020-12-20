import re
import sys
import operator


def read_expressions():
    return [line.rstrip() for line in sys.stdin]


def part1(expressions):
    return sum(solve(expr) for expr in expressions)


def solve(expr):
    expr = expr.replace(' ', '')
    ops = {
        '+': operator.add,
        '*': operator.mul,
    }

    while '(' in expr:
        start = expr.rindex('(') + 1
        end = start + expr[start:].index(')')
        res = solve(expr[start:end]) # sub-expression contains no parenthesis
        expr = f'{expr[:start - 1]}{res}{expr[end + 1:]}' # replace sub-expression with result

    while any(op in expr for op in ops):
        m = re.match(r'^(\d+)([\+\*])(\d+)(.*)', expr)
        op, left, right, expr_rest = ops[m[2]], int(m[1]), int(m[3]), m[4]
        res = op(left, right)
        expr = f'{res}{expr_rest}'

    return int(expr)

if __name__ == '__main__':
    expressions = read_expressions()
    print(f'Part 1: {part1(expressions)}')
