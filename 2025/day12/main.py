*presents, regions = open("day12/input").read().split("\n\n")
pres = {}
for p in presents:
    key, *data = p.split(':\n')
    data = data[0].split('\n')
    pos_empty, pos_in = list(), list()
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == "#":
                pos_in.append((i,j))
            else:
                pos_empty.append((i,j))
    pres[key] = dict({"#" : pos_in, "." : pos_empty})
possible = 0
for r in regions.split("\n"):
    size, p = r.split(":")
    size = size.split("x")
    size = int(size[0]) * int(size[1])
    p = p.strip().split(" ")
    present_size = sum([len(pres[str(i)]["#"]) * int(p[i]) for i in range(len(p))])
    if present_size <= size:
        possible += 1
print(possible)

