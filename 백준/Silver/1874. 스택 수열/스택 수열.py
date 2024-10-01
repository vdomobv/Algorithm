import sys
input = sys.stdin.readline
n = int(input())
lst = [int(input()) for _ in range(n)]
stack = []
tmp = []

answer = []
j = 0
for i in range(1, n+1):
    while stack and lst[j] == stack[-1]:
        tmp.append(stack.pop())
        j += 1
        answer.append("-")
    
    stack.append(i)
    answer.append("+")

while stack:
    tmp.append(stack.pop())
    answer.append("-")

if tmp == lst:
    for i in answer:
        print(i)
else:
    print("NO")