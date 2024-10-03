import sys
input = sys.stdin.readline

n, m = map(int, input().split())
directions = [(-1, 0), (0, 1), (1, 0), (0,-1)]
now = tuple(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]

answer = 0
stack = [now]

while stack:
    x, y, d = stack.pop()
    if arr[x][y] == 0:
        answer += 1
        arr[x][y] = 2

    for i in range(d-1, d-5, -1):
        j = i%4
        dx, dy = directions[j]

        nx, ny = x+dx, y+dy
        if arr[nx][ny] == 0:
            stack.append((nx, ny, j))
            break
    else:
        dx, dy = directions[d]
        nx, ny = x-dx, y-dy
        if arr[nx][ny] != 1:
            stack.append((nx, ny, d))

print(answer)
