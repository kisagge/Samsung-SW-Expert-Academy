TC = int(input())   
ans = []
for tc in range(1, TC + 1):
    k = "#"+str(tc) + " "
    N = int(input())
    count = 0
    while N >= 10:
        a = N%10
        N //= 10
        b = N%10
        N //= 10
        if a + b >= 10:
            N = N * 100 + a + b
        else:
            N = N * 10 + a + b
        count += 1
    if count&1 == 0:
        k += 'B'
    else:
        k += 'A'
    ans.append(k)
for e in ans:
    print(e)