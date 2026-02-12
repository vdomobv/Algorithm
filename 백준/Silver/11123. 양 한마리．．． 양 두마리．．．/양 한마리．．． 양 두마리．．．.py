import sys
input = sys.stdin.readline
from collections import deque

t = int(input())
direction = [(-1,0), (1,0), (0,1), (0,-1)]
for _ in range(t):
    h, w = map(int, input().split())
    arr = [list(input().strip()) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    answer = 0

    for x in range(h):
        for y in range(w):
            if visited[x][y] == 0:
                visited[x][y] = 1
                if arr[x][y] == "#":
                    q = deque([(x, y)])
                    answer += 1

                    while q:
                        i, j = q.popleft()
                        for di, dj in direction:
                            ni, nj = i+di, j+dj
                            if 0 <= ni < h and 0 <= nj < w and visited[ni][nj] == 0:
                                visited[ni][nj] = 1

                                if arr[ni][nj] == "#":
                                    q.append((ni, nj))
    
    print(answer)