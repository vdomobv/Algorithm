def find(park, n, m):
    for i in range(n):
        for j in range(m):
            if park[i][j] == 'S':
                return i, j

def solution(park, routes):
    d = {'N':(-1,0), 'S':(1,0), 'W': (0,-1), 'E':(0,1)}
    n, m = len(park), len(park[0])
    x, y = find(park, n, m)
    
    for route in routes:
        tx, ty = x, y
        way, num = route.split()
        dx, dy = d[way]
        num = int(num)
        
        for i in range(1, num+1):
            nx, ny = tx+dx*i, ty+dy*i
            if 0 > nx or nx >= n or 0 > ny or ny >= m or park[nx][ny] == "X":
                break
        else:
            x, y = x+num*dx, y+num*dy
            
    return [x, y]