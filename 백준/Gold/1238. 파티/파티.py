import sys
input = sys.stdin.readline
import heapq

n, m, x = map(int, input().split())
nodes = [[] for _ in range(n+1)]

for _ in range(m):
    s, e, t = map(int, input().split())
    nodes[s].append((e, t))

answer = [0] * (n+1)

q = []
for i in range(n+1):
    result = [1e9] * (n+1)

    heapq.heappush(q, (0, i))

    while q:
        v, w = heapq.heappop(q)

        for y, z in nodes[w]:
            new = v+z

            if new < result[y]:
                result[y] = new
                heapq.heappush(q, (new, y))
    answer[i] = result[x]

result = [1e9] * (n+1)
heapq.heappush(q, (0, x))

while q:
    v, w = heapq.heappop(q)

    for y, z in nodes[w]:
        new = v+z

        if new < result[y]:
            result[y] = new
            heapq.heappush(q, (new, y))
answer[x] = 0
result[x] = 0

a = 0
for i in range(1, n+1):
    answer[i] += result[i]
    if answer[i] > a:
        a = answer[i]

print(a)