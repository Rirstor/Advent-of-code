data = [line.strip() for line in open("input")][0]


# part 1

positions_points = list()
positions = dict()
offset = 0
for id_elt in range(0, len(data) - 1, 2):
    id_number = str(id_elt // 2)
    nb_blocks = data[id_elt]
    nb_free_space = int(data[id_elt + 1])
    positions[id_number] = [offset + i for i in range(int(data[id_elt]))]
    for i in range(int(nb_free_space)):
        positions_points.append(offset + int(nb_blocks) + i)
    offset += int(nb_blocks) + nb_free_space
if len(data) % 2 != 0:
    positions[str(len(data) // 2)] = [offset + i for i in range(int(data[-1]))]

min_, max_ = positions_points[0], positions[list(positions.keys())[-1]][-1]
id_pos_count = 0
for id_number in sorted(list(positions.keys()), key=lambda x: int(x))[::-1]:
    pos_number = positions[id_number][::-1]
    for id_pos in range(len(pos_number)):
        if (max_ - min_) >= len(positions_points):
            pos_numbernew = positions_points[id_pos_count]
            pos_point_new = pos_number[id_pos]

            positions_points[id_pos_count] = pos_point_new

            pos_number[id_pos] = pos_numbernew
            id_pos_count += 1
            min_ = positions_points[id_pos_count]
    positions[id_number] = pos_number
part1 = sum(int(elt) * val for elt in positions.keys() for val in positions[elt])
print(part1)