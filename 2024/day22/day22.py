secret = list(map(int, [line.strip() for line in open("input")]))


def mix(sn, number):
    return sn ^ number


def prune(number):
    return number % 16777216


def f(sn):
    sn = prune(mix(sn, sn * 64))
    sn = prune(mix(sn, sn // 32))
    sn = prune(mix(sn, sn * 2048))
    return sn


mapsequence = dict()


def generator(sn, nbtimes):
    result = [sn]
    sns = [int(str(sn)[-1])]
    check = dict()
    while nbtimes != 0:
        newsn = f(result[-1])
        result.append(newsn)
        sns.append(int(str(newsn)[-1]))
        sequence = tuple(sns[-5:])
        if len(sequence) == 5:
            seq = tuple(y - x for y, x in zip(sequence[1:], sequence[:-1]))
            if seq not in check:
                check[seq] = sns[-1]
        nbtimes -= 1
    for key in check:
        if key not in mapsequence:
            mapsequence[key] = check[key]
        else:
            mapsequence[key] += check[key]
    return result[-1]


part1 = sum([generator(sn, 2000) for sn in secret])
print(part1)
part2 = max(mapsequence.values())
print(part2)
