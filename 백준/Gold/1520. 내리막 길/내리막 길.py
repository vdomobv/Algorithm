import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]
directions = [(-1,0), (1,0), (0,-1), (0,1)]
answer = 0

def solution(i, j):
    global visited

    if (i, j) == (n-1, m-1):
        return 1
    
    if visited[i][j] == -1:
        visited[i][j] = 0
        
        for di, dj in directions:
            ni, nj = i+di, j+dj
            if 0 <= ni < n and 0 <= nj < m and arr[i][j] > arr[ni][nj]:
                visited[i][j] += solution(ni, nj)
    return visited[i][j]

print(solution(0, 0))