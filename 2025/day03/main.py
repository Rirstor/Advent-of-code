def func(bank, nb_batteries=12):
    start = bank[:nb_batteries]
    numbers = list(map(int, start))
    for v in bank[nb_batteries:]:
        added = 0
        for index, n in enumerate(numbers[:-1]):
            if n < numbers[index+1] and added == 0:
                numbers.pop(index)
                numbers.append(int(v))
                added += 1
        if numbers[-1] < int(v) and added == 0:
            numbers.pop(-1)
            numbers.append(int(v))
    return int(''.join(map(str,numbers)))

bats = [l.strip("\n") for l in open("day03/input").readlines()]
print(sum([func(bat, nb_batteries=2) for bat in bats]), sum([func(bat, nb_batteries=12) for bat in bats]))
    