def solution(players, m, k):
    answer = 0
    
    lst = [0] * 24
    for i in range(24):
        player = players[i]
        server = lst[i]
        
        if player < m:
            continue
        else:
            needed_server = player // m
            plus = needed_server - server
            if plus > 0:                
                answer += plus
                for j in range(i, i+k):
                    if j < 24:
                        lst[j] += plus
        
    return answer