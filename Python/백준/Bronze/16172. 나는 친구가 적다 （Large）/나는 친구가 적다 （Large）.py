text = str(input())
wantFind = str(input())

for i in range(10):
    text = text.replace(str(i), "")
if wantFind in text:
    print(1)
else: 
    print(0)