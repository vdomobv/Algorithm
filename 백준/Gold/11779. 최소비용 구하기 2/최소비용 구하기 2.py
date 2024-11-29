import sys
input = sys.stdin.readline
import heapq

n = int(input())
m = int(input())

bus = [[] for _ in range(n+1)]
for _ in range(m):
    f, t, w = map(int, input().split())
    heapq.heappush(bus[f], (t, w))

f, t = map(int, input().split())

INF = 1e9
visited = [INF] * (n+1)
visited[f] = 0

q = [(0, f, [f])]
answer = []

while q:
    w, i, route = heapq.heappop(q)

    if visited[i] < w:
        continue
    
    for j, v in bus[i]:
        tmp = w+v
        if visited[j] > tmp:
            visited[j] = tmp
            heapq.heappush(q, (tmp, j, route + [j]))
            if j == t:
                answer = route+[j]

print(visited[t])
print(len(answer))
print(" ".join(list(map(str, answer))))