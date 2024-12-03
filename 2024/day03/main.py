import re

commands = "".join(["".join(elt.strip()) for elt in open("day03/input")])

# part1

regex = "mul\((\d+),(\d+)\)"

values = re.findall(regex, commands)

result = sum(int(x[0]) * int(x[1]) for x in values)
print(result)
# part 2

prod = re.finditer(regex, commands)
list_indices = list()
data = list(prod)
pos = [elt.span() for elt in data]

indices = [(commands.rfind("do()", 0, elt[0]) >= commands.rfind("don't()", 0, elt[0])) for elt in pos]
res = sum(int(x[0]) * int(x[1]) * int(y) for x, y in zip(values, indices))
print(res)
