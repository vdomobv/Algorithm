import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[0] * n for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = c if graph[a-1][b-1] == 0 else min(c, graph[a-1][b-1])

visited = [[0] * n for _  in range(n)]

def sol(start):
    lst = deque([start])
    check = [0] * n
    check[start] = -1

    while lst:
        x = lst.popleft()
        
        for i in range(n):
            if graph[x][i] != 0 and (check[i] == 0 or visited[start][i] > visited[start][x] + graph[x][i]):
                check[i] = 1
                lst.append(i)
                visited[start][i] = visited[start][x] + graph[x][i]

for i in range(n):
    sol(i)

for i in visited:
    print(*i)    
            