#!/bin/env python3

from collections import Counter

from helpers.io import read_lines
from helpers.timing import timethis

def read_rack() -> dict[str, list[str]]:
    rack: dict[str, list[str]] = dict()
    for l in read_lines("day11.input"):
        left, right = l.split(":")
        rack[left] = right.split()
    return rack

@timethis
def part1(rack: dict[str, list[str]]) -> int:
    sources: dict[str, list[str]] = dict()
    for device, outs in rack.items():
        for out in outs:
            if out not in sources:
                sources[out] = []
            sources[out].append(device)
    starts_reached: int = 0
    frontier: Counter[str] = Counter(["out"])
    next_frontier: Counter[str] = Counter()
    while frontier:
        for front in frontier:
            for source in sources.get(front, ()):
                if source == "you":
                    starts_reached += frontier[front]
                else:
                    next_frontier[source] += frontier[front]
        frontier, next_frontier = next_frontier, frontier
        next_frontier.clear()
    return starts_reached

def main():
    rack: dict[str, list[str]] = read_rack()
    print(part1(rack))

if __name__ == "__main__":
    main()