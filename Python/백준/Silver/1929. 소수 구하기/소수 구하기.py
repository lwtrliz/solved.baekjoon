import sys
import math

n, m = map(int, sys.stdin.readline().strip().split())

for i in range(n, m+1):
    notPrime = 0
    x = int(1 + math.sqrt(i))
    if i == 1:
        notPrime += 1
        pass
    else:
        for j in range(2, x):
            if i % j == 0:
                notPrime += 1
                break
    if notPrime == 0:
        print(i)
        