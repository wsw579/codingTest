class Solution {
    public int[] solution(String[] wallpaper) {
        int[] answer = {}; 

        int lux = Integer.MAX_VALUE;
        int luy = Integer.MAX_VALUE;
        int rdx = Integer.MIN_VALUE;
        int rdy = Integer.MIN_VALUE;
        
        
        int h = wallpaper.length; //  전체 길이 , 세로
        int w = wallpaper[0].length(); //  첫번째 줄 길이, 가로

        for(int i = 0; i<h; i++){
            for(int j = 0; j<w; j++){
                if(wallpaper[i].charAt(j) == '#'){
                    // 시작점(왼쪽 위): 가장 작은 i, j 찾기
                    lux = Math.min(lux, i);
                    luy = Math.min(luy, j);
                    
                    // 끝점(오른쪽 아래): 가장 큰 i, j 찾아서 +1 하기
                    rdx = Math.max(rdx, i + 1);
                    rdy = Math.max(rdy, j + 1);
                }
            }
        }
        answer = new int[]{lux, luy, rdx, rdy};
        return answer;
    }
}