def hash(cs, v=None):
    if v is None:
        v = 0
    if len(cs) == 1:
        return h_value(cs, v)
    else:
        return hash(cs[1:], h_value(cs[0], v))


def h_value(c, v):
    return ((ord(c) + v) * 17) % 256


strings = [l for l in open("day15/input").read().split(",")]
# part 1
print(sum([hash(s) for s in strings]))

boxes = dict()


def process_step(cs):
    if "=" in cs:
        id_len, focal = cs.split("=")
        focal = int(focal)
        id_box = hash(id_len)
        data = [id_len, focal]
        if id_box in boxes:
            values = boxes[id_box]
            if any(s := [elt[0] == id_len for elt in values]):
                values[[i for i in range(len(s)) if s[i]][0]][1] = focal
            else:
                boxes[id_box].append(data)
        else:
            boxes[id_box] = [data]
    elif "-" in cs:
        id_len, _ = cs.split("-")
        id_box = hash(id_len)
        if id_box in boxes:
            d = boxes[id_box]
            for elt in d:
                if elt[0] == id_len:
                    boxes[id_box].remove(elt)
            if boxes[id_box] == []:
                boxes.pop(id_box)
    print(1)


# part 2

[process_step(s) for s in strings]
res = 0
for k, v in boxes.items():
    fp = sum([(k + 1) * (i + 1) * v[i][1] for i in range(len(v))])
    res += fp
print(res)
