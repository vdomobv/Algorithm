class Solution {
    public int solution(String myString, String pat) {
        String answer = "";
        for (int i=0; i<myString.length(); i++){
            if ('A' == myString.charAt(i)){
                answer += "B";
            } else {
                answer += "A";
            }
        }
        return answer.contains(pat) ? 1 : 0;
    }
}