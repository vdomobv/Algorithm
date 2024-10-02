import sys
input = sys.stdin.readline

n = int(input())
arr = [input().strip() for _ in range(n)]

d = [(-1,0), (1,0), (0,-1), (0,1)]
visited = [[0]*n for _ in range(n)]
non, colorblind = 0, 0

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            stack = [(i, j)]
            non += 1
            visited[i][j] = 1

            while stack:
                x, y = stack.pop()
                for dx, dy in d:
                    nx, ny = x+dx, y+dy
                    
                    if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and arr[i][j] == arr[nx][ny]:
                        visited[nx][ny] = 1
                        stack.append((nx, ny))

for i in range(n):
    arr[i] = arr[i].replace("R", "G")

visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            q2 = [(i, j)]
            visited[i][j] = 1
            colorblind += 1

            while q2:
                x, y = q2.pop()
                for dx, dy in d:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and arr[nx][ny] == arr[i][j]:
                        visited[nx][ny] = 1
                        q2.append((nx, ny))

print(non, colorblind)