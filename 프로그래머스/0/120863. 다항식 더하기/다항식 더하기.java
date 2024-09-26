import java.util.*;

class Solution {
    public String solution(String polynomial) {
        String answer = "";
        
        String[] tmp = polynomial.split(" \\+ ");
        int[] lst = new int[2];
        
        for (String i: tmp){
            if (i.contains("x")){
                String t = i.replace("x", "");
                if (t == "") {
                    lst[1] += 1;
                } else {
                    lst[1] += Integer.parseInt(t);
                }
            } else {
                lst[0] += Integer.parseInt(i);
            }
        }
        
        if (lst[1]==0) {
            answer = Integer.toString(lst[0]);
        } else {
            if (lst[1] == 1){
                answer = "x";
            } else {
                answer = lst[1] + "x";
            }

            if (lst[0]!=0){
                answer += " + " + lst[0];
            }
        }
        return answer;
    }
}