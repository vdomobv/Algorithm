import sys
input = sys.stdin.readline

n = int(input())
ts = []
ps = []

for _ in range(n):
    t, p = map(int, input().split())
    ts.append(t)
    ps.append(p)

dp = [0] * n
answer = 0
def solution(x, v):
    global dp, answer

    if x+ts[x] > n:
        m = max(dp)
        if answer < m:
            answer = m
        return
    elif x+ts[x] == n:
        m = max(dp)
        m = max(m, v+ps[x])
        if answer < m:
            answer = m
        return
    
    if dp[x] < v+ps[x]:
        dp[x+ts[x]] = v + ps[x]
        
    
    for i in range(x+ts[x], n):
        solution(i, v+ps[x])

for i in range(n):
    if i + ts[i] <= n:
        solution(i, 0)

print(answer)