import sys
input = sys.stdin.readline

E, S, M = map(int, input().split())
a, b, c = 1, 1, 1
answer = 1

while (E,S,M) != (a, b, c):

    a, b, c = a+1, b+1, c+1

    if a > 15:
        a = 1
    if b > 28:
        b = 1
    if c > 19:
        c = 1
    answer += 1

print(answer)