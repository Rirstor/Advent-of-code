
points = [list(map(int, elt.split(","))) for elt in open("day09/input").readlines()]
points = [i[0] +1j*i[1] for i in points]
areas = [(abs(x.real-y.real)+1) * (abs(x.imag-y.imag)+1) for x in points for y in points]
center_real = sum([x.real for x in points]) / len(points)
center_imag = sum([x.imag for x in points]) / len(points)
print(max(areas))
def manhattan(number):
    return abs(number.real-center_real) + abs(number.imag - center_imag)
# part2
candidates = []
for p1 in points:
    for p2 in set(points) - {p1}:
        rect = {min(p1.real, p2.real) + 1j*min(p1.imag, p2.imag),
                max(p1.real, p2.real) + 1j*min(p1.imag, p2.imag),
                max(p1.real, p2.real) + 1j*max(p1.imag, p2.imag),
                min(p1.real, p2.real) + 1j*max(p1.imag, p2.imag)} - {p1, p2}
        to_add = 0
        for c in rect:
            p = [p for p in set(points) - {p1,p2} if p.real == c.real or c.imag == p.imag]
            distances = [manhattan(c) - manhattan(v) for v in p]
            if all(dist <= 0 for dist in distances):
                to_add += 1
        if to_add == 2:
            import matplotlib.pyplot as plt
            plt.plot([x.real for x in points], [x.imag for x in points])
            plt.scatter(p1.real, p1.imag, marker="x")
            plt.scatter(p2.real, p2.imag, marker="x")
            plt.show()
            candidates.append((abs(p1.real-p2.real)+1) * (abs(p1.imag-p2.imag)+1))
print(int(max(candidates)))
