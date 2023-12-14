# -*- coding: utf-8 -*-

field = []

with open('14.input', 'r') as f:
    while l:=f.readline():
        field.append(list(l.strip()))

NUM_ROWS = len(field)

def move_up():
    for rownr in range(NUM_ROWS - 1, 0, -1):
        for colnr, val in enumerate(field[rownr]):
            if val == 'O':
                for potential_pos in range(rownr - 1, -1, -1):
                    if field[potential_pos][colnr] == '.':
                        field[rownr][colnr] = '.'
                        field[potential_pos][colnr] = 'O'
                        break
                    if field[potential_pos][colnr] == '#':
                        break

def weight():
    total_weight = 0
    for rownr, row in enumerate(field):
        total_weight += sum(NUM_ROWS - rownr for val in row if val == 'O')
    return total_weight

move_up()
for r in field:
    print(''.join(r))
print(weight())

