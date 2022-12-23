#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aoccommon import *
from collections import namedtuple
from operator import itemgetter

Drop = namedtuple('Drop', ['x','y','z'])
droplets_pos = list()

with open('18.input', 'r') as f:
	while l:=f.readline():
		pos = Drop(*map(int, l.strip().split(',')))
		droplets_pos.append(pos)
#max_x = max(map(itemgetter(0), droplets_pos)) + 1
#max_y = max(map(itemgetter(1), droplets_pos)) + 1
#max_z = max(map(itemgetter(2), droplets_pos)) + 1
#cube = [[[False for _ in range(max_z)] for _ in range(max_y)] for _ in range(max_x)]
drops_set = set(droplets_pos)
all_sides = 0
for d in droplets_pos:
	sides = 0
	if Drop(d.x, d.y, d.z - 1) not in drops_set:
		sides += 1
	if Drop(d.x, d.y, d.z + 1) not in drops_set:
		sides += 1
	if Drop(d.x, d.y - 1, d.z) not in drops_set:
		sides += 1
	if Drop(d.x, d.y + 1, d.z) not in drops_set:
		sides += 1
	if Drop(d.x - 1, d.y, d.z) not in drops_set:
		sides += 1
	if Drop(d.x + 1, d.y, d.z) not in drops_set:
		sides += 1
	all_sides += sides
print('All non-covered sides', all_sides)
