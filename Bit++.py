n = int(input())
lst = list()
for i in range(n):
    lst.append(list(input()))
x = 0
for i in lst:
    if i[1] == '+':
        x += 1
    if i[1] == '-':
        x -= 1
print(x)
