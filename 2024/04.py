#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

with open('04.input', 'r') as f:
    grid = []
    while l:=f.readline():
        grid.append(l)

xmas_count = 0
lines = len(grid)
columns = len(grid[0])

def in_grid(l, c):
    return l >= 0 and c >= 0 and l < lines and c < columns

UP    = (-1, 0)
DOWN  = ( 1, 0)
RIGHT = ( 0, 1)
LEFT  = ( 0,-1)
D_UL  = (-1,-1)
D_DL  = ( 1,-1)
D_UR  = (-1, 1)
D_DR  = ( 1, 1)

DIRECTIONS = [UP, DOWN, RIGHT, LEFT, D_UL, D_DL, D_UR, D_DR]
WORD = "XMAS"
WORDLEN = len(WORD)

def search_xmas(l, c, direction):
    pos_l = l
    pos_c = c
    for ci in range(WORDLEN):
        if not in_grid(pos_l, pos_c):
            return False
        if grid[pos_l][pos_c] != WORD[ci]:
            return False
        pos_l += direction[0]
        pos_c += direction[1]
    return True

for l in range(lines):
    for c in range(columns):
        for d in DIRECTIONS:
            if search_xmas(l, c, d):
                xmas_count += 1

print(xmas_count)
