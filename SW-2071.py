TC = int(input())
for tc in range(1, TC+1):
    avg = 0
    lst = list(map(int, input().split()))
    for ele in lst:
        avg += ele
    print("#%s"%tc, round(avg/len(lst)))