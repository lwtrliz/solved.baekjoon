numberStr = str(input())


strBox = []

for i in range(len(numberStr)):
    strBox.append(int(numberStr[i]))

needSet = 0
needRotable = 0

canRotate = strBox.count(6) + strBox.count(9)

for i in range(len(strBox)):
    if strBox[i] == 6 or strBox[i] == 9:
        strBox[i] = -1


for i in range(10):
    if i in strBox:
        if strBox.count(i) > needSet:
            needSet = strBox.count(i)

if needSet < (canRotate//2+canRotate%2):
    print(canRotate//2+canRotate%2)
else:
    print(needSet)