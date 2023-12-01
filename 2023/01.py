#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

codec = (
	('one', 1,),
	('two', 2,),
	('three', 3,),
	('four', 4,),
	('five', 5,),
	('six', 6,),
	('seven', 7,),
	('eight', 8,),
	('nine', 9,),
)

def sum_dig(line: str) -> int:
	replaced = re.sub('[^0-9]', '', line)
	if len(replaced) < 1: return 0
	first, last = replaced[0], replaced[-1]
	return int(first + last)

with open('01.input', 'r') as f:
	sum_1 = 0
	sum_2 = 0
	while l:=f.readline():
		l = l.strip()
		digits = ''
		for i in range(len(l)):
			for spelled, digit in codec:
				if l[i] == str(digit) or l[i:].startswith(spelled):
					digits += str(digit)
					continue
		sum_1 += sum_dig(l)
		sum_2 += sum_dig(digits)
	print(sum_1)
	print(sum_2)
