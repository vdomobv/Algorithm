import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [0] * n
answer = sys.maxsize

def backtracking(now, start, value, cnt):
    global answer

    if cnt == n:
        if arr[now][start]:
            value += arr[now][start]
            if value < answer:
                answer = value
        return
    
    if value > answer:
        return
    
    for i in range(n):
        if visited[i] == 0 and arr[now][i]:
            visited[i] = 1
            backtracking(i, start, value+arr[now][i], cnt+1)
            visited[i] = 0

for i in range(n):
    visited[i] = 1
    backtracking(i, i, 0, 1)
    visited[i] = 0

print(answer)