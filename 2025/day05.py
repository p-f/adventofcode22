#!/bin/env python3

def main():
    ranges: list[tuple[int, int]] = []
    incredients: list[int] = []
    with open("day05.input") as handle:
        parse_as_range: bool = True
        while l := handle.readline():
            l = l.strip()
            if not l:
                parse_as_range = False
                continue
            if parse_as_range:
                r_from, r_to = l.split("-")
                ranges.append((int(r_from), int(r_to)))
            else:
                incredients.append(int(l))
    # Part 1
    fresh_count: int = 0
    for inc in incredients:
        if any(rf <= inc and inc <= rt for rf, rt in ranges):
            fresh_count += 1
    print("Part 1", fresh_count, sep="\t")
    # Part 2
    ranges.sort()
    total_count: int = 0
    last_start: int
    last_end: int
    last_start, last_end = ranges[0]
    for r_s, r_e in ranges:
        if last_start <= r_s <= last_end:
            # Start overlaps previous
            if r_e > last_end:
                last_end = r_e
        else:
            total_count += 1 + (last_end - last_start)
            last_start = r_s
            last_end = r_e
    total_count += 1 + (last_end - last_start)
    print("Part 2", total_count, sep="\t")

if __name__ == "__main__":
    main()