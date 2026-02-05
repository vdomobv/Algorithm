import sys
input = sys.stdin.readline

lst = [input().strip() for _ in range(36)]
arr = [[0] * 6 for _ in range(6)]
# 나이트 움직임 앞으로 한칸 대각선 한칸

alphabet = ['A','B','C','D','E','F']
number = ['1','2','3','4','5','6']

result = 'Valid'

i, j = lst[0]
arr[alphabet.index(i)][number.index(j)] = 1


for x in range(1, 36):
    ni, nj = list(lst[x])

    if arr[alphabet.index(ni)][number.index(nj)] == 0 and ((abs(alphabet.index(i) - alphabet.index(ni)) == 2 and abs(number.index(j) - number.index(nj)) == 1) 
        or (abs(alphabet.index(i) - alphabet.index(ni)) == 1 and abs(number.index(j) - number.index(nj)) == 2)):
        arr[alphabet.index(ni)][number.index(nj)] = 1
        i, j = ni, nj
    else:
        result = 'Invalid'
        break

li, lj = lst[0]
if result == 'Valid' and ((abs(alphabet.index(i) - alphabet.index(li)) == 2 and abs(number.index(j) - number.index(lj)) == 1) 
    or (abs(alphabet.index(i) - alphabet.index(li)) == 1 and abs(number.index(j) - number.index(lj)) == 2)):
    result = 'Valid'
else:
    result = 'Invalid'
    
print(result)