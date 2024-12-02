#!/usr/bin/env python
# -*- coding: utf-8 -*-

from santashelpers import parse_numbers, pairs
from collections import Counter

with open('02.input', 'r') as f:
    numbers = []
    while l:=f.readline():
        numbers.append(parse_numbers(l))
    def is_valid(rule):
        valid_rule = True
        for l, r in pairs(rule):
            if abs(l - r) < 1 or abs(l - r) > 3:
                valid_rule = False
                break
        if valid_rule and (rule == sorted(rule) or rule[::-1] == sorted(rule)):
            return True
        else: return False
    rulecount = 0
    for rule in numbers:
        if is_valid(rule): rulecount += 1
    print(rulecount)
    # Part 2
    def skip_item(data, skip_index):
        for i, item in enumerate(data):
            if i != skip_index: yield item
    def is_valid_with_skips(rule):
        for skip in range(-1, len(rule)):
            if is_valid(list(skip_item(rule, skip))):
                print("Valid with skip", skip, list(skip_item(rule, skip)))
                return True
        return False
    rulecount = 0
    for rule in numbers:
        print(rule)
        if is_valid_with_skips(rule): rulecount += 1
    print(rulecount)
