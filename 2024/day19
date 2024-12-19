from functools import cache

towel, design = [line for line in open("input").read().split("\n\n")]
towel = set(towel.split(', '))
length_towels = set(len(elt) for elt in towel)
design = design.split()


@cache
def f(pattern, index, length):
    count = 0
    p = pattern[index: index + length]
    if len(p) < length:
        return False
    if p in towel:
        if index + length == len(pattern):
            count += 1
        else:
            for l in length_towels:
                count += f(pattern, index + length, l)
    return count


part1 = [f(d, 0, l) for d in design for l in length_towels]
print(sum(part1))
part1 = sum(x > 0 for x in [sum(part1[i:i + len(length_towels)]) for i in range(0,
                                                                                len(
                                                                                    part1),
                                                                                len(length_towels))])
print(part1)
