from functools import cache

codes = [line.strip() for line in open("input")]

numeric_pad = {'7': (0, 0), '8': (0, 1), '9': (0, 2), '4': (1, 0), '5': (1, 1), '6': (1, 2), '1': (2, 0), '2': (2, 1),
               '3': (2, 2),
               '0': (3, 1), "A": (3, 2), "bad": (3, 0)}

keypads = {"^": (0, 1), "A": (0, 2), "<": (1, 0), "v": (1, 1), ">": (1, 2), "bad": (0, 0)}

sequences = {(0, 1): ">", (0, -1): "<", (1, 0): "v", (-1, 0): "^"}


@cache
def getmove(start, end):
    ref = keypads if (start in keypads and end in keypads) else numeric_pad
    badpos = ref["bad"]
    pos1, pos2 = ref[start], ref[end]
    xx = pos2[0] - pos1[0]
    yy = pos2[1] - pos1[1]
    movey = sequences[0, (int(yy / abs(yy)))] * abs(yy) if yy != 0 else ''
    movex = sequences[(int(xx / abs(xx))), 0] * abs(xx) if xx != 0 else ''
    checky = (pos1[0], pos1[1] + yy)
    checkx = (pos1[0] + xx, pos1[1])
    prefer_xx_first = (yy > 0 or checky == badpos) and checkx != badpos
    return (movex + movey if prefer_xx_first else movey + movex) + "A"


@cache
def f(code, depth, result=0):
    if depth == 0:
        return len(code)
    else:
        for i, c in enumerate(code):
            result += f(getmove(code[i - 1], c), depth - 1)
    return result


part1 = sum([int(code[:-1]) * f(code, 3) for code in codes])
part2 = sum([int(code[:-1]) * f(code, 26) for code in codes])
print(part1, part2)
