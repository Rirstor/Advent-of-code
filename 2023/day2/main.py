import numpy as np
import re
from itertools import chain


def get_score_games(file):
    colors_cubes = ["red", "green", "blue"]
    pattern = "|".join(colors_cubes)
    with open(file, "r") as f:
        lines = f.readlines()
        nb_draws = np.max([len(elt.split(":")[1].split(";")) for elt in lines])
        score_game = np.zeros((len(lines), nb_draws * len(colors_cubes)), dtype=int)

        for id_line, line in enumerate(lines):

            for id_results, results in enumerate(line.split(":")[1].split(';')):
                dict_init = {key: value for key, value in zip(colors_cubes, np.zeros((3,), dtype=int))}
                scores = re.findall(r"\d+", results)
                colors = re.findall(pattern, results)
                dict_init.update({key: int(value) for key, value in zip(colors, scores)})

                score_game[id_line, id_results * 3: (id_results + 1) * 3] = list(dict_init.values())

    return score_game


def process_score(score, nb_cubes: list):
    # Order of nb_cubes : red, green, blue
    list_ids = list()
    for id_cube, nb_cube in enumerate(nb_cubes):
        impossible_game_ids = np.argwhere(score[:, id_cube + np.arange(len(score[0]), step=3)] > nb_cube)
        list_ids.append(impossible_game_ids[:, 0].tolist())
    unique_ids = np.unique(list(chain.from_iterable(list_ids)))

    return unique_ids


def day2_part1(file, nb_cubes):
    score = get_score_games(file)
    ids = process_score(score, nb_cubes)
    result = np.sum(np.arange(1, len(score) + 1)) - np.sum(ids + 1)
    return result


def day2_part2(file):
    score = get_score_games(file)
    nb_min_cubes = np.zeros((len(score), 3), dtype=int)
    for id_cube in range(3):
        col_cube = score[:, id_cube + np.arange(len(score[0]), step=3)]
        values = np.max(col_cube, axis=1)
        nb_min_cubes[:, id_cube] = values
    result = np.prod(nb_min_cubes, axis=1).sum()
    return result


if __name__ == "__main__":
    file_part1 = "day2/inputs/data_part1.txt"
    result = day2_part1(file_part1, [12, 13, 14])
    print("The sum of the IDS of the game possible for part 1 is ", result)

    file_part2 = "day2/inputs/data_part1.txt"
    result = day2_part2(file_part2)
    print("The power of the fumes for part 2 is ", result)
