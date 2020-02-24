s = int(input())
t = s+1
while(True):
    lst = set(list(str(t)))
    if(len(lst) == 4):
        print(t)
        break
    else:
        t += 1