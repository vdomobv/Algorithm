import java.util.*;
import java.util.stream.IntStream;

class Solution {
    public int solution(int a, int b, int c, int d) {
        int answer = 0;
        int[] dice = new int[7];
        
        dice[a]++;
        dice[b]++;
        dice[c]++;
        dice[d]++;
        
        int q = 0;
        int p = 0;
        int r = 0;
        
        if (IntStream.of(dice).anyMatch((x) -> x == 4)){
            for (int i=1; i<dice.length; i++){
                if (dice[i] == 4){
                    answer = 1111 * i;
                    break;
                }
            }
        } else if (IntStream.of(dice).anyMatch((x) -> x == 3)){
            for (int i = 1; i<dice.length; i++) {
                if (dice[i] == 1){
                    q = i;
                } else if (dice[i] == 3) {
                    p = i;
                }
            }
            
            answer = (10*p + q)*(10*p + q);
        } else if (IntStream.of(dice).anyMatch((x) -> x == 2)) {
            for (int i = 1; i<dice.length; i++) {
                if (p==0 && dice[i] == 2){
                    p = i;
                } else if (dice[i] != 0) {
                    if (q == 0) {
                        q = i;
                    } else {
                        r = i;
                        break;
                    }
                }
            }
            
            if (r!= 0) {
                answer = q * r;
            } else {
                answer = (p+q)*(p>q?p-q:q-p);
            }
            
            
        } else {
            answer = Collections.min(List.of(a, b, c, d));
        }
        return answer;
    }
}