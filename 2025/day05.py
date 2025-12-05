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
    print(fresh_count)

if __name__ == "__main__":
    main()