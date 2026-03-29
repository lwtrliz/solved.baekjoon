n = int(input())

for _ in range(n):
    gameWord = str(input())
    p1 = []
    p2 = []
    if len(gameWord)%2 == 0:
        for i in range(len(gameWord)):
            if i%2 == 0:
                p1.append(gameWord[i])
            else:
                p2.append(gameWord[i])
        for a in range(len(p1)):
            print(p1[a], end="")
        print("")
        for b in range(len(p1)):
            print(p2[b], end="")
        print("")
    else:
        gameWord = gameWord+gameWord
        for i in range(len(gameWord)):
            if i % 2 == 0:
                p1.append(gameWord[i])
            else:
                p2.append(gameWord[i])
        for a in range(len(p1)):
            print(p1[a], end="")
        print("")
        for b in range(len(p2)):
            print(p2[b], end="")
        print("")

