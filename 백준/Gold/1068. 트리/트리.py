import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
nodes = [[] for _ in range(n)]
a = int(input())

q = []
answer = 0

for i in range(n):
    if arr[i] != -1:
        nodes[arr[i]].append(i)
    else:
        q.append(i)

while q:
    i = q.pop()
    if i == a:
        continue

    if nodes[i] != []:
        if nodes[i] == [a]:
            answer += 1
            continue

        for j in nodes[i]:
            q.append(j)
    else:
        answer += 1

print(answer)