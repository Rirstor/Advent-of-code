# part1


inputs = [l.strip("\n") for l in open("day1/input").readlines()]

start = 50

def apply_rot(state, command, count):
    rot, value = command[0], int(command[1:])
    new_state = state + value if rot == "R" else state - value
    if new_state * start <0:
        count += 1
    
    count += abs(new_state) // 100 + int(new_state == 0)
    new_state = abs(new_state % 100)
    return abs(new_state % 100), count
count = 0
for i in inputs:
    new_state, count = apply_rot(start, i, count)
    start = new_state
print(count)

