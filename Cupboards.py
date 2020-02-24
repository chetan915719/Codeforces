n = int(input())
lst = list()
for i in range(n):
    lst.append(list(map(int,input().split())))

open_left = 0
open_right = 0

for i in range(n):
    if(lst[i][0] == 1):
        open_left += 1
    if(lst[i][1] == 1):
        open_right += 1
        

print(min(open_left,n-open_left)+min(open_right,n-open_right))
