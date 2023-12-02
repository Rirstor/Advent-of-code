import re
import numpy as np
from itertools import chain


def calibration_part1(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        digits = [re.findall(r"\d", elt) for elt in lines]

        numbers = [int(elt[0] + elt[-1]) for elt in digits]
    return np.array(numbers).sum()


def calibration_part2(file):
    accepted_digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    dict_digits = {key: value for key, value in zip(accepted_digits, np.arange(1, 10).astype(str))}

    with open(file, 'r') as f:
        lines = f.readlines()

        possible_digits = [re.findall(r"(\d)|(?=(" + "|".join(accepted_digits) + r"))", elt) for elt in lines]
        possible_digits = [np.array(list(chain.from_iterable(elt))) for elt in possible_digits]
        possible_digits = [elt[elt != ""] for elt in possible_digits]
        digits = list()
        for d in possible_digits:
            tmp = ""
            for index in [0, -1]:
                value = d[index]
                tmp += dict_digits[value] if value in dict_digits else value
            digits.append(int(tmp))

    return np.array(digits).sum()


if __name__ == "__main__":
    file = "day1/inputs/data.txt"
    cal = calibration_part1(file)
    print("The calibration coefficient for day 1 part 1 is ", cal)

    file2 = "day1/inputs/data_part2.txt"

    cal = calibration_part2(file2)

    print("The calibration coefficient for day 1 part 2 is ", cal)
