s = list(input())
s1 = ''
i = 0
while(i < len(s)):
    if(s[i] == '.'):
        s1 += '0'
    else:
        if(s[i+1] == "."):
            s1 += '1'
        else:
            s1 += '2'
        i += 1
    i += 1
print(s1)