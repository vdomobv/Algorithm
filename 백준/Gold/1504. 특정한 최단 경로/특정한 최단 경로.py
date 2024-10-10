import sys
input = sys.stdin.readline
import heapq

n, e = map(int, input().split())
nodes = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    nodes[a].append((b, c))
    nodes[b].append((a, c))
v1, v2 = map(int, input().split())

q = []
def dijkstra(x, end):
    if x == end:
        return 0
    
    distance = [3e9] * (n+1)
    heapq.heappush(q, (0, x))

    while q:
        v, i = heapq.heappop(q)
        for j, vv in nodes[i]:
            new = v + vv

            if new < distance[j]:
                distance[j] = new
                heapq.heappush(q, (new, j))

    return distance[end] if distance[end] != 3e9 else -1

answer = -1
aa = dijkstra(1, v1)
bb = dijkstra(v1, v2)
cc = dijkstra(v2, n)
if aa != -1 and bb != -1 and cc != -1:
    answer = aa+bb+cc

a = dijkstra(1, v2)
b = dijkstra(v2, v1)
c = dijkstra(v1, n)
if a != -1 and b != -1 and c != -1 and answer > a+b+c:
    answer = a+b+c

print(answer)