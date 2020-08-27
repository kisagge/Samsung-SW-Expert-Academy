TC = int(input())   
ans = []
for tc in range(1, TC + 1):
    k = "#"+str(tc) + " "
    D, A, B, F = map(int, input().split())
    k += str(float(D*F/(A+B)))
    ans.append(k)
for e in ans:
    print(e)