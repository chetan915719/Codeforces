k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())
lst = [0]*d
for i in range(0+k-1,d,k):
    lst[i] = 1
for i in range(0+l-1,d,l):
    lst[i] = 1
for i in range(0+m-1,d,m):
    lst[i] = 1
for i in range(0+n-1,d,n):
    lst[i] = 1
print(lst.count(1))
