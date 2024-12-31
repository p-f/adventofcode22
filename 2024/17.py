#!/usr/bin/env python
# -*- coding: utf-8 -*-

from santashelpers import parse_numbers_after_char, parse_numbers

reg_a, reg_b, reg_c = 0, 0, 0
instructions = None

with open('17.input', 'r') as f:
    reg_a = parse_numbers_after_char(f)[0]
    reg_b = parse_numbers_after_char(f)[0]
    reg_c = parse_numbers_after_char(f)[0]
    f.readline()
    instructions = parse_numbers(f.readline().strip().split(": ")[1], ",")

print(reg_a, reg_b, reg_c, instructions)

inst_pt = 0

out = list()

while inst_pt < len(instructions):
    op_code = instructions[inst_pt]
    print("Instr", inst_pt, "op", op_code, "Reg", reg_a, reg_b, reg_c)
    print("out", out)
    def com_operand():
        raw_operand = instructions[inst_pt + 1]
        if raw_operand >= 0 and raw_operand <= 3:
            return raw_operand
        assert raw_operand != 7
        return [reg_a, reg_b, reg_c][raw_operand - 4]
    if op_code == 0:
        reg_a //= (2 ** com_operand())
    elif op_code == 1:
        reg_b ^= instructions[inst_pt + 1]
    elif op_code == 2:
        reg_b = com_operand() % 8
    elif op_code == 3:
        if reg_a != 0:
            inst_pt = instructions[inst_pt + 1]
            continue
    elif op_code == 4:
        reg_b ^= reg_c
    elif op_code == 5:
        out.append(com_operand() % 8)
    elif op_code == 6:
        reg_b = reg_a // (2 ** com_operand())
    else:
        assert op_code == 7
        reg_c = reg_a // (2 ** com_operand())
    inst_pt += 2

print(','.join(map(str, out)))
    