def solution(keyinput, board):
    x, y = 0, 0
    d = {'left':(-1, 0), 'right':(1,0), 'up':(0, 1), 'down':(0,-1)}
    n, m = board
    n, m = (n-1)//2, (m-1)//2
    
    for key in keyinput:
        dx, dy = d[key]
        nx, ny = x+dx, y+dy
        if -n <= nx <= n and -m <= ny <= m:
            x, y = nx, ny
    
    return [x, y]