import sys
input = sys.stdin.readline


def sol(k): 
    global n, cnt
    
    if k == n:
        cnt += 1
        return

    for i in range(n):
        if not visited_c[i] and not visited_up[k+i] and not visited_down[(n-1)+k-i]:
            visited_c[i] = True
            visited_up[k+i] = True
            visited_down[(n-1)+k-i] = True
            sol(k+1)
            visited_c[i] = False
            visited_up[k+i] = False
            visited_down[(n-1)+k-i] = False


n = int(input())
board = [[0]*n for _ in range(n)]
visited_c = [False]*n
visited_up = [False]*(2*(n-1)+1)
visited_down = [False]*(2*(n-1)+1)

cnt = 0

sol(0)
print(cnt)