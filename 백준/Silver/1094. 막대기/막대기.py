import sys
import heapq
input = sys.stdin.readline

x = int(input())

lst = [64]

while sum(lst) > x:
    mi = heapq.heappop(lst) // 2
    heapq.heappush(lst, mi)

    if x > sum(lst):
        heapq.heappush(lst, mi)

print(len(lst))
