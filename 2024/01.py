#!/usr/bin/env python
# -*- coding: utf-8 -*-

from santashelpers import parse_numbers, transpose

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
