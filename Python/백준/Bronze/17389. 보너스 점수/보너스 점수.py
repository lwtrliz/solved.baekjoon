n = int(input())
s = str(input().strip())

ans = 0
bonus = 0

for i in range(n):
    if s[i] == "O":
        ans += i + 1 + bonus
        bonus += 1
    else:
        bonus = 0

print(ans)