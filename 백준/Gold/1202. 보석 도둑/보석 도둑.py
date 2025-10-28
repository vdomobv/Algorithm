import sys
input = sys.stdin.readline

import heapq

n, k = map(int, input().split())
jewel = [list(map(int, input().split())) for _ in range(n)]
bag = [int(input()) for _ in range(k)]
jewel.sort()
bag.sort()

answer = 0
tmp = []

for b in bag:
    while jewel and jewel[0][0] <= b:
        heapq.heappush(tmp, -jewel[0][1])
        heapq.heappop(jewel)
    if tmp:
        answer -= heapq.heappop(tmp)

print(answer)