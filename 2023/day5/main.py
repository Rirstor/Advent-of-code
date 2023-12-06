import re

test = [re.findall('\d+', l) for l in open("day5/data.txt")]

seeds = [int(elt) for elt in test[0]]


def isolate(lst):
    output = list()
    tmp = list()
    for id_elt, elt in enumerate(lst):
        if id_elt == len(lst) - 1 and len(tmp) != 0:
            output.append(tmp)
        if len(elt) == 0:
            if len(tmp) != 0:
                output.append(tmp)
                tmp = list()
            continue
        else:
            tmp.append(elt)
    return output


def convert(dest_range_start, source_range_start, range_length, seed_value: str):
    dest_range_start, source_range_start, range_length = int(dest_range_start), int(source_range_start), int(
        range_length)
    max_source = source_range_start + range_length - 1

    if source_range_start <= int(seed_value) <= max_source:
        return str(int(seed_value) + (dest_range_start - source_range_start))
    else:
        return seed_value


def iter_convert(lst_lst, seed_value):
    value = convert(*lst_lst[0], seed_value)
    if value != seed_value:
        return value
    if len(lst_lst) == 1:
        return value
    else:
        return iter_convert(lst_lst[1:], value)


def iter_seed(lst_changes, seed_value):
    value = iter_convert(lst_changes[0], seed_value)
    if len(lst_changes) == 1:
        return value
    else:
        return iter_seed(lst_changes[1:], value)


tmp = isolate(test[1:])
result = [int(iter_seed(tmp, seed_value)) for seed_value in seeds]

start_point = [elt for elt in tmp[-1] if elt[0] in min((elt[0] for elt in tmp[-1]))]

new_modif = [[[elt[1], elt[0], elt[2]] for elt in values] for values in tmp]

test = iter_seed(new_modif, start_point[0][1])
