"""
Part 1:
Find all correct updates, those following all the rules.

Part 2:

"""

example = 'inputs/ex_05.txt'
actual = 'inputs/day_05.txt'


def part1(data):
    ordering = open(data, 'r').readlines()
    separator = ordering.index('\n')
    rules = [l.strip().split('|') for l in ordering[:separator]]
    updates = [l.strip().split(',') for l in ordering[separator+1:]]

    res = 0
    for update in updates:
        for rule in rules:
            if rule[0] in update and rule[1] in update:
                if not update.index(rule[0]) < update.index(rule[1]):
                    break
        else:
            res += int(update[len(update)//2])
    return res


assert part1(example) == 143
print(f'Part 1: {part1(actual)}')
