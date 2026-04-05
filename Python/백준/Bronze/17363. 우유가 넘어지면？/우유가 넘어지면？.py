n, m = map(int, input().split())

pic = []

for i in range(n):
    pic.append(list(str(input())))
for i in range(m-1, -1, -1):
    for j in range(0, n):
        x = (pic[j])[i]
        if x == '-':
            x = '|'
        elif x == '|':
            x = '-'
        elif x == '/':
            x = '\\'
        elif x == '\\':
            x = '/'
        elif x == '^':
            x = '<'
        elif x == '<':
            x = 'v'
        elif x == 'v':
            x = '>'
        elif x == '>':
            x = '^'
        print(x,end="")
    print()