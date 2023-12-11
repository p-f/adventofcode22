# -*- coding: utf-8 -*-

from santashelpers import parse_numbers

sequences = []
with open('09.input', 'r') as f:
    while l:=f.readline():
        sequences.append(parse_numbers(l))

def extrapolate_sequence(seq) -> int:
    diff = [-1]
    res = seq[-1]
    def all_zeros(data):
        for d in data:
            if d != 0: return False
        return True
    while not all_zeros(diff):
        diff = []
        for i in range(len(seq) - 1):
            diff.append(seq[i + 1] - seq[i])
        res += diff[-1]
        seq = diff
    return res

total_extra = 0
for s in sequences:
    print('Sequence', s)
    s_ex = extrapolate_sequence(s)
    print('Extra: ', s_ex)
    total_extra += s_ex
print('Sum of extrapolated value:', total_extra)
