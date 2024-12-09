"""
Part 1:
Compact hard drive and calculate checksum.
    - Single string of numbers alternating between length of file and length of
    free space.
    - move file blocks one at a time from the end of the disk to the leftmost
    free space block.
    - checksum: add up the result of multiplying each of these blocks' position
    with the file ID number it contains.

Part 2:


"""

example = 'inputs/ex_09.txt'
actual = 'inputs/day_09.txt'


def checksum(long):
    return sum(i*int(e) for i, e in enumerate(long))


def part1(data):
    drive = open(data, 'r').read().strip()

    sizes = []
    spaces = []
    for i in range(0, len(drive), 2):
        sizes.append(int(drive[i]))
        try:
            spaces.append(int(drive[i+1]))
        except IndexError:  # no free space after last file
            spaces.append(0)
            break

    fileindex = list(range(0, len(sizes)))

    long = []
    for i, fileid in enumerate(fileindex):
        long += [fileid] * sizes[i] + ['.'] * spaces[i]

    # before compacting
    # print(''.join([str(e) for e in long]))

    original = long.copy()
    for space in spaces:
        if space > 0:
            try:
                free = long.index(".")  # first free block
            except ValueError:  # no more space 
                break
            tail = long[free+space:][::-1]
            trim = space
            while trim - tail[:trim].count('.') < space:
                trim += 1

            insert = tail[:trim]
            while "." in insert:
                insert.remove(".")
            # print(long[:free], insert, long[free+space:-trim])
            long = long[:free] + insert + long[free+space:-trim]

    # print(  # after compacting
    #     ''.join([str(e) for e in long])
    # )

    return checksum(long)


part1(example) == 1928
print("Part 1:", part1(actual))
