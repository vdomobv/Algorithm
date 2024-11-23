import sys
input = sys.stdin.readline

n = int(input().strip())
p = [0]
p.extend(list(map(int, input().strip().split())))

lst = [0] * (n+1)

for i in range(1, n+1):
    for j in range(1, i+1):
        lst[i] = max(lst[i], lst[i-j] + p[j])

print(lst[n])