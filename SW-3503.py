TC = int(input())   
ans = []
for tc in range(1, TC + 1):
    k = "#"+str(tc) + " "
    N = int(input())
    lst = list(map(int, input().strip().split()))
    lst.sort(reverse=True)
    mx = max(lst[0]-lst[1], lst[0]-lst[2])
    for i in range(1, N-2):
        mx = max(mx, lst[i] - lst[i+2])
    mx = max(mx, lst[len(lst)-2] - lst[len(lst)-1])
    k += str(mx)
    ans.append(k)
for e in ans:
    print(e)