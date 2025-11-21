class Solution {
    public long solution(int price, int money, int count) {
        long answer = 0;
        long total = 0;
        for(int i=1; i<count+1; i++){
            total += (long)price * i;
        }
        if(total>money){
        answer = Math.abs(money-total);
        }
        return answer;
    }
}