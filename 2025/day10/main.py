from collections import deque

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp

inputs = [elt for elt in open("day10/input").read().split("\n")]

def solve(diagram, buttons):
    to_be_on = set(i for i in range(len(diagram)) if diagram[i] == "#")
    queue = deque([0])
    visited = {0:0}
    while len(queue) >0:
        state = queue.popleft()
        press = visited[state]
        next_presses = press + 1
        actual_state = set(() if isinstance(state, int) else state)
        for b in buttons:
            new_state = (b | actual_state) - actual_state.intersection(b)

            if new_state == to_be_on:
                return next_presses
            new_state = tuple(new_state)
            if new_state not in visited:
                visited[new_state] = next_presses
                queue.append(new_state)

def solve2(voltage, buttons):
    nb_buttons = len(buttons)
    nb_voltage = len(voltage)
    row = list()
    for b in buttons:
        new_row = []
        for i in range(nb_voltage):
            new_row.append(1 if i in b else 0)
        row.append(new_row)

    A = np.array(row).T
    b_l = np.array(list(voltage))
    c = np.ones(nb_buttons)
    constraints = LinearConstraint(A,b_l,b_l)
    integrality = np.ones(nb_buttons)
    bounds = Bounds(lb=0, ub=np.inf)

    res = milp(c=c, constraints=constraints, integrality=integrality, bounds=bounds)
    return res.fun
    
result = 0
result2 = 0
for s in inputs:
    diagram, *buttons, voltage = s.split(' ')
    diagram, buttons = diagram[1:-1], [eval(a) for a in buttons]
    buttons = [{x} if isinstance(x, int) else set(x) for x in buttons ]
    voltage = [int(x) for x in voltage[1:-1].split(',')]
    result+= solve(diagram, buttons)
    result2 += solve2(voltage, buttons)
print(result, result2)