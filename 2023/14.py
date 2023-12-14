# -*- coding: utf-8 -*-

field = []

with open('14.input', 'r') as f:
    while l:=f.readline():
        field.append(list(l.strip()))

NUM_ROWS = len(field)
NUM_COLS = len(field[0])

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

def move_down():
    for rownr in range(NUM_ROWS - 1):
        for colnr, val in enumerate(field[rownr]):
            if val != 'O':
                continue
            for potential_row in range(rownr + 1, NUM_ROWS):
                if field[potential_row][colnr] == '.':
                    field[rownr][colnr] = '.'
                    field[potential_row][colnr] = 'O'
                    break
                if field[potential_row][colnr] == '#':
                    break

def move_left():
    for colnr in range(NUM_COLS - 1, 0, -1):
        for rownr in range(NUM_ROWS):
            if field[rownr][colnr] != 'O':
                continue
            for potential_pos in range(colnr - 1, -1, -1):
                if field[rownr][potential_pos] == '.':
                    field[rownr][colnr] = '.'
                    field[rownr][potential_pos] = 'O'
                    break
                if field[rownr][potential_pos] == '#':
                    break

def move_right():
    for colnr in range(NUM_COLS - 1):
        for rownr in range(NUM_ROWS):
            if field[rownr][colnr] != 'O':
                continue
            for potential_col in range(colnr + 1, NUM_COLS):
                if field[rownr][potential_col] == '.':
                    field[rownr][colnr] = '.'
                    field[rownr][potential_col] = 'O'
                    break
                if field[rownr][potential_col] == '#':
                    break

def cycle():
    move_up()
    move_left()
    move_down()
    move_right()

def weight():
    total_weight = 0
    for rownr, row in enumerate(field):
        total_weight += sum(NUM_ROWS - rownr for val in row if val == 'O')
    return total_weight

def part1():
    move_up()
    for r in field:
        print(''.join(r))
    print(weight())

def fieldhash():
    def code(c):
        if c == '.': return 1
        if c == '#': return 2
        return 3
    total_hash = 0
    for line in field:
        for c in line:
            total_hash = code(c) + 10 * total_hash
    return total_hash

hashes = []
def add_or_find_hash():
    current_hash = fieldhash()
    for i, oldhash in enumerate(hashes):
        if current_hash == oldhash:
            return i + 1
    hashes.append(current_hash)
    return -1

TOTAL_STEPS = 1000000000

def part2():
    steps_done = 0
    cycle_found = False
    while steps_done < TOTAL_STEPS:
        cycle()
        steps_done += 1
        h = add_or_find_hash()
        if h != -1 and not cycle_found:
            cycle_found = True
            print('Found cycle from', h, 'at', steps_done)
            diff = steps_done - h
            print('Cycle lenght is', diff)
            to_skip = (TOTAL_STEPS - steps_done) // diff * diff
            print('Skipping', to_skip)
            steps_done += to_skip
            print('Now at ', steps_done)
    print(weight())

#for r in field:
#    print(''.join(r))

part2()
