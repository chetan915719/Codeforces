n = int(input())
lst = list()
for i in range(n):
    lst.append(list(map(int,input().split())))
count = 0
for i in lst:
    if i.count(1) >= 2:
        count += 1
print(count)
