import sys
input = sys.stdin.readline
from collections import deque

r, c = map(int, input().split())
arr = []
now = []
water = []
visited = [[-1] * c for _ in range(r)]
directions = [(-1, 0), (1,0), (0,-1), (0,1)]
ai, aj = 0, 0

for i in range(r):
    arr.append(list(input().strip()))

    for j in range(c):
        if arr[i][j] == "S":
            now.append((i, j))
            visited[i][j] = 0
            arr[i][j] = "."
        elif arr[i][j] == "*":
            water.append((i, j))
            visited[i][j] = 0
        elif arr[i][j] == "D":
            ai, aj = i, j

while True:
    flag = False

    tmp = []
    for x, y in water:
        for dx, dy in directions:
            nx, ny = dx+x, dy+y
            if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] == ".":
                arr[nx][ny] = "*"
                tmp.append((nx, ny))
    water, tmp = tmp, []

    while now:
        i, j = now.pop()
        for di, dj in directions:
            ni, nj = di+i, dj+j
            if 0 <= ni < r and 0 <= nj < c and visited[ni][nj] == -1:
                if arr[ni][nj] == "D":
                    flag = True
                    visited[ni][nj] = visited[i][j] + 1
                    tmp.append((ni, nj))
                    break
                elif arr[ni][nj] == ".":
                    visited[ni][nj] = visited[i][j] + 1
                    tmp.append((ni, nj))
    
    now, tmp = tmp, []
    if now == []:
        break

    if flag:
        break

print(visited[ai][aj] if visited[ai][aj] != -1 else "KAKTUS")