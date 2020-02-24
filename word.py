s = list(input())
count_upper = 0
count_lower = 0
for i in s:
    if i.isupper():
        count_upper += 1
    else:
        count_lower += 1

string = ''.join(s)

if count_upper > count_lower:
    string = string.upper()
else:
    string = string.lower()

print(string)
