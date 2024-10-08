import copy
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
office = []
cctv = []
empty = 0
visited = [[0] * m for _ in range(n)]
for i in range(n):
    office.append(list(map(int, input().split())))

    for j in range(m):
        if 1 <= office[i][j] < 6:
            cctv.append((i, j, office[i][j]))
        elif office[i][j] == 0:
            empty += 1

directions = {
    1: [[(-1,0)], [(0,-1)], [(1,0)], [(0,1)]],
    2: [[(-1,0), (1,0)], [(0,-1), (0,1)]],
    3: [[(-1,0), (0,-1)], [(0,-1), (1,0)], [(0,1), (1,0)], [(0, 1), (-1,0)]],
    4: [[(1,0), (0,-1), (0,1)], [(-1,0), (0,-1), (0,1)], [(-1,0), (1,0), (0,1)], [(-1,0), (1,0), (0,-1)]],
    5: [[(-1,0), (1,0), (0,-1), (0,1)]]
}

def backtracking(i, office, cnt):
    global answer

    if i == len(cctv):
        if cnt < answer:
            answer = cnt
        return
        
    ci, cj, cd = cctv[i]

    for direction in directions[cd]:       
        t = 0
        tmp = [copy.deepcopy(j) for j in office]

        for dx, dy in direction:
            q = deque([(ci, cj)])
            while q:
                x, y = q.popleft()
                nx, ny = dx+x, dy+y

                if 0 <= nx < n and 0 <= ny < m:
                    if tmp[nx][ny] != 6:
                        if tmp[nx][ny] == 0:
                            tmp[nx][ny] = -1
                            t += 1
                        q.append((nx, ny))
        
        backtracking(i+1, tmp, cnt-t)

answer = empty
backtracking(0, office, empty)
print(answer)