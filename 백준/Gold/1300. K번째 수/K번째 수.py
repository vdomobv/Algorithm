import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

s, e = 1, k
answer = 0

while s <= e:
    m = (s+e)//2

    cnt = 0
    for i in range(1, n+1):
        cnt += min(m//i, n)
    
    if cnt >= k:
        answer = m
        e = m-1        
    else:
        s = m+1

print(answer)