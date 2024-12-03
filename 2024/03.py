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
