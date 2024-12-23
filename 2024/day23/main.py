from functools import reduce
from itertools import combinations

pairs = set(tuple(map(tuple, (line.strip().split("-") for line in open("input")))))
pairs = pairs.union((elt[::-1]) for elt in pairs)
computers = set(reduce(tuple.__add__, (tuple([i]) for elt in pairs for i in elt)))
part1 = 0
for pc in combinations(computers, 3):
    p1, p2, p3 = pc
    mask = list(p.startswith("t") for p in pc)
    if any(mask):
        check = {(p1, p2), (p2, p3), (p3, p1)} < pairs
        if check:
            part1 += 1

# part2
network = [{c} for c in computers]
for n in network:
    for c in computers - n:
        if all((c, elt) in pairs for elt in n):
            n.add(c)
maxl = max(len(l) for l in network)
result = [network[i] for i in range(len(network)) if len(network[i]) == maxl]

print(",".join(sorted(result[0])))
