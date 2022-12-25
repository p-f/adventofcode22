#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
field = []
start, end = None, None

def height(p: Point) -> int:
	if p.y in range(len(field)) and p.x in range(len(field[p.y])):
		char = field[p.y][p.x]
		if char == 'S':
			return ord('a') - 1
		elif char == 'E':
			return ord('z') + 1
		else:
			return ord(char)
	else:
		return 1000

def move(p, x, y):
	return Point(p.x + x, p.y + y)

global min_a
min_a = 10000000

def scanfield(position, current_length, distances):
	if current_length > 400:
		return
	global min_a
	if distances[position.x][position.y] <= current_length:
		return
	else:
		distances[position.x][position.y] = current_length
	next_possible = move(position, 1, 0), move(position, 0, 1), move(position, -1, 0), move(position, 0, -1)
	moves_to_take = []
	current_height = height(position)
	if current_height == ord('a'):
		if current_length < min_a:
			min_a = current_length
		else:
			return
	if current_height == height(end):
		print(f'Found end at {current_length} steps')
	for try_move in next_possible:
		height_move = height(try_move)
		if height_move - current_height <= 1:
			moves_to_take.append(try_move)
	for m in moves_to_take:
		scanfield(m, current_length + 1, distances)


with open('12.input', 'r') as f:
	line = 0
	while l:=f.readline():
		l = l.strip()
		field.append(l)
		if (s:= l.find('S')) != -1:
			start = Point(s, line)
		if (s:= l.find('E')) != -1:
			end = Point(s, line)
		line += 1
	print(f'Start: {start} End: {end}')
	dim = max(len(field), len(field[0]))
	distances = [[100000 for _ in range(dim)] for _ in range(dim)]
	scanfield(start, 0, distances)
	print()
	print('Result 1', distances[end.x][end.y])
	

