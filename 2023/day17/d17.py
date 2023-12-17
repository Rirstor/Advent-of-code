import heapq

movements = dict(N=(-1, 0), S=(1, 0), E=(0, 1), W=(0, -1))
excluded_movements = dict(N="S", S="N", E="W", W="E", Start="")
maze = [[i for i in l.split()[0]] for l in open("day17/input")]


def graph(starting_node, end_node, part=True):
    distances = [(0, *starting_node, "Start", -1)]
    output = dict()

    while distances:
        dist, r, c, d, nb_d = heapq.heappop(distances)
        if (r, c, d, nb_d) in output:
            continue
        output[(r, c, d, nb_d)] = dist

        for new_d, offsets in movements.items():

            if new_d != excluded_movements[d]:
                new_r = r + offsets[0]
                new_c = c + offsets[1]
                new_nb_d = 1 if new_d != d else nb_d + 1
                if part:
                    isvalid = new_nb_d <= 3 or nb_d == -1
                else:
                    isvalid = (new_nb_d <= 10 and ((nb_d >= 4 if new_d != d else True) or (nb_d == -1)))

                if 0 <= new_r < len(maze) and 0 <= new_c < len(maze[0]) and isvalid:
                    cost = int(maze[new_r][new_c])
                    heapq.heappush(distances, (cost + dist, new_r, new_c, new_d, new_nb_d))

    for (r, c, d, nb_d), dist in output.items():
        if r == end_node[0] and c == end_node[1]:
            return dist


part1 = graph((0, 0), (len(maze) - 1, len(maze[0]) - 1), True)
part2 = graph((0, 0), (len(maze) - 1, len(maze[0]) - 1), False)
print(part1, part2)
