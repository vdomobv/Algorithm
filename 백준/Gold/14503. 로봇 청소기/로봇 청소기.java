import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    static int n, m, r, c, d, cnt;
    static int[][] arr;
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stk = new StringTokenizer(br.readLine(), " ");

        n = Integer.parseInt(stk.nextToken());
        m = Integer.parseInt(stk.nextToken());
        arr = new int[n][m];

        stk = new StringTokenizer(br.readLine(), " ");
        r = Integer.parseInt(stk.nextToken());
        c = Integer.parseInt(stk.nextToken());
        d = Integer.parseInt(stk.nextToken());
        cnt = 1;

        for (int i = 0; i<n; i++){
            stk = new StringTokenizer(br.readLine(), " ");
            for (int j = 0; j<m; j++){
                arr[i][j] = Integer.parseInt(stk.nextToken());
            }
        }

        dfs(r, c, d);
        System.out.println(cnt);

    }

    public static void dfs(int x, int y, int direction) {
        arr[x][y] = 2;

        for (int i = 0; i<4; i++) {
            direction = (direction + 3) % 4;

            int nx = x + dx[direction];
            int ny = y + dy[direction];

            if (0 <= nx && nx < n && 0 <= ny && ny < m && arr[nx][ny] == 0){
                cnt++;
                dfs(nx, ny, direction);
                return;
            }
        }

        int back = (direction + 2) % 4;
        int bx = x + dx[back];
        int by = y + dy[back];

        if (0 <= bx && bx < n && 0 <= by && by < m && arr[bx][by] != 1){
            dfs(bx, by, direction);
        }
    }
}
