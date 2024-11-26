import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cheeze = [list(input().split()) for _ in range(n)]
time = 0

directions = [(-1, 0), (1,0), (0,-1), (0,1)]
q = [(0,0)]
edge = []
prev = 0

while q:
    check = False
    for i in cheeze:
        if "1" in i:
            check = True
            break
    if check:
        prev = 0
        for i in cheeze:
            prev += i.count("1") 
    
    while q:
        x, y = q.pop()
        cheeze[x][y] = 0

        for dx, dy in directions:
            nx, ny = dx+x, dy+y
            if 0 <= nx < n and 0 <= ny < m:
                if cheeze[nx][ny] == "0":
                    q.append((nx, ny))
                    cheeze[nx][ny] = 0
                elif cheeze[nx][ny] == "1":
                    edge.append((nx, ny))
        
    for i, j in edge:
        cheeze[i][j] = 0
    
    q, edge = edge, []
    time += 1

print(time-1)
print(prev)