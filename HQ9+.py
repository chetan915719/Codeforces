lst = list(input())
lst1 = ['H','Q','9']
f = 0
for i in lst:
    if i in lst1:
        f = 1
if f == 1:
    print("YES")
else:
    print("NO")
