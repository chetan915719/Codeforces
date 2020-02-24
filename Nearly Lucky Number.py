num = list(input())
lucky_num = ['4','7']
lucky_count = 0
for i in num:
    if i in lucky_num:
        lucky_count += 1

if lucky_count == 4 or lucky_count == 7:
    print("YES")
else:
    print("NO")
