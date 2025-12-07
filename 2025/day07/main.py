positions = {"S": [], ".": [], "^": []}

inputs = open("day07/input").read().split("\n")

[positions[inputs[row][col]].append(row + 1j * col) for row in range(len(inputs)) for col in range(len(inputs[0]))]

index_row, end, beams = 1, len(inputs) - 1, {positions["S"][0]: 1}
splitters = ()
while index_row != end:
    splitters_row = [x for x in positions["^"] if x.real == index_row]
    to_remove = list()
    new_bs = list()
    value = 0
    keys_to_add, to_remove = {}, list()
    for b in beams:
        value = beams[b]

        for s in splitters_row:
            if b.real +1 == s.real and b.imag == s.imag:
                splitters += (s, )
                to_remove.append(b)
                b1, b2 = b - 1j, b + 1j
                for key, value in zip((b1, b2), (value, value)):
                    if key == 6 +8j:
                        print(1)
                    if key in keys_to_add:
                        keys_to_add[key] += value
                    else:
                        keys_to_add[key] = value
                break
    [beams.pop(elt) for elt in set(to_remove)]
    for key, value in keys_to_add.items():
        if key in beams:
            beams[key] += value
        else:
            beams[key] = value
    beams = {key + 1 : value for key, value in beams.items()}
    index_row += 1

print(len(set(splitters))), print(sum(beams.values()))
