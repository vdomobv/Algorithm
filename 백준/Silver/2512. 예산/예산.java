import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main{
    static int n, m, l, u, mid;
    static int[] arr;

    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stk = new StringTokenizer(br.readLine(), " ");

        n = Integer.parseInt(stk.nextToken());

        arr = new int[n];
        u = 0;
        stk = new StringTokenizer(br.readLine());
        for (int i=0; i<n; i++){
            arr[i] = Integer.parseInt(stk.nextToken());
            if (arr[i] > u){
                u = arr[i];
            }
        }
        Arrays.sort(arr);

        stk = new StringTokenizer(br.readLine());
        m = Integer.parseInt(stk.nextToken());

        l = 1;
        int answer = 0;

        while (l <= u) {
            mid = (l + u) / 2;

            int t = 0;
            for (int i: arr){

                t += Math.min(i, mid);
            }

            if (t <= m) {
                answer = mid;
                l = mid+1;
            } else {
                u = mid-1;
            }
        }

        System.out.println(answer);
    }
}