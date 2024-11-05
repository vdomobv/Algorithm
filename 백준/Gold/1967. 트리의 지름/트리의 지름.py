import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
nodes = [[] for _ in range(n+1)]
leaf = [True] * (n+1)
for _ in range(n-1):
    p, c, w = map(int, input().split())
    nodes[c].append((p, w))
    nodes[p].append((c, w))

def bfs(i):
    visited = [-1] * (n + 1)
    visited[i] = 0
    q = deque()
    q.append(i)
    
    while q:
        cur = q.popleft()
        for next, next_d in nodes[cur]:
            if visited[next] == -1:
                q.append(next)
                visited[next] = visited[cur] + next_d
    m = max(visited)
    return [visited.index(m), m]

print(bfs(bfs(1)[0])[1])