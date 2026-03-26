a, b = map(int, input().split())

if a%b == 0:
    print(a//b)
else:
    r = a%b
    for i in range(2001):
        if i == 0:
            print(a//b, end="")
            print(".", end="")
        else:
            if (r*10)//b !=0:
                print((r*10)//b, end="")
                r = (r*10)%b
            else:
                break