import sys
input = sys.stdin.readline
from collections import deque

m, n = map(int, input().split())
maze = [list(input().strip()) for _ in range(n)]

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

visited = [[-1] * m for _ in range(n)]

q = deque([(0, 0)])
visited[0][0] = 0

while q:
    x, y = q.popleft()
    for dx, dy in direction:
        nx, ny = dx+x, dy+y
        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == -1:
                if maze[nx][ny] == "0":
                    visited[nx][ny] = visited[x][y]
                    q.appendleft((nx, ny))
                else:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

print(visited[n-1][m-1])
