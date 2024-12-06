from copy import copy
from tqdm import tqdm

path = [line.strip() for line in open("day06/input")]

# part1

directions = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}
chaining = {"<": "^", "^": ">", ">": "v", "v": "<"}
breakcond = {"<": (1, 0), ">": (1, len(path[0]) - 1), "^": (0, 0), "v": (0, len(path) - 1)}

start_point = sum(x for x in ["".join(path).rfind(symbol) for symbol in directions] if x > 0)
start_point = (start_point // len(path[0]), start_point % len(path[0]))
actualpos = start_point
actualvalue = path[actualpos[0]][actualpos[1]]
actualor = directions[actualvalue]
posvisited = list()
posvisited.append(actualpos)

nextpos = actualpos
while nextpos[breakcond[actualvalue][0]] != breakcond[actualvalue][1]:
    nextpos = (actualpos[0] + actualor[0], actualpos[1] + actualor[1])
    if path[nextpos[0]][nextpos[1]] == "#":
        actualvalue = chaining[actualvalue]
        actualor = directions[actualvalue]
        nextpos = (actualpos[0] + actualor[0], actualpos[1] + actualor[1])
    posvisited.append(nextpos)
    actualpos = nextpos

part1 = len(set(posvisited))
print(part1)

# part2

part2 = list()
posvisited_set = set(posvisited)
posvisited_set.remove(start_point)
for pos in tqdm(posvisited_set):
    posvisited_f = set()
    path_updated = copy(path)
    path_updated[pos[0]] = path_updated[pos[0]][:pos[1]] + "#" + path_updated[pos[0]][pos[1] + 1:]

    actualpos = start_point
    actualvalue = path_updated[actualpos[0]][actualpos[1]]
    actualor = directions[actualvalue]
    posvisited_f.add((actualpos, actualvalue))
    nextpos = actualpos
    while actualpos[breakcond[actualvalue][0]] != breakcond[actualvalue][1]:
        nextpos = (actualpos[0] + actualor[0], actualpos[1] + actualor[1])

        if path_updated[nextpos[0]][nextpos[1]] == "#":
            actualvalue = chaining[actualvalue]
            actualor = directions[actualvalue]
        else:
            actualpos = nextpos
        if (nextpos, actualvalue) in posvisited_f:
            part2.append(pos)
            break
        posvisited_f.add((nextpos, actualvalue))

print(len(part2))
