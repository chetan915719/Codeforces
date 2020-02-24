n = int(input())
lst = list(map(int,input().split()))
max_score = lst[0]
min_score = lst[0]
count = 0
for i in range(1,n):
    if lst[i] > max_score:
        max_score = lst[i]
        count += 1
    if lst[i] < min_score:
        min_score = lst[i]
        count += 1
print(count)
