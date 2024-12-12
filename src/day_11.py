"""
Part 1:
Evolve system according to rules:
    - 0 becomes 1
    - even digits split into two
    - value of stone is multiplied by 2024



"""

import numpy as np


example = 'inputs/ex_11.txt'
actual = 'inputs/day_11.txt'


def blink(stone, memo=None):
    if memo is None:
        memo = {
            "0": ["1"],
        }

    if stone in memo:
        return memo[stone]

    if len(stone) % 2 == 0:
        head = stone[:len(stone)//2]
        tail = stone[len(stone)//2:]
        memo.update({
            stone: [
                str(int(head)),
                str(int(tail)),
            ]
        })
    else:
        memo.update({stone: [str(int(stone)*2024)]})

    return memo[stone]


def part1(stones, n, memo=None):
    if memo is None:
        memo = {"0": "1"}
    for i in range(n):
        newline = []
        for stone in stones:
            new = blink(stone, memo)
            newline += new if type(new) == list else [new]
        stones = newline
        # print(f"{i+1}:", stones)

    return stones


print(part1(["125", "17"], 6))
                    