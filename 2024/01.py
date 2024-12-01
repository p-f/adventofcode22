#!/usr/bin/env python
# -*- coding: utf-8 -*-

from santashelpers import parse_numbers, transpose
from collections import Counter

with open('01.input', 'r') as f:
    numbers = []
    while l:=f.readline():
        numbers.append(parse_numbers(l))
    left, right = transpose(numbers)
    left.sort()
    right.sort()
    diff_sum = 0
    for i in range(len(left)):
        diff_sum += abs(left[i] - right[i])
    print(diff_sum)
    rcount = Counter(right)
    simm_score = 0
    for l in left:
        simm_score += l * rcount[l]
    print(simm_score)
