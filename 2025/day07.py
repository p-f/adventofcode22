#!/bin/env python3

from helpers.geo2d import Coordinate, Directions, Grid, to_coordinate, to_xy

def _find_start(grid: Grid[str]) -> Coordinate:
    for c in grid.all_coordinates():
        if grid[c] == "S":
            return to_coordinate(*to_xy(c))
    raise ValueError("Not found")

def _part1(grid: Grid[str], start: Coordinate) -> int:
    splits: int = 0
    current_coordinates: list[Coordinate] = [start]
    next_coordinates: set[Coordinate] = set()
    while grid.is_in_grid(current_coordinates[0] + Directions.DOWN.value):
        next_coordinates.clear()
        for c in current_coordinates:
            c_down: Coordinate = c + Directions.DOWN.value
            if grid[c_down] == "^":
                splits += 1
                next_coordinates.add(c_down + Directions.LEFT.value)
                next_coordinates.add(c_down + Directions.RIGHT.value)
            else:
                next_coordinates.add(c_down)
        current_coordinates.clear()
        current_coordinates += next_coordinates
    return splits

def main():
    grid: Grid[str] = Grid.read("day07.test.input")
    start: Coordinate = _find_start(grid)
    # Part 1
    print("Part 1", _part1(grid, start), sep="\t")

if __name__ == "__main__":
    main()