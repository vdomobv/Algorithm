import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m, r = map(int, input().split())
items = list(map(int, input().split()))

arr = [[] for _ in range(n+1)]
answer = 0

for i in range(r):
    x, y, v = map(int, input().split())
    arr[x].append((y, v))
    arr[y].append((x, v))

for i in range(1, n+1):
    distance = [INF] * (n+1)

    q = []
    heapq.heappush(q, (0,i))
    distance[i] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in arr[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    
    tmp = 0
    for i, d in enumerate(distance):
        if d <= m:
            tmp += items[i-1]
    
    if tmp > answer :
        answer = tmp

print(answer)