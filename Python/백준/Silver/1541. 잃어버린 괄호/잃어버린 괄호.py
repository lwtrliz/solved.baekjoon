number = list(input().split("-")) #str

result = 0
for i in range(len(number)):
    willCompute = number[i].split("+")
    if i == 0:
        for value in willCompute:
            result += int(value)
    else:
        for value in willCompute:
            result -= int(value)

print(result)
    