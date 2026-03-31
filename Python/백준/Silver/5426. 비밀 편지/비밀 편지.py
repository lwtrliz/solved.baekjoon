n = int(input())

for _ in range(n):
    
    string = str(input())
    f = int(len(string)**(1/2))
    alist = []
    z= 0 
    for k in range(f):
        alist.append(list(string[k*f + l] for l in range(0, f, +1)))
    for j in range(f-1, -1, -1):
        for i in range(f):
            print(alist[i][j], end="")
    print("")