TC = int(input())   
ans = []
for tc in range(1, TC + 1):
    k = "#"+str(tc) + " "
    N = int(input())
    lst = list(map(int, input().strip().split()))
    s = sum(lst) / len(lst)
    count = 0
    for e in lst:
        if e <= s:
            count += 1
    k += str(count)
    ans.append(k)
for e in ans:
    print(e)