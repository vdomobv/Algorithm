def solution(board):
    d = [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (1,1), (-1,1), (1,-1)]
    n = len(board)
    answer = n*n
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                answer -= 1
                for di, dj in d:
                    ni, nj = i+di, j+dj
                    if 0 <= ni < n and 0 <= nj < n and board[ni][nj] == 0:
                        board[ni][nj] = -1
                        answer -= 1
    
    return answer