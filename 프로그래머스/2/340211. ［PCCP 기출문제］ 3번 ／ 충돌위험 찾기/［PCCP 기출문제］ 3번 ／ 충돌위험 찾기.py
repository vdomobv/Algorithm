from collections import Counter

def solution(points, routes):
    answer = 0
    
    d = [(-1,0), (1,0), (0,-1), (0, 1)]
    
    p = {}
    for i in range(len(points)):
        p[i+1] = points[i]
    
    n = len(routes)
    history = []
    
    for route in routes:
        i, j = p[route[0]]
        tmp = [(i, j, 0)]
        time = 0
        
        for i in range(len(route)-1):
            s, e = p[route[i]]
            x, y = p[route[i+1]]

            while s != x:
                time += 1
                if s > x:
                    s -= 1
                elif s < x:
                    s += 1
                tmp.append((s, e, time))

            while e != y:
                time += 1
                if e > y:
                    e -= 1
                elif e < y:
                    e += 1
                tmp.append((s, e, time))  
        
        history.extend(tmp)
        
    counter = Counter(history)    
    for v in counter.values():
        if v >= 2:
            answer += 1
                
    return answer