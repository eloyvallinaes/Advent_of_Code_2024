"""
Part 1:
Compact hard drive and calculate checksum.
    - Score trailheads [0] by counting the number of peaks [9] they can reach.


"""

import numpy as np


example = 'inputs/ex_10.txt'
actual = 'inputs/day_10.txt'


def path(i, j, topo, visited=None):
    if visited is None:
        visited = set()
    if (i, j) in visited:
        return 0

    visited.add((i, j))

    height = topo[i][j]
    if height == 9:
        return 1  # Reached a peak

    candidates = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
    score = 0
    for cand in candidates:
        ni, nj = cand
        if 0 <= ni < len(topo) and 0 <= nj < len(topo[0]):  # Bounds check
            next_height = topo[ni][nj]
            if next_height - height == 1:
                score += path(ni, nj, topo, visited)

    return score


def part1(data):
    topo = np.array([
        [int(e) for e in line.strip()]
        for line in open(data, 'r').readlines()
    ])

    heads = np.where(topo == 0)
    scores = []
    for n in range(len(heads[0])):
        i = int(heads[0][n])
        j = int(heads[1][n])
        scores.append(path(i, j, topo))

    return sum(scores)


assert part1(example) == 36
print("Part 1:", part1(actual))  # 786


#.................................. Part 2 ...................................
def router(i, j, topo):
    routes = []

    def pathtrack(i, j, topo, route=None):
        if route is None:
            route = [(i, j)]
        height = topo[i][j]
        if height == 9:
            routes.append(route)  # Reached a peak

        candidates = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        for cand in candidates:
            ni, nj = cand
            if 0 <= ni < len(topo) and 0 <= nj < len(topo[0]):  # Bounds check
                next_height = topo[ni][nj]
                if next_height - height == 1:
                    pathtrack(ni, nj, topo, route + [cand])
        return route

    pathtrack(i, j, topo)

    return len(routes)


def part2(data):
    topo = np.array([
        [int(e) for e in line.strip()]
        for line in open(data, 'r').readlines()
    ])
    heads = np.where(topo == 0)
    ratings = []
    for n in range(len(heads[0])):
        i = int(heads[0][n])
        j = int(heads[1][n])
        ratings.append(router(i, j, topo))

    return sum(ratings)


assert part2(example) == 81
print("Part 2:", part2(actual))
