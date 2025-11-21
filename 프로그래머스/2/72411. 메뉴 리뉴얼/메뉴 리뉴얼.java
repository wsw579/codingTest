import java.util.*;

class Solution {
    static HashMap<String, Integer> map;
    public String[] solution(String[] orders, int[] course) {
        ArrayList<String> answerList = new ArrayList<>();
        
        for(int courseSize : course){
             map = new HashMap<>();
             for(String order : orders){
                 char[] charArr = order.toCharArray();
                 Arrays.sort(charArr);
                 combination(charArr, "", 0, courseSize);
       
             }
            
        
        
        int maxCount = 0;
        for (String key : map.keySet()) {
            maxCount = Math.max(maxCount, map.get(key));
        }
        
        if (maxCount >= 2) {
            for (String key : map.keySet()) {
                if (map.get(key) == maxCount) {
                    answerList.add(key);
                }
            }
        }
        }
        
         Collections.sort(answerList);
    return answerList.toArray(new String[0]);
}

    
    
    public void combination(char[]arr , String current, int start, int targetSize){
        if (current.length() == targetSize) {
        // Map에 추가하거나 횟수 증가시키기
        map.put(current, map.getOrDefault(current, 0) + 1);
        return;
    }
        // 백트래킹(조합) 로직
    for (int i = start; i < arr.length; i++) {
        combination(arr, current + arr[i], i + 1, targetSize);
    }
    }
}