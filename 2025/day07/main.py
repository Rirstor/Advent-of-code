positions = {"S": [], ".": [], "^": []}

inputs = open("day07/input").read().split("\n")

[positions[inputs[row][col]].append(row + 1j * col) for row in range(len(inputs)) for col in range(len(inputs[0]))]

start_point, end = positions["S"][0], len(inputs)
beams, visited, splitters, timelines = [start_point], (start_point,), (), 0
beams_count = {start_point : 1}
for b in beams:
    current_pos = b
    index_row = 0
    while index_row != end - 1:
        index_row += 1
        new_pos = current_pos + 1
        if new_pos in positions["^"]:
            splitters += (new_pos,)
            pos1 = new_pos + 1j
            pos2 = new_pos - 1j
            beams_count[b] += 1
            visited += (pos1,) + (pos2,)
            if pos1 not in beams:
                beams += (pos1,)
                beams_count[pos1] = 1
            if pos2 not in beams:
                beams += (pos2,)
            current_pos = pos2
        elif new_pos in positions["."] and new_pos not in visited:
            visited += (new_pos,)
            current_pos = new_pos

print(len(splitters))