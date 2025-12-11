from collections import deque
from functools import cache

components = {
    values[0]: values[1].strip().split(" ")
    for elt in open("day11/input").read().strip().split("\n")
    for c in [elt.split(":")]
    for values in [c]
}

paths = 0

start = "you"
visited = {start : 1}
to_visit = deque(components[start])
while len(to_visit) > 0:
    actual_c = to_visit.pop()
    visited[actual_c] = 1
    new_c = components[actual_c]

    for nc in new_c:
        if nc == "out":
            paths +=1
        else:
            to_visit.append(nc)
print(paths)

@cache
def func(c, has_dac, has_fft):
    if not has_dac:
        has_dac = c== "dac"
    if not has_fft:
        has_fft = c == "fft"
    if c == "out":
        if has_dac and has_fft:
            return 1
        else:
            return 0
    else:
        return sum(func(x, has_dac, has_fft) for x in components[c])
    
test = func("svr", False, False)
print(test)
