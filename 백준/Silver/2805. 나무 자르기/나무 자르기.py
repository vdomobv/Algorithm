from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

u, l = max(trees), 1
answer = 0

while l < u:
    mid = (u+l) // 2
    
    s = 0
    for i in range(n):
        if trees[i] - mid > 0:
            s += (trees[i] - mid)
        if s >= m:
            break
    
    if s >= m:
        if answer < mid:
            answer = mid
        l = mid+1
    else:
        u = mid

print(answer)