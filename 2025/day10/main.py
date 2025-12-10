from collections import deque
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
result = 0
for s in inputs:
    diagram, *buttons, voltage = s.split(' ')
    diagram, buttons = diagram[1:-1], [eval(a) for a in buttons]
    buttons = [{x} if isinstance(x, int) else set(x) for x in buttons ]
    result+= solve(diagram, buttons)
print(result)
