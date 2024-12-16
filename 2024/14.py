#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import namedtuple
import re
from santashelpers import coordinates, coord_based, to_row_col

numbers = re.compile("-?[0-9]+")

def extract_numbers(l):
    return tuple(map(int, numbers.findall(l)))

robots = list()

with open('14.input', 'r') as f:
    while l := f.readline():
        px, py, vx, vy = extract_numbers(l)
        robots.append([coordinates(py, px), coordinates(vy, vx)])

COLS, ROWS = 101, 103

robots2 = list()
for r in robots: robots2.append(list(r))

@coord_based
def wrap_field(r, c):
    return r % ROWS, c % COLS

def apply_move(robot):
    robot[0] += robot[1]

for _ in range(100):
    for robot in robots:
        apply_move(robot)

for robot in robots:
    robot[0] = wrap_field(robot[0])

quadrant_counts = [[0,0],[0,0]]

MID_ROWS, MID_COLS = ROWS // 2, COLS // 2

for rob_pos, _ in robots:
    r_r, r_c = to_row_col(rob_pos)
    if r_r == MID_ROWS or r_c == MID_COLS:
        continue
    quadrant_counts[r_r // (MID_ROWS + 1)][r_c // (MID_COLS + 1)] += 1

prod = 1
for q1 in quadrant_counts:
    for q in q1:
        prod *= q
print(prod)

# Part 2
field = []
for _ in range(ROWS):
    field.append([' ' for _ in range(COLS)])

robots = robots2
scan_seq = '***************'
i = 0
# There's some somewhat structured output every 101 steps, but just looking for sequences of * is faster
print_iter = 115
while True:
    for r in range(ROWS):
        for c in range(COLS):
            field[r][c] = ' '
    for robot in robots:
        r, c = to_row_col(robot[0])
        field[r][c] = '*'
    found_seq = False
    for r in field:
        r_s = ''.join(r)
        if scan_seq in r_s:
            print('Found sequence!')
            print(i)
            found_seq = True
            break
    if found_seq:
        print("Iter", i)
        for r in field:
            print(*r, sep='')
        print_iter += 101
    for robot in robots:
        apply_move(robot)
        robot[0] = wrap_field(robot[0])
    #input()
    i += 1
    if i == ROWS * COLS: break

