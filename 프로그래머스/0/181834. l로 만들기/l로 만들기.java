class Solution {
    public String solution(String myString) {
        String answer = "";
        int t = (int)'l';
        for (int i=0; i<myString.length(); i++){
            if ((int)myString.charAt(i) < t){
                answer += 'l';
            } else {
                answer += myString.substring(i, i+1);
            }
        }
        return answer;
    }
}