from copy import copy
from itertools import chain

wires, commands = [l.split("\n") for l in open("input").read().split("\n\n")]
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


def g(listops, dictwires):
    while any(x is None for x in dictwires.values()):
        for ops in listops:
            ws = operations[ops]
            for w in ws:
                v1 = dictwires.get(w[0])
                v2 = dictwires.get(w[1])
                v3 = dictwires.get(w[2])
                if all(x is not None for x in (v1, v2)) and v3 is None:
                    dictwires[w[-1]] = f(v1, v2, ops)
    res = sorted([key for key in dictwires if key.startswith("z")])[::-1]
    binary = "0b" + "".join(str(dictwires[k]) for k in res)
    return binary, res


part1, keys = g(operations, copy(dictw))
print(eval(part1))


def flatten(dct):
    return chain.from_iterable(chain.from_iterable(chain.from_iterable(dct.values())))
# part2
bad_keys = list()
keysx = sorted([key for key in dictw if key.startswith("x")])[::-1]
keysy = sorted([key for key in dictw if key.startswith("y")])[::-1]
valuex = "0b" + "".join(str(dictw[k]) for k in keysx)
valuey = "0b" + "".join(str(dictw[k]) for k in keysy)
expected = bin(eval(valuex) + eval(valuey))
for index in range(len(expected)-2):
    bitexp = expected[len(expected) - (index +2)]
    bitres = part1[len(expected) - (index +2)]
    if bitexp != bitres:
        commands = dict()
        for indexz in [index+1, index, index-1]:
            keyz = f"z{indexz:02d}"
            for c in operations:
                res = [elt for elt in operations[c] if elt[-1]==keyz]
                if len(res) != 0:
                    if c not in commands:
                        commands[c] = [res]
                    else:
                        commands[c].append(res)
        for _ in range(4):
            values = list(flatten(commands))
            for elt in values:
                if not (elt.startswith("x") or elt.startswith("y") or elt.startswith("z")):
                    for c in operations:
                        res = [xx for xx in operations[c] if xx[-1] == elt]
                        if len(res) != 0:
                            if c not in commands:
                                commands[c] = [res]
                            else:
                                if res not in commands[c]:
                                    commands[c].append(res)
        print(1)

