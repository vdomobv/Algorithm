def solution(routes):
    answer = []
    routes = sorted(routes, key = lambda x : x[1])
    for s, e in routes:
        if len(answer) == 0:
            answer.append([s, e])
        else:
            a, b = answer.pop()
            if s <= b:
                answer.append([s, b])
            else:
                answer.append([a, b])
                answer.append([s, e])
    return len(answer)