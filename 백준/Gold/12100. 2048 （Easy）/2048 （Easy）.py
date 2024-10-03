import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

answer = 0
direction = ["L", "R", "U", "D"]

def backtracking(arr, cnt):
    global answer
    if cnt == 5:
        for ar in arr:
            m = max(ar)
            if answer < max(ar):
                answer = m
        return

    for d in direction:
        new_arr = []
        for i in arr:
            new_arr.append(deque(i))

        if d == "L":            
            for i in range(n):
                tmp = deque()
                a = new_arr[i]
                while len(tmp) < n:
                    if a:
                        t = a.popleft()
                        if t == 0:
                            continue
                        elif tmp and t == tmp[-1]:
                            tmp.pop()
                            tmp.append(t*2)
                            while a and a[0] == 0:
                                a.popleft()
                            if a:
                                tmp.append(a.popleft())
                        else:
                            tmp.append(t)
                    else:
                        tmp.append(0)
                new_arr[i] = tmp
        elif d == "R":            
            for i in range(n):
                tmp = deque()
                a = new_arr[i]
                while len(tmp) < n:
                    if a:
                        t = a.pop()
                        if t == 0:
                            continue
                        elif tmp and t == tmp[0]:
                            tmp.popleft()
                            tmp.appendleft(t*2)
                            while a and a[-1] == 0:
                                a.pop()
                            if a:
                                tmp.appendleft(a.pop())
                        else:
                            tmp.appendleft(t)
                    else:
                        tmp.appendleft(0)
                new_arr[i] = tmp
        elif d == "U":
            for j in range(n):
                tmp = deque()
                a = deque()

                for i in range(n):
                    a.append(new_arr[i][j])
                                
                while len(tmp) < n:
                    if a:
                        t = a.popleft()
                        if t == 0:
                            continue
                        elif tmp and t == tmp[-1]:
                            tmp.pop()
                            tmp.append(t*2)
                            while a and a[0]== 0:
                                a.popleft()
                            if a:
                                tmp.append(a.popleft())
                        else:
                            tmp.append(t)
                    else:
                        tmp.append(0)
                
                for i in range(n):
                    new_arr[i][j] = tmp[i]
        elif d == "D":
            for j in range(n):
                tmp = deque()
                a = deque()
                
                for i in range(n):
                    a.append(new_arr[i][j])
                                
                while len(tmp) < n:
                    if a:
                        t = a.pop()
                        if t == 0:
                            continue
                        elif tmp and t == tmp[0]:
                            tmp.popleft()
                            tmp.appendleft(t*2)
                            while a and a[-1]== 0:
                                a.pop()
                            if a:
                                tmp.appendleft(a.pop())
                        else:
                            tmp.appendleft(t)
                    else:
                        tmp.appendleft(0)
                
                for i in range(n):
                    new_arr[i][j] = tmp[i]
        backtracking(new_arr, cnt + 1)

backtracking(board, 0)
print(answer)