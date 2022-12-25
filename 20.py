#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aoccommon import *

numbers_list = list()
num_count = 0
with open('20.input', 'r') as f:
	while l:=f.readline():
		numbers_list.append((int(l.strip()), num_count,))
		num_count += 1

def find(pos):
	for idx, item in enumerate(numbers_list):
		if item[1] == pos:
			return idx

for pos in range(num_count):
	idx = find(pos)
	#print(f'Moving number at position {pos} currently at {idx}')
	item = numbers_list.pop(idx)
	shift = item[0]
	new_pos = idx + shift
	new_pos %= (num_count -1)
	if new_pos > 0:
		numbers_list.insert(new_pos, item)
	else:
		numbers_list.append(item)
	#print(f'Number {item} new position {new_pos} into {list(map(lambda x: x[0], numbers_list))}')
	#print('New list', list(map(lambda x: x[0], numbers_list)))

print('New list', list(map(lambda x: x[0], numbers_list)))
result_sum = 0

idx0 = 0
for idx in range(len(numbers_list)):
	if numbers_list[idx][0] == 0:
		print('0 at', idx)
		idx0 = idx

for i in [1000, 2000, 3000]:
	result_sum += numbers_list[(idx0 + i) % num_count][0]
print('Result:', result_sum)
