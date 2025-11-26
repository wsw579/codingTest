import java.util.*;

class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        int[] answer = new int[photo.length];
        
        Map<String,Integer> nameMap = new HashMap<>();
        int i = 0; 
        for(String n :name){
            nameMap.put(n,yearning[i]);
            i++;
            }
        
       for (int j = 0; j < photo.length; j++) {
            String[] currentPhoto = photo[j];
            int result = 0;
           
            for (String personName : currentPhoto) {
                if (nameMap.containsKey(personName)) {
                    result += nameMap.get(personName);
                }
            }
            answer[j] = result;
        }
        return answer;
    }
}