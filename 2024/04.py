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

# Part 2

def gridget(l, c):
    if in_grid(l, c):
        return grid[l][c]
    else:
        return None

def is_as(corner1, corner2):
    return (corner1 == 'M' and corner2 == 'S') or (corner1 == 'S' and corner2 == 'M')

def search_xmas_2d(l, c):
    if grid[l][c] != 'A':
        return False
    top_left  = gridget(l - 1, c - 1)
    top_right = gridget(l - 1, c + 1)
    bot_left  = gridget(l + 1, c - 1)
    bot_right = gridget(l + 1, c + 1)
    return is_as(top_left, bot_right) and is_as(top_right, bot_left)

xmas_count = 0

for l in range(lines):
    for c in range(columns):
        if search_xmas_2d(l, c):
            xmas_count += 1

print(xmas_count)
