#!/usr/bin/env python
# -*- coding: utf-8 -*-


def part1(l, sublen = 4):
	ll = len(l)
	print('Total lenght', ll)
	for i in range(sublen, ll):
		sub = l[i-sublen:i]
		if len(set(sub)) == sublen:
			print('Result ', i)
			break

def main(args):
	with open('6.input', 'r') as f:
		l = f.readline().strip()
		part1(l)
		part1(l, 14)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
