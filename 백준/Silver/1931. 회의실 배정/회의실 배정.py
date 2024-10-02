from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
lst = [tuple(map(int, input().split())) for _ in range(n)]
lst.sort(key=lambda x: (x[1], x[0]))

b = 0
answer= 0
for s, e in lst:
    if b <= s:
        answer += 1
        b = e
print(answer)