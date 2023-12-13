# -*- coding: utf-8 -*-

from santashelpers import chunks, transpose

fields = []

with open('13.input', 'r') as f:
    for chunk in chunks(f):
        fields.append(chunk)

def find_reflection(field) -> int:
    for r in range(1, len(field)):
        #print(f'Trying {r-1}><{r}')
        for pair in range(min(r, len(field) - r)):
            li, ri = r - pair -1, r + pair
            if field[li] != field[ri]:
                break
        else:
            return r
    return -1

row_based = 0
col_based = 0

for f in fields:
    r = find_reflection(f)
    if r >= 0:
        row_based += r
    c = find_reflection(transpose(f))
    if c >= 0:
        col_based += c
    if r < 0 and c < 0:
        print(f'Warn, none at \n{"\n".join(f)}')

print(row_based * 100 + col_based)
