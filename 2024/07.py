#!/usr/bin/env python
# -*- coding: utf-8 -*-

from santashelpers import parse_numbers

equations = []

with open('07.input', 'r') as f:
    while l:=f.readline():
        l, r = map(parse_numbers, l.split(':'))
        equations.append((l[0], r))

OPS = (int.__add__, int.__mul__)

def fulfills_equation(expected_res, operands, current_res, next_operand):
    if next_operand == len(operands):
        return expected_res == current_res
    if current_res > expected_res:
        return False # Fail fast
    for op in OPS:
        next_res = op(current_res, operands[next_operand])
        if fulfills_equation(expected_res, operands, next_res, next_operand + 1):
            return True
    return False

sum_fulfilled = 0
for res, values in equations:
    if fulfills_equation(res, values, 0, 0):
        sum_fulfilled += res


print(sum_fulfilled)
