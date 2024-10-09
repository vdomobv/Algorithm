import sys
input = sys.stdin.readline

n = int(input())
stairs = [int(input()) for _ in range(n)]
score = [0] * n
if n == 1:
    print(stairs[0])
elif n == 2:
    print(stairs[0] + stairs[1])
else:
    score[0] = stairs[0]
    score[1] = stairs[0] + stairs[1]
    score[2] = max(stairs[0]+stairs[2], stairs[1]+stairs[2])

    for i in range(3, n):
        score[i] = stairs[i]+max(stairs[i-1]+score[i-3], score[i-2])
    print(score[n-1])