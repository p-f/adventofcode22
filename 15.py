#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aoccommon import *
from re import match

locations = []

with open('15.input', 'r') as f:
	while l:=f.readline():
		data = match('Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)', l.strip()).group(1,2,3,4)
		s_x, s_y, b_x, b_y = tuple(map(int, data))
		locations.append((Pair(s_x, s_y), Pair(b_x, b_y),))

def blocked_locations(y):
	blocked = set()
	for sensor, beacon in locations:
		dist = ma_dist(sensor, beacon)
		distance_to_y = abs(sensor.y - y)
		if distance_to_y > dist:
			continue
		remaining = dist - distance_to_y
		for p in irange(0, remaining):
			blocked.add(sensor.x + p)
			blocked.add(sensor.x - p)
		if beacon.y == y:
			blocked.remove(beacon.x)
	return blocked

print('Part 1:', len(blocked_locations(2000000)))
