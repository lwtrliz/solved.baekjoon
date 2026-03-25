N = int(input())

size_list = list(map(int, input().split()))
buy_list = [0]*len(size_list)

T, P = map(int, input().split())

for i in range(len(size_list)):
    if size_list[i] == 0:
        buy_list[i] = 0
    elif size_list[i] <= T:
        buy_list[i] = 1
    elif size_list[i]%T == 0:
        buy_list[i] = size_list[i]//T
    else:
        buy_list[i] = size_list[i]//T +1

print(sum(buy_list))

print(N//P, N%P)

