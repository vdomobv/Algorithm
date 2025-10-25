import sys
input = sys.stdin.readline

n = input().strip()
if '0' not in n:
    print(-1)
else:
    answer = -1

    tmp = 0
    for i in n:
        tmp += int(i)

    if tmp % 3 == 0:
        lst = sorted(n, reverse=True)
        answer = "".join(lst)
            
    print(answer)