import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
arr = []
x, y = 0, 0

for i in range(n):
    tmp = list(map(int, input().split()))
    if 2 in tmp:
        x, y = i, tmp.index(2)
    arr.append(tmp)

q = deque([(x, y)])
visited = [[-1] * m for _ in range(n)]
visited[x][y] = 0
directions = [(-1,0), (1,0), (0,-1), (0,1)]
# print("================")
while q:
    i, j = q.popleft()

    for di, dj in directions:
        ii, jj = i+di, j+dj

        if 0 <= ii < n and 0 <= jj < m:
            if visited[ii][jj] == -1:
                if arr[ii][jj] == 1:
                    visited[ii][jj] = visited[i][j] + 1
                    q.append((ii, jj))

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0 and visited[i][j] == -1:
            print(0, end = ' ')
        else:
            print(visited[i][j], end = ' ')
    print()