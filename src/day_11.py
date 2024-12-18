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

memo = {}
def f(stone: str, remaining: int):
    key = ','.join([stone, str(remaining)])
    if key in memo:
        return memo[key]
    
    if remaining == 0:
        result = 1
    
    elif str(int(stone)) == "0":
        result = f("1", remaining-1)
    
    elif len(stone) % 2 == 0:
        head = str(int(stone[:len(stone)//2]))
        tail = str(int(stone[len(stone)//2:]))
        result = f(head, remaining-1) + f(tail, remaining-1)
    
    else:
        result = f(str(int(stone)*2024), remaining-1)

    memo[key] = result

    return result

stones = ["125",  "17"]
stones = "2 77706 5847 9258441 0 741 883933 12".split()
ss = 0
for stone in stones:
    ss += f(stone, 75)

print(ss)