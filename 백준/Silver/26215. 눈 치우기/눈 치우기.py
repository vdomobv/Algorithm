import sys
input = sys.stdin.readline
from collections import deque

n = int(input().strip())
snow = deque(sorted(list(map(int, input().split()))))
answer = 0

while snow:
    if answer > 1440:
        answer -= 1
        break

    if len(snow) >= 2:
        answer += 1
        a = snow.pop()
        b = snow.pop()

        a -= 1
        b -= 1
        if a != 0:
            snow.append(a)
        if b != 0:
            snow.append(b)

        snow = deque(sorted(snow))
    else:
        a = snow.pop()
        answer += a
        if answer > 1440:
            answer = -1
            break

print(answer)