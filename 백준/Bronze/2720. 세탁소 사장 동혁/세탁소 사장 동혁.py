import sys
input = sys.stdin.readline

t = int(input())

for tc in range(t):
    arr = [0] * 4
    c = int(input())
    coin = [25, 10, 5, 1]

    for i in range(4):
        arr[i] = c//coin[i]
        c %= coin[i]

    print(" ".join(list(map(str, arr))))