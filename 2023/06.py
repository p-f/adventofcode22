# -*- coding: utf-8 -*-

from santashelpers import parse_numbers_after_char
from typing import List

times, distances = None, None
with open('06.input', 'r') as f:
	times, distances = parse_numbers_after_char(f), parse_numbers_after_char(f)

races = len(times)
assert len(distances) == races

total_combinations = 1
for r in range(races):
	time, dist = times[r], distances[r]
	combinations = 0
	for holdtime in range(1, time):
		total_distance = (time - holdtime) * holdtime
		if total_distance > dist:
			combinations += 1
		elif combinations:
			break # Already found all
	total_combinations *= combinations

print('Total combinations', total_combinations)

