#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from functools import reduce


def common_items(line):
	line = line.strip()
	ln = len(line) // 2
	right = set(line[:ln])
	left = set(line[ln:])
	return left.intersection(right)

def common_in_lines(lines):
	return reduce(set.intersection, map(lambda x:set(x.strip()), lines))

def cost(item):
	a,z,A = ord('a'),ord('z'),ord('A')
	code = ord(item) + 1
	if code in range(a, z + 2):
		return code - a
	else:
		return code - A + 26

def part1(f):
	sum_total = 0
	while l := f.readline():
		ci = common_items(l)
		total_common = sum(map(cost, ci))
		print('Common:', ci, 'Cost:', total_common)
		sum_total += total_common
	print('Sum common all', sum_total)

def part2(f):
	sum_total = 0
	buf = []
	while l := f.readline():
		buf.append(l)
		if len(buf) == 3:
			cil = common_in_lines(buf)
			print('Common in lines:', cil)
			sum_total += sum(map(cost, cil))
			buf.clear()
	print('Sum common all', sum_total)

def main(args):
	with open('3.input', 'r') as f:
		part1(f)
	with open('3.input', 'r') as f:
		part2(f)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
