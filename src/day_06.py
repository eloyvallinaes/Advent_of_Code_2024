"""
Part 1:
Find all distinct positions in which the guard will be before leaving the area.

Part 2:
Find all ways to add an obstruction that would put the guard in a loop.

"""

example = 'inputs/ex_06.txt'
actual = 'inputs/day_06.txt'

update_going = {
    'up':'right',
    'right': 'down',
    'down': 'left',
    'left': 'up'
}


def walk(current, going, blueprint, path=[]):
    # forward
    if blueprint[current[0]][current[1]] != "#":
        path.append((current, going))
        if going == 'up':
            current = (current[0]-1, current[1])
        elif going == 'down':
            current = (current[0]+1, current[1])
        elif going == 'left':
            current = (current[0], current[1]-1)
        else:  # going right
            current = (current[0], current[1]+1)

    # backward and turn
    else:
        if going == 'up':
            current = (current[0]+1, current[1])
        elif going == 'down':
            current = (current[0]-1, current[1])
        elif going == 'left':
            current = (current[0], current[1]+1)
        else:  # going right
            current = (current[0], current[1]-1)

        going = update_going[going]
        del path[-1]
        
    return current, going


def part1(data):
    blueprint = [  # list of lists
        list(i.strip()) for i in  open(data).readlines()
    ]  
    for i, line in enumerate(blueprint):
        for j, square in enumerate(line):
            if square == "^":  # starting position
                current = (i, j)

    going = "up"
    path = []
    while True:
        try:
            current, going = walk(current, going, blueprint, path)

        except IndexError:  # went off the map
            break

    return len(set([p[0] for p in path]))


print(part1(example))
print("Part 1:", part1(actual))