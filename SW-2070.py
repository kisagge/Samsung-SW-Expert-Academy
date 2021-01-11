TC = int(input())
for tc in range(1, TC+1):
    n1, n2 = map(int, input().split())
    if n1<n2:
        print("#%s"%tc, '<')
    elif n1>n2:
        print("#%s"%tc, '>')
    else:
        print("#%s"%tc, '=')