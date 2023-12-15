import numpy as np

data = np.array([list(i.strip()) for i in open("day14/input")])
sr = np.argwhere(data == "#")
sp = np.argwhere(data == "O")


def move(p, data_f, sr_f):
    idx = sr_f[(sr_f[:, 1] == p[1]) * (sr_f[:, 0] < p[0])]
    if idx.size == 0:
        offset = sum(data_f[:p[0], p[1]] == ".")
    else:
        idx = np.max(idx[:, 0])
        offset = sum(data_f[idx:p[0], p[1]] == ".")
    return [p[0] - offset, p[1]]


# part 1
def cnt(indices):
    output = 0
    for i in range(len(data)):
        output += sum((elt[0] == i) for elt in indices) * (len(data) - i)
    return output


new_indices = [move(p, data, sr) for p in sp]
print(cnt(new_indices))


# part 2
def update_data(previous_points, new_points, data):
    for p in previous_points:
        data[p[0], p[1]] = "."
    for p in new_points:
        data[p[0], p[1]] = "O"
    return data


def cycle(point_rock, data, sr):
    flipped_sr = np.flip(sr)
    # north
    pn = [move(p, data, sr) for p in point_rock]
    data = update_data(point_rock, pn, data)
    # west
    pn = np.flip(pn)
    pw = [move(p, data.T, flipped_sr) for p in pn]
    data = update_data(pn, pw, data.T).T
    # south
    pw = [(len(data) - 1 - elt[0], elt[1]) for elt in np.flip(pw)]
    sr_south = np.array([(len(data) - 1 - elt[0], elt[1]) for elt in sr])
    ps = [move(p, np.flipud(data), sr_south) for p in
          pw]
    data = np.flipud(update_data(pw, ps, np.flipud(data)))
    # east
    ps = np.array([(len(data) - 1 - elt[0], elt[1]) for elt in ps])
    ps = np.array([(len(data) - 1 - elt[1], elt[0]) for elt in ps])
    sr_east = np.array([(len(data) - 1 - elt[1], elt[0]) for elt in sr])
    pe = [move(p, np.rot90(data), sr_east) for p in ps]
    data = np.rot90(update_data(ps, pe, np.rot90(data)), -1)
    pe = [(elt[1], len(data) - 1 - elt[0]) for elt in pe]

    return pe, data, sr


def h(data):
    return hash("".join(data.ravel()))


cache = {}
count = 1
start, data, sr = cycle(sp.tolist(), data, sr)
output = cnt(start)
cache[h(data)] = output

count = 0
while True:
    count += 1
    start, data, sr = cycle(start, data, sr)
    v = str(h(data))
    output = cnt(start)

    if v in cache:
        cycle_length = count - cache[v][0]
        values = list(cache.values())[-cycle_length:]
        print(values[int(1e9 - count) % cycle_length - 1][1])
        break
    cache[v] = (count, output)
