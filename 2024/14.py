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
