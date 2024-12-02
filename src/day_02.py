"""
Part 1:
Find safe reports.
Reports are safe if monotic and distances in [1, 3] interval.

Par 2:
Reports are safe if removing one element makes them safe.
"""

import numpy as np

example = 'inputs/ex_02.txt'
actual = 'inputs/day_02.txt'


def part1(data):
    safe = 0
    for report in open(data, 'r').readlines():
        levels = [int(i) for i in report.split()]
        diffs = np.diff(levels)
        if all(diffs > 0) or all(diffs < 0):
            if all(np.abs(diffs) <= 3):
                safe += 1
    return safe


assert part1(example) == 2
print(f'Part 1: {part1(actual)}')


def is_safe(levels):
    diffs = np.diff(levels)
    if all(diffs > 0) or all(diffs < 0):
        if all(np.abs(diffs) <= 3):
            return True
    return False


def part2(data):
    safe = 0
    for report in open(data, 'r').readlines():
        levels = [int(i) for i in report.split()]
        if is_safe(levels) is True:
            safe += 1
        else:
            for i in range(len(levels)):
                fudge = levels[:i] + levels[i+1:]
                if is_safe(fudge):
                    safe += 1
                    break
    return safe


assert part2(example) == 4
print(f'Part 2: {part2(actual)}')
