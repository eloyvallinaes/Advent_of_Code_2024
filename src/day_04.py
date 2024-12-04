"""
Part 1:
Find all occurrances of XMAS in letter soup

Part 2:
Find MAS and SAM pattern forming a cross.
"""

example = 'inputs/ex_04.txt'
actual = 'inputs/day_04.txt'


def part1(data):
    soup = [line.strip() for line in open(data, 'r').readlines()]
    limit = len(soup)
    result = 0
    reads = []
    for row in soup:
        result += row.count('XMAS') + row.count('SAMX')
        # reads.append(row)
    for col in soup[:]:
        result += col.count('XMAS') + col.count('SAMX')
        # reads.append(col)

    for offset in range(0, limit):
        diag = ''.join([soup[i][i+offset] for i in range(limit-offset)])
        result += diag.count('XMAS') + diag.count('SAMX')
        # reads.append(diag)

    for offset in range(1, limit):
        diag = ''.join([soup[i+offset][i] for i in range(limit-offset)])
        result += diag.count('XMAS') + diag.count('SAMX')
        # reads.append(diag)

    for offset in range(0, limit):
        diag = ''.join([soup[i][i+offset] for i in range(limit-1-offset, 0, -1)])
        result += diag.count('XMAS') + diag.count('SAMX')
        # reads.append(diag)

    for offset in range(limit-1, 0, -1):
        diag = ''.join([soup[i+offset][i] for i in range(limit-1-offset, 0, -1)])
        result += diag.count('XMAS') + diag.count('SAMX')
        reads.append(diag)
    return result


assert part1(example) == 18
print(f"Part 1: {part1(actual)}")


def part2(data):
    soup = [line.strip() for line in open(data, 'r').readlines()]
    count = 0
    for i, line in enumerate(soup):
        for j, letter in enumerate(line):
            if letter == 'A' and i > 0 and j > 0:
                try:
                    arm0 = soup[i-1][j-1] + 'A' + soup[i+1][j+1]
                    arm1 = soup[i+1][j-1] + 'A' + soup[i-1][j+1]
                    if arm0 in ['MAS', 'SAM'] and arm1 in ['MAS', 'SAM']:
                        count += 1
                except IndexError:
                    print(i, j)
                    continue

    return count


assert part2(example) == 9
print(f"Part 2: {part2(actual)}")
