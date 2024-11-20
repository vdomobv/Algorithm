import sys
input = sys.stdin.readline
from collections import deque

t = int(input())

for _ in range(t):
  visited = [False for _ in range(10001)]
  a, b = map(int, input().split())
  
  q = deque()
  q.append([a, ''])
  visited[a] = True

  while q:
    n, funs = q.popleft()
	
    if n == b:
      print(funs)
      break

    d = (n * 2) % 10000
    if not visited[d]:
      visited[d] = True
      q.append([d, funs + 'D'])

    s = (n - 1) % 10000
    if not visited[s]:
      visited[s] = True
      q.append([s, funs + 'S'])

    l = n//1000 + (n % 1000) * 10
    if not visited[l]:
      visited[l] = True
      q.append([l, funs + 'L'])

    r = n//10 + (n%10) * 1000
    if not visited[r]:
      visited[r] = True
      q.append([r, funs + 'R'])