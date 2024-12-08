"""
Part 1:
How many unique locations within the bounds of the map contain an antinode.

Part 2:


"""

import numpy as np
from itertools import permutations

example = 'inputs/ex_08.txt'
actual = 'inputs/day_08.txt'

p1_sol = """......#....#
...#....0...
....#0....#.
..#....0....
....0....#..
.#....A.....
...#........
#......#....
........A...
.........A..
..........#.
..........#."""

p1_sol = np.array([list(row) for row in p1_sol.split("\n")])


def part1(data):
    with open(data, 'r') as f:
        map = np.array(
            [list(l.strip()) for l in f.readlines()]
        )
        original = [row.copy() for row in map.copy()]

    MAPWIDTH = len(map[0])
    MAPHEIGHT = len(map)

    antinodes = []
    for kind in np.unique(map[map != '.']):
        ii, jj = np.where(map == kind)
        antenna = [(int(i), int(j)) for i, j in zip(ii, jj)]
        for a, b in permutations(antenna, 2):
            iback = a[0] - (b[0] - a[0])
            jup = a[1] - (b[1] - a[1])
            iforth = b[0] + (b[0] - a[0])
            jdown = b[1] + (b[1]- a[1])
            if 0 <= iback < MAPWIDTH and 0 <= jup < MAPHEIGHT:
                # antinode in map
                antinodes.append((iback, jup))
            
            if 0 <= iforth < MAPWIDTH and 0 <= jdown < MAPHEIGHT: 
                antinodes.append((iforth, jdown))

    return set(antinodes)
        
assert len(part1(example)) == 14
print("Part 1:", len(part1(actual)))



