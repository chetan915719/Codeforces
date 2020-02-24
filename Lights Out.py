sw = list()
for i in range(3):
    lst = list(map(int,input().split()))
    sw.append(lst)
light = [[1,1,1],[1,1,1],[1,1,1]]
for i in range(3):
    for j in range(3):
        while(sw[i][j] > 0):
            if i > 0:
                if(light[i-1][j] == 1):
                    light[i-1][j] = 0
                else:
                    light[i-1][j] = 1
            if i+1 < 3:
                if(light[i+1][j] == 1):
                    light[i+1][j] = 0
                else:
                    light[i+1][j] = 1
            if j > 0:
                if(light[i][j-1] == 1):
                    light[i][j-1] = 0
                else:
                    light[i][j-1] = 1
            if j+1 < 3:
                if(light[i][j+1] == 1):
                    light[i][j+1] = 0
                else:
                    light[i][j+1] = 1
            if(light[i][j] == 1):
                    light[i][j] = 0
            else:
                    light[i][j] = 1
            sw[i][j] -= 1
for i in light:
    for j in i:
        print(j,end='')
    print('')