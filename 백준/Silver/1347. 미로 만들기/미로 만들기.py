import sys
input = sys.stdin.readline

n = int(input())
note = input().strip()

# 모든 행과 열에는 적어도 하나의 이동할 수 있는 칸이 있음
# 미로의 모든 행과 열에서 이동할 수 있는 칸 다 감
# 처음에는 남쪽을 보고 있음
direction = [(0,1), (1,0), (0,-1), (-1,0)]
now_d = 1

maze = [[0]*101 for _ in range(101)]
x, y = 50, 50
maze[x][y] = 1
x_min, y_min, x_max, y_max = 50, 50, 50, 50

for n in note:
    if n == 'F':
        i, j = direction[now_d]
        x += i
        y += j
        maze[x][y] = 1
        x_min = min(x_min, x)
        x_max = max(x_max, x)
        y_min = min(y_min, y)
        y_max = max(y_max, y)
    elif n == 'L':
        now_d = (now_d - 1) % 4
    else:
        now_d = (now_d + 1) % 4

for a in range(x_min, x_max+1):
    for b in range(y_min, y_max+1):
        if maze[a][b] == 1:
            print(".", end="")
        else:
            print("#", end="")
    print()