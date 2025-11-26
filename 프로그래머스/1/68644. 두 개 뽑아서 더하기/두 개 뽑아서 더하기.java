import java.util.*;

class Solution {
    public int[] solution(int[] numbers) {
        Set<Integer> set = new HashSet<>(); // 중복제거 
        int result = 0;
        for(int i=0; i<numbers.length; i++){
            for(int j=i+1; j<numbers.length; j++){ // 1 + (2,3,4)
                result = numbers[i] + numbers[j];
                set.add(result);
                }
            }
        
        List<Integer> list = new ArrayList<>(set); // 오름차순 정렬
        Collections.sort(list);
        
        int[] answer = new int[list.size()]; 
        for(int i=0; i<list.size(); i++){ 
            answer[i] = list.get(i); // get함수로 값 가져오기
        }
        
        return answer;
    }
}