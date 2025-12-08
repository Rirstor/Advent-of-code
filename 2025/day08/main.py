import math

inputs = [list(map(int, elt.split(","))) for elt in open("day08/input").readlines()]
circuits = []

distances = [
    math.sqrt(sum([(k1 - k2) ** 2 for k1, k2 in zip(inputs[i], inputs[j])]))
    if i < j
    else 1e15
    for i in range(len(inputs))
    for j in range(len(inputs))
]
index = 0
while not circuits or len(circuits[0]) != len(inputs):
    index_ = distances.index(min(distances))
    i, j = index_ // len(inputs), index_ % len(inputs)
    distances[index_] = 1e15
    indexes = list()
    circuit_to_add, circuit_oi = inputs[i], inputs[j]
    for id_c, c in enumerate(circuits):
        for x in (circuit_to_add, circuit_oi):
            if x in c:
                indexes.append(id_c)
    if len(indexes) == 0:
        circuits.append([circuit_to_add, circuit_oi])
    elif len(indexes) == 1:
        circuits_to_update = circuits[indexes[0]]
        circuits[indexes[0]] += [
            x for x in (circuit_to_add, circuit_oi) if x not in circuits_to_update
        ]
    elif len(indexes) == 2:
        if indexes[0] == indexes[1]:
            pass
        else:
            circuits[indexes[0]] += circuits[indexes[1]]
            circuits.pop(indexes[1])
    index += 1
    if index == 999:
        res = 1
        for x in sorted([len(elt) for elt in circuits])[::-1][:3]:
            res *= x
        print(res)
    if len(circuits[0]) == len(inputs):
        print(circuit_to_add[0] * circuit_oi[0])
