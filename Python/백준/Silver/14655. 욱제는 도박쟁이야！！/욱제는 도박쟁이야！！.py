n = int(input())

sumation = 0

for i in range(2):
    box = list(map(int, input().split()))
    for j in range(n):
        sumation = sumation + abs(box[j])
print(sumation)

