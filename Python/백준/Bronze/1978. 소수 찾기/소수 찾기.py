n = int(input())



check_prine = list(map(int, input().split()))

count_prime = 0

for i in range(n):
    notPrime = 0
    if check_prine[i] <= 1:
        pass
    else:
        for j in range(2, check_prine[i]-1):
            if check_prine[i] % j == 0:
                notPrime += 1
                break
        if notPrime == 0:
            count_prime += 1

print(count_prime)
