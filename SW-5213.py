lst = [0] * 1000002
for i in range(1, 1000001, 2):
    for j in range(i, 1000001, i):
        lst[j] += i
        
for i in range(1, 1000001):
    lst[i+1] += lst[i]

TC = int(input())   
ans = []
for tc in range(1, TC + 1):
    k = "#"+str(tc)
    L, R = map(int, input().split())
    k += " " + str(lst[R] - lst[L-1])
    ans.append(k)
for e in ans:
    print(e)