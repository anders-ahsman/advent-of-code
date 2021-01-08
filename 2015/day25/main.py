def solve(row_target, col_target):
    diagonals_cnt = 1
    value = 20151125
    while True:
        for row in reversed(range(1, diagonals_cnt)):
            col = diagonals_cnt - row
            if row == row_target and col == col_target:
                return value
            value = (value * 252533) % 33554393
        diagonals_cnt += 1

print(f'Part 1: {solve(3010, 3019)}')
