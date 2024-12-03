#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

with open('03.input', 'r') as f:
    code = []
    while l:=f.readline():
        code.append(l)

result = 0
mul_instr = re.compile("mul\(([0-9]+),([0-9]+)\)")

for line in code:
    for l, r in mul_instr.findall(line):
       result += int(l) * int(r)

print(result)

# Part 2
instr = re.compile("(mul|do|don't)\((([0-9]+),([0-9]+))?\)")

result = 0
do = True

for line in code:
    for i, arg, l, r in instr.findall(line):
        if i == "mul" and arg and do:
            result += int(l) * int(r)
        elif i == "do" and not arg:
            do = True
        elif i == "don't" and not arg:
            do = False

print(result)
