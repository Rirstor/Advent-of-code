from itertools import pairwise
points = [list(map(int, elt.split(","))) for elt in open("day09/input").readlines()]
points = [i[1] +1j*i[0] for i in points]
def area(pos1, pos2):
    return (abs(pos1.real-pos2.real)+1) * (abs(pos1.imag-pos1.imag)+1)
areas = set(((x,y), (abs(x.real-y.real)+1) * (abs(x.imag-y.imag)+1)) for x in points for y in points)
print(max(areas, key = lambda x : x[-1]))
# part2
edges = [(points[i], points[i-1]) for i in range(len(points))]
for pos, ar in sorted(areas, key=lambda x : x[-1], reverse=True):
    p1, p2 = pos
    x1, y1 = p1.real, p1.imag
    x2, y2 = p2.real, p2.imag
    x1, x2 = sorted((x1, x2))
    y1, y2 = sorted((y1, y2))
    count = 0
    for e1, e2 in edges:
        x3, x4 = e1.real, e2.real
        y3, y4 = sorted((e1.imag, e2.imag))
        if x4 > x1 and x3< x2 and y4 > y1 and y3 < y2:
            count += 1
            break
    if count == 0:
        print(ar)
        break
