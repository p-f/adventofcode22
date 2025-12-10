#!/bin/env python3

from dataclasses import dataclass
from itertools import combinations, combinations_with_replacement
import math
from helpers.io import read_lines

import numpy as np
from scipy.optimize import linprog

type bitset = int

def _set_bit(index: int) -> bitset:
    return 1 << index

@dataclass
class Maschine:
    lights: bitset
    buttons: list[bitset]
    buttons_list: list[tuple[int, ...]]
    joltage_req: list[int]

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
        buttons_lists: list[tuple[int, ...]] = []
        for btn_str in components[1:-1]:
            button: bitset = 0
            btn_list: tuple[int, ...] = tuple(map(int, btn_str.strip("()").split(",")))
            for btn_id in btn_list:
                button |= _set_bit(btn_id)
            buttons.append(button)
            buttons_lists.append(btn_list)
        # Read joltage requirements
        joltage_req: list[int] = list(map(int, components[-1].strip("{}").split(",")))
        return Maschine(lights, buttons, buttons_lists, joltage_req)

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

def _part2_naive(machine: Maschine) -> int:
    print("Finding for ", machine)
    gcd: int = math.gcd(*machine.joltage_req)
    max_presses: int = sum(machine.joltage_req) // gcd
    num_counters: int = len(machine.joltage_req)
    for num_presses in range(1, max_presses + 1):
        for buttons in combinations_with_replacement(machine.buttons_list, num_presses):
            counters: list[int] = [0 for _ in range(num_counters)]
            for button in buttons:
                for index in button:
                    counters[index] += gcd
            if all(counters[i] == machine.joltage_req[i] for i in range(num_counters)):
                return num_presses
    raise RuntimeError("Not found for", machine)

def _part2(machine: Maschine) -> int:
    fact_list: list[list[int]] = []
    for eq_nr in range(len(machine.joltage_req)):
        coeff: list[int] = []
        for btn in machine.buttons_list:
            if eq_nr in btn:
                coeff.append(1)
            else:
                coeff.append(0)
        fact_list.append(coeff)
    # Right side: final joltages
    a = np.array(fact_list)           # Variables: number of button presses
    b = np.array(machine.joltage_req) # Expected joltages
    c = np.array([1 for _ in range(len(machine.buttons_list))]) # Optimize for sum of parameters
    integrality = [1 for _ in range(len(machine.buttons_list))] # Parameters have to be all ints
    res = linprog(c, A_eq=a, b_eq=b, integrality=integrality)
    return int(sum(res.x))

def main():
    machines: list[Maschine] = read_machines()
    print("Part 1", sum(_part1_naive(m) for m in machines))
    print("Part 2", sum(_part2(m) for m in machines))

if __name__ == "__main__":
    main()


