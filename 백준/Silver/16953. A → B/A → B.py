import sys
input = sys.stdin.readline
from collections import deque

a, b = map(int, input().split())
q = deque([(a, 1)])

answer = -1
while q:
    x, cnt = q.popleft()

    if x == b:
        answer = cnt
        break
    elif x > b:
        continue

    for i in range(2):
        if i == 1:
            nx = int(str(x)+"1")
            q.append((nx, cnt+1))
        else:
            nx = x*2
            q.append((nx, cnt+1))

print(answer)