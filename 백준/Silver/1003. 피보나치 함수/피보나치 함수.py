import sys
input = sys.stdin.readline

t = int(input())

arr = [int(input()) for _ in range(t)]

m = max(arr)

dp = [[0] * 2 for _ in range(m+1)]
dp[0][0] = 1
if m > 0:
    dp[1][1] = 1

def fibo(n):
    global dp
    if n == 0:
        dp[0][0] = 1
        return
    elif n == 1:
        dp[1][1] = 1
        return
    
    if n >= 2:
        i = 2
        while i <= n:
            dp[i][0] = dp[i-1][0] + dp[i-2][0]
            dp[i][1] = dp[i-1][1] + dp[i-2][1]
            i += 1

fibo(m)
for i in arr:
    print(" ".join(map(str, dp[i])))