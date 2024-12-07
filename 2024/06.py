#!/usr/bin/env python
# -*- coding: utf-8 -*-

from santashelpers import coordinates, to_row_col, Direction

grid = []
start_pos = 0

with open('06.input', 'r') as f:
    line_num = 0
    while l:=f.readline():
        row = list(l)
        for col, entry in enumerate(row):
            if entry == '^':
                start_pos = coordinates(line_num, col)
        grid.append(row)
        line_num += 1

n_rows = len(grid)
n_cols = len(grid[0])

def in_grid(coord):
    r, c = to_row_col(coord)
    return r >= 0 and c >= 0 and r < n_rows and c < n_cols

def is_obstructed(coord):
    r, c = to_row_col(coord)
    return grid[r][c] == '#'

current_pos = start_pos
current_dir = Direction.UP
visited = [[0 for _ in range(n_cols)] for _ in range(n_rows)]

def visit(coord):
    r, c = to_row_col(coord)
    visited[r][c] = 1

while True:
    # print(to_row_col(current_pos), current_dir)
    next_pos = current_pos + current_dir.value
    if not in_grid(next_pos):
        break
    if is_obstructed(next_pos):
        current_dir = Direction.rotate(current_dir)
        continue
    current_pos = next_pos
    visit(current_pos)

for row in visited:
    print(*row)

print("Total visited", sum(map(sum, visited)))
