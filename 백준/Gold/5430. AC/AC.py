from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for tc in range(t):
    p = input().strip()
    n = int(input())
    lst = []
    i = input().replace("[","").replace("]", "").strip().split(",")
    if n > 0:
        lst = deque(list(map(int, i)))
    
    front = True
    error = False
    for c in p:
        if c == "R":
            front = not front
        elif len(lst) == 0:
            print("error")
            error = True
            break
        else:
            if front:
                lst.popleft()
            else:
                lst.pop()
    
    
    if not error:
        l = len(lst)
        print("[", end = "")
        if front:
            for j in range(l):
                if j == l - 1:
                    print(lst[j], end="")
                else:
                    print(lst[j], end=",")
        else:
            for j in range(l-1, -1, -1):
                if j == 0:
                    print(lst[j], end="")
                else:
                    print(lst[j], end=",")
                
        print("]")