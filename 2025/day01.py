#!/bin/env python3

def main():
    rotations: list[int] = []
    with open("day01.input", "r") as handle:
        while l := handle.readline():
            rot: int = int(l[1:])
            if l.startswith("L"):
                rot *= -1
            rotations.append(rot)
    # Part 1
    dial: int = 50
    zeros: int = 0
    for r in rotations:
        dial = (dial + r) % 100
        if dial == 0:
            zeros += 1
    print(zeros)
    # Part 2
    dial = 50
    zeros = 0
    for r in rotations:
        # Count anything more than full rotation towards zero
        while r > 100:
            r -= 100
            zeros += 1
        while r < -100:
            r += 100
            zeros += 1
        # Remaining rotation
        dial_old = dial # If we start at zero, don´t count overflow
        dial += r
        if dial_old != 0 and dial <= 0 or dial > 99:
            # Lands on zero or overflow (passes 0)
            zeros += 1
        dial %= 100
        #print(r, dial, zeros, sep="\t")
    print(zeros)

if __name__ == "__main__":
    main()
