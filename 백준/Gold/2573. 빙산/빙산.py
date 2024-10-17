import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
q = []

def area(x, y):
    return 0 <= x < n and 0 <= y < m

directions = [(-1,0), (1,0), (0,-1), (0,1)]

for i in range(n):
    for j in range(m):
        if arr[i][j] != 0:
            cnt = 0
            for di, dj in directions:
                ni, nj = di+i, dj+j
                if area(ni, nj) and arr[ni][nj] == 0:
                    cnt += 1
            q.append((i, j, cnt))

answer = 0

while q:
    answer += 1
    tmp = []
    
    while q:
        i, j, ice = q.pop()
        if arr[i][j] > ice:
            arr[i][j] -= ice
            tmp.append((i, j))
        else:
            arr[i][j] = 0

    visited = {}
    if len(tmp) > 0:
        check = False

        c = 0
        for ti, tj in tmp:
            if not visited.get((ti, tj)):
                c += 1
                if c >= 2:
                    check = True
                    break

                visited[(ti, tj)] = c
                lst = [(ti, tj)]

                while lst:
                    li, lj = lst.pop()
                    cnt = 0

                    for di, dj in directions:
                        nx, ny = di+li, dj+lj

                        if area(nx, ny):
                            if not visited.get((nx, ny)) and arr[nx][ny] != 0:
                                visited[(nx, ny)] = c
                                lst.append((nx, ny))
                            elif arr[nx][ny] == 0:
                                cnt += 1
                    q.append((li, lj, cnt))

        
        if check:
            print(answer)
            break
if not check:
    print(0)