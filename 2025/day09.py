#!/bin/env python3

from itertools import combinations
from typing import Generator

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

type Pt = tuple[int, int]

def _in_square(x_min: int, y_min: int, x_max: int, y_max: int, point: Pt) -> bool:
    return x_min < point[0] < x_max and y_min < point[1] < y_max

def _all_corners(coordinates: list[Pt]) -> Generator[tuple[Pt, Pt], None, None]:
    for i in range(len(coordinates)):
        yield coordinates[i], coordinates[(i + 1) % len(coordinates)]

def _walk(p1: Pt, p2: Pt) -> Generator[Pt, None, None]:
    if p1[0] == p2[0]:
        y1, y2 = p1[1], p2[1]
        if y2 < y1: y1, y2 = y2, y1
        for y in range(y1, y2 + 1):
            yield p1[0], y
    else:
        assert p1[1] == p2[1]
        x1, x2 = p1[0], p2[0]
        if x2 < x1: x1, x2 = x2, x1
        for x in range(x1, x2 + 1):
            yield x, p1[1]

@timethis
def part2(coordinates: list[tuple[int, int]]) -> int:
    max_area: int = 0
    # For each 2 corners: Walk along the polygon, checking if we cross into the square bound
    # by the 2 corners at any point
    # If not: Square must be within -> aggregate area
    for i, c1 in enumerate(coordinates):
        print("Processing corner", i)
        for j, c2 in enumerate(coordinates[i + 1:]):
            if i == j: continue
            # Get square bounds
            x_min: int = min((c1[0], c2[0]))
            y_min: int = min((c1[1], c2[1]))
            x_max: int = max((c1[0], c2[0]))
            y_max: int = max((c1[1], c2[1]))
            this_area: int = _area(x_min, y_min, x_max, y_max)
            if this_area <= max_area:
                continue # Don't bother checking
            # Walk along the edges, we have to be on 4 sides of the square at some point
            # But we can´t cross into it!
            #                            UP     DOWN   LEFT   RIGHT
            crossed: bool = False
            visited_sides: list[bool] = [False, False, False, False]
            for cor1, cor2 in _all_corners(coordinates):
                if crossed: break
                for w in _walk(cor1, cor2):
                    if _in_square(x_min, y_min, x_max, y_max, w):
                        crossed = True
                        break
                    w_x, w_y = w
                    if w_x <= x_min:
                        visited_sides[2] = True # Left
                    if w_x >= x_max:
                        visited_sides[3] = True # Right
                    if w_y <= y_min:
                        visited_sides[1] = True # Down
                    if w_y >= y_max:
                        visited_sides[0] = True # Up
            if not crossed and all(visited_sides):
                max_area = this_area # Already has to be bigger

    return max_area

def main():
    coordinates: list[tuple[int, int]] = []
    for l in read_lines("day09.input"):
        coord: tuple[int, ...] = tuple(map(int, l.split(",")))
        assert len(coord) == 2, coord
        coordinates.append(coord)

    print("Part 1", part1(coordinates))
    print("Part 2", part2(coordinates))

if __name__ == "__main__":
    main()