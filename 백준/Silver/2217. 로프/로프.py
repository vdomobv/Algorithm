import sys
input = sys.stdin.readline

n = int(input())
weights = [int(input()) for _ in range(n)]

weights.sort(reverse=True)
answer = 0
t = 0
for i in range(n):
    t += weights[i]
    if weights[i] <= t/(i+1):
        if answer < weights[i]*(i+1):
            answer = weights[i]*(i+1)

print(answer)