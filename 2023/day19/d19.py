import json
from itertools import chain

commands, parts = open("day19/input").read().strip().split("\n\n")
commands = commands.split("\n")
parts = parts.split("\n")
pp = list()
for p in parts:
    for c in "xmas":
        p = p.replace(c, f'"{c}"')
    p = p.replace(",", " ,").replace("=", " : ")
    pp.append(json.loads(p))

commands = {elt[:elt.index("{")]: [[j for j in i.split(":")] for i in elt[elt.index("{") + 1: -1].split(",")] for elt in
            commands}


def apply(lst, part):
    if len(lst) > 1:
        value = lst[0][0]
        data = part[value]
        comparison = eval(lst[0].replace(value, str(data)))
        if comparison:
            return lst[1]
    else:
        return lst[0]


def process(part: dict, lc: dict):
    for c in lc:
        new_step = apply(c, part)
        if new_step is not None:
            if new_step in commands:
                return process(part, commands[new_step])
            else:
                return new_step


results = [process(p, commands["in"]) for p in pp]
# part 1

print(sum(sum(list(pp[i].values())) for i in range(len(results)) if results[i] == "A"))
