import sys
input = sys.stdin.readline

k = int(input())
lst = input().split()

def backtracking(now, idx, visited):
    global min_ans, max_ans

    if idx == k:
        t = "".join(list(map(str, now)))
        if t > max_ans:
            max_ans = t
        if t < min_ans:
            min_ans = t
        return

    if lst[idx] == "<":
        for x in range(10):
            if now[-1] < x and visited[x] == 0:
                now.append(x)
                visited[x] = 1
                backtracking(now, idx+1, visited)
                now.pop()
                visited[x] = 0
    elif lst[idx] == ">":
        for x in range(10):
            if now[-1] > x and visited[x] == 0:
                now.append(x)
                visited[x] = 1
                backtracking(now, idx+1, visited)
                visited[x] = 0
                now.pop()

visited = [0] * 10
min_ans, max_ans = "9"*(k+1), "0000"

for i in range(10):
    visited[i] = 1
    backtracking([i], 0, visited)
    visited[i] = 0

print(max_ans)
print(min_ans)