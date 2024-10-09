import sys
input = sys.stdin.readline

n, c = map(int, input().split())
arr = sorted([int(input()) for _ in range(n)])

answer = 0
l, u = 1, arr[n-1]-arr[0]
while l <= u:
    mid = (l+u)//2
    now = arr[0]
    cnt = 1

    for i in range(1, n):
        if arr[i] >= now+mid:
            cnt += 1
            now = arr[i]
    
    if cnt >= c:
        l = mid + 1
        answer = mid
    else:
        u = mid - 1

print(answer)