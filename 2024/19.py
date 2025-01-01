#!/usr/bin/env python
# -*- coding: utf-8 -*-

from santashelpers import chunks
from functools import lru_cache

all_towels = []
designs = None

with open("19.input", "r") as f:
    tow, designs = chunks(f)
    all_towels = tow[0].split(", ")

shortest_towel_design = min(map(len, all_towels))
longest_towel_design = max(map(len, all_towels))

@lru_cache
def try_make_design(target_design :str):
    if len(target_design) == 0: return 1
    if len(target_design) < shortest_towel_design: return 0
    possible_design_count = 0
    for t in all_towels:
        if target_design.startswith(t):
            possible_design_count += try_make_design(target_design[len(t):])
    return possible_design_count

possible_designs = 0
possible_design_combinations = 0
for t_d in designs:
    #print("Design", t_d)
    if m_d := try_make_design(t_d): possible_designs += 1
    possible_design_combinations += m_d
    #print("Combibations", possible_design_combinations)
print(possible_designs)
print(possible_design_combinations)