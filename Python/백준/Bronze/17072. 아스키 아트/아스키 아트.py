n, m = map(int, input().split())

for i in range(n):
    line = list(map(int, input().split()))
    for j in range(m):
        iRGB = 2126*line[3*j]+7152*line[3*j+1]+(722*line[3*j+2])
        if iRGB>= 0 and iRGB < 510000:
            print("#", end="")
        elif iRGB >= 510000 and iRGB < 1020000:
            print("o", end="")
        elif iRGB >= 1020000 and iRGB < 1530000:
            print("+", end="")
        elif iRGB >= 1530000 and iRGB < 2040000:
            print("-", end="")
        else:
            print(".", end="")   
    if i == n-1:
        pass
    else:
        print("")