wires, commands = [l.split("\n") for l in open("example").read().split("\n\n")]
dictw = dict()
for w in wires:
    key, value = w.split(':')
    dictw[key] = int(value)


def f(w1, w2, command):
    if command == "XOR":
        return w1 ^ w2
    elif command == "OR":
        return w1 | w2
    elif command == "AND":
        return w1 & w2


operations = dict()
for c in commands:
    data = c.split()
    for w in (data[0], data[2], data[-1]):
        if w not in dictw:
            dictw[w] = None
    ops = data[1]
    if ops not in operations:
        operations[ops] = [[data[0], data[2], data[-1]]]
    else:
        operations[ops].append([data[0], data[2], data[-1]])
print(1)
while any(x is None for x in dictw.values()):
    for ops in operations:
        wires = operations[ops]
        for w in wires:
            v1 = dictw.get(w[0])
            v2 = dictw.get(w[1])
            v3 = dictw.get(w[2])
            if all(x is not None for x in (v1, v2)) and v3 is None:
                dictw[w[-1]] = f(v1, v2, ops)

keys_withz = sorted([key for key in dictw if key.startswith("z")])[::-1]

part1 = "0b" + "".join(str(dictw[k]) for k in keys_withz)
print(eval(part1))
