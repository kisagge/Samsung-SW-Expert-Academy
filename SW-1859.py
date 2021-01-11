TC = int(input())
 
for tc in range(1, TC+1):
    N = int(input())
    lst = list(map(int, input().split()))[::-1]
    margin = 0
    maxVal = lst[0]
    for i in range(1, N):
        if maxVal > lst[i]:
            margin += maxVal - lst[i]
        else:
            maxVal = lst[i]
    print("#%s"%tc, margin)