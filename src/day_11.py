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


def part1(data, n):
    stones = open(data, 'r').read().strip().split()  # string
    for _ in range(n):
        newline = []
        for stone in stones:
            if int(stone) == 0:
                newline += ["1"]
            elif len(stone) % 2 == 0:
                head = stone[:len(stone)//2]
                tail = stone[len(stone)//2:]
                newline += [str(int(head))] + [str(int(tail))]
            else:
                newline += [str(int(stone) * 2024)]

        stones = newline.copy()

    return len(stones)


def part2(stones, n):

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
                stone: [blink(str(int(head)), memo), blink(str(int(tail)), memo)]
            })
        else:
            memo.update({stone: [str(int(stone)*2024)]})

        return memo[stone]

    memo = {"0": ["1"]}
    for i in range(1):
        newline = []
        for stone in stones:
            newline += blink(stone, memo)

        stones = newline
        print("i:", stones)

    return


if __name__ == "__main__":
    # assert len(part1(example, 25)) == 55312
    part2(["125", "17"], 6)
