import java.util.*;

class Solution {
    public int[] solution(String[] keymap, String[] targets) {
        int[] answer = new int[targets.length];
        Map<String, Integer> map = new HashMap<>();
        
        for (String key: keymap){
            for (int k = 0; k < key.length(); k++){
                String m = key.substring(k, k+1);
                if (map.containsKey(m)){
                    if (map.get(m) > k+1) map.put(m, k+1);
                } else {
                    map.put(m, k+1);
                }
            }            
        }
        
        for (int i = 0; i< targets.length; i++){
            String target = targets[i];
            int tmp = 0;
            for (String t: target.split("")){
                if (map.containsKey(t)){
                    tmp += map.get(t);
                } else {
                    tmp = -1;
                    break;
                }
            }
            answer[i] = tmp; 
        }
        return answer;
    }
}