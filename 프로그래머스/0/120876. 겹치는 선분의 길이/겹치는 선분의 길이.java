import java.util.*;

class Solution {
    public int solution(int[][] lines) {
        int answer = 0;
        
        Arrays.sort(lines, (o1, o2) -> {
            return o1[0]-o2[0];
        });
        
        int bs = lines[0][0];
        int be = lines[0][1];
        
        for (int i = 1; i<lines.length; i++){
            int s = lines[i][0];
            int e = lines[i][1];
            System.out.print(bs + "," + be + "," + s + "," + e + ": ");
            if (be > s) {
                if (bs > s) {
                    answer += be < e? be-bs : e-bs;
                    System.out.println(be < e? be-bs : e-bs);
                } else {
                    answer += be < e? be-s : e-s;
                    System.out.println(be < e? be-s : e-s + " , " + answer);
                }
                bs = be;
                be = e;
            } else {
                be = e;
                bs = s;
                System.out.println();
            }
            if (be < bs) {
                int t = be;
                be = bs;
                bs = t;
            }
        }
        
        return answer;
    }
}