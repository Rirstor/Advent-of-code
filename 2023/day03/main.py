import re
import numpy as np

with open("day3/inputs/data_part1.txt", 'r') as file:
    lines = file.readlines()
    length_line = len(lines[0])

    result = dict()

    whole_file = "".join(lines).replace("\n", ".")
    indices_numbers = [(elt.start(), elt.end()) for elt in re.finditer(r"\d+", whole_file)]
    serial_numbers = list()
    for index in indices_numbers:
        index_range = np.arange(index[0] - 1, index[1] + 1)
        indices = np.array(
            (index_range - length_line).tolist() + index_range.tolist() + (index_range + length_line).tolist())
        indices = indices[(indices >= 0) & (indices <= len(whole_file) - 1)]
        values = np.array([whole_file[idx] for idx in indices])
        mask = [elt not in "0123456789." for elt in values]

        if any(mask):
            number = int("".join([whole_file[idx] for idx in np.arange(*index)]))
            idx = indices[[idx for idx, a in enumerate(mask) if a][0]]

            if idx in result:
                result[idx].append(number)
            else:
                result[idx] = [number]

    print("The sum of the mechanical engine schematic is ", sum([sum(elt) for elt in result.values()]))
    print("Part 2 answer : ", sum([np.prod(elt) for elt in result.values() if len(elt) == 2]))
