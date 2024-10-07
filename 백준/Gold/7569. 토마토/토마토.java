import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.*;

public class Main {
    static int m, n, h, cnt;
    static int[][][] tomato, visited;
    static int[][] directions = {{0, -1, 0}, {0, 1, 0}, {0, 0, -1}, {0, 0, 1}, {-1, 0, 0}, {1, 0, 0}};

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stk = new StringTokenizer(br.readLine());

        m = Integer.parseInt(stk.nextToken());
        n = Integer.parseInt(stk.nextToken());
        h = Integer.parseInt(stk.nextToken());

        visited = new int[h][n][m];

        Queue<int[]> rotten = new LinkedList<>();
        cnt = 0;
        tomato = new int[h][n][m];
        for (int i = 0; i<h; i++){
            for (int j = 0; j<n; j++){
                stk = new StringTokenizer(br.readLine());
                for (int k = 0; k<m; k++){
                    tomato[i][j][k] = Integer.parseInt(stk.nextToken());
                    if (tomato[i][j][k] == 1){
                        int[] tmp = {i, j, k};
                        visited[i][j][k] = 1;
                        rotten.add(tmp);
                    } else if (tomato[i][j][k] == 0) {
                        cnt ++;
                    }
                }
            }
        }

        while (!rotten.isEmpty()) {
            int[] r = rotten.remove();
            int x = r[0];
            int y = r[1];
            int z = r[2];

            for (int[] direction: directions){
                int nx = direction[0] + x;
                int ny = direction[1] + y;
                int nz = direction[2] + z;

                if (0 <= nx && nx < h && 0 <= ny && ny < n && 0 <= nz && nz < m && visited[nx][ny][nz] == 0 && tomato[nx][ny][nz] == 0) {
                    visited[nx][ny][nz] = visited[x][y][z] + 1;
                    int[] tmp = {nx, ny, nz};
                    rotten.add(tmp);
                    cnt--;
                }
            }
        }

        if (cnt > 0) {
            System.out.println(-1);
        } else {
            int answer = 0;
            for (int i = 0; i < h; i++){
                for (int j=0; j < n; j++){
                    for (int k=0; k<m; k++){
                        if (visited[i][j][k] > answer) {
                            answer = visited[i][j][k];
                        }
                    }
                }
            }
            System.out.println(answer-1);
        }
    }
}