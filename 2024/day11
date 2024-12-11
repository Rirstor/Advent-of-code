from functools import cache

inputs = [line for line in open("input").read().split()]


@cache
def f(pebble, blinks, max_blinks):
    count = 0
    if blinks == max_blinks:
        return count
    elif pebble == "0":
        count += f("1", blinks + 1, max_blinks)
    else:
        length = len(pebble)
        if length % 2 == 0:
            count += 1
            for peb in (pebble[:length // 2], pebble[length // 2:]):
                count += f(str(int(peb)), blinks + 1, max_blinks)
        else:
            count += f(str(int(pebble) * 2024), blinks + 1, max_blinks)
    return count


part1 = sum([f(stone, 0, 25) + 1 for stone in inputs])
print(part1)
part2 = sum([f(stone, 0, 75) + 1 for stone in inputs])
print(part2)
