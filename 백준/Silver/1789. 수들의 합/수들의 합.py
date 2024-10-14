import sys
input = sys.stdin.readline

s = int(input())
num = 0
cnt = 0
while num <= s:
    cnt += 1
    num += cnt
print(cnt - 1)