from itertools import product

inputs = [[elt.split() for elt in line.strip().split(':')] for line in open("day07/input")]


# part1
def compute(numbers, sequence):
    if len(numbers) == 2:
        return eval_expression(numbers[0], numbers[1], sequence[0])
    else:
        newnumber = eval_expression(numbers[0], numbers[1], sequence[0])
        return compute([newnumber] + numbers[2:], sequence[1:])


def eval_expression(n1, n2, operator):
    if operator == "*":
        return n1 * n2
    elif operator == "+":
        return n1 + n2
    else:
        return int(str(n1) + str(n2))


def f(element, part=1):
    target = int(element[0][0])
    numbers = list(map(int, element[1]))
    sequences = list(product("+*" if part == 1 else ("+*|"), repeat=len(numbers) - 1))
    values = [compute(numbers, seq) for seq in sequences]
    return target if target in values else 0


part1 = sum([f(elt) for elt in inputs])

print(part1)

part2 = sum([f(elt, part=2) for elt in inputs])

print(part2)
