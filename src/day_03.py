"""
Part 1:
Read corrupted instructions fitting the pattern mul(X, Y).
Add up the result of all valid multiplications.

Part 2:
Reports are safe if removing one element makes them safe.
"""

import re

example = open('inputs/ex_03_bis.txt').read()
actual = open('inputs/day_03.txt').read()


def part1(instructions):
    pattern = r"mul\(([0-9]{1,3}),([0-9]{1,3})\)"
    result = 0
    for hit in re.findall(pattern, instructions):
        result += int(hit[0]) * int(hit[1])
    return result


assert part1(example) == 161
print(f'Part 1: {part1(open('inputs/day_03.txt', 'r').read())}')


def part2(instructions):
    instructions = 'do()' + instructions + "don't()"
    dos = [m.end() for m in re.finditer(r"do\(\)", instructions)]
    donts = [m.start() for m in re.finditer(r"don't\(\)", instructions)]
    print(dos)
    print(donts)
    result = 0
    start = 0
    end = 0
    while True:
        try:
            start = [s for s in dos if s > end][0]
            end = [e for e in donts if e > start][0]
            chunk = instructions[start:end]
            print(start, end)
            result += part1(chunk)
        except IndexError:
            return result

assert part2(example) == 48
print(f'Part 2: {part2(actual)}')
