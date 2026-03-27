a, b, goal = map(int,input().split())


if a > goal:
    print(a)
else:
    if (goal-b)/(a-b) > (goal-b)//(a-b):
        print((goal-b)//(a-b)+ 1)
    else:
        print((goal-b)//(a-b))