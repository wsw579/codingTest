import java.util.*;
class Solution {
    public boolean solution(String[] phone_book) {
        Set<String> result = new HashSet<>(Arrays.asList(phone_book));

        for(String phone : phone_book){
            for(int i=0; i<phone.length(); i++){
                String prefix = phone.substring(0,i);
                if(result.contains(prefix) && !(prefix).equals(phone)){
                    return false;
                }   
            }
        }
        return true;
    }
}