n = int(input())

if n%2 == 0:
    print("I LOVE CBNU")
else:
    print("*"*n)
    x = (n+1)//2
    for i in range(1, x+1):
        if i == 1:
            print(" "*(x-i)+"*")
        else:
            print(" "*(x-i)+"*"+" "*(2*(i-1)-1)+"*")

        