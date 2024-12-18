"""
Part 1:
Calculate perimeter and area of plant plots to work out fencing price.

Part 2:
Calculate number of sides and area of plant plots to work out fencing price.

"""

actual = 'inputs/day_12.txt'

ex1 = """OOOOO
OXOXO
OOOOO
OXOXO
OOOOO"""

ex2 = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""

# grid = [[e for e in line ]for line in ex2.splitlines()]
grid = [[e for e in line ]for line in open(actual, 'r').read().splitlines()]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def isInside(i, j, grid):
    rows = len(grid)
    cols = len(grid[0])
    return 0 <= i < rows and 0 <= j < cols 


def explore(i, j):
    plant = grid[i][j]
    queue = set([(i, j)])
    visited.add((i, j))
    perimeter = 0
    area = 1
    while queue:
        i, j = queue.pop()
        
        for move in directions:
            ni = i + move[0]
            nj = j + move[1]
            if not isInside(ni, nj, grid) or grid[ni][nj] != plant:
                perimeter += 1
            
            else:
                if (ni, nj) in visited:
                    continue
                area += 1
                queue.add((ni, nj))
                visited.add((ni, nj))

    return area * perimeter    


rows = len(grid)
cols = len(grid[0])
visited = set()
result = 0
for i in range(rows):
    for j in range(cols):
        if (i, j) not in visited:
            plant = grid[i][j]
            price =  explore(i, j)
            result += price

print(result)