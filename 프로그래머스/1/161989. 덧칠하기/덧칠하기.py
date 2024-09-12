from collections import deque
def solution(n, m, section):
    answer = 0
    
    section = deque(section)
    while section:
        q = section.popleft()
        answer += 1
        while section and section[0] < q+m:
            section.popleft()
    
    return answer