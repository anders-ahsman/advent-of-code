from collections import deque, defaultdict
from math import prod
import sys

import numpy as np


def read_tiles():
    tiles = {}
    for tile_lines in [l.split('\n') for l in sys.stdin.read().split('\n\n')]:
        key = int(tile_lines[0].replace(':', '').replace('Tile ', ''))
        tiles[key] = np.array([list(line) for line in tile_lines[1:]])
    return tiles


def solve(tiles, is_part1):
    tile_to_neighbours = defaultdict(list)
    for t1, a1 in tiles.items():
        for t2, a2 in tiles.items():
            if t1 == t2:
                continue
            for a2_comb in array_combinations(a2):
                is_neighbour, direction = possible_neighbours(a1, a2_comb)
                if is_neighbour:
                    tile_to_neighbours[t1].append((t2, direction))
    if is_part1:
        return prod(t for t in tile_to_neighbours if len(tile_to_neighbours[t]) == 2)

    board = np.full((12 * 10, 12 * 10), ' ')

    def set_board(x, y, arr):
        board[y:y + 10, x:x + 10] = arr

    tile_to_pos = {}
    tiles_adjusted = {}

    # upper left corner
    t_corner = next(t for t, n in tile_to_neighbours.items()
                    if len(n) == 2 and
                    ((n[0][1] == 'R' and n[1][1] == 'D') or (n[0][1] == 'D' and n[1][1] == 'R')))

    # place tiles on board
    frontier = deque([t_corner])
    while frontier:
        t = frontier.popleft()
        if t not in tile_to_pos:
            # place first tile in the upper left corner
            pos_x, pos_y = 0, 0
            tile_to_pos[t] = pos_x, pos_y
            set_board(pos_x, pos_y, tiles[t])
            tiles_adjusted[t] = tiles[t]

        for t2, a2 in tiles.items():
            if t == t2 or t2 in tile_to_pos:
                continue
            for a2_comb in array_combinations(a2):
                a1 = tiles_adjusted[t] if t in tiles_adjusted else tiles[t]
                is_neighbour, direction = possible_neighbours(a1, a2_comb)
                if is_neighbour:
                    pos_x, pos_y = tile_to_pos[t]
                    if direction == 'U': pos_y -= 10
                    elif direction == 'D': pos_y += 10
                    elif direction == 'L': pos_x -= 10
                    elif direction == 'R': pos_x += 10
                    tile_to_pos[t2] = pos_x, pos_y

                    tiles_adjusted[t2] = a2_comb
                    set_board(pos_x, pos_y, a2_comb)
                    frontier.append(t2)

    board_temp = np.full((12 * 8, 12 * 8), ' ')
    for t, (pos_x, pos_y) in tile_to_pos.items():
        pos_x_dest = pos_x // 10 * 8
        pos_y_dest = pos_y // 10 * 8
        board_temp[pos_y_dest:pos_y_dest + 8, pos_x_dest:pos_x_dest + 8] = \
            board[pos_y + 1:pos_y + 9, pos_x + 1:pos_x + 9]
    board = board_temp

    sea_monster = ['                  # ',
                   '#    ##    ##    ###',
                   ' #  #  #  #  #  #   ']

    def is_sea_monster(board, row_board, col_board):
        board_rows = board.shape[0]
        board_cols = board.shape[1]
        for row_monster in range(len(sea_monster)):
            if row_board + row_monster >= board_rows:
                return False
            for col_monster in range(len(sea_monster[0])):
                if col_board + col_monster >= board_cols:
                    return False
                ch_monster = sea_monster[row_monster][col_monster]
                ch_board = board[row_board + row_monster][col_board + col_monster]
                if ch_monster == '#' and ch_board != '#':
                    return False
        return True

    row_count, col_count = board.shape
    char_count = {char: int(count) for char, count in
                  zip(*np.asarray(np.unique(board, return_counts=True)))}
    for board_comb in array_combinations(board):
        monster_count = sum(1 for c in range(col_count)
                              for r in range(row_count)
                              if is_sea_monster(board_comb, r, c))
        if monster_count > 0:
            water_roughness = char_count['#'] - monster_count * sum(l.count('#') for l in sea_monster)
            return water_roughness


def array_combinations(a):
    for _ in range(4):
        a = np.rot90(a)
        yield a
    a = np.fliplr(a)
    for _ in range(4):
        a = np.rot90(a)
        yield a


def possible_neighbours(a1, a2):
    h, w = a1.shape
    h_range = list(range(h))

    # a2 above a1
    if (a2[h - 1] == a1[0]).all():
        return True, 'U'

    # a2 below a1
    if (a1[h - 1] == a2[0]).all():
        return True, 'D'

    # a2 to the left of a1
    if ((a2[h_range, [w - 1]]) == a1[h_range, [0]]).all():
        return True, 'L'

    # a2 to the right of a1
    if ((a1[h_range, [w - 1]]) == a2[h_range, [0]]).all():
        return True, 'R'

    return False, None


if __name__ == '__main__':
    tiles = read_tiles()
    print(f'Part 1: {solve(tiles, True)}')
    print(f'Part 2: {solve(tiles, False)}')
