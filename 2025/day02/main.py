
def func(number):
    str_number = str(number)
    if len(str_number) % 2 !=0:
        return 0
    else:
        length = len(str_number) // 2
        n1,n2 = int(str_number[:length]), int(str_number[length:])
        if n1 == n2:
            return number
        else:
            return 0

def func2(number):
    str_number = str(number)
    for i in range(1, len(str_number)):
        if len(str_number) % i == 0:
            step = len(str_number) // i
            numbers = [str_number[i*j:(j+1)*i] for j in range (step)]
            if all(numbers[0] == numbers[k] for k in range(1, len(numbers))):
                return number
    return 0

inputs =[list(map(int,elt.split("-"))) for elt in open("day02/input").readlines()[0].split(",")]

# elts = [func(i) for elt in inputs for i in range(elt[0], elt[1]+1) ]
elts2 = [func2(i) for elt in inputs for i in range(elt[0], elt[1]+1) ]
print(sum(elts2))
