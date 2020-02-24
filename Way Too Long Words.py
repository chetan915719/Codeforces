n = int(input())
lst = list()
for i in range(n):
    lst.append(input())
newLst = list()
for i in lst:
    if len(i) > 10:
        s = i[0] + str(len(i)-2) + i[len(i)-1]
    else:
        s = i
    newLst.append(s)
for i in newLst:
    print(i)
