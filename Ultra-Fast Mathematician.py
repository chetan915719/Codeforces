lst1 = list(input())
lst2 = list(input())
lst3 = list()
for i in range(len(lst1)):
    if lst1[i] == lst2[i]:
        lst3.append("0")
    else:
        lst3.append("1")
num = ''.join(lst3)
print(num)
