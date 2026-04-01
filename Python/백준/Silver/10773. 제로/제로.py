import sys

input = sys.stdin.readline

n = int(input())

number = []

lastNb = 0

for i in range(n):
    x = int(input())

    if x == 0:
        number.pop()
    else:
        number.append(x)

print(sum(number))