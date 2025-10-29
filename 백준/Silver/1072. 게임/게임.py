import sys
from decimal import Decimal
input = sys.stdin.readline

x, y = map(int, input().split())
z = int(Decimal(y)/Decimal(x)*100)

mi, ma = 1, sys.maxsize
answer = -1

while mi <= ma:
    middle = (mi+ma) // 2

    if int(Decimal(y+middle) / Decimal(x+middle) * 100) > z:
        answer = middle
        ma = middle-1    
    else:
        mi = middle+1

print(answer)