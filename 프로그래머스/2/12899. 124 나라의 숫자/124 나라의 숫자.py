def solution(n):
    answer = ''
    while(n!=0):
        if n % 3 == 0 :
            answer += '4'
            n -= 1
            n //= 3 
        elif n % 3 == 1 :
            answer += '1'
            n //= 3 
        elif n % 3 == 2 :
            answer += '2'
            n //= 3 
    
    return answer[::-1]
