#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import namedtuple
from functools import reduce

RGB = namedtuple('RGB', ['r', 'g', 'b'])

def parse_rgb(val: str) -> RGB:
	r,g,b = 0,0,0
	for item in val.split(','):
		amount, color = tuple(map(str.strip, item.strip().split(' ')))
		if color == 'red':
			r += int(amount)
		elif color == 'green':
			g += int(amount)
		else:
			b += int(amount)
	return RGB(r, g, b)

def possible(val: RGB, max_val: RGB) -> bool:
	return val.r <= max_val.r and val.g <= max_val.g and val.b <= max_val.b

def max_rgb(val1: RGB, val2: RGB) -> RGB:
	return RGB(max(val1.r, val2.r), max(val1.g, val2.g), max(val1.b, val2.b))

EXPECTED_MAX = RGB(12, 13, 14)

with open('02.input', 'r') as f:
	games = []
	while l:=f.readline():
		shows = l.split(':')[1].split(';')
		games += [list(map(parse_rgb, shows))]
	all_possible = 0
	powers = 0
	for game_nr, game in enumerate(games):
		print(f'Game {game_nr + 1} is {game}')
		# Possible?
		for show in game:
			if not possible(show, EXPECTED_MAX):
				print('Not possible')
				break
		else:
			print('Possible')
			all_possible += 1 + game_nr
		# Part 2
		max_rgb_game = reduce(max_rgb, game)
		power = reduce(int.__mul__, max_rgb_game)
		print('Power:', power)
		powers += power
	print('All possible: ', all_possible)
	print('Total power:  ', powers)
