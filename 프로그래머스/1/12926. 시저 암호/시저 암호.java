class Solution {
    public String solution(String s, int n) {
        String answer = "";
        for(int i=0; i<s.length(); i++){
              char ch = s.charAt(i);
              if(ch == ' '){
                  answer += " ";
              }
              if(ch >= 'a' && ch <= 'z'){
                  answer += (char) (((ch - 'a') + n) % 26 + 'a');
                }
              if(ch >= 'A' && ch <= 'Z'){
                   answer += (char) (((ch - 'A') + n) % 26 + 'A');
                }
            }
        
        return answer;
    }
}