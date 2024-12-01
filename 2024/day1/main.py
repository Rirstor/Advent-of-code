# part 1


list1, list2 = map(list, zip(*[map(int, line.strip().split()) for line in open("day1/input")]))
list1.sort()
list2.sort()

result = sum(abs(x - y) for x, y in zip(list1, list2))
print(result)
# part 2

similarity = sum([elt * sum([elt == elt2 for elt2 in list2]) for elt in list1])
print(similarity)
