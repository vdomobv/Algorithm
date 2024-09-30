def solution(keymap, targets):
    answer = []
    d = {}
    
    for key in keymap:
        for k in range(len(key)):
            if d.get(key[k]):
                if d[key[k]] > k+1:
                    d[key[k]] = k+1
            else:
                d[key[k]] = k+1
                    
    for target in targets:
        tmp = 0
        for t in target:
            if d.get(t):
                tmp += d[t]
            else:
                tmp = -1
                break
        answer.append(tmp)
        
    return answer