import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]
visited = [[[0] * m for _ in range(n)] for _ in range(2)]
direction = [(-1,0), (1,0), (0,-1), (0,1)]
visited[0][0][0] = 1

q = deque([(0, 0, 0)])
answer = -1
while q:
    z, x, y = q.popleft()

    if x == n-1 and y == m-1:
        answer = visited[z][x][y]
        break

    for di, dj in direction:
        ni, nj = x+di, y+dj
        if 0<= ni < n and 0 <= nj < m:
            if arr[ni][nj] == "0" and visited[z][ni][nj] == 0:
                visited[z][ni][nj] = visited[z][x][y] + 1
                q.append((z, ni, nj))
            elif arr[ni][nj] == "1" and z == 0:
                visited[1][ni][nj] = visited[0][x][y] + 1
                q.append((1, ni, nj))

print(answer)