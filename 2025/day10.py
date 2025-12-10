#!/bin/env python3

from dataclasses import dataclass
from itertools import combinations
from helpers.io import read_lines

type bitset = int

def _set_bit(index: int) -> bitset:
    return 1 << index

@dataclass
class Maschine:
    lights: bitset
    buttons: list[bitset]

    @classmethod
    def read(cls, line: str) -> Maschine:
        components: list[str] = line.split()
        # Read initial lights
        lights: bitset = 0
        for i, l in enumerate(components[0].strip("[]")):
            if l == "#":
                lights |= _set_bit(i)
            else:
                assert l == ".", (lights, i, l)
        # Read buttons
        buttons: list[bitset] = []
        for btn_str in components[1:-1]:
            button: bitset = 0
            for btn_id in map(int, btn_str.strip("()").split(",")):
                button |= _set_bit(btn_id)
            buttons.append(button)
        return Maschine(lights, buttons)

def _part1_naive(machine: Maschine) -> int:
    # Each button can at most be pressed once, pressing twice will lead back to original state
    for num_buttons in range(1, len(machine.buttons) + 1):
        for buttons in combinations(machine.buttons, num_buttons):
            state: bitset = machine.lights
            for b in buttons:
                state ^= b
            if state == 0:
                return num_buttons
    raise RuntimeError("Could not find solution", machine)

def read_machines() -> list[Maschine]:
    machines: list[Maschine] = []
    for l in read_lines("day10.input"):
        machines.append(Maschine.read(l))
    return machines

def main():
    machines: list[Maschine] = read_machines()
    # Test
    print("Part 1", sum(_part1_naive(m) for m in machines))

if __name__ == "__main__":
    main()


