import sys
input = sys.stdin.readline

n = int(input())

if n == 1:
    print(int(input()))
else:
    zero_yn = 0
    positive = []
    negative = []

    for _ in range(n):
        a = int(input())
        if a > 0:
            positive.append(a)
        elif a < 0:
            negative.append(a)
        else:
            zero_yn = 1
    
    positive.sort()
    negative.sort(reverse=True)
    answer = 0

    while positive and len(positive) >= 2:
        a = positive.pop()
        b = positive.pop()
        if a == 1 or b == 1:
            answer += (a+b)
        else:
            answer += (a*b)
    
    while negative and len(negative) >= 2:
        answer += negative.pop() * negative.pop()
    
    if negative and zero_yn:
        negative.pop()
    
    if negative:
        answer += sum(negative)
    
    if positive:
        answer += sum(positive)
    
    print(answer)