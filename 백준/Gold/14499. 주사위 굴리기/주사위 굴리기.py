import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
moves = list(map(int, input().split()))
direction = {1:(0, 1), 2:(0, -1), 3:(-1,0), 4:(1,0)}
dice = [0] * 6

def roll(x):
    global dice
    a, b, c, d, e, f = dice

    if x == 1:
        dice = [f, b, e, d, a, c]
    elif x == 2:
        dice = [e, b, f, d, c, a]
    elif x == 3:
        dice = [d, a, b, c, e, f]
    elif x == 4:
        dice = [b, c, d, a, e, f]
    
    print(dice[2])

for move in moves:
    mi, mj = direction[move]
    ni, nj = x+mi, y+mj
    
    if 0 <= ni < n and 0 <= nj < m:
        roll(move)
        if arr[ni][nj] == 0:
            arr[ni][nj] = dice[0]
        else:
            dice[0] = arr[ni][nj]
            arr[ni][nj] = 0
        x, y = ni, nj
