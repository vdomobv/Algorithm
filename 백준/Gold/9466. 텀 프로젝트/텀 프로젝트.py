import sys
input = sys.stdin.readline
sys.setrecursionlimit(111111)
t = int(input())

def sol(i):
    global result

    visited[i] = 1
    team.append(i)
    j = lst[i]

    if visited[j]:
        if j in team:
            result += len(team[team.index(j):])
    else:
        sol(j)

for _ in range(t):
    n = int(input())
    lst = [0] + list(map(int, input().split()))

    visited = [0] * (n+1)
    result = 0
    for i in range(1, n+1):
        if not visited[i]:
            team = []
            sol(i)

    print(n-result)