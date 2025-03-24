from collections import deque

n, m = map(int, input().split())
ladder = [0] * 101
for _ in range(n):
    x, y = map(int, input().split())
    ladder[x] = y

snake = [0] * 101
for _ in range(m):
    x, y = map(int, input().split())
    snake[x] = y

q = deque([(1, 0)])
visited = [0] * 101
visited[1] = 1

answer = 0
while q:
    now, cnt = q.popleft()

    for i in range(1, 7):
        if now + i > 100:
            break

        if visited[now+i] == 0 or visited[now+i] > cnt+1:
            visited[now+i] = cnt + 1
            if ladder[now+i] != 0:
                u = ladder[now+i]
                q.append((u, cnt+1))
                if visited[u] > cnt + 1 and visited[u] == 0:
                    visited[u] = cnt + 1
            elif snake[now + i] != 0:
                d = snake[now+i]
                q.append((d, cnt+1))
                if visited[d] > cnt + 1 or visited[d] == 0:
                    visited[d] = cnt + 1
            else:
                q.append((now+i, cnt+1))

print(visited[100])