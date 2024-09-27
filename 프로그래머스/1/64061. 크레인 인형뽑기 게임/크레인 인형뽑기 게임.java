import java.util.*;

class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        
        Stack <Integer> stack = new Stack<>();
        int now = 0;
        for (int move: moves){
            now = move-1;
            for (int i =0; i<board.length; i++){
                if (board[i][now] != 0){
                    if (stack.empty()){
                        stack.push(board[i][now]);
                    } else if (stack.peek() == board[i][now]){
                        stack.pop();
                        answer += 2;
                    } else {
                        stack.push(board[i][now]);
                    }
                    board[i][now] = 0;
                    break;
                }
            }
        }
        
        
        return answer;
    }
}