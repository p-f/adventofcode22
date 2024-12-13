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

# Part 2

def conv_btn(btn):
    return ButtonRule(btn.ax, btn.ay, btn.bx, btn.by, 10000000000000 + btn.px, 10000000000000 + btn.py)

# a * ax + b * bx = px
# a = (px - b * bx) / ax
# a * ay + b * by = py
# a = (py - b * by) / ay
# (px - b * bx) / ax = (py - b * by) / ay
# ay (px - b * bx) = ax (py - b * by)
# ay px - ay b bx = ax py - ax b by
# ay px - ax py = -ax b by + ay b bx
# ay px - ax py = b (ay bx - ax by)
# b = (ay px - ax py) / (ay bx - ax by)

def calc_b(btn):
    return (btn.ay * btn.px - btn.ax * btn.py) / (btn.ay * btn.bx - btn.ax * btn.by)

def calc_a(btn, b):
    return (btn.px - b * btn.bx) / (btn.ax)

total_cost = 0
for btn in buttons:
    btn2 = conv_btn(btn)
    b = calc_b(btn2)
    a = calc_a(btn2, b)
    if a >= 0 and b >= 0 and int(a) == a and int(b) == b:
        total_cost += 3 * a + b
print(total_cost)
