import numpy as np

patterns = [l.split() for l in open("day13/input").read().split("\n\n")]


def mirror(p, part=1):
    for data, factor in zip([p, p.T], [100, 1]):
        for i in range(len(data) - 1):
            if part == 1:
                if all(data[i] == data[i + 1]):
                    before = data[:i]
                    after = data[i + 2:]
                    shape = min(before.shape[0], after.shape[0])
                    if shape == 0:
                        return (i + 1) * factor
                    else:
                        mask = after[:shape] == before[-shape:][::-1]
                        if np.all(mask):
                            return (i + 1) * factor
            elif part == 2:
                if (data[i] != data[i + 1]).sum(0) == 1:
                    before = data[:i]
                    after = data[i + 2:]
                    shape = min(before.shape[0], after.shape[0])
                    if shape == 0:
                        return (i + 1) * factor
                    else:
                        mask = after[:shape] == before[-shape:][::-1]
                        if np.all(mask):
                            return (i + 1) * factor
                elif all(data[i] == data[i + 1]):
                    before = data[:i]
                    after = data[i + 2:]
                    shape = min(before.shape[0], after.shape[0])
                    if shape != 0:
                        mask = after[:shape] != before[-shape:][::-1]
                        if mask.sum() == 1:
                            return (i + 1) * factor


part1 = part2 = 0
for k in range(len(patterns)):
    data = np.array([[elt for elt in i] for i in patterns[k]])

    part1 += mirror(data)
    part2 += mirror(data, 2)

print(part1, part2)
