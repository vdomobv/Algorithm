import sys
input = sys.stdin.readline

n = int(input())

if n == 1:
    print(1)
else:
    arr = [0] * (n+1)
    arr[1] = 1
    for i in range(2, n+1):
        if i % 2:
            arr[i] = arr[i-1] * 2 - 1
        else:
            arr[i] = arr[i-1] * 2 + 1

    print(arr[n]%10007)
