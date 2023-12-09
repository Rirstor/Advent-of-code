import numpy as np

histories = [[int(elt) for elt in l.split()] for l in open("day9/input.txt")]


def increment(history):
    if sum(i != 0 for i in history) == 0:
        return 0
    else:
        return history[-1] + increment(np.diff(history))


test = [increment(np.array(hist).astype(np.int64)) for hist in histories]
test2 = [increment(np.array(hist).astype(np.int64)[::-1]) for hist in histories]

print(sum(test))
print(sum(test2))
