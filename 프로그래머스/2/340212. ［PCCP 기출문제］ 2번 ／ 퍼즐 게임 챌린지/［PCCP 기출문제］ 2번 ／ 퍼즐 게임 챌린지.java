class Solution {
    public int solution(int[] diffs, int[] times, long limit) {
        int answer = 100000;
        
        int l = 1;
        int u = 100000;
        int n = times.length;
        
        while (l < u){
            int level = (l+u)/2;
            long t = 0;
            
            boolean check = true;
            for (int i=0; i<n; i++){
                if (diffs[i] <= level){
                    t += times[i];
                } else {
                    t += (diffs[i] - level) * (times[i] + times[i-1]) + times[i];
                }
                
                if (t > limit){
                    check = false;
                    l = level+1;
                    break;
                }
            }
            
            if (check){
                u = level;
                if (answer > level) answer = level;
            }
        }
        
        
        return answer;
    }
}