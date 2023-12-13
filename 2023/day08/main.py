import math as m
steps, *commands = [line.strip().split("=") for line in open("day8/input.txt")]
steps = steps[0]
dict_steps = dict(R=1, L=0)

dict_commands = {elt[0].strip(): elt[1].replace("(", "").replace(")", "").replace(",", "").split() for elt in
                 commands[1:]}
step = 0
output = "AAA"
while output != "ZZZ":
    output = dict_commands[output][dict_steps[steps[step % len(steps)]]]
    step += 1
print(step)

keys = [key for key in dict_commands if key.endswith("A")]
steps_res = list()
for key in keys:
    output = key
    step = 0
    while not output.endswith("Z"):
        output = dict_commands[output][dict_steps[steps[step % len(steps)]]]
        step += 1
    steps_res.append(step)
print(m.lcm(*steps_res))
