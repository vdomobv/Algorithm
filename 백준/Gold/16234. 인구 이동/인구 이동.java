import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int n, l, r, cnt, before;
    static int[][] arr, visited;
    static int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stk = new StringTokenizer(br.readLine());

        n = Integer.parseInt(stk.nextToken());
        l = Integer.parseInt(stk.nextToken());
        r = Integer.parseInt(stk.nextToken());

        arr = new int[n][n];
        for (int i=0; i<n; i++){
            stk = new StringTokenizer(br.readLine());
            for (int j=0; j<n; j++){
                arr[i][j] = Integer.parseInt(stk.nextToken());
            }
        }

        Map<Integer, ArrayList<Integer[]>> map = new HashMap<>();
        Stack<Integer[]> stack = new Stack<>();

        int answer = -1;
        before = n*n;

        while (before != map.size()) {
            for (Integer key: map.keySet()){
                int sum = 0;
                for (Integer[] xy: map.get(key)) {
                    sum += arr[xy[0]][xy[1]];
                }
                int average = sum / map.get(key).size();

                for (Integer[] xy: map.get(key)) {
                    arr[xy[0]][xy[1]] = average;
                }
            }

            answer++;

            cnt = 0;
            map = new HashMap<>();
            visited = new int[n][n];

            for (int i = 0; i<n; i++){
                for (int j = 0; j<n; j++){
                    if (visited[i][j] == 0){
                        cnt++;

                        Integer[] t = {i, j};
                        stack.add(t);

                        ArrayList<Integer[]> lst = new ArrayList<>();
                        lst.add(t);

                        map.put(cnt, lst);
                        visited[i][j] = cnt;

                        while (!stack.isEmpty()){
                            Integer[] now = stack.pop();

                            for (int[] d: directions){
                                int x = now[0];
                                int y = now[1];

                                int nx = d[0] + x;
                                int ny = d[1] + y;

                                if (check(x, y, nx, ny, visited)){
                                    visited[nx][ny] = cnt;

                                    Integer[] xy = {nx, ny};
                                    stack.add(xy);

                                    ArrayList<Integer[]> v = map.get(cnt);
                                    v.add(xy);

                                    map.put(cnt, v);
                                }
                            }
                        }
                    }

                }
            }

            if (map.size() == before){
                break;
            }
        }
        System.out.println(answer);
    }

    public static boolean check(int x, int y, int nx, int ny, int[][] visited) {
        if (0 <= nx && nx < n && 0 <= ny && ny < n && visited[nx][ny] == 0){
            int diff = arr[x][y] > arr[nx][ny] ? arr[x][y] - arr[nx][ny] : arr[nx][ny] - arr[x][y];
            return diff >= l && diff <= r;
        }
        return false;
    }
}