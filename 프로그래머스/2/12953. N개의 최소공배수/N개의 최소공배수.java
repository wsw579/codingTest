
class Solution {
    
    int gcd(int a, int b) {
        if (b == 0) {
            return a;
        }
        return gcd(b, a % b); // 재귀 호출
    }
    

    int lcm(int a, int b) {
        
        return (a * b) / gcd(a, b);
    }
    
    public int solution(int[] arr) {
        
        int currentLCM = arr[0]; 

       
        for (int i = 1; i < arr.length; i++) {
           
            currentLCM = lcm(currentLCM, arr[i]);
        }
        
        return currentLCM;
    }
}