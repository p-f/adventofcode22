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

sum_hashes = 0

for s in splits:
    sh = hash(s)
    print(s, sh)
    sum_hashes += sh

print(sum_hashes)
