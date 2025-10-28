import sys
input = sys.stdin.readline

t = int(input())
answer = []

for i in [300, 60, 10]:
    answer.append(t//i)
    t %= i

if t > 0:
    print(-1)
else:
    print(*answer)