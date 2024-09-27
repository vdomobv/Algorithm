import java.util.*;

class Solution {
    public ArrayList<int[]> solution(int[][] data, String ext, int val_ext, String sort_by) {
        ArrayList<int[]> answer = new ArrayList<>();
        
//         code, date, max, remain
        Map<String, Integer> map = new HashMap<>();
        String[] t = {"code", "date", "maximum", "remain"};
        for (int i = 0; i < 4; i++){
            map.put(t[i], i);
        }
        
        for (int[] d : data){
            if (d[map.get(ext)] <= val_ext){
                answer.add(d);
            }
        }
        
        int s = map.get(sort_by);
        Collections.sort(answer, (a, b) -> a[s] - b[s]);
        
        return answer;
    }
}