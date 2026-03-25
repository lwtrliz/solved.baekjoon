import math

n = int(input())

number = list(map(int,input().split()))
countPrime = 0

for i in range(n):
    notPrime = 0
    if number[i] <= 1:
        pass
    else:
        sqrt_n = int(math.sqrt(number[i]))

        for j in range(2, sqrt_n+1):
            if number[i] % j == 0:
                notPrime += 1
                break
        if notPrime ==0:
            countPrime += 1

print(countPrime)
