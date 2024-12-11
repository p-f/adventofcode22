#!/usr/bin/env python
# -*- coding: utf-8 -*-

from santashelpers import parse_numbers
from collections import Counter

numbers = []

with open('11.input', 'r') as f:
    while l:=f.readline():
        numbers += parse_numbers(l)

num_freq = Counter(numbers)

def try_split_num(n):
    n_str = str(n)
    if len(n_str) % 2 == 1:
        return None
    mid = len(n_str) // 2
    return int(n_str[0:mid]), int(n_str[mid:])

def step(in_freq):
    next_freq = Counter()
    for num, factor in in_freq.items():
        if num == 0:
            next_freq[1] += factor
        elif split := try_split_num(num):
            l, r = split
            next_freq[l] += factor
            next_freq[r] += factor
        else:
            next_freq[2024 * num] += factor
    return next_freq

curr_freq = num_freq
for it_count in range(25):
    print("Iter", it_count, len(curr_freq))
    curr_freq = step(curr_freq)

print(sum(curr_freq.values()))

for it_count in range(50):
    print("Iter", it_count, len(curr_freq))
    curr_freq = step(curr_freq)

print(sum(curr_freq.values()))
