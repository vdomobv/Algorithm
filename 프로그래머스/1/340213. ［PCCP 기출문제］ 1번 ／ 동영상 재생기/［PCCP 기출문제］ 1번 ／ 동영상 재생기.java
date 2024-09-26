class Solution {
    public String solution(String video_len, String pos, String op_start, String op_end, String[] commands) {

        String[] now = pos.split(":");
        int time = Integer.parseInt(now[0]) * 60 + Integer.parseInt(now[1]);
        
        String[] video = video_len.split(":");
        int total = Integer.parseInt(video[0]) * 60 + Integer.parseInt(video[1]);
        
        String[] os = op_start.split(":");
        int start = Integer.parseInt(os[0]) * 60 + Integer.parseInt(os[1]);
        
        String[] oe = op_end.split(":");
        int end = Integer.parseInt(oe[0]) * 60 + Integer.parseInt(oe[1]);
        
        if (start <= time && time <= end) {
            time = end;
        }
        
        for (String command:commands){
            if (command.equals("next")){
                if (total - 10 < time){
                    time = total;
                } else {
                    time += 10;
                }
            } else {
                if (time < 10) {
                    time = 0;
                } else {
                    time -= 10;
                }
            }
            
            if (start <= time && time <= end) {
                time = end;
            }
        }
        
        String minutes = time/60 < 10? "0" + time/60 : Integer.toString(time/60);
        String seconds = time%60 < 10? "0" + time%60: Integer.toString(time%60);
        return minutes + ":" + seconds;
    }
}