import sys
input = sys.stdin.readline

t = int(input())
def sol(m, n, x, y):
    while x <= m*n:
        if (x-y) % n == 0:
            return x
        x += m
    return -1

for _ in range(t):
    m,n,x,y = map(int, input().split())
    print(sol(m, n, x, y))