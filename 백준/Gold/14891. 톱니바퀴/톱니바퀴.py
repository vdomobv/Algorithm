import sys
input = sys.stdin.readline

wheel = [list(input().strip()) for _ in range(4)]

k = int(input())

def check(now, i, directions):
    if i == 2:
        if now < 3 and wheel[now][i] != wheel[now+1][6]:
            directions[now+1] = -directions[now]
            directions = check(now+1, i, directions)
    elif i == 6:
        if now > 0 and wheel[now][i] != wheel[now-1][2]:
            directions[now-1] = -directions[now]
            directions = check(now-1, i, directions)
    return directions

def move(before, direction):
    result = before
    if direction == 1:
        result = [before[7]] + before[:7]
    elif direction == -1:
        result = before[1:] + [before[0]]
    return result

        
for _ in range(k):
    n, d = map(int, input().split())
    n -= 1

    directions = [0] * 4
    directions[n] = d
    directions = check(n, 2, directions)
    directions = check(n, 6, directions)

    for i in range(4):
        wheel[i] = move(wheel[i], directions[i])

answer = 0
for i in range(4):
    if wheel[i][0] == "1":
        answer += 2**i
print(answer)