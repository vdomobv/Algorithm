class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
        
        int before = 0;
        int t = bandage[0];
        int x = bandage[1];
        int y = bandage[2];
        int hp = health;
        
        for (int[] attack: attacks){
            int time = attack[0] - 1 - before;
            hp += (time/t)*y + time*x;
            
            if (hp > health) hp = health;
            
            hp -= attack[1];
            if (hp <= 0) return -1;
            
            before = attack[0];
        }
        return hp;
    }
}