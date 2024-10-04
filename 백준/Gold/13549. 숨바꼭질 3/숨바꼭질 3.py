import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
l = 100001
time = [0] * l

def bfs(x):
    q = deque()
    if x == 0:
        q.append(1)
    else:
        q.append(x)

    while q:
        x = q.popleft()
        if k == x:
            return time[x]
    
        for nx in (x-1, x+1, x*2):
            if 0 <= nx < l and time[nx] == 0:
                if nx == 2*x:
                    time[nx] = time[x]
                    q.appendleft(nx)
                else:
                    time[nx] = time[x] + 1
                    q.append(nx)

if n ==0:
    if n == k:
        print(0)
    else:
        print(bfs(n) + 1)
else:
    print(bfs(n))
