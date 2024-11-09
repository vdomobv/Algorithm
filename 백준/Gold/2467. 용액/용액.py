import sys
input = sys.stdin.readline

n = int(input())
liquids = list(map(int, input().split()))

answer = float("INF")
left = 0
right = 0

for i in range(n-1):
    now = liquids[i]
    s, e = i+1, n-1

    while s <= e:
        mid = (s+e) // 2
        tmp = now + liquids[mid]

        if abs(tmp) < answer:
            answer = abs(tmp)
            left = i
            right = mid

            if tmp == 0:
                break
        
        if tmp < 0:
            s = mid + 1
        else:
            e= mid - 1

print(liquids[left], liquids[right])