#!/bin/env python3

from collections import Counter
from helpers.geo2d import Coordinate, Directions, Grid, to_coordinate, to_xy

def _find_start(grid: Grid[str]) -> Coordinate:
    for c in grid.all_coordinates():
        if grid[c] == "S":
            return to_coordinate(*to_xy(c))
    raise ValueError("Not found")

def _do_splits(grid: Grid[str], start: Coordinate) -> tuple[int, int]:
    splits: int = 0
    current_coordinates: Counter[Coordinate] = Counter([start])
    next_coordinates: Counter[Coordinate] = Counter()
    while grid.is_in_grid(current_coordinates.most_common(1)[0][0] + Directions.DOWN.value):
        next_coordinates.clear()
        for c in current_coordinates:
            current_count: int = current_coordinates[c]
            c_down: Coordinate = c + Directions.DOWN.value
            if grid[c_down] == "^":
                splits += 1
                next_coordinates[c_down + Directions.LEFT.value] += current_count
                next_coordinates[c_down + Directions.RIGHT.value] += current_count
            else:
                next_coordinates[c_down] += current_count
        current_coordinates.clear()
        current_coordinates += next_coordinates
    return splits, current_coordinates.total()

def main():
    grid: Grid[str] = Grid.read("day07.input")
    start: Coordinate = _find_start(grid)
    splits: int
    dimensions: int
    splits, dimensions = _do_splits(grid, start)
    print("Part 1", splits, sep="\t")
    print("Part 2", dimensions, sep="\t")

if __name__ == "__main__":
    main()