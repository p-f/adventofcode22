#!/usr/bin/env python
# -*- coding: utf-8 -*-

from santashelpers import parse_numbers, pairs
from collections import Counter

with open('02.input', 'r') as f:
    numbers = []
    while l:=f.readline():
        numbers.append(parse_numbers(l))
    rulecount = 0
    for rule in numbers:
        valid_rule = True
        for l, r in pairs(rule):
            if abs(l - r) < 1 or abs(l - r) > 3:
                valid_rule = False
                break
        if valid_rule and (rule == sorted(rule) or rule[::-1] == sorted(rule)):
            rulecount += 1
    print(rulecount)
