xmas = [line.strip() for line in open("day04/input")]


# part1
def find_xmaspart1(id_row, id_col):
    candidates = list()
    for offsetrow, offsetcol in [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]:
        index_rows = [id_row + offsetrow * i for i in range(1, 4)]
        index_cols = [id_col + offsetcol * i for i in range(1, 4)]
        if (all(0 <= x < len(xmas) for x in index_rows)) and (all(0 <= y < len(xmas[0]) for y in index_cols)):
            word = xmas[id_row][id_col] + "".join([xmas[x][y] for x, y in zip(index_rows, index_cols)])
            candidates.append(word)
    return sum([elt == "XMAS" for elt in candidates])


part1 = sum([find_xmaspart1(id_row, id_col) for id_row in range(len(xmas)) for id_col in range(len(xmas[0]))])
print(part1)


# part2

def find_xmaspart2(id_row, id_col):
    letter = xmas[id_row][id_col]
    if letter != "A":
        return 0
    else:
        index_rows = [id_row + offsetrow for offsetrow in (-1, 1)]
        if not all(0 <= x < len(xmas) for x in index_rows):
            return 0
        for offsetcol in [(1, -1), (-1, 1)]:
            index_col = [id_col + y for y in offsetcol]
            if not all(0 <= x < len(xmas[0]) for x in index_col):
                return 0
            word = "".join(xmas[x][y] for x, y in zip(index_rows, index_col))
            if word not in ["MS", "SM"]:
                return 0
        return 1


part2 = sum([find_xmaspart2(id_row, id_col) for id_row in range(len(xmas)) for id_col in range(len(xmas[0]))])
print(part2)
