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
Compact the disk by moving whole files instead.
    - Attempt to move each file exactly once starting with the file with the
    highest file ID number.
    - If there is no span of free space to the left of a file that is large
    enough to fit the file, the file does not move.


"""

example = 'inputs/ex_09.txt'
actual = 'inputs/day_09.txt'


def part1(data):

    def checksum(long):
        return sum(i*int(e) for i, e in enumerate(long))

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
# print("Part 1:", part1(actual))


def part2(data):

    def checksum(long):
        return sum(i*int(e) for i, e in enumerate(long) if e != ".")

    drive = open(actual, 'r').read().strip()
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
    for fileid, size in zip(fileindex[::-1], sizes[::-1]):
        filestart = long.index(fileid)
        fileend = filestart + size
        scan = long.copy()
        offset = 0
        while True:
            try:
                free = scan.index(".")
            except ValueError:
                break

            if free+offset >= filestart:
                break

            span = 1
            while set(scan[free:free+span]) == set("."):
                span += 1

            if span-1 >= size:
                head = long[:offset+free]
                middle = long[offset+free+size:filestart]
                newgap = ["."] * size
                tail = long[fileend:]
                long = head + [fileid] * size + middle + newgap + tail
                break
            else:
                offset += free+span
                scan = long[offset:]

    # print(  # after compacting
    #     ''.join([str(e) for e in long])
    # )

    return checksum(long)


assert part2(example) == 2858
print('Calculating Part 2, this takes a while...')
print("Part 2:", part2(actual))
