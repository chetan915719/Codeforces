n =int(input())
lst = list(map(int,input().split()))

max_value = 0
min_value = 1000000

for i in range(n-1,-1,-1):
    if lst[i] >= max_value:
        max_value = lst[i]
        max_index = i
for i in range(n):
    if lst[i] <= min_value:
        min_value = lst[i]
        min_index = i
if max_index > min_index:
    f = 1
else:
    f = 0
print(max_index + n-1 - min_index - f)
