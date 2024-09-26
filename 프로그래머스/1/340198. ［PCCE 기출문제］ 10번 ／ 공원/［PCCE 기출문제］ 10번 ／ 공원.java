import java.util.*;

class Solution {
    public int solution(int[] mats, String[][] park) {
        int answer = -1;
        
        int n = park.length;
        int m = park[0].length;
        
        Arrays.sort(mats);
        for (int k = mats.length-1; k>-1; k--) {
            int mat = mats[k];
            
            for (int i=0; i<=n-mat; i++){
                for (int j=0; j<=m-mat; j++){
                    if (park[i][j].equals("-1")) {
                        boolean check = true;
                        for (int x = i; x < i+mat; x++){
                            for (int y = j; y < j+mat; y++) {
                                if (!park[x][y].equals("-1")){
                                    check = false;
                                    break;
                                }
                            }
                            if (!check) break;
                        }
                        if (check) return mat;
                    }
                }
            }
        }
        return answer;
    }
}