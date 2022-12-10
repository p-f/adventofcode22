#!/usr/bin/env python
# -*- coding: utf-8 -*-


from re import match

def parse(line):
	matcher = match(r"(\d+)-(\d+),(\d+)-(\d+)", line)
	return list(map(int, matcher.group(1,2,3,4)))

def part1(f):
	subsets = 0
	overlap = 0
	while l := f.readline():
		parsed = parse(l)
		if (parsed[0] >= parsed[2] and parsed[1] <= parsed[3]) or (parsed[2] >= parsed[0] and parsed[3] <= parsed[1]):
			subsets += 1
		if (set(range(parsed[0], parsed[1] + 1)).intersection(set(range(parsed[2], parsed[3] + 1)))):
			overlap += 1
	print('Subsets', subsets)
	print('Overlap', overlap)


def main(args):
	with open('4.input', 'r') as f:
		part1(f)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
