def solution(diffs, times, limit):
    answer = 100000
    l, u = 1, 100000
    
    n = len(diffs)
    while l < u:
        m = (l+u) // 2
        time = 0
        
        for i in range(n):
            if diffs[i] <= m:
                time += times[i]
            else:
                time += (diffs[i] - m) * (times[i]+times[i-1])
                time += times[i]
                
            if time > limit:
                l = m+1
                break
        else:
            u = m
            if answer > m:
                answer = m
                
    
    return answer