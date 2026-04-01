n = int(input())


for i in range(n):
    player = dict()
    j = int(input())
    for _ in range(j):
        value, name = map(str, input().split())
        player[int(value)] = name
    maxValue = max(player)
    print(player[maxValue])