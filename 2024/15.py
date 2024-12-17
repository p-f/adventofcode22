#!/usr/bin/env python
# -*- coding: utf-8 -*-

from santashelpers import coordinates, chunks, Direction, to_row_col


field = []
instructions = []

robots = list()

with open('15.input', 'r') as f:
    field, instructions = chunks(f)
field = list(map(list, field))

INSTR = {
    '<' : Direction.LEFT,
    '>' : Direction.RIGHT,
    'v' : Direction.DOWN,
    '^' : Direction.UP
}

def find_start_pos():
    for r, r_data in enumerate(field):
        for c in range(len(r_data)):
            if field[r][c] == '@':
                field[r][c] = '.'
                return coordinates(r, c)
pos = find_start_pos()

def do_move(pos, move_instr):
    assert move_instr in INSTR, move_instr
    pos_delta = INSTR[move_instr].value
    next_pos = pos + pos_delta
    next_row, next_col = to_row_col(next_pos)
    if field[next_row][next_col] == '#':
        # Obstructed
        return pos # stay here
    if field[next_row][next_col] == 'O':
        # Moveable piece, see if we can move
        mov_pos = next_pos
        mov_row, mov_col = to_row_col(mov_pos)
        while field[mov_row][mov_col] == 'O': # Find end of sequence of moveable pieces
            mov_pos += pos_delta
            mov_row, mov_col = to_row_col(mov_pos)
        if field[mov_row][mov_col] == '#': # Can't move
            return pos
        # Put . at start and O at end
        #print("Movable to", mov_row, mov_col, "next", next_row, next_col)
        field[mov_row][mov_col] = 'O'
        field[next_row][next_col] = '.'
    return next_pos

def iter_instr():
    for il in instructions:
        for i in il: yield i

def draw_field(pos):
    p_r, p_c = to_row_col(pos)
    for r, r_data in enumerate(field):
        if r != p_r:
            print(*r_data, sep='')
        else:
            r_data_cpy = list(r_data)
            r_data_cpy[p_c] = '@'
            print(*r_data_cpy, sep='')

SANTA_DEBUG = False

if SANTA_DEBUG:
    print("Start")
    draw_field(pos)

for i in iter_instr():
    pos = do_move(pos, i)
    if SANTA_DEBUG:
        print("Move", i)
        draw_field(pos)

end_row, end_col = to_row_col(pos)
gps_pos = 100 * end_row + end_col
if SANTA_DEBUG: print("End pos.", gps_pos)

def box_gps_sum():
    gps_sum = 0
    for r, r_data in enumerate(field):
        for ci, c in enumerate(r_data):
            if c == 'O':
                gps_sum += 100 * r + ci
    return gps_sum

print("Sum boxes", box_gps_sum())
