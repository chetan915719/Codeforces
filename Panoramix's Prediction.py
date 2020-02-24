n,m = input().split()
n=int(n)
m=int(m)

def isPrime(num):
    for i in range(2,num):
        if num%i == 0:
            return False
    return True

for i in range(n+1,100):
    if isPrime(i):
        prime = i
        break
if prime == m:
    print("YES")
else:
    print("NO")
