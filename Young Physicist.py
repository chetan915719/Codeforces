n=int(input(""))
lst = []
for x in range(n):
    t = list(map(int,input().split()))
    lst.append(t)
sum = [0,0,0]
for x in range(n):
    for y in range(3):
        sum[y] = sum[y] + lst[x][y]

if sum == [0,0,0]:
    print("YES")
else:
    print("NO")
