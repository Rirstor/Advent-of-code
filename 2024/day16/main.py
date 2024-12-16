from heapq import heappop, heappush
from functools import reduce

inputs = [line.strip() for line in open("example2")]

walls = set((x, y) for y in range(len(inputs[0])) for x in range(len(inputs)) if inputs[x][y] == "#")
space = set((x, y) for y in range(len(inputs[0])) for x in range(len(inputs)) if inputs[x][y] == ".")

start = [(x, y) for y in range(len(inputs[0])) for x in range(len(inputs)) if inputs[x][y] == "S"][0]
road = []
heappush(road, (0, ">", start, [start]))

goal = [(x, y) for y in range(len(inputs[0])) for x in range(len(inputs)) if inputs[x][y] == "E"][0]

rotations = dict({">": [((0, 1), 1, ">"), ((-1, 0), 1001, "^"), ((1, 0), 1001, "v")],
                  "<": [((0, -1), 1, "<"), ((-1, 0), 1001, "^"), ((1, 0), 1001, "v")],
                  "^": [((-1, 0), 1, "^"), ((0, -1), 1001, "<"), ((0, 1), 1001, ">")],
                  "v": [((1, 0), 1, "v"), ((0, -1), 1001, "<"), ((0, 1), 1001, ">")]})


def djikstra(start, score, direction, visited):
    road = []
    heappush(road, (score, direction, start, [start]))
    reached = False
    while not reached:
        score, direction, pos, posvisited = heappop(road)
        for newdir, newscore, neworientation in rotations[direction]:
            newpos = (pos[0] + newdir[0], pos[1] + newdir[1])
            if newpos not in walls and newpos not in visited:
                heappush(road, (score + newscore, neworientation, newpos, posvisited + [newpos]))

                visited.add(newpos)
            if newpos == goal:
                reached = True
    return road[0]


part1 = djikstra(start, 0, ">", {start})
print(part1[0])

# part2

starts = [(0, ">", start, {start})]
visited = {start}
road = []
heappush(road, (0, ">", start, [start]))
result = list()
while len(road) != 0:
    score, direction, pos, posvisited = heappop(road)

    if pos == goal:
        result.append((score, posvisited))

    for newdir, newscore, neworientation in rotations[direction]:
        newpos = (pos[0] + newdir[0], pos[1] + newdir[1])
        newscore = score + newscore
        if newscore <= part1[0]:
            if newpos not in walls and newpos not in set(posvisited):
                heappush(road, (newscore, neworientation, newpos, posvisited + [newpos]))
positions = reduce(list.__add__, [elt[1] for elt in result if elt[0] == part1[0]])
part2 = len(set(positions))
print(part2)
