from math import prod
import re
# part 1
inputs = [elt.split() for elt in open("day06/input").read().split("\n")]
values = [[elt[j] for elt in inputs]  for j in range(len(inputs[0]))]
print(sum([prod(map(int,elt[:-1])) if elt[-1] == "*" else sum(map(int, elt[:-1])) for elt in values]))

# part2
max_l_columns = [max(len(elt) for elt in v) for v in values]
index = 0
procesed = []
for length in max_l_columns:
    new_list = []
    for v in open("day06/input").read().split("\n"):
        new_list.append(v[index : index + length])
    index += 1 + length
    procesed.append(new_list)
final_columns = list()
for col, l in zip(procesed, max_l_columns):
    new_col = []
    for index_ in range(l):
        new_number = ""
        for c in col[:-1]:
            new_number += c[index_].strip()
        new_col.append(new_number)
    new_col.append(col[-1].strip())
    final_columns.append(new_col)
print(sum([prod(map(int,elt[:-1])) if elt[-1] == "*" else sum(map(int, elt[:-1])) for elt in final_columns]))
