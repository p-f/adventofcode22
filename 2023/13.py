# -*- coding: utf-8 -*-

from santashelpers import chunks, transpose

fields = []

with open('13.input', 'r') as f:
    for chunk in chunks(f):
        fields.append(chunk)

def str_diff(l, r, max_diff = 2):
    diff = 0
    for i in range(len(l)):
        if l[i] != r[i]:
            diff += 1
            if diff >= max_diff:
                return diff
    return diff

def find_reflection(field, expected_diff = 0, exclude = -1) -> int:
    for r in range(1, len(field)):
        #print(f'Trying {r-1}><{r}')
        total_diff = 0
        for pair in range(min(r, len(field) - r)):
            li, ri = r - pair -1, r + pair
            total_diff += str_diff(field[li], field[ri])
        if total_diff == expected_diff and r != exclude:
            return r
    return 0

row_based = 0
col_based = 0

row_based2 = 0
col_based2 = 0

for f in fields:
    r = find_reflection(f)
    row_based += r
    f_trans = transpose(f)
    c = find_reflection(f_trans)
    col_based += c
    # Find alternatives
    r_alt = find_reflection(f, 1, r)
    c_alt = find_reflection(f_trans, 1, c)
    assert (r, c,) != (r_alt, c_alt,)
    row_based2 += r_alt
    col_based2 += c_alt

print(row_based * 100 + col_based)
print(row_based2 * 100 + col_based2)
