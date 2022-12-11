#!/usr/bin/env python
# -*- coding: utf-8 -*-

from re import match

items = []
rules = []
div_tests = []
targets = []

def eval_rule(nr, score):
	operator, operand = rules[nr]
	operand = operand or score
	if operator == '+':
		return score + operand
	elif operator == '*':
		return score * operand
	else:
		raise ValueError(f'Unknown operator {operator}')

with open('11_test.input', 'r') as f:
	monke_nr = None
	monke_items = None
	monke_rule = None
	monke_div_test = None
	monke_target_true = None
	while l:=f.readline():
		l = l.strip()
		if m := match('Monkey (\d+):', l):
			monke_nr = m.group(1)
		elif m := match('Starting items: ([0-9, ]+)', l):
			monke_items = list(map(int, m.group(1).split(', ')))
		elif m := match('Operation: new = old ([+*]) ([old0-9]+)', l):
			operator, operand = m.group(1, 2)
			operand = None if operand == 'old' else int(operand)
			monke_rule = (operator, operand,)
		elif m := match('Test: divisible by (\d+)', l):
			monke_div_test = int(m.group(1))
		elif m := match('If (true|false): throw to monkey (\d+)', l):
			is_false = m.group(1) == 'false'
			target = int(m.group(2))
			if not is_false:
				monke_target_true = target
			else:
				items.append(monke_items)
				rules.append(monke_rule)
				div_tests.append(monke_div_test)
				targets.append((monke_target_true, target,))
				print(f'Added monke. Items: {monke_items}, Rule: {monke_rule}, Test: {monke_div_test}, Targets: {targets[-1]}')
		else:
			if len(l) != 0:
				raise ValueError(f'Unexpected line {l}')

print(f'Total monkeys: {len(items)}')
seen_items = [0 for _ in items]
def run_iteration(divide = True, output=True):
	for nr, itemlist in enumerate(items):
		if output: print(f'Processing monke {nr} with items: {itemlist}')
		for score in itemlist:
			seen_items[nr] += 1
			score = eval_rule(nr, score)
			if divide:
				score //= 3
			target_true, target_false = targets[nr]
			if score % div_tests[nr] == 0:
				if output: print(f'Passing {score} to {target_true}')
				items[target_true].append(score)
			else:
				if output: print(f'Passing {score} to {target_false}')
				items[target_false].append(score)
		itemlist.clear()
	print('Total seen items:', seen_items)
	if output:
		for nr, itemlist in enumerate(items):
			print(f'Now held by {nr}: {itemlist}')

def monkey_business():
	top1, top2 = sorted(seen_items)[-2:]
	return top1 * top2

def part1():
	for iternr in range(20):
		print('Running iteration: ', iternr)
		run_iteration()
		print(f'Business after round {iternr}: {monkey_business()}')

def part2():
	for iternr in range(10000):
		print('Running iteration: ', iternr)
		run_iteration(False, False)
	print(f'Business after round {iternr}: {monkey_business()}')

part1()
