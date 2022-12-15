#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import namedtuple

none, wall, drop = 0, 1, 2
Pair = namedtuple('Pair', ['x', 'y'])
part2 = True

def pairs(v):
	for i in range(len(v) - 1):
		yield v[i], v[i + 1]

def irange(start, end):
	return range(start, end + (1 if end >= start else -1), 1 if end >= start else -1)

def point_range(point1, point2):
	if point1.x == point2.x:
		return map(lambda y:Pair(point1.x, y), irange(point1.y, point2.y))
	else:
		return map(lambda x:Pair(x, point1.y), irange(point1.x, point2.x))

paths = []
min_x, max_x, max_y = None, None, None
with open('14.input', 'r') as f:
	while l:=f.readline():
		path = tuple()
		for path_part in l.strip().split(' -> '):
			x,y = path_part.split(',')
			x, y = int(x), int(y)
			if not min_x:
				min_x = x
				max_x = x
				max_y = y
			else:
				min_x = min(min_x, x)
				max_x = max(max_x, x)
				max_y = max(max_y, y)
			path += (Pair(x, y),)
		print('Input path: ', path)
		paths.append(path)
if part2:
	max_y += 2
	min_x = 500 - max_y
	max_x = 500 + max_y
	paths.append((Pair(min_x, max_y), Pair(max_x, max_y),))
width = max_x - min_x
field = [[none for _ in range(width + 1)] for _ in range(max_y + 1)]

def set(x, y, value):
	field[y][x - min_x] = value
	if value == drop:
		print('Dropping to ', x, y)

def get(x, y):
	f = field[y][x - min_x]
	return f

def print_field():
	def fv(c):
		if c == none:
			return ' '
		elif c == wall:
			return '#'
		else:
			return 'o'
	print('-' * (1 + len(field[0])))
	for line in field:
		print('|' + ''.join(map(fv, line)))

for path in paths:
	for start, end in pairs(path):
		for point in point_range(start, end):
			set(point.x, point.y, wall)

def do_drop(x = 500, y = 0):
	c_x, c_y = x, y
	while True:
		if c_y > max_y:
			return False
		elif c_x < min_x:
			return False
		elif c_x > max_x:
			return False
		if get(c_x, c_y + 1) == 0:
			c_y += 1
		elif get(c_x - 1, c_y + 1) == 0:
			c_y += 1
			c_x -= 1
		elif get(c_x + 1, c_y + 1) == 0:
			c_y += 1
			c_x += 1
		else:
			break
	set(c_x, c_y, drop)
	return Pair(c_x, c_y)

drops = 0
drops_part2 = None
while True:
	d = do_drop()
	if not d:
		break
	elif part2 and d == Pair(500, 0):
		drops_part2 = drops + 1
		break
	drops += 1
	if not part2: print_field()
print_field()
print('Drops', drops)
print('Part 2', drops_part2)
