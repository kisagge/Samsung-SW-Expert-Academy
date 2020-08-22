TC = int(input())   
ans = []
for tc in range(1, TC + 1):
    k = "#"+str(tc) + " "
    N = int(input())
    count = 0
    lst = []
    for i in range(N):
        a, b = map(int, input().split())
        for e in lst:
            if (a - e[0]) * (b - e[1]) < 0:
                count += 1
        lst.append((a,b))
    k += str(count)
    ans.append(k)
for e in ans:
    print(e)