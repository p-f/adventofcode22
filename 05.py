#!/usr/bin/env python
# -*- coding: utf-8 -*-

from re import match

def parse_header(f):
	stacks = None
	while l := f.readline():
		if '[' not in l:
			f.readline() #drop
			return stacks
		items = l[1::4]
		if stacks is None:
			print('Init #stacks:' , len(items))
			stacks = [[] for _ in items]
		for index, item in enumerate(items):
			if item != ' ':
				stacks[index].insert(0, item)
	raise Error()

def main(args):
	with open('5.input', 'r') as f:
		stacks = parse_header(f)
		print(stacks)
		while l := f.readline():
			count, from_stack, to_stack =  tuple(map(int, match('move (\d+) from (\d+) to (\d+)', l).group(1,2,3)))
			source = stacks[from_stack - 1]
			dest = stacks[to_stack - 1]
			# Part 1:
			# for _ in range(count):
			#	item = source.pop()
			#	dest.append(item)
			dest += source[-count:]
			for _ in range(count):
				source.pop()
		print('Result stacks:', stacks)
		print(''.join([stack.pop() for stack in stacks]))
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
