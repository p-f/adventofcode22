# -*- coding: utf-8 -*-

field = []

with open('16.input', 'r') as f:
    while l:=f.readline():
        field.append(list(l.strip()))

NUM_ROWS = len(field)
NUM_COLS = len(field[0])

UP    = (-1,  0,)
DOWN  = ( 1,  0,)
LEFT  = ( 0, -1,)
RIGHT = ( 0,  1,)

V_UP = 0b1
V_DOWN = 0b10
V_RIGHT = 0b100
V_LEFT = 0b1000

def dirmarker(direction):
    if direction == UP:
        return V_UP
    elif direction == DOWN:
        return V_DOWN
    elif direction == RIGHT:
        return V_RIGHT
    else:
        return V_LEFT

visited = [[0 for _ in range(NUM_COLS)] for _ in range(NUM_ROWS)]

def outofbounds(row, col):
    return row < 0 or col < 0 or row >= NUM_ROWS or col >= NUM_COLS

def visit(row, col, direction):
    while True:
        print('Checking', row, col, 'in', direction)
        if outofbounds(row, col):
            return
        marker = dirmarker(direction)
        if marker & visited[row][col]:
            return # Already visited
        visited[row][col] |= marker
        op = field[row][col]
        if op == '|' and (direction == RIGHT or direction == LEFT):
            visit(row - 1, col, UP)
            visit(row + 1, col, DOWN)
            return
        elif op == '-' and (direction == UP or direction == DOWN):
            visit(row, col + 1, RIGHT)
            visit(row, col - 1, LEFT)
            return
        elif op == '/':
            if direction == UP:
                visit(row, col + 1, RIGHT)
            elif direction == DOWN:
                visit(row, col - 1, LEFT)
            elif direction == RIGHT:
                visit(row - 1, col, UP)
            else: #left
                visit(row + 1, col, DOWN)
            return
        elif op == '\\':
            if direction == UP:
                visit(row, col - 1, LEFT)
            elif direction == DOWN:
                visit(row, col + 1, RIGHT)
            elif direction == RIGHT:
                visit(row + 1, col, DOWN)
            else: #left
                visit(row - 1, col, UP)
            return
        row += direction[0]
        col += direction[1]

def print_visited():
    for row in visited:
        print(''.join(('#' if c else '.') for c in row))

def count_visited():
    visitcount = 0
    for row in visited:
        for cell in row:
            if cell:
                visitcount += 1
    return visitcount

visit(0, 0, RIGHT)
print_visited()

print('Number total visited', count_visited())
