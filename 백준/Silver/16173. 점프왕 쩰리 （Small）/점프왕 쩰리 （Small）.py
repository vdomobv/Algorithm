import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

direction = [(1,0), (0,1)]
visited = [[0]* n for _ in range(n)]

q = deque([(0, 0)])
visited[0][0] = 1

answer = "Hing"
while q:
    i, j = q.popleft()

    if i == j == (n-1):
        answer = "HaruHaru"
        break

    d = arr[i][j]

    for di, dj in direction:
        ni, nj = i+di*d, j+dj*d

        if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0:
            q.append((ni, nj))    
            visited[ni][nj] = 1
            
print(answer)