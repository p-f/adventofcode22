#!/usr/bin/env python
# -*- coding: utf-8 -*-

from santashelpers import parse_numbers

page_order = []
page_rules = []
with open('05.input', 'r') as f:
    first_section = True
    while l:=f.readline():
        if len(l.strip()) == 0:
            first_section = False
            continue
        if first_section:
            page_order.append(parse_numbers(l, '|'))
        else:
            page_rules.append(parse_numbers(l, ','))

page_orderset = set(map(tuple, page_order))

def in_order(rule):
    for pos in range(len(rule)):
        cur = rule[pos]
        for before_pos in range(pos):
            bef = rule[before_pos]
            if (cur, bef,) in page_orderset:
                return None
        for after_pos in range(pos + 1, len(rule)):
            aft = rule[after_pos]
            if (aft, cur,) in page_orderset:
                return None
    return rule[len(rule) // 2]

rsum = 0
for r in page_rules:
    o = in_order(r)
    if o:
        rsum += o

print(rsum)
