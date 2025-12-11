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

def _find_sources(rack: dict[str, list[str]]) -> dict[str, list[str]]:
    sources: dict[str, list[str]] = dict()
    for device, outs in rack.items():
        for out in outs:
            if out not in sources:
                sources[out] = []
            sources[out].append(device)
    return sources

@timethis
def part1(rack: dict[str, list[str]]) -> int:
    sources: dict[str, list[str]] = _find_sources(rack)
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

@timethis
def part2(rack: dict[str, list[str]]) -> int:
    sources: dict[str, list[str]] = _find_sources(rack)
    starts_reached: int = 0
    frontier: Counter[tuple[str, bool, bool]] = Counter([("out", False, False,)])
    next_frontier: Counter[tuple[str, bool, bool]] = Counter()
    while frontier:
        for front in frontier:
            front_machine, visited_dac, visited_fft = front
            for source in sources.get(front_machine, ()):
                if source == "svr" and visited_dac and visited_fft:
                    starts_reached += frontier[front]
                else:
                    visited_fft_new: bool = visited_fft or (source == "fft")
                    visited_dac_new: bool = visited_dac or (source == "dac")
                    next_frontier[(source, visited_dac_new, visited_fft_new)] += frontier[front]
        frontier, next_frontier = next_frontier, frontier
        next_frontier.clear()
    return starts_reached

def main():
    rack: dict[str, list[str]] = read_rack()
    print(part1(rack))
    print(part2(rack))

if __name__ == "__main__":
    main()