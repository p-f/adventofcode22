#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import namedtuple

Pair = namedtuple('Pair', ['x', 'y'])

def irange(start, end):
	return range(start, end + (1 if end >= start else -1), 1 if end >= start else -1)

def ma_dist(p1: Pair, p2: Pair) -> int:
	return abs(p1.x - p2.x) + abs(p1.y - p2.y)

def pairs(v):
	for i in range(len(v) - 1):
		yield v[i], v[i + 1]
