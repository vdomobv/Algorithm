import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort(key=lambda x:-x)
b.sort()

answer = 0
for i in range(n):
    answer += b[i] * a[i]
print(answer)