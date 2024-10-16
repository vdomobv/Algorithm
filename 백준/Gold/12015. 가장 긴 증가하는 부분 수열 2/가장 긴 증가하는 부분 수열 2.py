import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
lst = [arr[0]]

def solution(i):
    s, e = 0, len(lst)-1

    while s <= e:
        m = (s+e)//2

        if lst[m] == i:
            return m
        elif lst[m] < i:
            s = m+1
        else:
            e = m-1
    
    return s

for a in arr:
    if a > lst[-1]:
        lst.append(a)
    else:
        idx = solution(a)
        lst[idx] = a

print(len(lst))