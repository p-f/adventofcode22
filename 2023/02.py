#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import namedtuple
import re

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

EXPECTED_MAX = RGB(12, 13, 14)

with open('02.input', 'r') as f:
	games = []
	while l:=f.readline():
		shows = l.split(':')[1].split(';')
		games += [list(map(parse_rgb, shows))]
	all_possible = 0
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
	print('All possible: ', all_possible)
