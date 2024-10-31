import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
board = []
ri, rj, bi, bj, hi, hj = 0, 0, 0, 0, 0, 0

for i in range(n):
    board.append(list(input().strip()))
    for j in range(m):
        if board[i][j] == "B":
            bi, bj = i, j
        elif board[i][j] == "R":
            ri, rj = i, j
        elif board[i][j] == "O":
            hi, hj = i, j

def area(x, y):
    return 0 <= x < n and 0 <= y < m

directions = [(-1,0), (1,0), (0,-1), (0,1)]

def bfs(ri, ry, bi, bj):
    q = deque([(ri, rj, bi, bj, 0)])
    visited = []
    
    while q:
        rx, ry, bx, by, cnt = q.popleft()
        if cnt > 10:
            print(-1)
            return
        
        if board[rx][ry] == "O":
            print(cnt)
            return
            
        for dx, dy in directions:
            nrx, nry, nbx, nby = rx, ry, bx, by
            while True:
                nrx += dx
                nry += dy

                if board[nrx][nry] == "O":
                    break
                elif board[nrx][nry] == "#":
                    nrx -= dx
                    nry -= dy
                    break
            
            while True:
                nbx += dx
                nby += dy

                if board[nbx][nby] == "O":
                    break
                elif board[nbx][nby] == "#":
                    nbx -= dx
                    nby -= dy
                    break
            
            if board[nbx][nby] == "O":
                continue

            if (nrx, nry) == (nbx, nby):
                if abs(nrx-rx) + abs(nry-ry) < abs(nbx-bx) + abs(nby-by):
                    nbx -= dx
                    nby -= dy
                else:
                    nrx -= dx
                    nry -= dy
            
            if (nrx, nry, nbx, nby) not in visited:
                q.append((nrx, nry, nbx, nby, cnt+1))
                visited.append((nrx, nry, nbx, nby))
        
    print(-1)

bfs(ri, rj, bi, bj)