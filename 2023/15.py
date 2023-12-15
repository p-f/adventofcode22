# -*- coding: utf-8 -*-

splits = []

with open('15.input', 'r') as f:
    while l:=f.readline():
        splits += l.strip().split(',')

def hash(instr):
    hashval = 0
    for c in instr:
        hashval += ord(c)
        hashval = (hashval * 17) % 256
    return hashval

def part1():
    sum_hashes = 0
    for s in splits:
        sh = hash(s)
        print(s, sh)
        sum_hashes += sh
    return sum_hashes

#print(part1())

import re
boxes = [(list(), dict(),) for _ in range(256)]

rule_pattern = re.compile('([a-z]+)(-|=)([0-9])*')

for s in splits:
    label, op, focal_length = rule_pattern.match(s).group(1, 2, 3)
    box = hash(label)
    box_inst = boxes[box]
    if op == '-':
        if label in box_inst[0]:
            box_inst[0].remove(label)
    else: # =
        if label not in box_inst[0]:
            box_inst[0].append(label)
        box_inst[1][label] = int(focal_length)

total_power = 0
for bn, b in enumerate(boxes):
    for slot, lens in enumerate(b[0]):
        total_power += (1 + bn) * b[1][lens] * (1 + slot)
print(total_power)
