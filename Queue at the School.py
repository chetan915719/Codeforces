n,t = map(int,input().split())
s = list(input())
counter = 0
while(counter != t):
    i = 0
    while(i < n-1):
        if(s[i] == 'B' and s[i+1] == 'G'):
            s[i] = 'G'
            s[i+1] = 'B'
            i += 1
        i += 1
    counter += 1
ans = ''.join(s)
print(ans)