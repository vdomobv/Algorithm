import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

blocks = [
    [(0,1), (0,2), (0,3)],
    [(-1,0), (-2,0), (-3,0)],

    [(0,1), (1,0), (1,1)],

    [(1,0), (2,0), (2,1)],
    [(1,0), (0,1), (0,2)],
    [(0,1), (1,1), (2,1)],
    [(1,0), (1,-1), (1,-2)],

    [(0,1), (1,0), (2,0)],    
    [(1,0), (1,1), (1,2)],
    [(1,0), (2,0), (2,-1)],
    [(0,1), (0,2), (1,2)],

    [(1,0), (1,1), (2,1)],
    [(0, -1), (1,-1), (1,-2)],
    [(1,0), (1,-1), (2,-1)],
    [(0,1), (1,1), (1, 2)],

    [(0,1), (1,1), (0,2)],
    [(1,0), (1,-1), (1, 1)],
    [(1,0), (1,-1), (2,0)],
    [(1,0), (1,1), (2,0)]
    ]

answer = 0
for i in range(n):
    for j in range(m):
        for b in blocks:
            t = arr[i][j]
            for dx, dy in b:
                nx, ny = i+dx, j+dy
                if 0 <= nx < n and 0 <= ny < m:
                    t += arr[nx][ny]
                else:
                    break
            else:
                if answer < t:
                    answer = t
print(answer)