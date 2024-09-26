import java.util.*;
import java.lang.Math;

class Solution {
    public ArrayList<Integer> solution(int[] numlist, int n) {
        ArrayList<Integer> answer = new ArrayList<>();
        
        Arrays.sort(numlist);
        // System.out.println(Arrays.toString(numlist));
        int e = numlist.length - 1;
        int s = 0;
        
        while (s <= e) {
            if (Math.abs(n-numlist[s]) < Math.abs(n-numlist[e])){
                answer.add(numlist[e]);
                e--;
            } else {
                answer.add(numlist[s]);
                s++;
            }
        }
        
        Collections.reverse(answer);
        return answer;
    }
}