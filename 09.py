#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
pos = Point(0,0)
pos_t = Point(0,0)
seen = {pos}

def move(p, x, y):
	return Point(p.x + x, p.y + y)

def sgn(n):
	if n < 0:
		return -1
	elif n > 0:
		return 1
	else:
		return 0

def follow(head, tail):
	new_x, new_y = tail
	dx = head.x - tail.x
	dy = head.y - tail.y
	if abs(dx) > 1 or abs(dy) > 1:
		mx, my = sgn(dx), sgn(dy)
		new_x += mx
		new_y += my
	n = Point(new_x, new_y)
	seen.add(n)
	return n

def printpos(head, tail, mx, my):
	for y in range(my + 1):
		print()
		for x in range(my + 1):
			c = ' '
			if head.x == x and head.y == y:
				c = 'H'
			elif tail.x == x and tail.y == y:
				c = 'T'
			print(c, end='')

def printset(s):
	mx = max(s, key=lambda e:e.x).x
	my = max(s, key=lambda e:e.y).y
	print(mx, my)
	print(s)
	for y in range(my + 1):
		print(''.join(['X' if Point(x,y) in s else ' ' for x in range(mx + 1)]))

with open('9.input', 'r') as f:
	while l:=f.readline():
		d, steps = l.split()
		for i in range(int(steps)):
			if d == 'U':
				pos = move(pos, 0, 1)
			elif d == 'D':
				pos = move(pos, 0, -1)
			elif d == 'R':
				pos = move(pos, 1, 0)
			else:
				pos = move(pos, -1, 0)
			pos_t = follow(pos, pos_t)
	printset(seen)
	print("Num seen", len(seen))

# Part 2:
rope = [Point(0,0) for _ in range(10)]
seen2 = set()
with open('9.input', 'r') as f:
	while l:=f.readline():
		d, steps = l.split()
		head = rope[0]
		for i in range(int(steps)):
			if d == 'U':
				head = move(head, 0, 1)
			elif d == 'D':
				head = move(head, 0, -1)
			elif d == 'R':
				head = move(head, 1, 0)
			else:
				head = move(head, -1, 0)
			rope[0] = head
			for part in range(1, len(rope)):
				local_head = rope[part - 1]
				local_tail = rope[part]
				new_local_tail = follow(local_head, local_tail)
				rope[part] = new_local_tail
			tail = rope[-1]
			seen2.add(tail)
	print("New seen", seen2, "#=", len(seen2))
