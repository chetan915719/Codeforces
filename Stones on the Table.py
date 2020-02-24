n = int(input())
color = input()
sub_color = list()
for i in range(0,len(color)-1):
    sub_color.append(color[i:i+2])
count = 0
for i in sub_color:
    if len(set(i)) == 1:
        count += 1

print(count)
