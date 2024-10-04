import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
parents = [0] * (n+1)
nodes = [[] for _ in range(n+1)]

for _ in range(n-1):
    x, y = map(int, input().split())
    nodes[x].append(y)
    nodes[y].append(x)

q= deque([1])

while q:
    i = q.popleft()

    for ii in nodes[i]:
        if parents[ii] == 0:
            parents[ii] = i
            q.append(ii)

for i in range(2, n+1):
    print(parents[i])