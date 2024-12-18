import re

def tokens(buttons):
    price = {'A': 3, 'B': 1}
    return sum([price[b] for b in buttons])


def bestSum(x, y, arms, memo=None):
    if memo is None:
        memo = {}
    
    if (x, y) in memo: return memo[(x, y)]
    if (x, y) == (0, 0): return []
    if all(x < dx or y < dy for dx, dy in arms.values()):
        return None


    best = None
    for b, (dx, dy) in arms.items():
        result = bestSum(x-dx, y-dy, arms, memo)
        memo.update({
            (x-dx, y-dy): result
        })
        if result is not None:
            if  best is None or tokens(result) <= tokens(best):
                best = [b] + result  # list extension
        
    return best


machines = open('inputs/day_13.txt', 'r').read()
machines = machines.split('\n\n')

# spend = 0
# for machine in machines:
#     nums = [int(i) for i in re.findall(r'[XY][+=](\d+)', machine)]
#     arms = {'A': (nums[0], nums[1]), 'B': (nums[2], nums[3])}
#     X, Y = nums[4:]
#     best = bestSum(X, Y, arms)
#     if best is not None and best.count('A') <= 100 and best.count('B') <= 100:
#         spend += tokens(best)


# print(spend)

############################### Part 2 ########################################
import math

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

machines = open('inputs/ex_13.txt', 'r').read()
machines = machines.split('\n\n')

# spend = 0
# for machine in machines:
offset = 1000
nums = [int(i) for i in re.findall(r'[XY][+=](\d+)', machines[2])]
arms = {'A': (nums[0], nums[1]), 'B': (nums[2], nums[3])}
X, Y = nums[4], nums[5]

# best = bestSum(X, Y, arms)
# if best is not None and best.count('A') <= 100 and best.count('B') <= 100:
#     spend += tokens(best)

