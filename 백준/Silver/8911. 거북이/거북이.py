import sys
input = sys.stdin.readline

t = int(input())
direction = [(0, -1), (1,0), (0, 1), (-1, 0)]
now_direction = 1

for _ in range(t):
    x_min, y_min, x_max, y_max = 0, 0, 0, 0
    lst = input().strip()
    i, j = 0, 0

    for l in lst:
        if l == 'F':
            ni, nj = direction[now_direction]
            i += ni
            j += nj
        elif l == 'B':
            ni, nj = direction[(now_direction+2)%4]
            i += ni
            j += nj
        elif l == 'L':
            now_direction = (now_direction - 1) % 4
        else:
            now_direction = (now_direction + 1) % 4

        x_min = min(x_min, i)
        x_max = max(x_max, i)
        y_min = min(y_min, j)
        y_max = max(y_max, j)

    result = (x_max-x_min) * (y_max - y_min)
    print(result)