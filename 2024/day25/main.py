data = [l.split() for l in open("input").read().split("\n\n")]

results = dict(keys=[], lock=[])


def f(elt):
    kelt = "keys" if all(x == "#" for x in elt[-1]) else "lock"
    reslist = list()
    for i in range(len(elt[0])):
        elements = [elt[k][i] == "." for k in range(len(elt))]
        res = len(elt[0]) - sum(elements) + 1
        reslist.append(res)
    results[kelt].append(reslist)


[f(d) for d in data]
part1 = 0
for lock in results["lock"]:
    for key in results["keys"]:
        res = [x + y for x, y in zip(lock, key)]
        if all(x <= len(data[0])-2 for x in res):
            part1 += 1
print(part1)