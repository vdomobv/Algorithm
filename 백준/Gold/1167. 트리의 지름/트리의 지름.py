import sys
input = sys.stdin.readline
from collections import deque

v = int(input())
nodes = [[] for _ in range(v+1)]

for _ in range(v):
    q = deque(list(map(int, input().split())))
    x = q.popleft()

    while q:
        y = q.popleft()
        if y == -1:
            break
        
        w = q.popleft()
        nodes[x].append((y, w))
        nodes[y].append((x, w))
    
def bfs(i):
    visited = [-1] * (v+1)
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