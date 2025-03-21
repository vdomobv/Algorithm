def solution(storage, requests):
    
    n, m = len(storage), len(storage[0])
    answer = n*m
    arr = [[0] * (m+2)]
    for i in range(n):
        arr.append([0] + list(storage[i]) + [0])
    arr.append([0] * (m+2))
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    
    for request in requests:
        if len(request) == 1:
            q = [(0,0)]
            boxes = []
            visited = [[0] * (m+2) for _ in range(n+2)]
            visited[0][0] = 1
            
            while q:
                i, j = q.pop()
                for di, dj in directions:
                    ni, nj = di+i, dj+j
                    if 0 <= ni < n+2 and 0 <= nj < m+2 and visited[ni][nj] == 0:
                        if arr[ni][nj] == 0:
                            q.append((ni, nj))
                            visited[ni][nj] = 1
                        elif arr[ni][nj] == request:
                            boxes.append((ni, nj))
                            visited[ni][nj] = 1
            
            answer -= len(boxes)
            for x, y in boxes:
                arr[x][y] = 0
            
        else:
            for i in range(1, n+1):
                for j in range(1, m+1):
                    if arr[i][j] == request[0]:
                        arr[i][j] = 0
                        answer -= 1
            
    return answer