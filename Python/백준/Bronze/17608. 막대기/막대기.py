import sys

n = int(sys.stdin.readline().strip())

sticks = [int(sys.stdin.readline().strip()) for _ in range(n)]

count = 1
maxIndex = n-1

for i in range(n-1, 0, -1):
    if sticks[i-1] > sticks[maxIndex] and sticks[i-1] > sticks[i]:
        count += 1
        maxIndex = i-1

print(count)