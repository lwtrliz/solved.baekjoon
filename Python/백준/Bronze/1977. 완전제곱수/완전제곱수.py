import math

n = int(input())

m = int(input())

low = 0
count = 0

for i in range(n, m+1, 1):
    if i == int(math.sqrt(i))**2:
        if low > 0: pass
        else: low = i
        count += i
if count != 0: print(count); print(low)
else: print(-1)