import numpy as np
import shapely as sh

pipes = np.array([[i for elt in l.split() for i in elt] for l in open("day10/input.txt")])

dict_mapping = {"|": {"S": ("S", (-1, 0)), "N": ("N", (1, 0))},
                "-": {"E": ("E", (0, 1)), "W": ("W", (0, -1))},
                "L": {"N": ("E", (0, 1)), "W": ("S", (-1, 0))},
                "J": {"N": ("W", (0, -1)), "E": ("S", (-1, 0))},
                "7": {"S": ("W", (0, -1)), "E": ("N", (1, 0))},
                "F": {"S": ("E", (0, 1)), "W": ("N", (1, 0))}}

pipes_offsets = {""}


def get_available_movements(pipe):
    return [key for key in dict_mapping if pipe in dict_mapping[key]]


def get_new_card(pipe, old_card):
    return dict_mapping[pipe][old_card][0]


def get_adjacent_pipes(coords, pipe, card):
    offset_pipe = dict_mapping[pipe][card][1]

    return (coords[0] + offset_pipe[0], coords[1] + offset_pipe[1])


start_point = tuple(elt[0] for elt in np.where(pipes == "S"))
start_dict = {start_point: "Start"}
coord_start = ""
# next_pipe = pipes[start_point] +

dict_pipe1 = {**start_dict, (29, 72): "S"}
dict_pipe2 = {**start_dict, (30, 73): "E"}
dicts = [dict_pipe1, dict_pipe2]

for d in dicts:
    current_coords = [key for key in d if d[key] != "Start"][0]
    key = None
    pipe_oi = pipes[current_coords]
    while pipe_oi != "S" and pipe_oi != ".":
        card = d[current_coords]

        current_coords = get_adjacent_pipes(current_coords, pipe_oi, card)
        new_card = get_new_card(pipe_oi, card)
        d[current_coords] = new_card
        pipe_oi = pipes[current_coords]
print(len(d) // 2)

# part 2


points_poly = np.array(list(dict_pipe1.keys()))
points_poly = np.append(points_poly, points_poly[-1][None], axis=0)
poly = sh.Polygon(points_poly)
xx = np.arange(len(pipes))

xx, yy = np.meshgrid(xx, xx)

points = [sh.Point(elt) for elt in zip(xx.ravel(), yy.ravel())]

result = sum(poly.contains_properly(points))
print(1)
