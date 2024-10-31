import sys
input = sys.stdin.readline

n = int(input())
liquids = sorted(list(map(int, input().split())))

answer = []
tmp = 2e9+1        

for i in range(n):
    l, u = i+1, n-1

    while l <= u:
        m = (l+u)//2

        if abs(liquids[i] + liquids[m]) < tmp:
            tmp = abs(liquids[i] + liquids[m])
            answer = [liquids[i], liquids[m]]
        
        if liquids[i] < 0:
            if liquids[m] > 0:
                if liquids[i] + liquids[m] > 0:
                    u = m-1
                else:
                    l = m+1
            else:
                l = m+1
        else:
            u = m-1
            
print(answer[0], answer[1])