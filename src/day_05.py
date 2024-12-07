"""
Part 1:
Find all correct updates, those following all the rules.

Part 2:
Fix incorrectly ordered.

"""

example = 'inputs/ex_05.txt'
actual = 'inputs/day_05.txt'


def check_rules(update, rules):
    for rule in rules:
            if rule[0] in update and rule[1] in update:
                if not update.index(rule[0]) < update.index(rule[1]):
                    return False
    return True


def part1(data):
    ordering = open(data, 'r').readlines()
    separator = ordering.index('\n')
    rules = [l.strip().split('|') for l in ordering[:separator]]
    updates = [l.strip().split(',') for l in ordering[separator+1:]]

    res = 0
    for update in updates:
       if check_rules(update, rules):
        res += int(update[len(update)//2])
            
    return res


assert part1(example) == 143
print(f'Part 1: {part1(actual)}')


def part2(data):
    ordering = open(data, 'r').readlines()
    separator = ordering.index('\n')
    rules = [l.strip().split('|') for l in ordering[:separator]]
    updates = [l.strip().split(',') for l in ordering[separator+1:]]

    toFix = []
    for update in updates:
        if check_rules(update, rules) is False:
            toFix.append(update)
            
    res = 0
    for update in toFix:
        while check_rules(update, rules) is False:
            for rule in rules:
                if rule[0] in update and rule[1] in update:
                    if not update.index(rule[0]) < update.index(rule[1]):
                        update.remove(rule[0])
                        update.insert(update.index(rule[1]), rule[0])
                        print('Fixed:', update)
                        
        res += int(update[len(update)//2])
    return res
    
assert part2(example) == 123
print(f'Part 2: {part2(actual)}')
