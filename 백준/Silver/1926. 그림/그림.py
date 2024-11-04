import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
picture = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
cnt, answer = 0, 0
q = deque([])

direction = [(-1,0), (1,0), (0,-1), (0,1)]

for i in range(n):
    for j in range(m):
        if picture[i][j] == 1 and visited[i][j] == 0:
            cnt += 1
            visited[i][j] = 1
            q.append((i, j))
            tmp = 0

            while q:
                x, y = q.popleft()
                tmp += 1

                for dx, dy in direction:
                    nx, ny = dx+x, dy+y
                    if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and picture[nx][ny] == 1:
                        q.append((nx, ny))
                        visited[nx][ny] = 1

            if tmp > answer:
                answer = tmp

print(cnt)
print(answer)