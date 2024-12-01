"""
Part 1:
Find the total distance between the left list and the right list by adding up
the distances between all of the pairs you found.
"""

example = 'inputs/ex_01.txt'
actual = 'inputs/day_01.txt'


def part1(exercise):
    left = []
    right = []
    for line in open(exercise, 'r').readlines():
        pair = line.split()
        left.append(int(pair[0]))
        right.append(int(pair[1]))

    left = sorted(left)
    right = sorted(right)

    distance = 0
    for l, r in zip(left, right):
        distance += abs(r-l)
    return distance

assert part1(example) == 11
print(f'Part 1: {part1(actual)}')


def part2(exercise):
    left = []
    right = []
    for line in open(exercise, 'r').readlines():
        pair = line.split()
        left.append(int(pair[0]))
        right.append(int(pair[1]))

    left = sorted(left)
    right = sorted(right)
    left_counts = {k: left.count(k) for k in left}
    right_counts = {k: right.count(k) for k in right}

    return sum(
        [
            k * left_counts[k] * right_counts[k]
            for k in left_counts if k in right_counts
        ]
    )


assert part2(example) == 31
print(f'Part 2: {part2(actual)}')
