n, m = map(int, input().split())
box = []
cheeze = 0
for _ in range(n):
    t = input().strip()
    cheeze += t.count('1')
    box.append(t.split())

directions = [(-1,0), (1,0), (0,-1), (0,1)]
answer = 0

while cheeze > 0:
    answer += 1
    q = [(0,0)]
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    melt = []

    while q:
        i, j = q.pop()

        for di, dj in directions:
            ni, nj = di+i, dj+j

            if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] < 2:
                if box[ni][nj] == '1':
                    visited[ni][nj] += 1
                    if visited[ni][nj] == 2:
                        melt.append((ni, nj))
                elif box[ni][nj] == '0':
                    q.append((ni, nj))
                    visited[ni][nj] = 2
    
    cheeze -= len(melt)
    if cheeze == 0:
        break

    for mi, mj in melt:
        box[mi][mj] = '0'

print(answer)

