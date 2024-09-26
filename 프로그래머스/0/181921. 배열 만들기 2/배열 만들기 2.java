import java.util.*;
class Solution {
    public int[] solution(int l, int r) {
        ArrayList<Integer> answer = new ArrayList<>();
        
        for (int i=l/5*5; i<=r; i+= 5) {
            int cnt = 0;
            String[] tmp = Integer.toString(i).split("");
            boolean check = true;
            
            for (String t: tmp){
                if (!t.equals("5") && !t.equals("0")){
                    check = false;
                }
            }
            
            if (check) {
                answer.add(i);
            }
        }
        
        if (answer.isEmpty()){
            int[] result = {-1};
            return result;
        } 
        
        Collections.sort(answer);
        return answer.stream().mapToInt(i -> i).toArray();
    }
}