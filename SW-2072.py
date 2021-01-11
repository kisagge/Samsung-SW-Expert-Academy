TC = int(input())
for tc in range(1, TC+1):
    oddsum = 0
    lst = list(map(int, input().split()))
    for ele in lst:
        if ele&1 == 1:
            oddsum += ele
    print("#%s"%tc, oddsum)