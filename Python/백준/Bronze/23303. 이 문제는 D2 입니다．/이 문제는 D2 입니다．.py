string = str(input())
found_d2 = 0
for i in range(len(string)-1):
    if string[i] == 'd' or string[i] == 'D':
        if string[i+1] == '2':
            found_d2 += 1
            break

if found_d2 != 0:
    print("D2")
else:
    print("unrated")