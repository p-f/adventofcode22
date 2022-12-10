#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open('10.input', 'r') as f:
	value_x = 1
	clk = 0
	points = [20, 60, 100, 140, 180, 220]
	ln = 0
	sig_total = 0
	def draw(clock, value):
		pos = clock % 40
		if pos == 0:
			print()
		print(('#' if pos in range(value -1, value + 2) else '.'), end='')
	while l:=f.readline():
		ln += 1
		cmd = l.strip().split()
		clock_before = clk
		clk_inc, inc = 0,0
		if cmd[0] == 'noop':
			draw(clock_before, value_x)
			clk_inc = 1
		else:
			inc = int(cmd[1])
			draw(clock_before, value_x)
			draw(clock_before + 1, value_x)
			clk_inc = 2
		clk += clk_inc
		for p in points:
			if clock_before < p and clk >= p:
				#print(f'Instruction on line {ln}: {cmd} at clock {clock_before} before {p}, value before: {value_x}')
				sig_total += p * value_x
				break
		value_x += inc
	print("Total signal:", sig_total)

