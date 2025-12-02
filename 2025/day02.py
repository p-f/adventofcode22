#!/bin/env python3

from typing import Generator

def get_ranges(input_lines: list[str]) -> list[tuple[int, int]]:
    def _parse_range(range: str) -> tuple[int, int]:
        s, e = range.split("-")
        return int(s), int(e)
    ranges_per_line: list[tuple[int, int]] = []
    for line in input_lines:
        ranges_per_line += list(map(_parse_range, line.split(",")))
    return ranges_per_line

def _num_digits(num: int) -> int:
    digits: int = 0
    while num:
        digits += 1
        num //= 10
    return digits

def _half_number(num: int) -> int:
    # Warning: this only works if the number of digits is already even
    num_dig: int = _num_digits(num)
    shift_half: int = 10 ** (num_dig // 2)
    return num // shift_half

def _adjust_second_half_of_digits(num: int) -> int:
    num_dig: int = _num_digits(num)
    shift_half: int = 10 ** (num_dig // 2)
    upper: int = num // shift_half
    return upper * shift_half + upper

def find_invalid_ids(start: int, end: int) -> Generator[int, None, None]:
    start_orig: int = start
    end_orig: int = end
    # print("Finding", start, end)
    while start <= end:
        # print("Probing", start, end)
        if not _num_digits(start) % 2 == 0:
            # Move to next even digit number
            start = 10 ** (_num_digits(start))
            continue
        if not _num_digits(end) % 2 == 0:
            end = 10 ** (_num_digits(end) - 1) - 1
            continue
        # Adjust numbers to invalid ones
        start_new = _adjust_second_half_of_digits(start)
        if start_new != start:
            start = start_new
            continue
        end_new = _adjust_second_half_of_digits(end)
        if end_new != end:
            end = end_new
            continue
        # If we´re here we have a start and end number matching the pattern
        break
    # print("End probe", start, end)
    if start > end:
        return
    # Now just count how many number we can build
    start_half: int = _half_number(start)
    end_half: int = _half_number(end)
    # This could probably done faster, only consider numbers in original range:
    for half_i in range(start_half, end_half + 1):
        digits: int = _num_digits(half_i)
        new_number: int = half_i * (10 ** digits ) + half_i
        if new_number >= start_orig and new_number <= end_orig:
            yield new_number

def main():
    ranges: list[tuple[int, int]]
    with open("day02.input", "r") as handle:
        ranges = get_ranges(handle.readlines())
    sum_invalid: int = 0
    for s, e in ranges:
        for num in find_invalid_ids(s, e):
            sum_invalid += num
    print(sum_invalid)

if __name__ == "__main__":
    main()