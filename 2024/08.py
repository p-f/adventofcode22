#!/usr/bin/env python
# -*- coding: utf-8 -*-

antennas = dict()

n_rows = 0
n_cols = 0

with open('08.input', 'r') as f:
    line = 0
    while l:=f.readline():
        for idx, char in enumerate(l):
            if char.isalnum():
                if char not in antennas: antennas[char] = list()
                antennas[char].append((line, idx,))
        line += 1
        if n_cols == 0:
            n_cols = len(l.strip())
    n_rows = line

def in_grid(r, c):
    return r >= 0 and c >= 0 and r < n_rows and c < n_cols

def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

anti = set()
for antenna in antennas:
    locations = antennas[antenna]
    for l1 in locations:
        for l2 in locations:
            dr, dc = l2[0] - l1[0], l2[1] - l1[1]
            anti1 = l1[0] - dr, l1[1] - dc
            anti2 = l2[0] + dr, l2[1] + dc
            if in_grid(*anti1) and anti1 not in locations:
                anti.add(anti1)
                d1, d2 = distance(anti1, l1), distance(anti1, l2)
                assert (d1 == 2 * d2 or d2 == 2 * d1)

            if in_grid(*anti2) and anti2 not in locations:
                anti.add(anti2)
                d1, d2 = distance(anti2, l1), distance(anti2, l2)
                assert (d1 == 2 * d2 or d2 == 2 * d1)

print(len(anti), sorted(anti))

# Part 2

anti.clear()

for antenna in antennas:
    locations = antennas[antenna]
    for l1 in locations:
        for l2 in locations:
            dr, dc = l2[0] - l1[0], l2[1] - l1[1]
            if dr == 0 and dc == 0: continue
            dm = 0
            while True:
                dm += 1
                anti1 = l1[0] - (dm * dr), l1[1] - (dm * dc)
                anti2 = l2[0] + (dm * dr), l2[1] + (dm * dc)
                anti3 = l1[0] + (dm * dr), l1[1] + (dm * dc)
                anti4 = l2[0] - (dm * dr), l2[1] - (dm * dc)
                any_in_range = False
                for a in (anti1, anti2, anti3, anti4,):
                    if in_grid(*a):
                        any_in_range = True
                        anti.add(a)
                if not any_in_range: break
print(len(anti))
