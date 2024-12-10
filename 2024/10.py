#!/usr/bin/env python
# -*- coding: utf-8 -*-

from santashelpers import coordinates, Direction, to_row_col

field = []
with open('10.input', 'r') as f:
    while l := f.readline():
        row = []
        for c in l.strip():
            row.append(int(c) if c != '.' else -1)
        field.append(row)

n_rows = len(field)
n_cols = len(field[0])

def height(coord):
    r, c = to_row_col(coord)
    return field[r][c]

def in_field(coord):
    r, c = to_row_col(coord)
    return r >= 0 and c >= 0 and r < n_rows and c < n_cols

def find_peaks(current_coord):
    current_height = height(current_coord)
    if current_height == 9:
        return [current_coord]
    peaks_reachable = list()
    for d in Direction:
        next_pos = current_coord + d.value
        if in_field(next_pos) and height(next_pos) == current_height + 1:
            for p in find_peaks(next_pos):
                peaks_reachable.append(p)
    return peaks_reachable

all_peaks = 0
all_paths = 0
for r in range(n_rows):
    for c in range(n_cols):
        if height(coord := coordinates(r, c)) == 0:
            peaks = find_peaks(coord)
            all_peaks += len(set(peaks))
            all_paths += len(peaks)
print(all_peaks)
print(all_paths)
