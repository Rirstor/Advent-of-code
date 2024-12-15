maze, *commands = [line.split() for line in open("input").read().split('\n\n')]

verif = [line.strip() for line in open("verif")]
boxes_verif = set((x, y) for y in range(len(verif[0])) for x in range(len(verif)) if verif[x][y] == "O")
cond = max(len(maze), len(maze[0]))

commands = "".join(*commands)

walls = set((x, y) for y in range(len(maze[0])) for x in range(len(maze)) if maze[x][y] == "#")
boxes = set((x, y) for y in range(len(maze[0])) for x in range(len(maze)) if maze[x][y] == "O")
space = set((x, y) for y in range(len(maze[0])) for x in range(len(maze)) if maze[x][y] == ".")
robot = list((x, y) for y in range(len(maze[0])) for x in range(len(maze)) if maze[x][y] == "@")

space.add(robot[0])

directions = dict({">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)})


def move(command):
    pos = robot[-1]
    direction = directions[command]
    newpos = (pos[0] + direction[0], pos[1] + direction[1])
    if newpos in walls:
        robot.append(pos)
    elif newpos in space:
        robot.append(newpos)
    elif newpos in boxes:
        moved = False
        box_moved = [newpos]
        for i in range(2, cond):
            newnewpos = (pos[0] + i * direction[0], pos[1] + i * direction[1])
            if newnewpos in boxes:
                box_moved.append(newnewpos)
            elif newnewpos in space:
                newboxpos = [(elt[0] + direction[0], elt[1] + direction[1]) for elt in box_moved]
                _ = [boxes.remove(b) for b in box_moved]
                boxes.update(newboxpos)
                space.remove(newnewpos)
                space.add(newpos)
                moved = True
                break
            elif newnewpos in walls:
                break
        if moved:
            robot.append(newpos)
        else:
            robot.append(pos)


res = [move(c) for c in commands]
part1 = sum(elt[0] * 100 + elt[1] for elt in boxes)
print(part1)

# part2

maze_part2 = [elt.replace('.', '..').replace('@', "@.").replace("O", "[]").replace("#", "##") for elt in maze]
cond = max(len(maze_part2), len(maze_part2[0]))
walls = set((x, y) for y in range(len(maze_part2[0])) for x in range(len(maze_part2)) if maze_part2[x][y] == "#")
boxesl = set((x, y) for y in range(len(maze_part2[0])) for x in range(len(maze_part2)) if maze_part2[x][y] == "[")
boxesr = set((x, y) for y in range(len(maze_part2[0])) for x in range(len(maze_part2)) if maze_part2[x][y] == "]")
space = set((x, y) for y in range(len(maze_part2[0])) for x in range(len(maze_part2)) if maze_part2[x][y] == ".")
robot = list((x, y) for y in range(len(maze_part2[0])) for x in range(len(maze_part2)) if maze_part2[x][y] == "@")

space.add(robot[0])


def get_box(pos, side):
    if side == "left":
        return pos, (pos[0], pos[1] + 1)
    elif side == "right":
        return (pos[0], pos[1] - 1), pos


def move2(command, space=space):
    pos = robot[-1]
    direction = directions[command]
    newpos = (pos[0] + direction[0], pos[1] + direction[1])
    if newpos in walls:
        robot.append(pos)
    elif newpos in space:
        robot.append(newpos)
    elif newpos in boxesl or newpos in boxesr:
        moved = False
        if newpos in boxesl:
            box = get_box(newpos, "left")
        else:
            box = get_box(newpos, "right")

        boxlmoved = [box[0]]
        boxrmoved = [box[1]]
        if direction == (0, 1) or direction == (0, -1):
            for i in range(1, cond):
                newnewpos = (pos[0] + i * direction[0], pos[1] + i * direction[1])
                if newnewpos in boxlmoved or newnewpos in boxrmoved:
                    continue
                if newnewpos in boxesl or newnewpos in boxesr:
                    if newnewpos in boxesl:
                        box = get_box(newnewpos, "left")
                    else:
                        box = get_box(newnewpos, "right")
                    boxlmoved.append(box[0])
                    boxrmoved.append(box[1])
                elif newnewpos in space:
                    newboxl = [(elt[0] + direction[0], elt[1] + direction[1]) for elt in boxlmoved]
                    newboxr = [(elt[0] + direction[0], elt[1] + direction[1]) for elt in boxrmoved]
                    _ = [boxesl.remove(b) for b in boxlmoved]
                    _ = [boxesr.remove(b) for b in boxrmoved]

                    boxesl.update(newboxl)
                    boxesr.update(newboxr)
                    x = set(boxlmoved)
                    x.update(boxrmoved)

                    y = set(newboxl)
                    y.update(newboxr)

                    space.update(x)
                    _ = [space.remove(elt) for elt in y]
                    moved = True
                    break
                elif newnewpos in walls:
                    break

            if moved:
                robot.append(newpos)
            else:
                robot.append(pos)
        else:
            columns = [boxlmoved[0], boxrmoved[0]]
            list_space = list()
            for pos_box in columns:
                row, col = pos_box
                for i in range(1, cond):
                    newnewpos = (row + i * direction[0], col)
                    if newnewpos in boxlmoved or newnewpos in boxrmoved:
                        continue
                    if newnewpos in boxesl or newnewpos in boxesr:
                        if newnewpos in boxesl:
                            box = get_box(newnewpos, "left")
                        else:
                            box = get_box(newnewpos, "right")
                        boxlmoved.append(box[0])
                        boxrmoved.append(box[1])

                        columns.append(box[0])
                        columns.append(box[1])
                        break
                    elif newnewpos in space:
                        list_space.append(newnewpos)
                        break
                    elif newnewpos in walls:
                        robot.append(pos)
                        return None
            if len(set(elt[1] for elt in list_space)
                   ) == len({b[1] for b in columns}):
                newboxl = [(elt[0] + direction[0], elt[1] + direction[1]) for elt in boxlmoved]
                newboxr = [(elt[0] + direction[0], elt[1] + direction[1]) for elt in boxrmoved]
                _ = [boxesl.remove(b) for b in boxlmoved]
                _ = [boxesr.remove(b) for b in boxrmoved]
                boxesl.update(newboxl)
                boxesr.update(newboxr)

                x = set(boxlmoved)
                x.update(boxrmoved)

                y = set(newboxl)
                y.update(newboxr)

                space.update(x)
                space -= y
                robot.append(newpos)

            else:
                robot.append(pos)


[move2(c) for index, c in enumerate(commands)]
part2 = sum(elt[0] * 100 + elt[1] for elt in boxesl)
print(part2)
