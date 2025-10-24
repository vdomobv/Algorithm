import sys
import math
input = sys.stdin.readline
sys.setrecursionlimit(10)

N = int(input())
answer = 0
a = round(math.sqrt(N))
dp = [0] * (N+1)
dp[0], dp[1] = 0, 1
for i in range(1, N+1):
    if int(math.sqrt(i)) == i:
        dp[i] = 1
    else:
        dp[i] = dp[i-1] + 1
        for j in range(2, int(math.sqrt(i))+1):
            dp[i] = min(dp[i], dp[i-(j**2)]+1)

print(dp[N])
