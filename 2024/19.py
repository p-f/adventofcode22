#!/usr/bin/env python
# -*- coding: utf-8 -*-

from santashelpers import chunks

all_towels = []
designs = None

with open("19.input", "r") as f:
    tow, designs = chunks(f)
    all_towels = tow[0].split(", ")

shortest_towel_design = min(map(len, all_towels))
longest_towel_design = max(map(len, all_towels))

def try_make_design(target_design :str):
    if target_design in all_towels or len(target_design) == 0: return True
    if len(target_design) < shortest_towel_design: return False
    for t in all_towels:
        if target_design.startswith(t):
            if try_make_design(target_design[len(t):]):
                return True
    return False

possible_designs = 0
for t_d in designs:
    if try_make_design(t_d): possible_designs += 1
print(possible_designs)