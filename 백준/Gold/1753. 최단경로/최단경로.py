import sys
import heapq
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input())

INF = int(1e9)
node = [[] * (v+1) for _ in range(v+1)]
distance = [INF] * (v+1)

for _ in range(e):
    x, y, w = map(int, input().split())
    node[x].append((y, w))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        weight, n = heapq.heappop(q)

        if distance[n] < weight:
            continue
        
        for i in node[n]:
            new = weight + i[1]

            if new < distance[i[0]]:
                distance[i[0]] = new
                heapq.heappush(q, (new, i[0]))

dijkstra(k)
for i in range(1, v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
    