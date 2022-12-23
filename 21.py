#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

refnames = re.compile('([a-z]+)')
with open('21.input', 'r') as f, open('_21_data.py', 'w') as tmp:
	while l:=f.readline():
		print('def ' + refnames.sub(r'\1()', l.strip()).replace(':', ': return'), file=tmp)


print('Root', int(__import__('_21_data').root()))

# Part 2:
refnames = re.compile('([a-z]+)')
with open('21.input', 'r') as f, open('_21_data_part2.py', 'w') as tmp:
	print('class T:', file=tmp)
	print('  def __init__(self, i):', file=tmp)
	print('    self.i = i', file=tmp)
	print('  def set(self, i_new): self.i = i_new', file=tmp)
	print('  def humn(self): return self.i', file=tmp)
	while l:=f.readline():
		if l.startswith('humn'):
			continue
		elif l.startswith('root'):
			refs = re.findall('[a-z]+', l)
			print(f'  def root(self): return (self.{refs[1]}(),self.{refs[2]}(),)', file=tmp)
			continue
		if m := re.match('([a-z]+): ([0-9]+)', l):
			print(f'  def {m.group(1)}(self): return {m.group(2)}', file=tmp)
		elif m:= re.match('([a-z]+): ([a-z]+) (.) ([a-z]+)', l):
			print(f'  def {m.group(1)}(self): return self.{m.group(2)}() {m.group(3)} self.{m.group(4)}()', file=tmp)
		else:
			raise ValueError(f'Invalid line {l}')

T = __import__('_21_data_part2').T
value = 3403989691750
# I was too lazy to implement binary search here, just pick a start value and a high increment on line 49, then reset the values after it terminates, should take log_10(n) iterations
t = T(value)
while True:
	a, b = t.root()
	if a == b:
		print('Humn:', value)
		break
	else:
		print('Not found at', value, ':', a, b)
		if b>a:
			break
		value += 1
		t.set(value)
