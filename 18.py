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


def part1(drops_set):
	all_sides = 0
	for d in drops_set:
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

print('Part 1')
part1(set(droplets_pos))


max_x = max(map(itemgetter(0), droplets_pos)) + 1
max_y = max(map(itemgetter(1), droplets_pos)) + 1
max_z = max(map(itemgetter(2), droplets_pos)) + 1
none, filled, outer = 0, 1, 2
cube = [[[none for _ in range(max_z)] for _ in range(max_y)] for _ in range(max_x)]
for d in droplets_pos:
	cube[d.x][d.y][d.z] = filled

def neighbors(x, y, z):
	if z > 0: yield Drop(x, y, z - 1)
	if z < (max_z - 1): yield Drop(x, y, z + 1)
	if y > 0: yield Drop(x, y - 1, z)
	if y < (max_y - 1): yield Drop(x, y + 1, z)
	if x > 0: yield Drop(x - 1, y, z)
	if x < (max_x - 1): yield Drop(x + 1, y, z)

def mark_outer():
	def not_filled(d):
		return cube[d.x][d.y][d.z] == none
	def marked(d):
		return cube[d.x][d.y][d.z] == outer
	def mark(d):
		cube[d.x][d.y][d.z] = outer
	start = Drop(0,0,0)
	assert cube[start.x][start.y][start.z] == 0
	queue = list()
	queue.append(start)
	mark(start)
	while queue:
		current = queue.pop()
		for n in neighbors(*current):
			if not_filled(n) and not marked(n):
				queue.append(n)
				mark(n)

def find_and_fill_inner():
	for x in range(max_x):
		for y in range(max_y):
			for z in range(max_z):
				if cube[x][y][z] == none or cube[x][y][z] == filled:
					yield Drop(x,y,z)

print('Part 2')
mark_outer()
new_filled = set(find_and_fill_inner())
part1(new_filled)


