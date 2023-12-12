import re
from itertools import combinations
from copy import copy
from itertools import product, chain

lines = [(re.findall(r"([#?]+)", l), tuple(map(int, re.findall("\d+", l)))) for l in open("day12/input.txt")]

results = dict()


def get_possibilities(l):
    if l not in results:
        results[l] = dict()
        l2 = list(copy(l))
        if any([x in ["#"] for x in l2]):
            for i in range(len(l2)):
                if l2[i] == "?":
                    l2[i] = "."
            l2 = "".join(l2)
            values = tuple(len(elt) for elt in re.findall(r"([#]+)", l2))

            results[l][values] = l2

        mutable_c = [i for i in range(len(l)) if l[i] != "#"]
        results[l][(0,)] = ["." * len(l)]

        if len(mutable_c) == 0:
            results[l][(len(l),)] = [l]

        for i in range(len(mutable_c)):
            for p in combinations(mutable_c, i + 1):
                l2 = list(copy(l))
                for j in mutable_c:
                    if j in p:
                        l2[j] = "#"
                    else:
                        l2[j] = "."
                l2 = "".join(l2)
                values = tuple(len(elt) for elt in re.findall(r"([#]+)", l2))

                if values in results[l]:
                    results[l][values].append(l2)
                else:
                    results[l][values] = [l2]


for l, nb in lines:
    for l2 in l:
        get_possibilities(l2)

output = 0
for l, nb in lines:
    prod = 0

    x = [results[key] for key in l if len(results[key]) >= min(nb)]

    y = [elt for elt in product(*[tuple(d.keys()) for d in x])]

    z = [tuple(chain.from_iterable(i)) for i in y]
    new_z = [tuple(i for i in elt if i != 0) for elt in z]
    idx = [i for i in range(len(z)) if new_z[i] == nb]
    res = []
    for i in idx:
        p = []
        indexes = y[i]
        prod = 1
        for k, j in enumerate(indexes):
            prod *= len(x[k][j])
            p.append(x[k][j])
        res.append(p)
        output += prod
    print(output)
print(output)

from functools import lru_cache


@lru_cache
def ways(springs, groups):
    if len(groups) == 0:
        return len(springs) == 0 or all(s in ["?", "."] for s in springs)
    elif len(springs) == 0:
        return 0
    elif springs[0] == "?":
        return sum(ways(f"{c}{springs[1:]}", groups) for c in [".", "#"])
    elif springs[0] == ".":
        return ways(springs[1:], groups)
    elif springs[0] == "#":
        if not all(s in ["?", "#"] for s in springs[: groups[0]]):
            return 0
        elif len(springs) > groups[0]:
            if springs[groups[0]] == "#":
                return 0
            if springs[groups[0]] in ["?", "."]:
                return ways(springs[1 + groups[0]:], groups[1:])
        elif len(springs) < groups[0]:
            return 0
        elif len(springs) == groups[0]:
            return ways(springs[groups[0]:], groups[1:])


lines = [((list(l.split(" ")[0])), list(map(int, l.split(" ")[1].strip().split(",")))) for l in
         open("day12/input.txt").readlines()]
part_1 = part_2 = 0

for springs, contiguous in lines:
    part_1 += ways("".join(springs), tuple(contiguous))
    part_2 += ways("?".join(["".join(springs)] * 5), tuple(contiguous * 5))

print(part_1)
print(part_2)
