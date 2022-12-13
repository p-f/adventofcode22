#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import cmp_to_key

div1 = [[2]]
div2 = [[6]]

def compare(first, second):
	#print('Comparing', first, second)
	if isinstance(first, list) and isinstance(second, list):
		for l,r in zip(first, second):
			if (c := compare(l, r)) != 0:
				return c
		# Either same size but equal, or one is longer
		return compare(len(first), len(second))
	elif isinstance(first, int) and isinstance(second, int):
		return second - first
	else:
		first_list = first if isinstance(first, list) else [first]
		second_list = second if isinstance(second, list) else [second]
		return compare(first_list, second_list)

def lines_in_order(first, second):
	first = eval(first)
	second = eval(second)
	return compare(first, second) > 0

def order_all(lines):
	arrays = list(map(eval, lines))
	arrays.append(div1)
	arrays.append(div2)
	arrays.sort(key=cmp_to_key(compare))
	return arrays

with open('13.input', 'r') as f:
	buff = []
	all_lines = []
	index = 1
	result = 0
	while l:=f.readline():
		l = l.strip()
		if len(l) > 0:
			buff.append(l)
			all_lines.append(l)
		if len(buff) == 2:
			if lines_in_order(buff[0], buff[1]):
				print('In order', buff[0], buff[1])
				result += index
			else:
				print('Not in order', buff[0], buff[1])
			buff.clear()
			index += 1
	print('Result', result)
	sorted_lines = order_all(all_lines)
	sorted_lines.reverse()
	div1_pos = 0
	div2_pos = 0
	for idx, s in enumerate(sorted_lines):
		if compare(s, div1) == 0:
			print('Found divider one at', div1_pos := idx + 1)
		elif compare(s, div2) == 0:
			print('Found divider two at', div2_pos := idx + 1)
	print('Result 2', div1_pos * div2_pos)
