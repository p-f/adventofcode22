#!/usr/bin/env python
# -*- coding: utf-8 -*-
#


def main(args):
	max_cal = []
	with open('1.input', 'r') as in_file:
		cur = 0
		while (l := in_file.readline()):
			l = l.strip()
			if len(l) > 0:
				cur += int(l)
			else:
				if len(max_cal) < 3:
					max_cal.append(cur)
				elif cur >= min(max_cal):
					max_cal.append(cur)
					max_cal = sorted(max_cal)[-3:]
					print("new", max_cal)
				cur = 0
	print(max_cal)
	print(sum(max_cal))
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
