n, l = map(int, input().split())

count = 0
i = 1
while True:
    if count == n:
        break
    if str(l) in str(i):
        i += 1
    else:
       max = i
       i += 1
       count += 1
print(max)
