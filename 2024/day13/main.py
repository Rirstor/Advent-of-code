import re

inputs = [line for line in open("day13/input").read().split("\n\n")]
values_A = [re.findall("X[\+\=](\d+)", elt) for elt in inputs]
values_B = [re.findall("Y[\+\=](\d+)", elt) for elt in inputs]


def f(vA, vB, part=0):
    xA, yA = int(vA[0]), int(vB[0])
    xB, yB = int(vA[1]), int(vB[1])
    if part == 2:
        offset = 10000000000000
    else:
        offset = 0
    targetX = int(vA[-1]) + offset
    targetY = int(vB[-1]) + offset

    target = sum((targetX, targetY))
    coeffX = sum((xA, yA))
    coeffY = sum((xB, yB))

    line = lambda x: (target - coeffX * x) / coeffY
    a = (targetX * coeffY - target * xB) / (coeffY * xA - coeffX * xB)
    b = line(a)
    return int(3 * a + b) if a.is_integer() and b.is_integer() else 0


part1 = [f(vA, vB) for vA, vB in zip(values_A, values_B)]
print(sum(part1))

part2 = [f(vA, vB, part=2) for vA, vB in zip(values_A, values_B)]
print(sum(part2))
