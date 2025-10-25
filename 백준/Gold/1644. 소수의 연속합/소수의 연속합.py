import sys
input = sys.stdin.readline

n = int(input())
if n == 1:
    print(0)
else:
    arr = [True for _ in range(n+1)]

    for i in range(2, int(n**(1/2))+1):
        if arr[i] == True:
            j = 2
            while i * j <= n:
                arr[i*j] = False
                j += 1

    lst = [i for i in range(2, n+1) if arr[i] == True]
    left, right, tmp, cnt = 0, 0, lst[0], 0

    while left <= right:
        if tmp > n:
            tmp -= lst[left]
            left += 1
        else:
            if tmp == n:
                cnt += 1
            right += 1
            if right == len(lst):
                break
            tmp += lst[right]

    print(cnt)