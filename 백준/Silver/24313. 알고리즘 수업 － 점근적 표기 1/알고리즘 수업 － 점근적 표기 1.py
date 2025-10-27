import sys
input = sys.stdin.readline

a, b = map(int, input().split())
c = int(input())
x = int(input())

if c >= a and a*x+b <= c*x:
    print(1)
else:
    print(0)