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
visit_dir = [[' ' for _ in range(n_cols)] for _ in range(n_rows)]

def visit(coord, direction):
    r, c = to_row_col(coord)
    visited[r][c] = 1
    vert, _ = to_row_col(direction.value)
    old = visit_dir[r][c]
    if vert == 0: # -
        if old == ' ' or old == '-':
            visit_dir[r][c] = '-'
        else:
            visit_dir[r][c] = '+'
    else:
        if old == ' ' or old == '|':
            visit_dir[r][c] = '|'
        else:
            visit_dir[r][c] = '+'

while True:
    # print(to_row_col(current_pos), current_dir)
    next_pos = current_pos + current_dir.value
    if not in_grid(next_pos):
        break
    if is_obstructed(next_pos):
        current_dir = Direction.rotate(current_dir)
        continue
    current_pos = next_pos
    visit(current_pos, current_dir)

for row in visited:
    print(*row, sep='')

for row in visit_dir:
    print(*row, sep='')

print("Total visited", sum(map(sum, visited)))

# Part 2
def leads_to_loop(start_pos, start_dir, insert_pos):
    visited = set()
    current_pos = start_pos
    current_dir = start_dir
    while True:
        next_pos = current_pos + current_dir.value
        if not in_grid(next_pos):
            return False
        if is_obstructed(next_pos) or next_pos == insert_pos:
            current_dir = Direction.rotate(current_dir)
            continue
        current_pos = next_pos
        if (current_pos, current_dir,) in visited:
            return True
        visited.add((current_pos, current_dir,))

current_pos = start_pos
current_dir = Direction.UP
loops = set()

used = set()
while True:
    used.add(current_pos)
    next_pos = current_pos + current_dir.value
    if not in_grid(next_pos):
        break
    if is_obstructed(next_pos):
        current_dir = Direction.rotate(current_dir)
        continue
    # Assume we insert a block here
    elif next_pos not in used:
        if leads_to_loop(current_pos, current_dir, next_pos):
            loops.add(next_pos)
    current_pos = next_pos

for l in loops:
    r, c = to_row_col(l)
    visit_dir[r][c] = 'O'
r_s, c_s = to_row_col(start_pos)
visit_dir[r_s][c_s] = '^'

for row in visit_dir:
    print(*row, sep='')
print("Possible loops:", len(loops))
