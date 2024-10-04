import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
arr = []

sx, sy = 0, 0
size = [2, 0]

for i in range(n):
    arr.append(list(map(int, input().split())))
    for j in range(n):
        if arr[i][j] == 9:
            sx, sy = i, j
            break

d = [(-1, 0), (0,-1), (1,0), (0,1)]

def bfs(x, y):
    visited = [[0]*n for _ in range(n)]
    q = deque([(x, y)])
    candidate = []

    visited[x][y] = 1
    while q:
        i, j = q.popleft()

        for di, dj in d:
            ni, nj = di+i, dj+j

            if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0:
                if arr[x][y] > arr[ni][nj] and arr[ni][nj] != 0:
                    visited[ni][nj] = visited[i][j] + 1
                    candidate.append((visited[ni][nj]-1, ni, nj))
                elif arr[x][y] == arr[ni][nj]:
                    visited[ni][nj] = visited[i][j] + 1
                    q.append((ni, nj))
                elif arr[ni][nj] == 0:
                    visited[ni][nj] = visited[i][j] + 1
                    q.append((ni, nj))
    
    return sorted(candidate, key=lambda x: (x[0], x[1], x[2]))

answer = 0
while True:
    arr[sx][sy] = size[0]
    candidates = deque(bfs(sx, sy))
    
    if not candidates:
        break

    a, ax, ay = candidates.popleft()
    answer += a
    size[1] += 1

    if size[0] == size[1]:
        size[0]+= 1
        size[1] = 0
    
    arr[sx][sy] = 0
    sx, sy = ax, ay

print(answer)