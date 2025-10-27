import sys
input = sys.stdin.readline

n, k = map(int,input().split())

def sol(n, k):
    dp = [True] * (n+1)

    cnt = 0
    for i in range(2, n+1):
        if dp[i]:
            
            j = 1
            while i*j < n+1:
                if dp[i*j]:
                    dp[i*j] = False
                    cnt += 1

                    if cnt == k:
                        return i*j
                j += 1

print(sol(n, k))