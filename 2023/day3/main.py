import re
import numpy as np

with open("day3/inputs/data_part1.txt", 'r') as file:
    lines = file.readlines()
    length_line = len(lines[0]) - 1

    whole_file = "".join(lines).replace("\n", "")
    indices_numbers = [(elt.start(0), elt.end(0)) for elt in re.finditer(r"\d+", whole_file)]
    serial_numbers = list()
    for index in indices_numbers:
        index_range = np.arange(index[0] - 1, index[1] + 1)
        indices = np.array(
            (index_range - length_line).tolist() + index_range.tolist() + (index_range + length_line).tolist())
        indices = indices[(indices >= 0) & (indices <= len(whole_file) - 1)]
        values = np.array([whole_file[idx] for idx in indices])

        if any([elt not in ".0123456789" for elt in values]):
            serial_numbers.append(int("".join([whole_file[idx] for idx in np.arange(*index)])))

    print("The sum of the mechanical engine schematic is ", sum(serial_numbers))
