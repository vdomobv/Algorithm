import sys
input = sys.stdin.readline

r, c, time = map(int, input().split())
arr = []
purifier = []

for i in range(r):
    arr.append(list(map(int, input().split())))
    for j in range(c):
        if arr[i][j] == -1:
            purifier.append((i, j))

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
opposite = [(0, 1), (-1, 0), (0, -1),  (1, 0)]

def area(x, y):
    return 0 <= x < r and 0 <= y < c

def diffusion(arr):
    tmp = [[[0,0] for _ in range(c)] for _ in range(r)]
    
    for i in range(r):
        for j in range(c):
            if arr[i][j] != 0 and arr[i][j] != -1:
                cnt = 0
                v = arr[i][j] // 5
                for dx, dy in directions:
                    ni, nj = dx+i, dy+j
                    if area(ni, nj):
                        if arr[ni][nj] != -1:
                            tmp[ni][nj][1] += v
                            cnt += 1

                tmp[i][j][0] = v*cnt
    
    return tmp

def change(tmp):
    global arr
    for i in range(r):
        for j in range(c):
            if arr[i][j] == -1:
                continue

            if arr[i][j] - tmp[i][j][0] + tmp[i][j][1] < 0:
                arr[i][j] = 0
            else:
                arr[i][j] = arr[i][j] - tmp[i][j][0] + tmp[i][j][1] 

def purify():
    global arr

    for x in range(2):
        i, j = purifier[x]
        tmp = 0
        if x == 0:
            for di, dj in opposite:
                while True:
                    ni, nj = di+i, dj+j
                    if area(ni, nj):
                        t = arr[ni][nj]
                        if arr[ni][nj] == -1:
                            break
                        arr[ni][nj] = tmp
                        tmp = t
                        i, j = ni, nj
                    else:
                        break
        else:
            for di, dj in directions:
                while True:
                    ni, nj = di+i, dj+j
                    if area(ni, nj):
                        t = arr[ni][nj]
                        if arr[ni][nj] == -1:
                            break
                        arr[ni][nj] = tmp
                        tmp = t
                        i, j = ni, nj
                    else:
                        break

for _ in range(time):
    tmp = diffusion(arr)
    change(tmp)
    purify()


answer = 2
for i in arr:
    answer += sum(i)
print(answer)