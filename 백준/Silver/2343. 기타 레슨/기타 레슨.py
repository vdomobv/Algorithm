n, m = map(int, input().split())
times = list(map(int, input().split()))

s, e = max(times), sum(times)

while s <= e:
    mid = (s+e) // 2
    cnt, sum = 1, 0

    for time in times:
        if sum + time > mid:
            cnt += 1
            sum = 0
        sum += time
    
    if cnt > m:
        s = mid + 1
    else:
        e = mid - 1

print(s)