TC = int(input())
for tc in range(1, TC+1):
    N = input()
    if N[len(N)-1] in ['1','3','5','7','9']:
        print("#%s"%tc, "Odd")
    else:
        print("#%s"%tc, "Even")