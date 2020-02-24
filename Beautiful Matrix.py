mat = list()
for i in range(5):
    lst = list(map(int,input().split()))
    mat.append(lst)

for i in range(5):
    for j in range(5):
        if(mat[i][j] == 1):
            one_rowLoc = i+1
            one_columnLoc = j+1
ans = abs(3-one_rowLoc) + abs(3-one_columnLoc)
print(ans)