# -*- coding: utf-8 -*-

from collections import namedtuple
from santashelpers import parse_numbers, chunks
from typing import List

MapEntry = namedtuple('MapEntry', ['dst', 'src', 'len'])

def apply_map(mapdata: List[MapEntry], seed: int) -> int:
	for me in mapdata:
		if seed in range(me.src, me.src + me.len):
			return seed + (me.dst - me.src)
	return seed


seeds = None
maps = []
with open('05.input', 'r') as f:
	seeds = parse_numbers(f.readline().split(':')[1])
	for c in chunks(f):
		maps.append([MapEntry(*parse_numbers(l)) for l in c[1:]])

for m in maps:
	seeds = [apply_map(m, s) for s in seeds]
print('Lowest location', min(seeds))
