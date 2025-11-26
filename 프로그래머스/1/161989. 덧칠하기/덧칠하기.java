class Solution {
    public int solution(int n, int m, int[] section) {
        int paintCount = 0;
        int paintedUntil = 0;
        
        for (int requiredSection : section) {
            if (requiredSection > paintedUntil) {
                paintCount++;
                paintedUntil = requiredSection + m - 1;
            }
            
        }

        return paintCount;
    }
}