#!/bin/env python3

from helpers.io import read_lines

NUM_SHAPES: int = 6

def main():
    shapes: list[list[str]] = []
    containers: list[tuple[tuple[int, int], tuple[int, ...]]] = []
    lines: list[str] = list(read_lines("day12.input"))
    for s in range(NUM_SHAPES):
        offset: int = 1 + (5 * s)
        shapes.append(lines[offset: offset + 3])
    for c in lines[(5 * NUM_SHAPES):]:
        size, counts = c.split(":")
        h, w = tuple(map(int, size.split("x")))
        containers.append(((h, w,), tuple(map(int, counts.split()))))
    # Part 1
    fitting_trivial: int = 0
    for (h, w), sizes in containers:
        blocks_h: int = h // 3
        blocks_w: int = w // 3
        blocks_total: int = blocks_h * blocks_w
        if sum(sizes) <= blocks_total:
            #print((h, w), sizes, "Fit trivial")
            fitting_trivial += 1
            continue
        #print((h, w), sizes, "Not trivial", sum(sizes),  blocks_total)
    print(fitting_trivial)

if __name__ == "__main__":
    main()