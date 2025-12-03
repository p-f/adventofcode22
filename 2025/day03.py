#!/bin/env python3

def _max_value(battery_bank: list[int]) -> int:
    # Find largest digit, excluding last digit
    # Then find first occurance and then find largest after that occurance
    largest_val: int = max(battery_bank[:-1])
    pos1: int = -2
    for i, v in enumerate(battery_bank):
        if v == largest_val:
            pos1 = i
            break
    largest_val2: int = max(battery_bank[pos1 + 1:])
    return 10 * largest_val + largest_val2

def _pick_batteries2(battery_bank: list[int], picked: tuple[int, ...]) -> int:
    if len(picked) == 12: # picked all
        assert len(set(picked)) == 12
        res_value: int = 0
        for pick in picked:
            res_value = res_value * 10 + battery_bank[pick]
        return res_value
    assert len(picked) < 12
    # Pick next battery, just pick the largest one, making sure there's enough to pick in the next steps
    last_battery: int = -1 if not picked else picked[-1] # If none has been picked, start from 0 (+1 later)
    left_to_pick: int = 12 - len(picked)
    next_largest_bat: int = max(battery_bank[last_battery + 1: len(battery_bank) - left_to_pick + 1])
    # Find index and add
    for i in range(last_battery + 1, len(battery_bank) - left_to_pick + 1):
        if battery_bank[i] == next_largest_bat:
            return _pick_batteries2(battery_bank, picked + (i,))
    raise ValueError() # Should never happen

def _max_value2(battery_bank: list[int]) -> int:
    max_val: int = _pick_batteries2(battery_bank, ())
    return max_val

def main():
    batteries: list[list[int]] = []
    with open("day03.input", "r") as handle:
        while l := handle.readline():
            batteries.append(list(map(int, l.strip())))
    # Part 1
    print(sum(_max_value(b) for b in batteries))
    # Part 2
    print(sum(_max_value2(b) for b in batteries))

if __name__ == "__main__":
    main()