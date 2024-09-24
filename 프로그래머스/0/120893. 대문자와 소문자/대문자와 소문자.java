class Solution {
    public String solution(String my_string) {
        char[] chars = my_string.toCharArray();
        String answer = "";
        for (char i:chars){
            if (Character.isUpperCase(i)){
                answer += Character.toString(Character.toLowerCase(i));
            } else {
                answer += Character.toString(Character.toUpperCase(i));
            }
        }
        
        return answer;
    }
}