TC = int(input())   

n=1000000
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    if i == 2 or i%4 == 1:
        primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False

ans = []
for tc in range(1, TC + 1):
    k = "#"+str(tc) + " "
    count = 0
    L, R = map(int, input().split())
    for e in primes:
        if L <= e <=R:
            count += 1
    k += str(count)
    ans.append(k)
for e in ans:
    print(e)