TC = 10
ans = []
for tc in range(1, TC + 1):
    k = "#"+str(tc) + " "
    addr = {}
    N, s = map(int, input().split())
    addr[s] = []
    lst = list(map(int, input().split()))
    visited = []
    for i in range(0, N, 2):
        if lst[i] not in addr:
            addr[lst[i]] = []
        if lst[i+1] not in addr[lst[i]]:
            addr[lst[i]].append(lst[i+1])
    visited.append(s)
    temp = []
    temp.extend(addr[s])
    l = []
    l.extend(addr[s])
    maxnum = 0
    while len(l) > 0:
        maxnum = max(l)
        l.clear()
        for i in range(len(temp)):
            if temp[i] not in visited:
                visited.append(temp[i])
                if temp[i] in addr:
                    for e in addr[temp[i]]:
                        if e not in visited:
                            l.append(e)
        temp.clear()
        temp.extend(l)
    k += str(maxnum)
    ans.append(k)
for e in ans:
    print(e)