from heapq import heappop, heappush

inputs = [line.strip() for line in open("input")]

walls = set((x, y) for y in range(len(inputs[0])) for x in range(len(inputs)) if
            inputs[x][y] == "#")
space = set((x, y) for y in range(len(inputs[0])) for x in range(len(inputs)) if
            inputs[x][y] == ".")

start = [(x, y) for y in range(len(inputs[0])) for x in range(len(inputs)) if
         inputs[x][y] == "S"][0]

goal = [(x, y) for y in range(len(inputs[0])) for x in range(len(inputs)) if
        inputs[x][y] == "E"][0]


def shortest_path(start, end, visited, space):
    road = []
    heappush(road, (0, start))
    reached = False
    path = [start]
    final_score = 0
    while not reached:
        score, pos = heappop(road)
        for xx, yy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            newpos = (pos[0] + xx, pos[1] + yy)
            newscore = score + 1
            final_score = newscore
            if newpos in space and newpos not in visited:
                heappush(road, (newscore, newpos))
                visited.add(newpos)
                path.append(newpos)
            if newpos == end:
                reached = True
    return final_score, path + [goal]


bestscore, defaultpath = shortest_path(start, goal, set(), space)
defaultpathset = set(defaultpath)
results = dict()
walls_suppressed = dict()

results = dict()


def manhattan(idpos, refpos, length, data=dict()):
    pos = refpos[idpos]
    distance = [abs(pos[0] - elt[0]) + abs(pos[1] - elt[1]) for elt in refpos]
    candidates = [i for i in range(len(distance)) if 0 < distance[i] <= length and i > idpos + 1]
    for d in candidates:
        dd = distance[d]
        cheat = (d - idpos) - dd
        if cheat in data:
            data[cheat] += 1
        else:
            data[cheat] = 1


part1 = dict()
part2 = dict()
for idpos in range(len(defaultpath)):
    if idpos % 1000 == 0:
        print(idpos)
    manhattan(idpos, defaultpath, 2, part1)
    manhattan(idpos, defaultpath, 20, part2)

print(sum([part1[key] for key in part1 if key >= 100]))
print(sum([part2[key] for key in part2 if key >= 100]))
