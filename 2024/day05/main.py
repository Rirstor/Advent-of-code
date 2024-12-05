rules, orders = [line.split("\n") for line in open("day05/input").read().split("\n\n")]
orders = [order.split(",") for order in orders]

# part 1
dict_rules = dict()

for rule in rules:
    page1, page2 = rule.split("|")
    if page1 not in dict_rules:
        dict_rules[page1] = [page2]
    else:
        dict_rules[page1].append(page2)
middlepage = list()
for order in orders:
    check = 0
    for id_range in range(len(order) - 1):
        if (not all(x in dict_rules.get(order[id_range], ()) for x in order[id_range + 1:])):
            check += 1
    if check == 0:
        middlepage.append(int(order[len(order) // 2]))
part1 = sum(middlepage)
print(part1)


# part2
def update(order, moved=0):
    for id_range in range(len(order) - 1):
        if (not all(x in dict_rules.get(order[id_range], ()) for x in order[id_range + 1:])):
            pagetomove = order[id_range]
            for j in range(id_range + 1, len(order)):
                if pagetomove in dict_rules.get(order[j], ()):
                    order[id_range] = order[j]
                    order[j] = pagetomove
                    moved += 1
                    break
            moved, new_order = update(order, moved)
    return moved, int(order[len(order) // 2])


part2 = [update(order) for order in orders]
part2 = sum(elt[1] for elt in part2 if elt[0] > 0)
print(part2)
