# -*- coding: utf-8 -*-

import re

instr = None
network = dict()

net_pattern = re.compile(r'([A-Z]+) = \(([A-Z]+)\, ([A-Z]+)\)')

with open('08.input', 'r') as f:
    instr = f.readline().strip()
    f.readline()
    while l:=f.readline():
        m = net_pattern.match(l)
        st, l, r = m.group(1,2,3)
        network[st] = (l, r,)

steps = 0
pos = 'AAA'
while pos != 'ZZZ':
    for i in instr:
        pos = network[pos][0 if i == 'L' else 1]
        steps += 1
        if pos == 'ZZZ': break
    print(f'After {steps} steps at {pos}')
