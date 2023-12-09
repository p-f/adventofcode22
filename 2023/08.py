# -*- coding: utf-8 -*-

import re
from functools import reduce
from math import lcm

instr = None
network = dict()

net_pattern = re.compile(r'([A-Z12]+) = \(([A-Z12]+)\, ([A-Z12]+)\)')

with open('08.input', 'r') as f:
    instr = f.readline().strip()
    f.readline()
    while l:=f.readline():
        m = net_pattern.match(l)
        st, l, r = m.group(1,2,3)
        network[st] = (l, r,)

def count_steps(startpos, endpos):
    steps = 0
    pos = startpos
    while not pos.endswith(endpos):
        for i in instr:
            pos = network[pos][0 if i == 'L' else 1]
            steps += 1
            if pos.endswith(endpos): break
        print(f'After {steps} steps at {pos} - {startpos} -> {endpos}')
    return steps

print('Part 1', count_steps('AAA', 'ZZZ'))

ghosts = [k for k in network if k[-1] == 'A']

print(ghosts)

ghost_steps = []

for g in ghosts:
    s = count_steps(g, 'Z')
    print(f'Steps for {g}: {s}') 
    ghost_steps.append(s)

print('Part 2:', reduce(lcm, ghost_steps))
