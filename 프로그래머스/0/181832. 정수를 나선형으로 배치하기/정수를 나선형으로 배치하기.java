class Solution {
    public int[][] solution(int n) {
        int [][] directions = {{0,1}, {1, 0}, {0,-1}, {-1, 0}};
        int[][] answer = new int[n][n];
        int x = 0;
        int y = 0;
        int d = 0;
        int nx;
        int ny;
        
        for (int i = 1; i<=n*n; i++){
            answer[x][y] = i;
            
            nx = x + directions[d][0];
            ny = y + directions[d][1];
            if (0 <= nx && nx < n && 0 <= ny && ny < n && answer[nx][ny]==0){
                x = nx;
                y = ny;
            } else {
                d = (d+1)%4;
                x = x + directions[d][0];
                y = y + directions[d][1];
            }
        }
        return answer;
    }
}