from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
lst = [1, 1, 1, 2, 2, 3, 4]
for tc in range(t):
    n = int(input())
    
    if n < len(lst):
        print(lst[n-1])
    else:
        while len(lst) < n:
            l = len(lst)
            lst.append(lst[l-1]+lst[l-5])
        print(lst[len(lst)-1])