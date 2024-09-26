class Solution {
    public int solution(int[] common) {
        int n = common.length;
        int k = common[1]-common[0];
        boolean check = true;
        
        for (int i=1; i<n; i++){
            if (common[i] - common[i-1] != k) {
                check = false;
                break;
            }
        }
            
        if (check) {
            return common[n-1] + k;
        }
        
        k = common[1]/common[0];            
        for (int i=1; i<n-1; i++){
            if (common[i+1] / common[i] != k) {
                check = false;
                break;
            }
        }

        return common[n-1] * k;
    }
}