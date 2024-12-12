inputs = [line.strip() for line in open("input")]
bounds = [0, len(inputs) - 1]

# part1

explored = set()


def f(pos, fruit=None):
    if pos not in explored:
        explored.add(pos)

    nb_neighbors = 4
    elts = [[pos, nb_neighbors]]
    x, y = pos[0], pos[1]
    if fruit is None:
        fruit = inputs[x][y]
    for xx, yy in ([0, 1], [1, 0], [0, -1], [-1, 0]):
        xnew = x + xx
        ynew = y + yy
        if all(bounds[0] <= elt <= bounds[1] for elt in (xnew, ynew)):
            newf = inputs[xnew][ynew]
            if fruit == newf:
                elts[0][1] -= 1
                if (xnew, ynew) not in explored:
                    elts += f((xnew, ynew), fruit)
    return elts


data = [f((id_row, id_col)) for id_col in range(len(inputs[0])) for id_row in range(len(inputs)) if
        (id_row, id_col) not in explored]
area = [len(elt) for elt in data]
perimeters = [sum([i[1] for i in elt]) for elt in data]
part1 = sum(a * p for a, p in zip(area, perimeters))
print(part1)


# part2

def compute_nb_sides(elements):
    positions = {elt[0] for elt in elements}
    nb_side = 0
    for pos in positions:
        xx, yy = pos
        for directions in (((0, 1), (-1, 0)), ((0, -1), (1, 0)), ((-1, 0), (0, -1)), ((1, 0), (0, 1))):
            new_pos = {(xx + direction[0], yy + direction[1]) for direction in directions}
            intersection = positions.intersection(new_pos)
            if len(intersection) == 0:
                # Outer corners
                nb_side += 1
            elif len(intersection) == 2:
                # Inner corners
                new_direction = (sum([elt[0] for elt in directions]), sum([elt[1] for elt in directions]))
                diagonal_value = (xx + new_direction[0], yy + new_direction[1])
                if diagonal_value not in positions:
                    nb_side += 1
    return nb_side


nb_sides = [compute_nb_sides(elt) for elt in data]
part2 = sum(side * area for side, area in zip(nb_sides, area))
print(part2)
