import sys
input = sys.stdin.readline

n = int(input())

lst = [0, 1, 2]

if n > 2:
    for i in range(3, n+1):
        lst.append((lst[i-1]+lst[i-2]) % 15746)
print(lst[n])