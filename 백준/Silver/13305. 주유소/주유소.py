import sys
input = sys.stdin.readline

n = int(input())
roads = list(map(int, input().split()))
price = list(map(int, input().split()))

now = 0
result = 0

while now < n:
    for i in range(now, n):
        if price[i] >= price[now]:
            if i < n-1:
                continue
            else:
                result += price[now]*sum(roads[now:])
                now = i+1
                break
        elif i < n-1:
            result += price[now]*sum(roads[now:i])
            now = i
            break
        else:
            result += price[now]*sum(roads[now:])
            now = i+1
            break

print(result)