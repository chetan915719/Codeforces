n = int(input())
lst = list()
for i in range(n):
    lst.append(list(map(int,input().split())))
maxCap = 0
x = 0
for i in range(n):
    x += lst[i][1]-lst[i][0]
    if x > maxCap:
        maxCap = x
print(maxCap)
