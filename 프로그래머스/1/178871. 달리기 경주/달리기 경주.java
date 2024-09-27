import java.util.*;

class Solution {
    public String[] solution(String[] players, String[] callings) {
        Map <String, Integer> map = new HashMap<>();
        
        for (int i = 0; i<players.length; i++){
            map.put(players[i], i+1);
        }
        
        for (String call:callings){
            int idx = map.get(call);
            
            String t = players[idx-1];
            players[idx-1] = players[idx-2];
            players[idx-2] = t;
            
            map.put(call, idx-1);
            map.put(players[idx-1], idx);
        }
        return players;
    }
}