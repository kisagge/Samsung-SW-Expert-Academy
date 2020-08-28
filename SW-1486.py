from itertools import chain, combinations
TC = int(input())   

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

ans = []
for tc in range(1, TC + 1):
    k = "#"+str(tc) + " "
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))
    lst1 = list(set(powerset(lst)))
    lst2 = []
    for e in lst1:
        if sum(e) >= B:
            lst2.append(sum(e))
    lst2 = list(set(lst2))
    k += str(min(lst2) - B)
    ans.append(k)
for e in ans:
    print(e)