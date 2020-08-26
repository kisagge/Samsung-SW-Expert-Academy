from cmath import *
TC = int(input())   
ans = []
for tc in range(1, TC + 1):
    k = "#"+str(tc) + " "
    p, q = map(int, input().split())
    x1, y1, x2, y2 = 0, 0, 0, 0
    for i in range(1,10000):
        y = 3-2*i
        l = pow((2*i-3)*(2*i-3) - 4 * (i**2 - i + 2 - 2 * p),0.5)
        y += l
        y /= 2
        if y.is_integer():
            x1 = i
            y1 = int(y)
            break
     
    for i in range(1,10000):
        y = 3-2*i
        l = pow((2*i-3)*(2*i-3) - 4 * (i**2 - i + 2 - 2 * q),0.5)
        y += l
        y /= 2
        if y.is_integer():
            x2 = i
            y2 = int(y)
            break
     
    x3 = x1 + x2
    y3 = y1 + y2
    n = (x3**2 + x3)//2 + (y3**2 - y3)//2 + (y3-1)*(x3-1)
    k += str(n)
    ans.append(k)
for e in ans:
    print(e)