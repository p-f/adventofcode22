# -*- coding: utf-8 -*-

field = []

with open('11.input', 'r') as f:
    while l:=f.readline():
        field.append(l.strip())

# Scan for empty columns
empty_cols = set()
for col_nr in range(len(field[0])):
    for row in field:
        if row[col_nr] == '#':
            break
    else:
        empty_cols.add(col_nr)

print('Empty columns', empty_cols)

galaxies = []

adj_lineno = 0
for line in field:
    adj_charno = 0
    for charno, char in enumerate(line):
        if char == '#':
            galaxies.append((adj_lineno, adj_charno,))
        if charno in empty_cols:
            # Empty column -> Adjust col number
            adj_charno += 1
        adj_charno += 1
    # Empty line -> Adjust line number
    if not '#' in line:
        adj_lineno += 1
    adj_lineno += 1

def ma_dist(ga, gb):
    return abs(ga[0] - gb[0]) + abs(ga[1] - gb[1])

print('Actual galaxy positions', galaxies)

sum_all = 0
for g1 in galaxies:
    for g2 in galaxies:
        if g1 != g2:
            sum_all += ma_dist(g1, g2)
sum_all /= 2
print('Total sum', sum_all)
