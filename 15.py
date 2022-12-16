#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aoccommon import *
from re import match

locations = []
scan_ranges = []

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


scan_ranges = [ma_dist(sensor, beacon) for sensor, beacon in locations]
sensors_with_range = list(zip(map(lambda x:x[0], locations), scan_ranges))

def sensor_in_range(pos):
	for sensor, r in sensors_with_range:
		if (d := ma_dist(sensor, pos)) <= r:
			return sensor, r, d

def scan_field(max_x, max_y):
	i = 0
	progress = 0
	while True:
		x = i % max_x
		y = i // max_y
		pos = Pair(x, y)
		if (new_progress := int(100 * y / max_y)) > progress:
			print('Progress:', new_progress, '%')
			progress = new_progress
		if sir := sensor_in_range(pos):
			near_sensor, sensor_range, dist = sir
			#print(f'Found sensor {near_sensor} in range of {pos}, remaining distance {sensor_range - dist}')
			remaining_range = sensor_range - dist
			i += 1 + remaining_range
		else:
			return pos


#print('Part 1:', len(blocked_locations(2000000)))
part2_point = scan_field(4000000, 4000000)
print('Part 2:', part2_point.x * 4000000 + part2_point.y)
