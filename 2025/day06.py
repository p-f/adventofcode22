#!/bin/env python3

from functools import reduce
from typing import Callable

OPS: dict[str, Callable[[int, int], int]] = {
    "+": int.__add__,
    "*": int.__mul__
}

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

if __name__ == "__main__":
    main()