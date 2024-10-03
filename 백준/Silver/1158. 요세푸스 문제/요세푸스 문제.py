import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [i for i in range(1, n+1)]

answer = []
cnt = 1

while len(arr):
    l = len(arr)    
    for i in range(l):
        if cnt % k == 0:
            answer.append(arr[i])
            arr = arr[i+1:] + arr[:i]
            cnt += 1
            break
        cnt += 1
4
print("<", end="")
for i in range(n):
    if i == n-1:
        print(answer[i], end="")
    else:
        print(answer[i], end=", ")
print(">")
