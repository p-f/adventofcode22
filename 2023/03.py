#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import namedtuple

Part = namedtuple('Part', ['nr', 'line', 'col'])

def find_parts(l: str, line: int, outlist: list) -> None:
	partnr = None
	for c in range(len(l)):
		if l[c].isdigit():
			if partnr is None:
				partnr = l[c]
			else:
				partnr += l[c]
		elif partnr is not None:
				outlist.append(Part(partnr, line, c - len(partnr)))
				partnr = None
	if partnr is not None:
		outlist.append(Part(partnr, line, len(l) - len(partnr)))

def is_part_adj(field: list, part: Part) -> bool:
	lines, cols = len(field), len(field[0])
	def is_symbol(linenr, colnr):
		s = field[linenr][colnr]
		#print(linenr, colnr, s)
		return (not s.isdigit()) and s != '.'
	#print('Checking ', part)
	for l in range(max(0, part.line - 1), min(lines, part.line + 2)):
		for c in range(max(0, part.col - 1), min(cols, part.col + len(part.nr) + 1)):
			# We also scan characters inside the part, but those are numbers anyway
			if is_symbol(l, c): return True
	return False

with open('03.input', 'r') as f:
	field = []
	parts = []
	line = 0
	while l:=f.readline():
		l = l.strip()
		field.append(l)
		find_parts(l, line, parts)
		line += 1
	part_sum = 0
	for p in parts:
		print(p, 'adjacent?', adj:=is_part_adj(field, p))
		if adj:
			part_sum += int(p.nr)
	print('Part Sum:', part_sum)
