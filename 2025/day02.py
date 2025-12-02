#!/bin/env python3

from typing import Callable, Generator
from sys import argv

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

# Part 2

def _high_digits(num: int, total_digits: int, digits: int) -> int:
    shift_low: int = 10 ** (total_digits - digits)
    upper: int = num // shift_low
    assert _num_digits(upper) == digits
    return upper

def _repeat_number(num: int, num_digits_part: int, repeats: int) -> int:
    assert repeats
    shift: int = 10 ** num_digits_part
    res: int = num
    for _ in range(repeats - 1):
        res = res * shift + num
    return res

def find_invalid2(start: int, end: int) -> Generator[int, None, None]:
    start_num_dig: int = _num_digits(start)
    end_num_dig: int = _num_digits(end)
    for digit_count in range(start_num_dig, end_num_dig + 1):
        # How can we split the number? 2 up to num digits parts
        for digit_split in range(2, digit_count + 1):
            # If we can´t split into this many parts -> try next
            if digit_count % digit_split != 0:
                continue
            repeated_digits: int = digit_count // digit_split
            start_r: int = start
            end_r: int = end
            # Adjust current range to expected number of digits
            if _num_digits(start_r) < digit_count:
                start_r = 10 ** (digit_count - 1)
            if _num_digits(end_r) > digit_count:
                end_r = (10 ** digit_count) - 1
            # Adjust to numbers with repeated digits
            scan_start: int = _high_digits(start_r, digit_count, repeated_digits)
            scan_end: int = _high_digits(end_r, digit_count, repeated_digits)
            for num_part_scan in range(scan_start, scan_end + 1):
                candidate: int = _repeat_number(num_part_scan, repeated_digits, digit_split)
                if candidate >= start and candidate <= end:
                    yield candidate

def part2_naive(start: int, end: int) -> Generator[int, None, None]:
    for num in range(start, end + 1):
        num_str: str = str(num)
        for split in range(2, len(num_str) + 1):
            if len(num_str) % split != 0:
                continue
            part_len: int = len(num_str) // split
            # Check if characters repeat
            if len({num_str[w_idx:w_idx + part_len] for w_idx in range(0, len(num_str), part_len)}) == 1:
                yield num

def main(args: list[str]):
    ranges: list[tuple[int, int]]
    with open("day02.input", "r") as handle:
        ranges = get_ranges(handle.readlines())
    sum_invalid: int = 0
    for s, e in ranges:
        for num in find_invalid_ids(s, e):
            sum_invalid += num
    print("Part 1", sum_invalid)
    # Part 2
    part2_solution: Callable[[int, int], Generator[int, None, None]] = find_invalid2
    if args and args[0] == "naive":
        print("Using naive solution!")
        part2_solution = part2_naive

    sum_invalid = 0
    for s, e in ranges:
        invalid: set[int] = set(part2_solution(s, e))
        sum_invalid += sum(invalid)
    print("Part 2", sum_invalid)

if __name__ == "__main__":
    main(argv[1:])