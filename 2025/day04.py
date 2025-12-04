#!/bin/env python3

from functools import partial
from helpers.geo2d import Coordinate, CoordinateLike, Directions, is_in_grid, to_coordinate, to_xy
from typing import Callable, Generator

ALL_DIRECTIONS: list[Coordinate] = [d.value for d in Directions]
for ud in (Directions.UP, Directions.DOWN):
    for lr in (Directions.LEFT, Directions.RIGHT):
        ALL_DIRECTIONS.append(ud.value + lr.value)

def main():
    grid: list[list[str]] = []
    with open("day04.input", "r") as handle:
        while l := handle.readline():
            grid.append(list(l.strip()))
    num_rows: int = len(grid)
    num_cols: int = len(grid[0])
    in_grid: Callable[[CoordinateLike], bool] = partial(is_in_grid, num_cols, num_rows)
    # Common functions
    def is_tp(coord: CoordinateLike) -> bool:
        if not in_grid(coord):
            return False
        x, y = to_xy(coord)
        return grid[y][x] == "@"
    def accessible() -> Generator[Coordinate, None, None]:
        for x in range(num_cols):
            for y in range(num_rows):
                if not is_tp((x, y,)):
                    continue # Only from TP rolls
                neighbor_tps: int = 0
                center: Coordinate = to_coordinate(x, y)
                for d in ALL_DIRECTIONS:
                    if is_tp(center + d):
                        neighbor_tps += 1
                if neighbor_tps < 4:
                    yield center
    # Part 1
    accessible_tp: list[Coordinate] = list(accessible())
    print("Part 1", len(accessible_tp), sep="\t")
    # Part 2
    removed: int = 0
    def remove():
        for tp in accessible_tp:
            x: int
            y: int
            x, y = to_xy(tp)
            grid[y][x] = ' '
    while accessible_tp:
        removed += len(accessible_tp)
        remove()
        accessible_tp = list(accessible())
    print("Part 2", removed, sep="\t")

if __name__ == "__main__":
    main()
