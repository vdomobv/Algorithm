import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(i, group):
    visited[i] = group

    for j in nodes[i]:
        if visited[j] == 0:
            result = dfs(j, -group)
            if not result:
                return False
        else:
            if visited[j] == group:
                return False
    return True

t = int(input())
for tc in range(t):
    v, e = map(int, input().split())
    
    nodes = [[] for _ in range(v+1)]
    for _ in range(e):
        f, t = map(int, input().split())
        nodes[f].append(t)
        nodes[t].append(f)

    visited = [0] * (v+1)
    for i in range(1, v+1):
        if visited[i] == 0:
            result = dfs(i, 1)
            if not result:
                break
    print("YES") if result else print("NO")