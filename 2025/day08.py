#!/bin/env python3

from collections import Counter
from math import prod, sqrt

from helpers.io import read_lines

type Box = tuple[int, int, int]

def main():
    boxes: list[Box] = []
    for l in read_lines("day08.input"):
        box: tuple[int, ...] = tuple(map(int, l.split(",")))
        assert len(box) == 3, box
        boxes.append(box)
    boxes.sort()
    distances: list[tuple[float, Box, Box]] = []
    for i1, b1 in enumerate(boxes):
        for b2 in boxes[i1 + 1:]:
            assert b1 < b2, (b1, b2)
            x1, y1, z1 = b1
            x2, y2, z2 = b2
            distances.append((sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2), b1, b2,))
    distances.sort()
    circuit_assignments: dict[Box, int] = {b: i for i, b in enumerate(boxes)}
    def _connect(circ1: int, circ2: int):
        if circ1 == circ2:
            return
        if circ1 > circ2:
            _connect(circ2, circ1)
        for box, ass in circuit_assignments.items():
            if ass == circ2:
                circuit_assignments[box] = circ1
    for _, b1, b2 in distances[:1000]:
        _connect(circuit_assignments[b1], circuit_assignments[b2])
    circuit_sizes: Counter[int] = Counter(circuit_assignments.values())
    print("Part 1", prod(n for _, n in circuit_sizes.most_common(3)))


if __name__ == "__main__":
    main()