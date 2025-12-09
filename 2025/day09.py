#!/bin/env python3

from itertools import combinations

from helpers.io import read_lines
from helpers.timing import timethis

def _area(x1: int, y1: int, x2: int, y2: int) -> int:
    return (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)

@timethis
def part1(coordinates: list[tuple[int, int]]) -> int:
    max_area: int = 0
    for (x1, y1), (x2, y2) in combinations(coordinates, 2):
        if (a := _area(x1, y1, x2, y2)) > max_area:
            max_area = a
    return max_area

def main():
    coordinates: list[tuple[int, int]] = []
    for l in read_lines("day09.input"):
        coord: tuple[int, ...] = tuple(map(int, l.split(",")))
        assert len(coord) == 2, coord
        coordinates.append(coord)
    print("Part 1", part1(coordinates))

if __name__ == "__main__":
    main()