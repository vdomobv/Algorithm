import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))
answer = 0

for i in range(n):
    goal = arr[i]
    s, e = 0, n-1
    
    while s < e:
        tmp = arr[s] + arr[e]
        if tmp == goal:
            if s == i:
                s += 1
            elif e == i:
                e -= 1
            else:
                answer += 1
                break
        elif tmp > goal:
            e -= 1
        elif tmp < goal:
            s += 1

print(answer)