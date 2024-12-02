reports = [list(map(int, line.strip().split())) for line in open("day02/input")]

# part1

differences = [[(x - y) for y, x in zip(elt[:-1], elt[1:])] for elt in reports]

safe = sum(
    [(all(i > 0 for i in elt) | all(i < 0 for i in elt)) * all([abs(i) < 4 for i in elt]) for elt in differences])
print(safe)
# part2
safe_dampener = 0

for elt in reports:
    check = list()
    for k in range(len(elt)):
        elt2 = elt[:k] + elt[k + 1:]
        differences = [(x - y) for y, x in zip(elt2[:-1], elt2[1:])]
        check.append((all(i > 0 for i in differences) | all(i < 0 for i in differences)) * all([abs(i) < 4 for i in differences]))
    safe_dampener += any(check)
print(safe_dampener)
