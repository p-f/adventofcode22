#!/bin/env python3

from functools import reduce
from typing import Callable
from itertools import groupby, starmap
from operator import itemgetter

OPS: dict[str, Callable[[int, int], int]] = {
    "+": int.__add__,
    "*": int.__mul__
}

def part2_single_iteration(input_lines: list[str]) -> int:
    col_nums: list[int] = [0 for _ in range(len(input_lines[0]))]
    for line in input_lines:
        for idx, c in enumerate(line):
            if c.isdigit():
                col_nums[idx] = 10 * col_nums[idx] + int(c)
    result: int = 0
    last_summand: int = 0
    last_op: str = ""
    for idx, c in enumerate(input_lines[-1]):
        if c in OPS:
            last_op = c
            result += last_summand
            last_summand = col_nums[idx]
        else:
            last_summand = OPS[last_op](last_summand, max(col_nums[idx], 0 if last_op == '+' else 1))
    return result + last_summand

def part2_with_transpose(input_lines: list[str]) -> int:
    # Transpose using zip, then convert columns to string, strip, group by to split by empty
    # Then get only the groups
    input_transposed: object = map(lambda s: map(int, s),
        map(itemgetter(1), filter(lambda t: t[0],
                                  groupby(map(str.strip,
                                              map(lambda t: "".join(t), zip(*input_lines[:-1]))),
                                              ''.__ne__))))
    ops: object = map(lambda c: int.__add__ if c == '+' else int.__mul__, input_lines[-1].split())
    return sum(starmap(reduce, zip(ops, input_transposed)))

def main():
    lines: list[str]
    input_components: list[list[int]] = []
    ops: list[str] = []
    with open("day06.input", "r") as handle:
        lines = handle.readlines()
        for l in lines[:-1]:
            input_components.append(list(map(int, l.strip().split())))
        ops += lines[-1].strip().split()
    # Verify
    for l_nr in range(len(input_components)):
        assert len(ops) == len(input_components[l_nr]), \
            f"Line #{l_nr}: Expected {len(ops)}, got {len(input_components[l_nr])}"
    # Part 1
    result: int = 0
    for col_nr in range(len(ops)):
        result += reduce(OPS[ops[col_nr]], (l[col_nr] for l in input_components))
    print("Part 1", result, sep="\t")

    # Part 2
    # Find operators and their start indices
    op_and_idx: list[tuple[str | None, int]] = []
    for idx, ch in enumerate(lines[-1].strip()):
        if ch in OPS:
            op_and_idx.append((ch, idx,))
    # Warning: only strip off newlines, we'll otherwise miss spaces at the end
    op_and_idx.append((None, len(lines[-1].rstrip("\r\n")))) # End marker
    result = 0
    for op_nr, (op, op_start) in enumerate(op_and_idx):
        if not op: break # Found end marker
        next_op_start: int = op_and_idx[op_nr + 1][1]
        numbers: list[int] = []
        # Scan column until next operator (or end of line, if none)
        for c in range(op_start, next_op_start):
            digits_in_column: list[str] = list(filter(str.isdigit, (line[c] for line in lines)))
            if digits_in_column:
                numbers.append(int("".join(digits_in_column)))
        result += reduce(OPS[op], numbers)
    print("Part 2", result, sep="\t")
    print("P 2.2", part2_single_iteration(lines), sep="\t")
    print("P 2.3", part2_with_transpose(lines), sep="\t")

if __name__ == "__main__":
    main()