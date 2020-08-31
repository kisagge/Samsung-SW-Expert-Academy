TC = int(input())     
for tc in range(1, TC + 1):
    N, M = map(int, input().split())
    board = [[0]*N for _ in range(N)]
    # 백 = 2, 흑 = 1
    board[N//2-1][N//2-1] = 2
    board[N//2-1][N//2] = 1
    board[N//2][N//2-1] = 1
    board[N//2][N//2] = 2

    for i in range(M):
        X, Y, S = map(int, input().split())
        board[Y-1][X-1] = S
        
        direc = 0
        while direc < 8:
            posX, posY = X - 1, Y - 1
            lst = []
            #위쪽 검사
            if direc == 0:
                if posY == 0:
                    direc += 1
                    continue
                else:
                    while board[posY-1][posX] != S:
                        posY -= 1
                        if board[posY][posX] == 0:
                            lst.clear()
                            break
                        lst.append([posX, posY])
                        if posY == 0:
                            lst.clear()
                            break
                    for e in lst:
                        board[e[1]][e[0]] = S
                    direc += 1
            # 위오른쪽
            elif direc == 1:
                if posY == 0 or posX == N-1:
                    direc += 1
                    continue
                else:
                    while board[posY-1][posX+1] != S:
                        posY, posX = posY - 1, posX + 1
                        if board[posY][posX] == 0:
                            lst.clear()
                            break
                        lst.append([posX, posY])
                        if posY == 0 or posX == N-1:
                            lst.clear()
                            break
                    for e in lst:
                        board[e[1]][e[0]] = S
                    direc += 1
            # 오른쪽
            elif direc == 2:
                if posX == N-1:
                    direc += 1
                    continue
                else:
                    while board[posY][posX+1] != S:
                        posX += 1
                        if board[posY][posX] == 0:
                            lst.clear()
                            break
                        lst.append([posX, posY])
                        if posX == N-1:
                            lst.clear()
                            break
                    for e in lst:
                        board[e[1]][e[0]] = S
                    direc += 1
            #아래오른쪽
            elif direc == 3:
                if posY == N-1 or posX == N-1:
                    direc += 1
                    continue
                else:
                    while board[posY+1][posX+1] != S:
                        posY, posX = posY + 1, posX + 1
                        if board[posY][posX] == 0:
                            lst.clear()
                            break
                        lst.append([posX, posY])
                        if posY == N-1 or posX == N-1:
                            lst.clear()
                            break
                    for e in lst:
                        board[e[1]][e[0]] = S
                    direc += 1
            # 아래쪽
            elif direc ==4:
                if posY == N-1:
                    direc += 1
                    continue
                else:
                    while board[posY+1][posX] != S:
                        posY+= 1
                        if board[posY][posX] == 0:
                            lst.clear()
                            break
                        lst.append([posX, posY])
                        if posY == N-1:
                            lst.clear()
                            break
                    for e in lst:
                        board[e[1]][e[0]] = S
                    direc += 1
            #아래왼쪽
            elif direc == 5:
                if posY == N-1 or posX == 0:
                    direc += 1
                    continue
                else:
                    while board[posY+1][posX-1] != S:
                        posY, posX = posY + 1, posX - 1
                        if board[posY][posX] == 0:
                            lst.clear()
                            break
                        lst.append([posX, posY])
                        if posY == N-1 or posX == 0:
                            lst.clear()
                            break
                    for e in lst:
                        board[e[1]][e[0]] = S
                    direc += 1
            #왼쪽
            elif direc == 6:
                if posX == 0:
                    direc += 1
                    continue
                else:
                    while board[posY][posX-1] != S:
                        posX -= 1
                        if board[posY][posX] == 0:
                            lst.clear()
                            break
                        lst.append([posX, posY])
                        if posX == 0:
                            lst.clear()
                            break
                    for e in lst:
                        board[e[1]][e[0]] = S
                    direc += 1
            #위왼쪽
            elif direc == 7:
                if posY == 0 or posX == 0:
                    direc += 1
                    continue
                else:
                    while board[posY-1][posX-1] != S:
                        posY, posX = posY - 1, posX - 1
                        if board[posY][posX] == 0:
                            lst.clear()
                            break
                        lst.append([posX, posY])
                        if posY == 0 or posX == 0:
                            lst.clear()
                            break
                    for e in lst:
                        board[e[1]][e[0]] = S
                    direc += 1
    black, white = 0, 0
    for e in board:
        black += e.count(1)
        white += e.count(2)
    print("#%s"%tc, black, white)