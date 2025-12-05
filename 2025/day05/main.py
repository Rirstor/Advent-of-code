from functools import reduce
ranges, vegetable = open("day05/input").read().split("\n\n")
ranges = [list(map(int,r.split("-"))) for r in ranges.split("\n")]
vegetable = list(map(int, vegetable.split("\n")))
# part1
not_spoiled = set([v for v in vegetable for r in ranges if r[0] <= v <= r[1]])
print(len(not_spoiled))

# part2
ranges_sorted = sorted(ranges, key= lambda elt: elt[0])
finals_ranges = list([ranges_sorted[0]])
index_fr = 0
for r in ranges_sorted[1:]:
    v1,v2 = r
    fr1, fr2 = finals_ranges[index_fr]
    if fr2 >= v1:
        finals_ranges[index_fr] = [fr1, max(fr2, v2)]
    else:
        finals_ranges.append(r)
        index_fr += 1
print(sum(elt[1]-elt[0] +1 for elt in finals_ranges))



