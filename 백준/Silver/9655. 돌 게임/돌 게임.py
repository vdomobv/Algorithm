import sys
input = sys.stdin.readline

N = int(input())
now = True

if N % 2 == 1 or N % 2 == 3 or N % 6 == 1 or N % 6 == 3 or N % 4 == 1 or N % 4 == 3:
    print("SK")
else:
    print("CY")
