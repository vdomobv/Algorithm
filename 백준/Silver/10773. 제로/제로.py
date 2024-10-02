import sys
input = sys.stdin.readline

k = int(input())
stack = []

for _ in range(k):
    t = int(input())
    if t == 0:
        stack.pop()
    else:
        stack.append(t)
    
answer = sum(stack)
print(answer)    