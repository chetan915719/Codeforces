lst1 = list(input())
lst2 = list(input())
lst3 = list(input())

temp = lst1+lst2
temp.sort()
lst3.sort()
if temp == lst3:
    print("YES")
else:
    print("NO")
