from heapq import heappop, heappush

inputs = [line.strip() for line in open("input")]

walls = set((x, y) for y in range(len(inputs[0])) for x in range(len(inputs)) if
            inputs[x][y] == "#")
space = set((x, y) for y in range(len(inputs[0])) for x in range(len(inputs)) if
            inputs[x][y] == ".")

start = [(x, y) for y in range(len(inputs[0])) for x in range(len(inputs)) if
         inputs[x][y] == "S"][0]
road = []
heappush(road, (0, ">", start, [start]))

goal = [(x, y) for y in range(len(inputs[0])) for x in range(len(inputs)) if
        inputs[x][y] == "E"][0]

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
                heappush(road, (
                    score + newscore, neworientation, newpos, posvisited + [newpos]))

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
result = set()
nodes = dict()
while road:
    print(len(road))
    score, direction, pos, posvisited = heappop(road)
    nodes[(pos, direction)] = score

    if pos == goal and score == part1[0]:
        result |= set(posvisited)

    for newdir, newscore, neworientation in rotations[direction]:
        newpos = (pos[0] + newdir[0], pos[1] + newdir[1])
        newscore = score + newscore
        if newpos not in walls:
            if nodes.get((newpos, neworientation), float("inf")) > newscore:
                heappush(road,
                         (newscore, neworientation, newpos, posvisited + [newpos]))
part2 = len(set(result))
print(part2)
