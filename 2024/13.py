#!/usr/bin/env python
# -*- coding: utf-8 -*-

from santashelpers import chunks
import re
from collections import namedtuple

numbers = re.compile("[0-9]+")

def extract_numbers(l):
    return tuple(map(int, numbers.findall(l)))

buttons = list()
ButtonRule = namedtuple("ButtonRule", ("ax", "ay", "bx", "by", "px", "py"))

with open('13.input', 'r') as f:
    for chunk in chunks(f):
        button_rule = []
        for l in chunk:
            button_rule += extract_numbers(l)
        buttons.append(ButtonRule(*button_rule))

# a * ax + b * bx = px
# a * ay + b * by = py
# a (ax + ay) + b (bx + by) = px + py
# b (bx + by) = px + py - a(ax + ay)
# b = (px + py - a(ax + ay)) / (bx + by)

def validate_res(btn, a, b):
    return a * btn.ax + b * btn.bx == btn.px and a * btn.ay + b * btn.by == btn.py

def probe_ab(btn):
    def calc_b(a):
        return (btn.px + btn.py - a * (btn.ax + btn.ay)) / (btn.bx + btn.by)
    for val_a in range(101):
        val_b = calc_b(val_a)
        if (val_b != int(val_b) or val_b > 100 or val_b < 0):
            continue
        #assert validate_res(btn, val_a, int(val_b)), f"{btn}, {val_a}, {val_b}"
        # Result may also be too high, just avoid anything that does not fit
        if not validate_res(btn, val_a, val_b):
            continue
        yield val_a, int(val_b)

def mincost_ab(results):
    cost = None
    for a, b in results:
        this_cost = 3 * a + b
        if cost is None:
            cost = this_cost
        elif this_cost < cost:
            cost = this_cost
    if cost is None: cost = 0
    return cost

total_cost = 0
for btn in buttons:
    total_cost += mincost_ab(probe_ab(btn))

print(total_cost)
