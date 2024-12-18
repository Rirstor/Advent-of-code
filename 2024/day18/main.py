from heapq import heappop, heappush

bytes = list(tuple(map(int, line.strip().split(','))) for line in open("input"))

size = 71

# part1

bytes_part1 = set(bytes[:1024])
space = set((x, y) for x in range(size) for y in range(size)) - bytes_part1

road = []
heappush(road, (0, (0, 0)))
visited = set()
while road:
    score, pos = heappop(road)
    if pos == (70, 70):
        print(score)
    for xx, yy in ((0, 1), (0, -1), (-1, 0), (1, 0)):
        newpos = (pos[0] + xx, pos[1] + yy)
        newscore = score + 1
        if newpos in space and newpos not in visited:
            heappush(road, (newscore, newpos))
            visited.add(newpos)
# part2

for id_bytes in range(1024, len(bytes)):
    space = set((x, y) for x in range(size) for y in range(size)) - set(bytes[:id_bytes])
    visited = set((0, 0))
    road = []
    heappush(road, (0, (0, 0)))
    while road:
        score, pos = heappop(road)
        for xx, yy in ((0, 1), (0, -1), (-1, 0), (1, 0)):
            newpos = (pos[0] + xx, pos[1] + yy)
            newscore = score + 1
            if newpos in space and newpos not in visited:
                heappush(road, (newscore, newpos))
                visited.add(newpos)
    if (70, 70) not in visited:
        part2 = id_bytes
        break
print(bytes[part2 - 1])
