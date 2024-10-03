import sys
input = sys.stdin.readline

k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]

l, u = 1, 2**31-1
answer = 0
while l <= u:
    m = (l+u)//2
    
    tmp = 0
    for i in arr:
        if i >= m:
            tmp += i//m

    if tmp >= n:
        if answer < m:
            answer = m
        l = m+1
    else:
        u = m-1 

print(answer)