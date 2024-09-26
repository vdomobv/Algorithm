import java.util.*;

class Solution {
    public int solution(String[] friends, String[] gifts) {
        int n = friends.length;
        int[] give = new int[n];
        int[] take = new int[n];
        
        int[][] nuga = new int[n][n];
        
        for (String gift : gifts) {
            String[] fromto = gift.split(" ");
            
            int f = Arrays.asList(friends).indexOf(fromto[0]);
            int t = Arrays.asList(friends).indexOf(fromto[1]);
            
            nuga[f][t] += 1;
            give[f] += 1;
            take[t] += 1;
        }
        
        int[] next = new int[n];
        int[] jisoo = new int[n];
        
        for (int i=0; i<n; i++){
            jisoo[i] = give[i]-take[i];
        }
        
        for (int i = 0; i< n ; i++){
            for (int j = i; j< n; j++){
                if (i!=j){
                    if (nuga[i][j] > nuga[j][i]){
                        next[i] += 1;
                    } else if(nuga[i][j] < nuga[j][i]) {
                        next[j] += 1;
                    } else {
                        if (jisoo[i] > jisoo[j]) {
                            next[i] += 1;
                        } else if (jisoo[i] < jisoo[j]) {
                            next[j] += 1;
                        }
                    }
                }
            }
        }
        
        return Arrays.stream(next).max().getAsInt();
    }
}