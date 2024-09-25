class Solution {
    public int[] solution(int[] arr, int k) {
        int t = arr.length;
        int[] answer = new int[t];
        if (k%2==0){
            for (int i = 0; i<t; i++){
                answer[i] = arr[i] + k;
            }
        } else {
            for (int i = 0; i<t; i++){
                answer[i] = arr[i] * k;
            }
        }
        return answer;
    }
}