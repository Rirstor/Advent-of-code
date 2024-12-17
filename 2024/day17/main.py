import re

registers, program = ["".join(elt.split()) for elt in open("input").read().split(
    '\n\n')]
registers = list(map(int, re.findall("(\d+)", registers)))
program = list(map(int, re.findall("(\d+)", program)))


def combo(value, r):
    if value <= 3:
        return value
    elif value == 4:
        return r[0]
    elif value == 5:
        return r[1]
    elif value == 6:
        return r[2]


def tick(r):
    pointer = 0
    result = list()
    while pointer < len(program):
        opcode, operand = program[pointer], program[pointer + 1]
        c = combo(operand, r)
        if opcode == 0:
            r[0] = r[0] // (2 ** c)
            pointer += 2
        elif opcode == 1:
            r[1] = r[1] ^ operand
            pointer += 2
        elif opcode == 2:
            r[1] = c % 8
            pointer += 2
        elif opcode == 3:
            if r[0] != 0:
                pointer = operand
            else:
                pointer += 2
        elif opcode == 4:
            r[1] = r[1] ^ r[2]
            pointer += 2
        elif opcode == 5:
            result.append(c % 8)
            pointer += 2
        elif opcode == 6:
            r[1] = r[0] // (2 ** c)
            pointer += 2
        elif opcode == 7:
            r[2] = r[0] // (2 ** c)
            pointer += 2
    return result


part1 = tick(registers)
part1 = ",".join(map(str, part1))
print(part1)

# part 2
def find(a, index):
    print(a)
    result = tick([a, 0, 0])
    if result == program: print(a)
    if result == program[-index:] or not index:
        for n in range(8): find(a * 8 + n, index + 1)


part2 = find(0, 0)
