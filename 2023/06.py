# -*- coding: utf-8 -*-

from functools import reduce
from santashelpers import parse_numbers_after_char
from typing import List

times, distances = None, None
with open('06.input', 'r') as f:
	times, distances = parse_numbers_after_char(f), parse_numbers_after_char(f)

races = len(times)
assert len(distances) == races

def combinations_for_race(time, dist):
	combinations = 0
	for holdtime in range(1, time):
		total_distance = (time - holdtime) * holdtime
		if total_distance > dist:
			combinations += 1
		elif combinations:
			break # Already found all
	return combinations

total_combinations = 1
for r in range(races):
	time, dist = times[r], distances[r]
	total_combinations *= combinations_for_race(time, dist)

print('Total combinations', total_combinations)

# Part 2
time2, distance2 = (int(reduce(str.__add__, map(str, e))) for e in (times, distances,))
print('Combinations for single race', combinations_for_race(time2, distance2))
# I would have implemented binary search here, but this was fast enough, ~5 sec
