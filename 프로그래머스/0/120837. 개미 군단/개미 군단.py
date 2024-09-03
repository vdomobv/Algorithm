def solution(hp):
    answer = 0
    
    for i in [5, 3, 1]:
        while hp // i > 0:
            answer += hp//i
            hp = hp%i
    
    return answer