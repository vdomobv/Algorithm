import sys
input = sys.stdin.readline
import heapq

directions = [(-1,0), (1,0), (0,-1), (0,1)]
cnt = 0
inf = int(1e9)

while True:
	cnt += 1
	n = int(input())
	if n == 0:
		break

	arr = [list(map(int, input().split())) for _ in range(n)]
	dist = [[inf for _ in range(n)] for _ in range(n)]
	dist[0][0] = arr[0][0]

	q = []
	heapq.heappush(q, (arr[0][0], 0, 0))

	while q:
		v, x, y = heapq.heappop(q)
		if dist[x][y] < v:
			continue

		for dx, dy in directions:
			nx, ny = dx+x, dy+y

			if 0 <= nx < n and 0 <= ny < n:
				tmp = v + arr[nx][ny]
				if tmp < dist[nx][ny]:
					dist[nx][ny] = tmp
					heapq.heappush(q, (tmp, nx, ny))

	print('Problem {}: {}'.format(cnt, dist[n-1][n-1]))